#!/usr/bin/env python3
"""GB Alien live observer.

Polls Elexon publication metadata every second, fetches only datasets whose
publication marker changed, keeps categorical series separate, and updates
online statistics only on genuinely new observations.

Important: this is an observation/discovery layer. It does not place orders and
it does not promote a statistical alert to a trading rule.
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

VERSION = "GB_ALIEN_CONTINUOUS_V1.1.0"
BASE_URL = "https://data.elexon.co.uk/bmrs/api/v1"
DEFAULT_DATASETS = [
    "FREQ", "FUELINST", "FUELHH", "WINDFOR", "NDF", "TSDF",
    "IMBALNGC", "INDDEM", "INDGEN", "MELNGC", "LOLPDRM", "MID",
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

# Dataset-specific dimensions that identify independent time series. Without
# this, e.g. coal MW followed by wind MW looks like an absurd generation jump.
IDENTITY_CANDIDATES = {
    "FUELINST": ("fuelType", "fuelTypeName", "generationType"),
    "FUELHH": ("fuelType", "fuelTypeName", "generationType"),
    "MID": ("dataProvider", "marketIndexDataProvider", "provider"),
}

NON_SIGNAL_EXACT = {
    "id", "sp", "period", "settlementperiod", "settlementperiodnumber",
    "year", "month", "day", "hour", "minute", "second", "revision",
    "revisionnumber", "sequence", "rownumber", "recordnumber",
}
TIME_TOKENS = ("time", "date", "timestamp", "published", "created", "updated")


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def norm(k: Any) -> str:
    return "".join(ch for ch in str(k).lower() if ch.isalnum())


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
    out: dict[str, str] = {}
    for d in iter_dicts(payload):
        ds = _first(d, ("dataset", "datasetName", "name", "code"))
        ts = _first(d, (
            "latestPublishTime", "latestPublishDateTime", "publishTime",
            "publishDateTime", "lastUpdated", "latest",
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


def parse_dt(v: Any) -> datetime | None:
    if not isinstance(v, str):
        return None
    try:
        return datetime.fromisoformat(v.strip().replace("Z", "+00:00")).astimezone(timezone.utc)
    except Exception:
        return None


def row_rank(row: dict) -> tuple[float, int]:
    best = 0.0
    for k, v in row.items():
        nk = norm(k)
        if any(t in nk for t in ("publishtime", "publishdatetime", "starttime", "measurementtime", "timestamp", "createddatetime")):
            dt = parse_dt(v)
            if dt:
                best = max(best, dt.timestamp())
    sp = 0
    for k, v in row.items():
        if norm(k) in {"settlementperiod", "settlementperiodnumber", "sp"}:
            try:
                sp = int(v)
            except Exception:
                pass
    return best, sp


def series_id(dataset: str, row: dict) -> str:
    candidates = IDENTITY_CANDIDATES.get(dataset, ())
    lower = {str(k).lower(): v for k, v in row.items()}
    parts = []
    for name in candidates:
        v = lower.get(name.lower())
        if v is not None and str(v).strip():
            parts.append(f"{name}={str(v).strip()}")
    return "|".join(parts) if parts else "TOTAL"


def latest_rows_by_series(dataset: str, rows: list[dict]) -> list[tuple[str, dict]]:
    best: dict[str, tuple[tuple[float, int], dict]] = {}
    for row in rows:
        sid = series_id(dataset, row)
        rank = row_rank(row)
        old = best.get(sid)
        if old is None or rank >= old[0]:
            best[sid] = (rank, row)
    return [(sid, item[1]) for sid, item in best.items()]


def flatten_numeric(d: dict, prefix: str = "") -> dict[str, float]:
    out: dict[str, float] = {}
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else str(k)
        nk = norm(k)
        if nk in NON_SIGNAL_EXACT or any(tok in nk for tok in TIME_TOKENS):
            continue
        if nk.endswith("id") or nk.endswith("number"):
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


def fresh_state(metadata: dict | None = None) -> dict:
    return {
        "version": VERSION,
        "metadata": metadata or {},
        "stats": {},
        "alerts": [],
        "events": [],
        "latest_values": {},
    }


def load_state(path: Path) -> dict:
    if not path.exists():
        return fresh_state()
    try:
        x = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return fresh_state()
    # V1.0 mixed categorical rows and identifiers into the same statistic.
    # Never inherit those polluted distributions into V1.1.
    if x.get("version") != VERSION:
        return fresh_state(dict(x.get("metadata", {})))
    for k, default in (("metadata", {}), ("stats", {}), ("alerts", []), ("events", []), ("latest_values", {})):
        x.setdefault(k, default)
    return x


def update_stat(st: dict, value: float, alpha: float = 0.20) -> tuple[float | None, float, float | None]:
    n = int(st.get("n", 0)); mean = float(st.get("mean", 0.0)); m2 = float(st.get("m2", 0.0))
    last = st.get("last"); ewma = st.get("ewma")
    prior_std = math.sqrt(m2 / (n - 1)) if n > 1 and m2 > 0 else None
    z = ((value - mean) / prior_std) if n >= 12 and prior_std and prior_std > 1e-12 else None
    delta = value - float(last) if last is not None else 0.0
    n2 = n + 1; dx = value - mean; mean2 = mean + dx / n2; m22 = m2 + dx * (value - mean2)
    ewma2 = value if ewma is None else alpha * value + (1.0 - alpha) * float(ewma)
    st.update({"n": n2, "mean": mean2, "m2": m22, "last": value, "ewma": ewma2})
    return z, delta, prior_std


def implication(dataset: str, delta: float) -> str:
    if dataset == "WINDFOR":
        return "renewable pressure up / residual-load pressure down" if delta > 0 else "renewable cushion down / residual-load pressure up"
    if dataset in {"NDF", "TSDF", "INDDEM"}:
        return "demand pressure up" if delta > 0 else "demand pressure easing"
    if dataset == "IMBALNGC":
        return "indicated imbalance moved; inspect sign/magnitude"
    if dataset in {"MELNGC", "LOLPDRM"}:
        return "margin/tightness state changed"
    if dataset == "FREQ":
        return "frequency excursion; balancing stress check"
    if dataset in {"FUELINST", "FUELHH"}:
        return "generation-mix component moved"
    if dataset == "MID":
        return "market-index price/volume moved"
    return "state changed"


def process_rows(state: dict, dataset: str, rows: list[dict], now: datetime) -> list[dict]:
    alerts: list[dict] = []
    for sid, row in latest_rows_by_series(dataset, rows):
        numeric = flatten_numeric(row)
        for field, value in numeric.items():
            key = f"{dataset}|{sid}|{field}"
            st = state["stats"].setdefault(key, {})
            z, delta, prior_std = update_stat(st, value)
            state["latest_values"][key] = {"value": value, "ts": iso(now), "n": st["n"]}
            # Warm-up must not generate pseudo-alerts. Alert only against a real
            # history for this exact series/field.
            unusual = z is not None and abs(z) >= 3.5
            jump = prior_std is not None and st["n"] >= 12 and abs(delta) >= 3.5 * prior_std
            if unusual or jump:
                alerts.append({
                    "ts": iso(now), "dataset": dataset, "series": sid, "field": field,
                    "value": value, "z": z, "delta": delta,
                    "interpretation": f"{DATASET_MEANING.get(dataset,dataset)} [{sid}] {field}: value={value:.5g}, delta={delta:.5g}, z={'NA' if z is None else f'{z:.2f}'} -> {implication(dataset, delta)}",
                })
    return alerts


def fetch_dataset(dataset: str, since: datetime, until: datetime) -> list[dict]:
    params = urllib.parse.urlencode({
        "publishDateTimeFrom": iso(since), "publishDateTimeTo": iso(until), "format": "json",
    })
    urls = [f"{BASE_URL}/datasets/{dataset}?{params}", f"{BASE_URL}/datasets/{dataset}/stream?{params}"]
    last_exc = None
    for url in urls:
        try:
            return extract_rows(http_json(url))
        except Exception as exc:
            last_exc = exc
    raise RuntimeError(f"{dataset}: {last_exc}")


def render_status(state: dict, path: Path, watched: list[str], started: datetime, polls: int, errors: int) -> None:
    alerts = list(state.get("alerts", []))[-15:][::-1]
    events = list(state.get("events", []))[-15:][::-1]
    latest = list(state.get("latest_values", {}).items())[-20:]
    lines = [
        "# GB Alien — live control room", "",
        f"Engine: `{VERSION}`  ",
        f"Last heartbeat UTC: `{iso(utcnow())}`  ",
        f"Current process started UTC: `{iso(started)}`  ",
        f"1-second metadata polls in this process: **{polls}**  ",
        f"HTTP/data errors in this process: **{errors}**  ", "",
        "The one-second loop is event-driven: a statistical observation is added only when",
        "the provider publishes a new marker. Categorical series are kept separate and",
        "identifiers such as settlementPeriod are excluded from signal statistics.", "",
        "## Watched Elexon feeds", "", ", ".join(f"`{x}`" for x in watched), "",
        "## Latest statistically unusual observations", "",
    ]
    if not alerts:
        lines.append("No qualified anomaly yet (series are warming up or no threshold was crossed).")
    else:
        for a in alerts:
            lines.append(f"- **{a['dataset']}** `{a['series']}` `{a['field']}` — {a['interpretation']}")
    lines += ["", "## Latest market values", ""]
    if not latest:
        lines.append("No numeric observations yet.")
    else:
        for key, v in latest[-15:]:
            lines.append(f"- `{key}` = **{v['value']:.5g}** (n={v['n']}, {v['ts']})")
    lines += ["", "## Latest publication events", ""]
    if not events:
        lines.append("No publication change recorded yet.")
    else:
        for e in events:
            err = f"; ERROR={e['error']}" if e.get("error") else ""
            lines.append(f"- `{e['ts']}` — **{e['dataset']}**: {e['rows']} rows; marker `{e['marker']}`{err}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def one_poll(state: dict, watched: list[str], now: datetime) -> tuple[int, list[str]]:
    meta = parse_metadata(http_json(f"{BASE_URL}/datasets/METADATA/latest"))
    if not meta:
        raise RuntimeError("METADATA_PARSE_EMPTY")
    prev = state["metadata"]
    fresh = not bool(prev)
    changed: list[str] = []
    for ds in watched:
        marker = meta.get(ds)
        if not marker:
            continue
        old = prev.get(ds)
        if fresh:
            prev[ds] = marker
        if not fresh and marker != old:
            changed.append(ds)
    if fresh:
        return 0, []
    fetched = 0; new_alerts: list[dict] = []
    for ds in changed:
        try:
            rows = fetch_dataset(ds, now - timedelta(minutes=20), now + timedelta(minutes=2))
            fetched += len(rows); new_alerts.extend(process_rows(state, ds, rows, now))
            # A failed fetch must remain pending on the next poll, including
            # after process restart from persisted state.
            prev[ds] = meta[ds]
            state["events"].append({"ts": iso(now), "dataset": ds, "rows": len(rows), "marker": prev[ds]})
        except Exception as exc:
            state["events"].append({"ts": iso(now), "dataset": ds, "rows": 0, "marker": meta[ds], "error": f"{type(exc).__name__}: {exc}"})
    state["events"] = state["events"][-MAX_ALERTS:]
    state["alerts"].extend(new_alerts); state["alerts"] = state["alerts"][-MAX_ALERTS:]
    return fetched, changed


def self_test() -> None:
    meta = {"data": [{"dataset": "WINDFOR", "latestPublishTime": "2026-09-14T10:00:00Z"}]}
    assert parse_metadata(meta)["WINDFOR"].startswith("2026")
    # settlementPeriod is an identifier, never a signal.
    assert "settlementPeriod" not in flatten_numeric({"settlementPeriod": 36, "generation": 100.0})
    # Different fuel types are different series; no fake gas->wind jump.
    rows = [
        {"fuelType": "GAS", "generation": 10000, "publishTime": "2026-09-14T10:00:00Z"},
        {"fuelType": "WIND", "generation": 2500, "publishTime": "2026-09-14T10:00:00Z"},
    ]
    got = dict(latest_rows_by_series("FUELINST", rows))
    assert set(got) == {"fuelType=GAS", "fuelType=WIND"}
    state = fresh_state()
    for i in range(15):
        process_rows(state, "WINDFOR", [{"forecast": 1000 + i}], utcnow())
    alerts = process_rows(state, "WINDFOR", [{"forecast": 10000}], utcnow())
    assert alerts and alerts[-1]["dataset"] == "WINDFOR"
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
        self_test(); return 0
    watched = [x.strip().upper() for x in args.datasets.split(",") if x.strip()]
    state_path, status_path = Path(args.state), Path(args.status)
    state = load_state(state_path); started = utcnow(); deadline = time.monotonic() + max(1, args.duration_seconds)
    polls = errors = 0
    while time.monotonic() < deadline:
        cycle = time.monotonic()
        try:
            _, changed = one_poll(state, watched, utcnow())
            if changed:
                print(f"{iso(utcnow())} changed={','.join(changed)}", flush=True)
        except Exception as exc:
            errors += 1; state["last_error"] = {"ts": iso(utcnow()), "error": f"{type(exc).__name__}: {exc}"}
            print(f"WARN {state['last_error']}", file=sys.stderr, flush=True)
        polls += 1; state["last_heartbeat"] = iso(utcnow()); state["version"] = VERSION
        atomic_json(state_path, state); render_status(state, status_path, watched, started, polls, errors)
        delay = max(0.0, args.poll_seconds - (time.monotonic() - cycle))
        if delay:
            time.sleep(delay)
    print(json.dumps({"version": VERSION, "polls": polls, "errors": errors, "alerts": len(state.get("alerts", []))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
