#!/usr/bin/env python3
"""Registry-driven, PIT-safe GB imbalance discovery engine.

Normalized Elexon sign convention used throughout:
    NIV > 0  -> system SHORT
    NIV < 0  -> system LONG

Raw sign is source-lineage dependent. Canonical historical master_wide.niv is
internal/inverted and must be negated; public Elexon/BMRS NIV must not be flipped.

Machine output can reach REVIEW_READY only; promotion/trading stays external.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from itertools import combinations
from pathlib import Path
from typing import Any, Optional

import numpy as np
import pandas as pd

ENGINE_VERSION = "GB_NIGHTLY_DISCOVERY_V1.1.1_NIV_LINEAGE"
NIV_SOURCE_MASTER_INTERNAL_INVERTED = "MASTER_INTERNAL_INVERTED"
NIV_SOURCE_ELEXON_OFFICIAL = "ELEXON_OFFICIAL"
VALID_GATES = {"DA", "IDA1", "IDA2"}
VALID_TARGETS = {"SIGN", "PRICE_SHORT", "PRICE_LONG"}
VALID_RES = {"PT15", "PT30", "PT60"}
ALLOWED_DAY_COUNTS = {46, 48, 50}
REG_REQUIRED = ["feature_id", "column_name", "family", "lineage_root", "source", "unit", "resolution",
                "time_domain", "pit_status", "gate_DA", "gate_IDA1", "gate_IDA2", "discovery_enabled"]


def boolish(v: Any) -> bool:
    if pd.isna(v):
        return False
    return str(v).strip().lower() in {"1", "true", "yes", "y", "si", "sì"}


def stable_json(v: Any) -> str:
    return json.dumps(v, sort_keys=True, separators=(",", ":"), default=str)


def stable_hash(v: Any, n: int = 24) -> str:
    return hashlib.sha256(stable_json(v).encode()).hexdigest()[:n]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_table(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".parquet":
        return pd.read_parquet(path)
    if path.suffix.lower() in {".csv", ".txt"}:
        return pd.read_csv(path)
    raise RuntimeError(f"UNSUPPORTED_TABLE:{path}")


def load_registry(path: Path) -> pd.DataFrame:
    r = read_table(path).copy()
    missing = [c for c in REG_REQUIRED if c not in r.columns]
    if missing:
        raise RuntimeError(f"REGISTRY_MISSING_COLUMNS:{missing}")
    r["feature_id"] = r["feature_id"].astype(str).str.strip()
    r["resolution"] = r["resolution"].astype(str).str.upper()
    r["time_domain"] = r["time_domain"].astype(str).str.upper()
    r["pit_status"] = r["pit_status"].astype(str).str.upper()
    if r["feature_id"].duplicated().any():
        raise RuntimeError("REGISTRY_DUPLICATE_FEATURE_ID")
    return r


def normalize_panel(df: pd.DataFrame, default_resolution: str = "") -> pd.DataFrame:
    x = df.copy()
    req = ["gb_delivery_date", "gb_sp", "delivery_start_utc", "gb_time_certified"]
    missing = [c for c in req if c not in x.columns]
    if missing:
        raise RuntimeError(f"GB_TIME_KEYS_OR_CERTIFICATION_MISSING:{missing}")
    x["gb_delivery_date"] = pd.to_datetime(x["gb_delivery_date"], errors="coerce").dt.normalize()
    x["gb_sp"] = pd.to_numeric(x["gb_sp"], errors="coerce").astype("Int64")
    x["delivery_start_utc"] = pd.to_datetime(x["delivery_start_utc"], errors="coerce", utc=True)
    x["gb_time_certified"] = x["gb_time_certified"].map(boolish)
    if "resolution" not in x.columns:
        if not default_resolution:
            raise RuntimeError("RESOLUTION_REQUIRED")
        x["resolution"] = default_resolution
    x["resolution"] = x["resolution"].astype(str).str.upper()
    bad = sorted(set(x.loc[~x["resolution"].isin(VALID_RES), "resolution"].dropna()))
    if bad:
        raise RuntimeError(f"BAD_RESOLUTION_VALUES:{bad}")
    x = x[x["gb_time_certified"]].copy()
    if x.duplicated(["delivery_start_utc", "resolution"]).any():
        raise RuntimeError("DUPLICATE_GB_PHYSICAL_IDENTITY")
    counts = x.groupby(["gb_delivery_date", "resolution"])["gb_sp"].nunique()
    invalid = sorted({int(v) for v in counts if int(v) not in ALLOWED_DAY_COUNTS})
    if invalid:
        raise RuntimeError(f"GB_PERIOD_COUNT_INVALID:{invalid}")
    return x.sort_values(["delivery_start_utc", "resolution"]).reset_index(drop=True)


def add_targets(df: pd.DataFrame, niv_col: str, price_col: str, niv_source: str = NIV_SOURCE_MASTER_INTERNAL_INVERTED) -> pd.DataFrame:
    if niv_col not in df.columns or price_col not in df.columns:
        raise RuntimeError(f"TARGET_COLUMNS_MISSING:niv={niv_col in df.columns}:price={price_col in df.columns}")
    if niv_source not in {NIV_SOURCE_MASTER_INTERNAL_INVERTED, NIV_SOURCE_ELEXON_OFFICIAL}:
        raise RuntimeError(f"NIV_LINEAGE_UNRESOLVED:{niv_source}")
    x = df.copy()
    raw = pd.to_numeric(x[niv_col], errors="coerce")
    x["niv_raw_source"] = raw
    if niv_source == NIV_SOURCE_MASTER_INTERNAL_INVERTED:
        x["niv_master_raw"] = raw
        norm = -raw
    else:
        norm = raw
    x["niv_elexon_sign"] = norm
    x["niv"] = norm
    x["psbil"] = pd.to_numeric(x[price_col], errors="coerce")
    x["short_flag"] = np.where(norm > 0, 1.0, np.where(norm < 0, 0.0, np.nan))
    x["long_flag"] = np.where(norm < 0, 1.0, np.where(norm > 0, 0.0, np.nan))
    return x


def target_series(df: pd.DataFrame, target: str) -> pd.Series:
    if target == "SIGN":
        return df["short_flag"].astype(float)
    if target == "PRICE_SHORT":
        return df["psbil"].where(df["niv"] > 0).astype(float)
    if target == "PRICE_LONG":
        return df["psbil"].where(df["niv"] < 0).astype(float)
    raise ValueError(target)


def eligible_registry(reg: pd.DataFrame, df: pd.DataFrame, gate: str, resolution: str) -> pd.DataFrame:
    gate_col = f"gate_{gate}"
    r = reg.copy()
    r = r[(r["time_domain"] == "GB_PHYSICAL") & (r["resolution"] == resolution)]
    r = r[r["pit_status"].eq("CERTIFIED")]
    r = r[r["discovery_enabled"].map(boolish) & r[gate_col].map(boolish)]
    r = r[r["column_name"].isin(df.columns)]
    forbidden = {"niv", "niv_raw_source", "niv_master_raw", "niv_elexon_sign", "psbil", "short_flag", "long_flag", "gb_sp", "delivery_start_utc", "gb_delivery_date"}
    return r[~r["column_name"].str.lower().isin(forbidden)].copy()


def dev_mask(date_s: pd.Series, months: int) -> pd.Series:
    periods = sorted(pd.PeriodIndex(date_s, freq="M").unique())
    if len(periods) <= months:
        raise RuntimeError(f"INSUFFICIENT_MONTHS:have={len(periods)} need>{months}")
    return pd.Series(pd.PeriodIndex(date_s, freq="M").isin(periods[:months]), index=date_s.index)


def cond_mask(df: pd.DataFrame, conds: list[dict[str, Any]]) -> pd.Series:
    m = pd.Series(True, index=df.index)
    for c in conds:
        s = pd.to_numeric(df[c["column_name"]], errors="coerce")
        m &= s <= c["threshold"] if c["op"] == "<=" else s >= c["threshold"]
    return m.fillna(False)


def effect(df: pd.DataFrame, y: pd.Series, conds: list[dict[str, Any]]):
    valid = y.notna()
    hit = cond_mask(df, conds) & valid
    n = int(hit.sum())
    days = int(df.loc[hit, "gb_delivery_date"].nunique())
    if n == 0 or valid.sum() == 0:
        return n, days, np.nan
    return n, days, float(y.loc[hit].mean() - y.loc[valid].mean())


def discover(train: pd.DataFrame, y: pd.Series, reg: pd.DataFrame, gate: str, target: str, resolution: str,
             min_cases: int, min_days: int, top_features: int, family_cap: int, max_pairs: int):
    seeds = []
    for _, row in reg.iterrows():
        s = pd.to_numeric(train[row.column_name], errors="coerce").dropna()
        if len(s) < max(20, min_cases):
            continue
        for op, th, label in [("<=", s.quantile(.25), "LOW"), (">=", s.quantile(.75), "HIGH")]:
            if not np.isfinite(th):
                continue
            c = [{"feature_id": row.feature_id, "column_name": row.column_name, "op": op,
                  "threshold": float(th), "label": label}]
            n, days, e = effect(train, y, c)
            if n >= min_cases and days >= min_days and np.isfinite(e):
                seeds.append((abs(e), n, days, e, row.to_dict(), c))
    seeds.sort(key=lambda z: (-z[0], -z[1], str(z[4]["family"]), str(z[4]["feature_id"])))
    chosen, fam_count = [], {}
    for z in seeds:
        fam = str(z[4]["family"])
        if fam_count.get(fam, 0) >= family_cap:
            continue
        chosen.append(z); fam_count[fam] = fam_count.get(fam, 0) + 1
        if len(chosen) >= top_features:
            break

    out, seen = [], set()
    def emit(conds, rows, kind):
        key = stable_hash({"gate": gate, "target": target, "resolution": resolution,
                           "conditions": sorted([(c["feature_id"], c["op"], round(c["threshold"], 10)) for c in conds])})
        if key in seen:
            return
        seen.add(key)
        n, days, e = effect(train, y, conds)
        if n < min_cases or days < min_days or not np.isfinite(e):
            return
        out.append({"candidate_key": key, "gate": gate, "target": target, "resolution": resolution,
                    "search_family": kind, "feature_ids": "|".join(str(r["feature_id"]) for r in rows),
                    "feature_families": "|".join(sorted({str(r["family"]) for r in rows})),
                    "lineage_roots": "|".join(sorted({str(r["lineage_root"]) for r in rows})),
                    "conditions": conds, "expected_direction": 1 if e >= 0 else -1,
                    "dev_n": n, "dev_days": days, "dev_effect": float(e)})
    for z in chosen:
        emit(z[5], [z[4]], "SINGLE")
    pairs = 0
    for a, b in combinations(chosen, 2):
        if pairs >= max_pairs:
            break
        if a[4]["lineage_root"] == b[4]["lineage_root"] or a[4]["family"] == b[4]["family"]:
            continue
        emit(a[5] + b[5], [a[4], b[4]], "PAIR")
        pairs += 1
    return out


def binom_p(values: np.ndarray) -> Optional[float]:
    x = values[np.isfinite(values) & (values != 0)]
    n = len(x)
    if n < 8:
        return None
    pos = int((x > 0).sum()); k = min(pos, n - pos)
    tail = sum(math.comb(n, i) for i in range(k + 1)) / (2 ** n)
    return float(min(1.0, 2 * tail))


def validate(df: pd.DataFrame, y: pd.Series, cand: dict[str, Any], train_months: int):
    periods = sorted(pd.PeriodIndex(df["gb_delivery_date"], freq="M").unique())
    oos = periods[train_months:]
    month_effects, hit_days, hits = {}, set(), 0
    for p in oos:
        m = pd.PeriodIndex(df["gb_delivery_date"], freq="M") == p
        q, tq = df.loc[m], y.loc[m]
        h = cond_mask(q, cand["conditions"]) & tq.notna()
        if h.sum() < 5:
            month_effects[str(p)] = None
            continue
        hits += int(h.sum()); hit_days.update(q.loc[h, "gb_delivery_date"].dt.strftime("%Y-%m-%d"))
        month_effects[str(p)] = float(tq.loc[h].mean() - tq.mean())
    vals = [v for v in month_effects.values() if v is not None and np.isfinite(v)]
    med = float(np.median(vals)) if vals else None
    consistency = float(np.mean([np.sign(v) == cand["expected_direction"] for v in vals])) if vals else None

    mask = pd.PeriodIndex(df["gb_delivery_date"], freq="M").isin(oos)
    q, tq = df.loc[mask], y.loc[mask]
    h = cond_mask(q, cand["conditions"]) & tq.notna()
    daily = []
    for _, g in q.assign(_y=tq, _h=h).groupby("gb_delivery_date"):
        a, b = g.loc[g._h, "_y"].dropna(), g.loc[~g._h, "_y"].dropna()
        if len(a) and len(b):
            daily.append(float(a.mean() - b.mean()))
    arr = np.asarray(daily, float)
    p = binom_p(arr)
    no_best = None
    if len(arr) >= 2:
        score = arr * cand["expected_direction"]
        no_best = float(np.delete(arr, int(np.argmax(score))).mean())
    robust = bool(len(vals) >= 2 and consistency is not None and consistency >= .60 and med is not None
                  and np.sign(med) == cand["expected_direction"] and no_best is not None
                  and np.sign(no_best) == cand["expected_direction"])
    return {"candidate_key": cand["candidate_key"], "oos_months": len(oos), "folds_with_hits": len(vals),
            "oos_days": len(hit_days), "oos_hits": hits, "median_oos_effect": med,
            "sign_consistency": consistency, "pvalue": p, "qvalue": None, "fdr_pass": False,
            "no_best_day_effect": no_best, "robust": robust, "month_effects": month_effects}


def bh(rows: list[dict[str, Any]], alpha: float = .10):
    ids = [(i, r["pvalue"]) for i, r in enumerate(rows) if r["pvalue"] is not None and np.isfinite(r["pvalue"])]
    ids.sort(key=lambda z: z[1]); m = len(ids); prev = 1.0
    for j in range(m - 1, -1, -1):
        i, p = ids[j]; q = min(prev, p * m / (j + 1)); prev = q
        rows[i]["qvalue"] = float(q); rows[i]["fdr_pass"] = bool(q <= alpha)


def persist_queue(batch: pd.DataFrame, queue_dir: Path):
    queue_dir.mkdir(parents=True, exist_ok=True)
    qpath, hpath = queue_dir / "candidate_queue.csv", queue_dir / "candidate_history.csv"
    old = pd.read_csv(qpath) if qpath.exists() else pd.DataFrame()
    hist = pd.read_csv(hpath) if hpath.exists() else pd.DataFrame()
    now = pd.Timestamp.now(tz="UTC").isoformat()
    b = batch.copy(); b["last_seen"] = now
    if old.empty:
        b["first_seen"] = now; b["times_seen"] = 1; q = b
    else:
        meta = old[[c for c in ["candidate_key", "first_seen", "times_seen"] if c in old.columns]].copy()
        b = b.merge(meta, on="candidate_key", how="left")
        b["first_seen"] = b["first_seen"].fillna(now)
        b["times_seen"] = pd.to_numeric(b["times_seen"], errors="coerce").fillna(0).astype(int) + 1
        q = pd.concat([old[~old.candidate_key.isin(b.candidate_key)], b], ignore_index=True)
    h = pd.concat([hist, b], ignore_index=True)
    q.to_csv(qpath, index=False); h.to_csv(hpath, index=False)
    return q


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--master-path", required=True); p.add_argument("--exante-path", default=""); p.add_argument("--join-keys", default="")
    p.add_argument("--registry-path", required=True); p.add_argument("--output-dir", required=True); p.add_argument("--queue-dir", required=True)
    p.add_argument("--gates", default="DA,IDA1,IDA2"); p.add_argument("--targets", default="SIGN,PRICE_SHORT,PRICE_LONG")
    p.add_argument("--niv-col", default="niv"); p.add_argument("--price-col", default="psbil"); p.add_argument("--niv-source", choices=[NIV_SOURCE_MASTER_INTERNAL_INVERTED,NIV_SOURCE_ELEXON_OFFICIAL], default=NIV_SOURCE_MASTER_INTERNAL_INVERTED); p.add_argument("--default-resolution", default="")
    p.add_argument("--min-train-months", type=int, default=6); p.add_argument("--min-cases", type=int, default=30); p.add_argument("--min-days", type=int, default=8)
    p.add_argument("--top-features", type=int, default=30); p.add_argument("--per-family-seed-cap", type=int, default=4); p.add_argument("--max-pairs", type=int, default=300)
    p.add_argument("--from-date", default=""); p.add_argument("--to-date", default=""); p.add_argument("--smoke", action="store_true")
    return p.parse_args()


def main() -> int:
    args = parse_args(); t0 = time.perf_counter(); run_ts = pd.Timestamp.now(tz="UTC")
    gates = [x.strip().upper() for x in args.gates.split(",") if x.strip()]
    targets = [x.strip().upper() for x in args.targets.split(",") if x.strip()]
    if not set(gates) <= VALID_GATES or not set(targets) <= VALID_TARGETS:
        raise RuntimeError("BAD_RUN_SELECTION")
    master = normalize_panel(read_table(Path(args.master_path)), args.default_resolution)
    if args.exante_path:
        keys = [x.strip() for x in args.join_keys.split(",") if x.strip()]
        if not keys:
            raise RuntimeError("EXANTE_JOIN_KEYS_REQUIRED")
        ex = normalize_panel(read_table(Path(args.exante_path)), args.default_resolution)
        if master.duplicated(keys).any() or ex.duplicated(keys).any():
            raise RuntimeError("EXANTE_JOIN_KEYS_NOT_UNIQUE")
        add = [c for c in ex.columns if c not in keys and c not in master.columns]
        master = master.merge(ex[keys + add], on=keys, how="left", validate="one_to_one")
    master = add_targets(master, args.niv_col, args.price_col, args.niv_source)
    if args.from_date:
        master = master[master.gb_delivery_date >= pd.Timestamp(args.from_date).normalize()]
    if args.to_date:
        master = master[master.gb_delivery_date <= pd.Timestamp(args.to_date).normalize()]
    reg = load_registry(Path(args.registry_path))
    run_id = f"NIGHTLY_V1_{run_ts:%Y%m%d_%H%M%S}"
    run_dir = Path(args.output_dir) / run_id; run_dir.mkdir(parents=True, exist_ok=True)
    all_rows = []
    for resolution in sorted(set(master.resolution) & VALID_RES):
        df = master[master.resolution.eq(resolution)].copy()
        if df.empty:
            continue
        dm = dev_mask(df.gb_delivery_date, args.min_train_months)
        for gate in gates:
            er = eligible_registry(reg, df, gate, resolution)
            if er.empty:
                continue
            for target in targets:
                y = target_series(df, target); train = df.loc[dm]; yt = y.loc[dm]
                cands = discover(train, yt, er, gate, target, resolution, args.min_cases, args.min_days,
                                 args.top_features, args.per_family_seed_cap, args.max_pairs)
                if args.smoke:
                    cands = cands[:20]
                vals = [validate(df, y, c, args.min_train_months) for c in cands]
                bh(vals)
                vmap = {v["candidate_key"]: v for v in vals}
                for c in cands:
                    v = vmap[c["candidate_key"]]
                    status = "REVIEW_READY" if (v["robust"] and v["fdr_pass"] and v["oos_days"] >= args.min_days) else "VALIDATING"
                    row = {k: val for k, val in c.items() if k != "conditions"}
                    row.update({k: val for k, val in v.items() if k not in {"candidate_key", "month_effects"}})
                    row["conditions_json"] = stable_json(c["conditions"]); row["month_effects_json"] = stable_json(v["month_effects"])
                    row["machine_status"] = status; all_rows.append(row)
    batch = pd.DataFrame(all_rows)
    batch.to_csv(run_dir / "candidate_batch.csv", index=False)
    queue = persist_queue(batch, Path(args.queue_dir)) if not batch.empty else batch
    review = queue.copy()
    if not review.empty:
        review["_ord"] = review.machine_status.map({"REVIEW_READY": 0, "VALIDATING": 1}).fillna(9)
        review = review.sort_values(["_ord", "qvalue", "oos_days"], ascending=[True, True, False], na_position="last").drop(columns="_ord")
    review.to_csv(run_dir / "TRADER_REVIEW_QUEUE.csv", index=False)
    manifest = {"engine_version": ENGINE_VERSION, "run_id": run_id, "created_at_utc": run_ts.isoformat(),
                "master_sha256": sha256_file(Path(args.master_path)), "registry_sha256": sha256_file(Path(args.registry_path)),
                "niv_source": args.niv_source, "sign_convention": "ELEXON_NORMALIZED_NIV_POSITIVE_SHORT_NEGATIVE_LONG",
                "physical_identity": "delivery_start_utc", "dst_policy": "46_48_50_FAIL_CLOSED",
                "candidate_generation": "SINGLE_PLUS_PAIR_ONLY", "promotion_policy": "MACHINE_MAX_REVIEW_READY",
                "candidate_count": int(len(batch)), "review_ready_count": int((batch.machine_status == "REVIEW_READY").sum()) if not batch.empty else 0,
                "runtime_seconds": round(time.perf_counter() - t0, 3)}
    (run_dir / "RUN_MANIFEST.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(run_dir)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        raise
