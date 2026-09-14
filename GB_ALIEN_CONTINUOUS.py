#!/usr/bin/env python3
"""
GB Alien Continuous Watcher.

Runs a 1-second control loop while the process is alive. It does not pretend
that a PT30 source becomes 1-minute data: it reacts to each newly published
Elexon dataset revision at its native resolution.

The watcher:
- polls Elexon metadata every second;
- fetches only datasets whose publish timestamp changed;
- maintains online mean/variance/EWMA for numeric fields;
- emits z-score shocks, jump/trend alerts and a trader-readable interpretation;
- persists compact state so an ephemeral GitHub Actions runner can continue
  from the previous run.

No order execution. No model promotion. This is a discovery/observation layer.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

VERSION = "GB_ALIEN_CONTINUOUS_V1.0.0"
BASE_URL = "https://data.elexon.co.uk/bmrs/api/v1"
DEFAULT_DATASETS = [
    "FREQ", "FUELINST", "FUELHH", "WINDFOR", "NDF", "TSDF",
    "IMBALNGC", "INDDEM", "INDGEN", "MELNGC", "LOLPDRM", "MID"
]
MAX_ALERTS = 60

DATASET_MEANING = {
    "FREQ": "system frequency",
    "FUELINST": "instantaneous generation mix",
    "FUELHH": "half-hour generation mix",
    "WINDFOR": "wind forecast",
    "NDF": "national-demand forecast",
    "TSDF": "transmission-demand forecast",
    "IMBALNGC": "indicated system imbalance",
    "INDDEM": "indicated demand",
    "INDGEN": "indicated generation",
    "MELNGC": "indicated margin",
    "LOLPDRM": "tightness / de-rated margin",
    "MID": "market-index price/volume",
}

TIME_KEYS = {
    "publishtime", "publishdatetime", "createddatetime", "starttime", "endtime",
    "settlementdate", "deliverydate", "timefrom", "timeto"
}

def utcnow() -> datetime:
    return datetime.now(timezone.utc)

def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")

def atomic_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
    os.replace(tmp, path)

def http_json(url: str, timeout: int = 25) -> Any:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": f"uk-official/{VERSION}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)

def iter_dicts(obj: Any):
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from iter_dicts(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from iter_dicts(v)

def _first(d: dict, names: tuple[str, ...]) -> Any:
    lower = {str(k).lower(): v for k, v in d.items()}
    for n in names:
        if n.lower() in lower:
            return lower[n.lower()]
    return None

def parse_metadata(payload: Any) -> dict[str, str]:
    """Tolerant parser because the API has changed response wrappers over time."""
    out: dict[str, str] = {}
    for d in iter_dicts(payload):
        ds = _first(d, ("dataset", "datasetName", "name", "code"))
        ts = _first(d, (
            "latestPublishTime", "latestPublishDateTime", "publishTime",
            "publishDateTime", "lastUpdated", "latest"
        ))
        if isinstance(ds, str) and isinstance(ts, str):
            key = ds.upper().strip()
            if 2 <= len(key) <= 20:
                out[key] = ts
    return out

def extract_rows(payload: Any) -> list[dict]:
    if isinstance(payload, dict):
        for key in ("data", "rows", "records", "results"):
            value = payload.get(key)
            if isinstance(value, list):
                return [x for x in value if isinstance(x, dict)]
        if payload and all(not isinstance(v, (list, tuple)) for v in payload.values()):
            return [payload]
    if isinstance(payload, list):
        return [x for x in payload if isinstance(x, dict)]
    return []

def flatten_numeric(d: dict, prefix: str = "") -> dict[str, float]:
    out: dict[str, float] = {}
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else str(k)
        low = str(k).lower()
        if low in TIME_KEYS or low.endswith("id") or low.endswith("number"):
            continue
        if isinstance(v, bool):
            continue
        if isinstance(v, (int, float)) and math.isfinite(float(v)):
            out[key] = float(v)
        elif isinstance(v, dict):
            out.update(flatten_numeric(v, key))
        elif isinstance(v, str):
            try:
                fv = float(v)
            except Exception:
                continue
            if math.isfinite(fv):
                out[key] = fv
    return out

def load_state(path: Path) -> dict:
    if not path.exists():
        return {"version": VERSION, "metadata": {}, "stats": {}, "alerts": [], "events": []}
    try:
        x = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"version": VERSION, "metadata": {}, "stats": {}, "alerts": [], "events": []}
    x.setdefault("metadata", {})
    x.setdefault("stats", {})
    x.setdefault("alerts", [])
    x.setdefault("events", [])
    return x

def update_stat(st: dict, value: float, alpha: float = 0.20) -> tuple[float | None, float, float | None]:
    n = int(st.get("n", 0))
    mean = float(st.get("mean", 0.0))
    m2 = float(st.get("m2", 0.0))
    last = st.get("last")
    ewma = st.get("ewma")
    z = None
    if n >= 20 and n > 1:
        var = m2 / (n - 1)
        if var > 1e-12:
            z = (value - mean) / math.sqrt(var)
    delta = value - float(last) if last is not None else 0.0
    trend = value - float(ewma) if ewma is not None else None

    n2 = n + 1
    dx = value - mean
    mean2 = mean + dx / n2
    m22 = m2 + dx * (value - mean2)
    ewma2 = value if ewma is None else alpha * value + (1.0 - alpha) * float(ewma)
    st.update({"n": n2, "mean": mean2, "m2": m22, "last": value, "ewma": ewma2})
    return z, delta, trend

def interpret(dataset: str, field: str, value: float, z: float | None, delta: float, trend: float | None) -> str:
    what = DATASET_MEANING.get(dataset, dataset)
    direction = "UP" if delta > 0 else "DOWN" if delta < 0 else "FLAT"
    shock = f"{abs(z):.1f}σ" if z is not None else "new baseline"
    if dataset in {"WINDFOR"}:
        implication = "more renewable pressure / lower residual load" if delta > 0 else "less renewable cushion / higher residual load"
    elif dataset in {"NDF", "TSDF", "INDDEM"}:
        implication = "demand pressure increasing" if delta > 0 else "demand pressure easing"
    elif dataset == "IMBALNGC":
        implication = "imbalance forecast moved materially; check short/long direction"
    elif dataset in {"MELNGC", "LOLPDRM"}:
        implication = "margin improving" if delta > 0 else "system tightness increasing"
    elif dataset == "FREQ":
        implication = "frequency excursion; balancing stress worth checking"
    elif dataset in {"FUELINST", "FUELHH"}:
        implication = "generation-mix shift"
    elif dataset == "MID":
        implication = "short-term market price/volume shift"
    else:
        implication = "state change"
    return f"{what}: {field} {direction}, value={value:.4g}, jump={delta:.4g}, anomaly={shock} → {implication}"

def process_rows(state: dict, dataset: str, rows: list[dict], now: datetime) -> list[dict]:
    alerts: list[dict] = []
    for row in rows:
        for field, value in flatten_numeric(row).items():
            key = f"{dataset}.{field}"
            st = state["stats"].setdefault(key, {})
            z, delta, trend = update_stat(st, value)
            std = math.sqrt(st["m2"] / (st["n"] - 1)) if st["n"] > 1 and st["m2"] > 0 else None
            large_delta = bool(std and abs(delta) >= 2.5 * std)
            unusual = bool(z is not None and abs(z) >= 3.5)
            if unusual or large_delta:
                alerts.append({
                    "ts": iso(now), "dataset": dataset, "field": field,
                    "value": value, "z": z, "delta": delta, "trend": trend,
                    "interpretation": interpret(dataset, field, value, z, delta, trend),
                })
    return alerts

def fetch_dataset(dataset: str, since: datetime, until: datetime) -> list[dict]:
    params = urllib.parse.urlencode({
        "publishDateTimeFrom": iso(since),
        "publishDateTimeTo": iso(until),
        "format": "json",
    })
    urls = [
        f"{BASE_URL}/datasets/{dataset}?{params}",
        f"{BASE_URL}/datasets/{dataset}/stream?{params}",
    ]
    last_exc = None
    for url in urls:
        try:
            return extract_rows(http_json(url))
        except Exception as exc:
            last_exc = exc
    raise RuntimeError(f"{dataset}: {last_exc}")

def render_status(state: dict, path: Path, watched: list[str], started: datetime, polls: int, errors: int) -> None:
    alerts = list(state.get("alerts", []))[-20:][::-1]
    events = list(state.get("events", []))[-20:][::-1]
    lines = [
        "# GB Alien — live control room",
        "",
        f"Engine: `{VERSION}`  ",
        f"Last heartbeat UTC: `{iso(utcnow())}`  ",
        f"Current process started UTC: `{iso(started)}`  ",
        f"1-second loop polls in this process: **{polls}**  ",
        f"HTTP/data errors in this process: **{errors}**  ",
        "",
        "The loop checks for newly published information every second. Heavy interpretation",
        "is event-driven: if the source did not change, it does not manufacture a new signal.",
        "",
        "## Watched public Elexon feeds",
        "",
        ", ".join(f"`{x}`" for x in watched),
        "",
        "## Latest interpreted anomalies",
        "",
    ]
    if not alerts:
        lines.append("No statistically unusual move has been observed yet with sufficient online history.")
    else:
        for a in alerts:
            z = "NA" if a.get("z") is None else f"{a['z']:.2f}"
            lines.append(f"- **{a['dataset']}** `{a['field']}` z={z}: {a['interpretation']}")
    lines += ["", "## Latest publication events", ""]
    if not events:
        lines.append("No dataset publication change recorded yet.")
    else:
        for e in events:
            lines.append(f"- `{e['ts']}` — **{e['dataset']}**: {e['rows']} rows fetched; publish marker `{e['marker']}`")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def one_poll(state: dict, watched: list[str], now: datetime) -> tuple[int, list[str]]:
    meta = parse_metadata(http_json(f"{BASE_URL}/datasets/METADATA/latest"))
    if not meta:
        raise RuntimeError("METADATA_PARSE_EMPTY")
    changed = []
    prev = state["metadata"]
    fresh = not bool(prev)
    for ds in watched:
        marker = meta.get(ds)
        if not marker:
            continue
        old = prev.get(ds)
        prev[ds] = marker
        if fresh or marker == old:
            continue
        changed.append(ds)
    if fresh:
        return 0, []
    alerts = []
    fetched = 0
    for ds in changed:
        try:
            rows = fetch_dataset(ds, now - timedelta(minutes=20), now + timedelta(minutes=2))
            fetched += len(rows)
            alerts.extend(process_rows(state, ds, rows, now))
            state["events"].append({"ts": iso(now), "dataset": ds, "rows": len(rows), "marker": prev[ds]})
        except Exception as exc:
            state["events"].append({"ts": iso(now), "dataset": ds, "rows": 0, "marker": prev[ds], "error": str(exc)})
    state["events"] = state["events"][-MAX_ALERTS:]
    state["alerts"].extend(alerts)
    state["alerts"] = state["alerts"][-MAX_ALERTS:]
    return fetched, changed

def self_test() -> None:
    payload = {"data": [{"dataset": "WINDFOR", "latestPublishTime": "2026-09-14T10:00:00Z"}]}
    assert parse_metadata(payload)["WINDFOR"].startswith("2026")
    state = {"metadata": {}, "stats": {}, "alerts": [], "events": []}
    alerts = []
    for i in range(30):
        alerts += process_rows(state, "WINDFOR", [{"forecast": 1000 + i}], utcnow())
    alerts += process_rows(state, "WINDFOR", [{"forecast": 10000}], utcnow())
    assert alerts and alerts[-1]["dataset"] == "WINDFOR"
    assert "renewable" in alerts[-1]["interpretation"]
    print("SELF_TEST=PASS")

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--duration-seconds", type=int, default=285)
    p.add_argument("--poll-seconds", type=float, default=1.0)
    p.add_argument("--state", default="live/state.json")
    p.add_argument("--status", default="live/LATEST.md")
    p.add_argument("--datasets", default=",".join(DEFAULT_DATASETS))
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    if args.self_test:
        self_test()
        return 0

    watched = [x.strip().upper() for x in args.datasets.split(",") if x.strip()]
    state_path, status_path = Path(args.state), Path(args.status)
    state = load_state(state_path)
    started = utcnow()
    deadline = time.monotonic() + max(1, args.duration_seconds)
    polls = errors = 0

    while time.monotonic() < deadline:
        cycle = time.monotonic()
        try:
            _, changed = one_poll(state, watched, utcnow())
            if changed:
                print(f"{iso(utcnow())} changed={','.join(changed)}", flush=True)
        except Exception as exc:
            errors += 1
            state["last_error"] = {"ts": iso(utcnow()), "error": f"{type(exc).__name__}: {exc}"}
            print(f"WARN {state['last_error']}", file=sys.stderr, flush=True)
        polls += 1
        state["last_heartbeat"] = iso(utcnow())
        state["version"] = VERSION
        atomic_json(state_path, state)
        render_status(state, status_path, watched, started, polls, errors)
        sleep_for = max(0.0, args.poll_seconds - (time.monotonic() - cycle))
        if sleep_for:
            time.sleep(sleep_for)

    print(json.dumps({"version": VERSION, "polls": polls, "errors": errors, "alerts": len(state.get("alerts", []))}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
