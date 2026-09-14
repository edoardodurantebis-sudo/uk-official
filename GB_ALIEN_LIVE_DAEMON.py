#!/usr/bin/env python3
"""Continuous public-data observer for UNDER THE BID / GB Alien.

The analysis loop ticks every second. Remote providers are polled at slower,
source-appropriate cadences; every tick re-evaluates the latest cached state
for outliers, persistent trends, reversals, acceleration and regime turns.
No trade execution and no private/raw desk data are required.
"""
from __future__ import annotations

import argparse
import json
import math
import signal
import statistics
import time
import urllib.parse
import urllib.request
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION = "GB_ALIEN_LIVE_DAEMON_1.0.0"
UA = "uk-official-gb-alien/1.0"
ELEXON = "https://data.elexon.co.uk/bmrs/api/v1"
NESO = "https://api.neso.energy/api/3/action/datastore_search"

SOURCES = {
    "elexon_metadata": {"url": f"{ELEXON}/datasets/METADATA/latest", "poll": 15, "kind": "url"},
    "elexon_imbalance": {"url": f"{ELEXON}/datasets/IMBALNGC", "poll": 30, "kind": "elexon_dataset"},
    "elexon_demand": {"url": f"{ELEXON}/datasets/INDDEM", "poll": 60, "kind": "elexon_dataset"},
    "elexon_generation": {"url": f"{ELEXON}/datasets/INDGEN", "poll": 60, "kind": "elexon_dataset"},
    "elexon_frequency": {"url": f"{ELEXON}/datasets/FREQ", "poll": 30, "kind": "elexon_dataset"},
    "elexon_wind": {"url": f"{ELEXON}/datasets/WINDFOR", "poll": 120, "kind": "elexon_dataset"},
    "elexon_market_index": {"url": f"{ELEXON}/datasets/MID", "poll": 60, "kind": "elexon_dataset"},
    "neso_da_demand": {"resource": "aec5601a-7f3e-4c4c-bf56-d8e4184d3c5b", "poll": 300, "kind": "neso"},
    "neso_da_wind": {"resource": "b2f03146-f05d-4824-a663-3a4f36090c71", "poll": 300, "kind": "neso"},
    "neso_embedded_renewables_2026": {"resource": "31861619-0b86-47ba-bac2-d008a760af54", "poll": 600, "kind": "neso"},
}

STOP = False


def _stop(*_: Any) -> None:
    global STOP
    STOP = True


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_json(url: str, timeout: int = 20) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch(spec: dict[str, Any]) -> Any:
    if spec["kind"] == "neso":
        q = urllib.parse.urlencode({"resource_id": spec["resource"], "limit": 200, "sort": "_id desc"})
        return get_json(f"{NESO}?{q}")
    if spec["kind"] == "elexon_dataset":
        day = datetime.now(timezone.utc).date().isoformat()
        try:
            return get_json(spec["url"] + "?" + urllib.parse.urlencode({"settlementDate": day}))
        except Exception:
            return get_json(spec["url"])
    return get_json(spec["url"])


def rows(obj: Any) -> list[dict[str, Any]]:
    if isinstance(obj, list):
        return [x for x in obj if isinstance(x, dict)]
    if not isinstance(obj, dict):
        return []
    for key in ("data", "records", "items", "result"):
        val = obj.get(key)
        if isinstance(val, list):
            return [x for x in val if isinstance(x, dict)]
        if isinstance(val, dict):
            for sub in ("records", "data", "items"):
                vv = val.get(sub)
                if isinstance(vv, list):
                    return [x for x in vv if isinstance(x, dict)]
    return [obj]


def num(v: Any) -> float | None:
    if v is None or isinstance(v, bool):
        return None
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def numeric_state(source: str, obj: Any) -> dict[str, float]:
    out: dict[str, float] = {}
    for row in rows(obj)[:20]:
        for k, v in row.items():
            x = num(v)
            if x is not None:
                out[f"{source}.{k}"] = x
    return out


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, sort_keys=True, default=str) + "\n")


def robust_z(hist: deque[float]) -> float | None:
    if len(hist) < 12:
        return None
    med = statistics.median(hist)
    mad = statistics.median(abs(x - med) for x in hist)
    return None if mad <= 1e-12 else 0.67448975 * (hist[-1] - med) / mad


def delta(hist: deque[float], n: int) -> float | None:
    if len(hist) < n + 1:
        return None
    return hist[-1] - list(hist)[-n-1]


def patterns(key: str, hist: deque[float]) -> list[dict[str, Any]]:
    if len(hist) < 3:
        return []
    out = []
    z = robust_z(hist)
    d5 = delta(hist, min(5, len(hist)-1))
    d30 = delta(hist, min(30, len(hist)-1))
    d60 = delta(hist, min(60, len(hist)-1))
    value = hist[-1]
    if z is not None and abs(z) >= 3:
        out.append({"pattern": "ROBUST_OUTLIER", "key": key, "value": value, "z_mad": z,
                    "meaning": "far from recent robust median"})
    if d5 is not None and d30 is not None and d5*d30 > 0 and d5 != 0:
        out.append({"pattern": "PERSISTENT_TREND", "key": key, "value": value, "d5": d5, "d30": d30,
                    "meaning": "short and medium windows move together"})
    if d5 is not None and d30 is not None and d5*d30 < 0:
        out.append({"pattern": "REVERSAL", "key": key, "value": value, "d5": d5, "d30": d30,
                    "meaning": "short move opposes medium trend"})
    if d5 is not None and d30 is not None and abs(d30) > 0 and abs(d5) >= 0.8*abs(d30):
        out.append({"pattern": "ACCELERATION", "key": key, "value": value, "d5": d5, "d30": d30,
                    "meaning": "recent move dominates medium window"})
    if d30 is not None and d60 is not None and d30*d60 < 0:
        out.append({"pattern": "REGIME_TURN", "key": key, "value": value, "d30": d30, "d60": d60,
                    "meaning": "medium direction differs from longer context"})
    return out


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
    tmp.replace(path)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--duration-seconds", type=int, default=0, help="0 = until stopped")
    ap.add_argument("--tick-seconds", type=float, default=1.0)
    ap.add_argument("--output-dir", default="live")
    ap.add_argument("--history", type=int, default=3600)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    signal.signal(signal.SIGINT, _stop)
    signal.signal(signal.SIGTERM, _stop)
    out = Path(a.output_dir)
    history: dict[str, deque[float]] = defaultdict(lambda: deque(maxlen=a.history))
    latest: dict[str, float] = {}
    next_poll = {k: 0.0 for k in SOURCES}
    start = time.monotonic(); ticks = 0

    while not STOP:
        cycle = time.monotonic(); errors = []
        for name, spec in SOURCES.items():
            if cycle < next_poll[name]:
                continue
            next_poll[name] = cycle + float(spec["poll"])
            if a.dry_run:
                continue
            try:
                obj = fetch(spec)
                fresh = numeric_state(name, obj)
                latest.update(fresh)
                append_jsonl(out/"source_updates.jsonl", {"ts": now_iso(), "source": name, "status": "OK", "numeric_fields": len(fresh)})
            except Exception as exc:
                err = {"source": name, "error": f"{type(exc).__name__}:{exc}"}
                errors.append(err)
                append_jsonl(out/"source_updates.jsonl", {"ts": now_iso(), "status": "ERROR", **err})

        events = []
        for k, v in latest.items():
            history[k].append(v)
            events.extend(patterns(k, history[k]))
        compact = []
        seen = set()
        for e in events:
            sig = (e["pattern"], e["key"])
            if sig not in seen:
                seen.add(sig); compact.append(e)
            if len(compact) >= 100:
                break
        state = {"version": VERSION, "ts": now_iso(), "tick": ticks,
                 "numeric_state_fields": len(latest), "pattern_events": compact,
                 "source_errors": errors, "analysis_tick_seconds": a.tick_seconds}
        atomic_json(out/"LATEST.json", state)
        if compact or errors:
            append_jsonl(out/"events.jsonl", state)
        ticks += 1
        if a.duration_seconds and time.monotonic()-start >= a.duration_seconds:
            break
        time.sleep(max(0.05, a.tick_seconds - (time.monotonic()-cycle)))

    atomic_json(out/"FINAL.json", {"version": VERSION, "ended_at": now_iso(), "ticks": ticks,
                                   "duration_seconds": time.monotonic()-start,
                                   "numeric_state_fields": len(latest)})
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
