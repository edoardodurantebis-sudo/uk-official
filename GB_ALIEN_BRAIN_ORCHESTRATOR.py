#!/usr/bin/env python3
"""Persistent market-memory brain for the GB Alien control plane.

This is the interpretive layer that runs after the 1-second publication watcher.
It keeps a compact 5-minute market memory, derives multi-scale trend/acceleration/
reversal/change-point states, builds a physical regime fingerprint, and searches
prior snapshots for nearest analogues plus their subsequent outcomes.

It does NOT execute trades and it does NOT replace the deeper recovered N10 /
Market Memory historical engine. It is the always-on brain between deep runs.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION = "GB_ALIEN_BRAIN_ORCHESTRATOR_1.0.0"
MAX_MEMORY = 2500  # ~8.5 days at one snapshot every 5 minutes


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def finite(x: Any) -> float | None:
    try:
        y = float(x)
        return y if math.isfinite(y) else None
    except Exception:
        return None


def median(xs: list[float]) -> float | None:
    return statistics.median(xs) if xs else None


def mad(xs: list[float]) -> float | None:
    if not xs:
        return None
    m = statistics.median(xs)
    return statistics.median(abs(x - m) for x in xs)


def rz(value: float, hist: list[float]) -> float | None:
    if len(hist) < 12:
        return None
    m = median(hist)
    a = mad(hist)
    if m is None or a is None or a <= 1e-9:
        return None
    return 0.67448975 * (value - m) / a


def atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def read_memory(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            x = json.loads(line)
            if isinstance(x, dict) and isinstance(x.get("v"), dict):
                out.append(x)
        except Exception:
            pass
    return out[-MAX_MEMORY:]


def write_memory(path: Path, rows: list[dict[str, Any]]) -> None:
    rows = rows[-MAX_MEMORY:]
    atomic(path, "".join(json.dumps(x, separators=(",", ":"), sort_keys=True) + "\n" for x in rows))


def latest_values(state: dict[str, Any]) -> dict[str, dict[str, Any]]:
    x = state.get("latest_values", {})
    return x if isinstance(x, dict) else {}


def match_values(vals: dict[str, dict[str, Any]], dataset: str, tokens: tuple[str, ...]) -> list[float]:
    out = []
    for k, rec in vals.items():
        if not str(k).startswith(dataset + "|"):
            continue
        low = str(k).lower()
        if tokens and not all(t.lower() in low for t in tokens):
            continue
        v = finite(rec.get("value") if isinstance(rec, dict) else None)
        if v is not None:
            out.append(v)
    return out


def first(vals: dict[str, dict[str, Any]], dataset: str, token_sets: tuple[tuple[str, ...], ...]) -> float | None:
    for toks in token_sets:
        xs = match_values(vals, dataset, toks)
        if xs:
            return xs[-1]
    return None


def snapshot_from_state(state: dict[str, Any]) -> dict[str, Any]:
    vals = latest_values(state)
    v: dict[str, float] = {}

    specs = {
        "frequency": ("FREQ", (("frequency",),)),
        "imbalance": ("IMBALNGC", (("imbalance",),)),
        "ind_demand": ("INDDEM", (("demand",),)),
        "ind_generation": ("INDGEN", (("generation",),)),
        "margin": ("MELNGC", (("margin",),)),
        "wind_forecast": ("WINDFOR", (("wind",), ("generation",), ("forecast",))),
        "demand_forecast": ("NDF", (("demand",), ("forecast",))),
        "ts_demand_forecast": ("TSDF", (("demand",), ("forecast",))),
        "mid_price": ("MID", (("price",),)),
        "mid_volume": ("MID", (("volume",),)),
    }
    for name, (ds, toks) in specs.items():
        z = first(vals, ds, toks)
        if z is not None:
            v[name] = z

    # Generation components stay series-aware in the watcher, so summing exact
    # fuel families is meaningful here.
    fuels = {
        "wind_gen": "fueltype=wind",
        "ccgt_gen": "fueltype=ccgt",
        "nuclear_gen": "fueltype=nuclear",
        "ps_gen": "fueltype=ps",
        "biomass_gen": "fueltype=biomass",
    }
    for name, tok in fuels.items():
        xs = match_values(vals, "FUELINST", (tok, "generation"))
        if not xs:
            xs = match_values(vals, "FUELHH", (tok, "generation"))
        if xs:
            v[name] = xs[-1]

    inter = []
    for k, rec in vals.items():
        low = str(k).lower()
        if (str(k).startswith("FUELINST|") or str(k).startswith("FUELHH|")) and "fueltype=int" in low and "generation" in low:
            z = finite(rec.get("value") if isinstance(rec, dict) else None)
            if z is not None:
                inter.append(z)
    if inter:
        v["interconnector_net"] = sum(inter)

    # Physical composites. Sign is deliberately not renamed SHORT/LONG here:
    # the indicated-imbalance feed is not the settled NIV target.
    demand = v.get("demand_forecast", v.get("ts_demand_forecast", v.get("ind_demand")))
    wind = v.get("wind_forecast", v.get("wind_gen"))
    if demand is not None and wind is not None:
        v["residual_proxy"] = demand - wind
    if "ccgt_gen" in v and "nuclear_gen" in v:
        v["thermal_base"] = v["ccgt_gen"] + v["nuclear_gen"]
    if "frequency" in v:
        v["frequency_abs_dev"] = abs(v["frequency"] - 50.0)

    return {"ts": state.get("last_heartbeat") or now_iso(), "v": v}


def series(memory: list[dict[str, Any]], key: str) -> list[float]:
    out = []
    for row in memory:
        z = finite(row.get("v", {}).get(key))
        if z is not None:
            out.append(z)
    return out


def delta(xs: list[float], lag: int) -> float | None:
    return xs[-1] - xs[-1-lag] if len(xs) > lag else None


def slope(xs: list[float], n: int) -> float | None:
    if len(xs) < n or n < 2:
        return None
    y = xs[-n:]
    mx = (n - 1) / 2.0
    my = sum(y) / n
    den = sum((i - mx) ** 2 for i in range(n))
    return sum((i - mx) * (yy - my) for i, yy in enumerate(y)) / den if den else None


def metric_state(memory: list[dict[str, Any]], key: str) -> dict[str, Any] | None:
    xs = series(memory, key)
    if len(xs) < 2:
        return None
    d1, d3, d12 = delta(xs, 1), delta(xs, 3), delta(xs, 12)
    prev_d1 = xs[-2] - xs[-3] if len(xs) >= 3 else None
    acc = d1 - prev_d1 if d1 is not None and prev_d1 is not None else None
    z = rz(xs[-1], xs[:-1][-96:])
    s6, s12 = slope(xs, 6), slope(xs, 12)
    tags = []
    ds = [d for d in (d1, d3, d12) if d is not None and abs(d) > 1e-12]
    if len(ds) >= 2 and all(d > 0 for d in ds): tags.append("PERSISTENT_UP")
    if len(ds) >= 2 and all(d < 0 for d in ds): tags.append("PERSISTENT_DOWN")
    if d1 is not None and d12 is not None and d1 * d12 < 0: tags.append("REVERSAL")
    if acc is not None and d12 is not None and abs(acc) > abs(d12) * 0.35: tags.append("ACCELERATION")
    if z is not None and abs(z) >= 3: tags.append("ROBUST_OUTLIER")
    if len(xs) >= 30:
        recent, prior = xs[-6:], xs[-30:-6]
        pr_mad = mad(prior)
        if pr_mad and abs(statistics.mean(recent) - statistics.mean(prior)) > 3 * pr_mad:
            tags.append("CHANGE_POINT")
    return {"value": xs[-1], "n": len(xs), "d1": d1, "d3": d3, "d12": d12,
            "accel": acc, "z_mad": z, "slope6": s6, "slope12": s12, "tags": tags}


def regime(states: dict[str, dict[str, Any]]) -> tuple[str, list[str]]:
    score = 0
    why = []
    r = states.get("residual_proxy")
    m = states.get("margin")
    w = states.get("wind_forecast") or states.get("wind_gen")
    f = states.get("frequency_abs_dev")
    if r and r.get("z_mad") is not None:
        if r["z_mad"] >= 1.5: score += 2; why.append("residual high")
        elif r["z_mad"] <= -1.5: score -= 2; why.append("residual low")
    if m and m.get("z_mad") is not None:
        if m["z_mad"] <= -1.5: score += 2; why.append("margin low")
        elif m["z_mad"] >= 1.5: score -= 2; why.append("margin high")
    if w and "PERSISTENT_UP" in w.get("tags", []): score -= 1; why.append("wind rising")
    if w and "PERSISTENT_DOWN" in w.get("tags", []): score += 1; why.append("wind falling")
    if f and f.get("z_mad") is not None and f["z_mad"] >= 2: score += 1; why.append("frequency stress")
    return ("TIGHT" if score >= 2 else "LOOSE" if score <= -2 else "BALANCED", why)


def vector(row: dict[str, Any], keys: list[str], scale: dict[str, tuple[float, float]]) -> list[float] | None:
    out = []
    for k in keys:
        x = finite(row.get("v", {}).get(k))
        if x is None or k not in scale:
            return None
        med, sc = scale[k]
        out.append((x - med) / sc)
    return out


def analogues(memory: list[dict[str, Any]], keys: list[str]) -> list[dict[str, Any]]:
    if len(memory) < 30 or not keys:
        return []
    scale = {}
    for k in keys:
        xs = series(memory[:-1], k)
        if len(xs) < 20: continue
        mm, aa = median(xs), mad(xs)
        if mm is not None and aa and aa > 1e-9: scale[k] = (mm, aa)
    keys = [k for k in keys if k in scale][:6]
    cur = vector(memory[-1], keys, scale)
    if not cur or len(keys) < 2:
        return []
    scored = []
    # Exclude the latest hour so we do not return the same local episode.
    for i in range(0, len(memory) - 13):
        vv = vector(memory[i], keys, scale)
        if vv is None: continue
        dist = math.sqrt(sum((a-b)**2 for a,b in zip(cur,vv))/len(keys))
        outcome = {}
        j = min(i + 6, len(memory) - 1)
        for target in ("imbalance", "mid_price", "margin", "residual_proxy"):
            a = finite(memory[i].get("v", {}).get(target)); b = finite(memory[j].get("v", {}).get(target))
            if a is not None and b is not None: outcome[f"next30m_{target}_delta"] = b-a
        scored.append({"ts": memory[i].get("ts"), "distance": dist, "outcome": outcome})
    scored.sort(key=lambda x: x["distance"])
    return scored[:5]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", default="live/state.json")
    ap.add_argument("--memory", default="live/market_memory.jsonl")
    ap.add_argument("--output-dir", default="live/brain")
    a = ap.parse_args()

    state = load_json(Path(a.state))
    if not state:
        raise SystemExit("missing/invalid live state")
    snap = snapshot_from_state(state)
    if not snap["v"]:
        raise SystemExit("no usable market values")

    mp = Path(a.memory)
    mem = read_memory(mp)
    if not mem or mem[-1].get("ts") != snap.get("ts"):
        mem.append(snap)
    mem = mem[-MAX_MEMORY:]
    write_memory(mp, mem)

    keys = sorted({k for r in mem for k in r.get("v", {})})
    states = {k: s for k in keys if (s := metric_state(mem, k)) is not None}
    reg, why = regime(states)
    active = []
    for k, s in states.items():
        for tag in s.get("tags", []):
            active.append({"metric": k, "pattern": tag, "value": s["value"], "d1": s.get("d1"),
                           "d12": s.get("d12"), "accel": s.get("accel"), "z_mad": s.get("z_mad")})
    active.sort(key=lambda x: abs(x.get("z_mad") or 0) + (2 if x["pattern"] == "CHANGE_POINT" else 0), reverse=True)

    analog_keys = [k for k in ("residual_proxy","margin","wind_forecast","ind_demand","frequency_abs_dev","mid_price") if k in states]
    ants = analogues(mem, analog_keys)
    out = {"version": VERSION, "generated_at": now_iso(), "source_heartbeat": state.get("last_heartbeat"),
           "memory_snapshots": len(mem), "regime": reg, "regime_reasons": why,
           "active_patterns": active[:40], "states": states, "analogues": ants,
           "note": "Live pattern evidence only; promotion requires PIT/OOS/autopsy in the deep historical engine."}
    od = Path(a.output_dir); od.mkdir(parents=True, exist_ok=True)
    atomic(od/"LATEST.json", json.dumps(out, indent=2, sort_keys=True) + "\n")

    lines = ["# GB Alien Brain — live market memory", "", f"Engine: `{VERSION}`  ",
             f"Heartbeat: `{state.get('last_heartbeat')}`  ", f"Memory snapshots: **{len(mem)}**  ",
             f"Current physical regime: **{reg}**", ""]
    if why: lines += ["Regime read: " + ", ".join(why) + ".", ""]
    lines += ["## Active patterns", ""]
    if not active: lines.append("No qualified multi-scale pattern yet; memory is still warming up.")
    else:
        for e in active[:15]:
            lines.append(f"- **{e['pattern']}** `{e['metric']}` value={e['value']:.4g} d1={e['d1']} d12={e['d12']} z={e['z_mad']}")
    lines += ["", "## Nearest historical live analogues", ""]
    if not ants: lines.append("Not enough accumulated live memory yet.")
    else:
        for x in ants:
            lines.append(f"- `{x['ts']}` distance={x['distance']:.3f} → {x['outcome']}")
    lines += ["", "Deep rule promotion remains delegated to the recovered Market Memory/N10 lineage engine.", ""]
    atomic(od/"LATEST.md", "\n".join(lines))
    print(json.dumps({"version": VERSION, "memory": len(mem), "regime": reg, "patterns": len(active), "analogues": len(ants)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
