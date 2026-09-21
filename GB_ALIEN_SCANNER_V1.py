#!/usr/bin/env python3
"""Broad PIT-aware pattern scanner for UNDER THE BID / GB.

V1 scans every certified delivery row at native source resolution. It does not
invent minute data from PT30 inputs. When tick/minute feeds are supplied later,
the same pattern factory can operate on those rows.

The scanner is a candidate generator, never an execution engine. It creates
raw/revision/profile-trend features, tests threshold states in development and
strict later-period OOS, applies robustness/autopsy checks, and writes a compact
candidate catalogue plus case-study dates.
"""
from __future__ import annotations
import argparse, json, math, re
from pathlib import Path
import numpy as np
import pandas as pd
from gb_legacy_canonicalizer import canonicalize

VERSION = "GB_ALIEN_SCANNER_V1.0.1_NIV_LINEAGE"
VINTAGE_RE = re.compile(r"^(?P<root>.+)_v(?P<v>\d+)_dd(?P<dd>[01])$")
NIV_SOURCE_MASTER_INTERNAL_INVERTED = "MASTER_INTERNAL_INVERTED"
NIV_SOURCE_ELEXON_OFFICIAL = "ELEXON_OFFICIAL"
FORBIDDEN_PREFIX = ("actual_", "error_", "fuelhh_", "boa_", "total_boa", "niv_", "niv_vs_", "itsdo_", "indo_")
FORBIDDEN_EXACT = {"niv", "psbil", "pida2", "actual_residual_load", "actual_net_demand"}

def read_table(path: Path) -> pd.DataFrame:
    return pd.read_parquet(path) if path.suffix.lower() == ".parquet" else pd.read_csv(path, low_memory=False)

def gate_allows_master(col: str, gate: str) -> bool:
    if col in FORBIDDEN_EXACT or col.startswith(FORBIDDEN_PREFIX): return False
    m = VINTAGE_RE.match(col)
    if m:
        v, dd = int(m.group("v")), int(m.group("dd"))
        if gate == "DA": return dd == 1 and v <= 8
        if gate == "IDA1": return dd == 1 and v <= 16
        if gate == "IDA2": return (dd == 1 and v <= 20) or (dd == 0 and v <= 8)
    if col in {"forecast_temp_anomaly_v7_dd1", "forecast_temp_anomaly_v8_dd1"}: return True
    if col == "pda_gbp": return gate in {"IDA1", "IDA2"}
    if col == "pida1": return gate == "IDA2"
    return False

def gate_allows_exante(col: str, gate: str) -> bool:
    if gate == "DA": return False
    low = col.lower()
    if "expost" in low or "taglio_" in low: return False
    safe = ("ic_da_", "remit_da_", "wind_scotland_da_", "cap_scotland_da_", "b6_pressure_exante", "b6_pressure_giganti_exante")
    if col.startswith(safe): return True
    return col in {"derated_margin_da_1830_mw", "lolp_da_1830"}

def family(col: str) -> str:
    c = col.lower()
    for k in ["residual_load", "net_demand", "wind", "solar", "demand", "temp", "b6", "remit", "margin", "lolp", "ic_da", "price"]:
        if k in c: return k
    return c.split("_")[0]

def canonical_merge(master: pd.DataFrame, exante: pd.DataFrame | None) -> tuple[pd.DataFrame, dict]:
    m, ma = canonicalize(master); m = m[m["gb_time_certified"]].copy(); audit = {"master": ma}
    if exante is not None:
        e, ea = canonicalize(exante); e = e[e["gb_time_certified"]].copy(); audit["exante"] = ea
        keep = [c for c in e.columns if c not in master.columns or c == "delivery_start_utc"]
        e = e[keep].drop_duplicates("delivery_start_utc")
        m = m.merge(e, on="delivery_start_utc", how="left", validate="one_to_one", suffixes=("", "_exante"))
    return m.sort_values("delivery_start_utc").reset_index(drop=True), audit

def add_targets(x: pd.DataFrame, niv_source: str = NIV_SOURCE_MASTER_INTERNAL_INVERTED) -> pd.DataFrame:
    if niv_source not in {NIV_SOURCE_MASTER_INTERNAL_INVERTED, NIV_SOURCE_ELEXON_OFFICIAL}:
        raise RuntimeError(f"NIV_LINEAGE_UNRESOLVED:{niv_source}")
    y = x.copy(); raw = pd.to_numeric(y["niv"], errors="coerce")
    y["niv_raw_source"] = raw
    if niv_source == NIV_SOURCE_MASTER_INTERNAL_INVERTED:
        y["niv_master_raw"] = raw
        niv = -raw
    else:
        niv = raw
    y["niv_elexon_sign"] = niv
    y["niv"] = niv
    y["short_flag"] = np.where(niv > 0, 1.0, np.where(niv < 0, 0.0, np.nan))
    y["long_flag"] = np.where(niv < 0, 1.0, np.where(niv > 0, 0.0, np.nan))
    ps = pd.to_numeric(y["psbil"], errors="coerce"); y["target_price"] = ps
    if "pda_gbp" in y: y["spread_da"] = ps - pd.to_numeric(y["pda_gbp"], errors="coerce")
    if "pida1" in y: y["spread_ida1"] = ps - pd.to_numeric(y["pida1"], errors="coerce")
    if "pida2" in y: y["spread_ida2"] = ps - pd.to_numeric(y["pida2"], errors="coerce")
    return y

def revision_features(df: pd.DataFrame, cols: list[str]) -> dict[str, pd.Series]:
    groups = {}
    for c in cols:
        m = VINTAGE_RE.match(c)
        if m: groups.setdefault((m.group("root"), int(m.group("dd"))), []).append((int(m.group("v")), c))
    out = {}
    for (root, dd), items in groups.items():
        items = sorted(items)
        if len(items) >= 2:
            v0, c0 = items[0]; v1, c1 = items[-1]
            out[f"REV__{root}__v{v1}-v{v0}__dd{dd}"] = pd.to_numeric(df[c1], errors="coerce") - pd.to_numeric(df[c0], errors="coerce")
        if len(items) >= 3:
            (va, ca), (vb, cb), (vc, cc) = items[-3:]
            r1 = pd.to_numeric(df[cb], errors="coerce") - pd.to_numeric(df[ca], errors="coerce")
            r2 = pd.to_numeric(df[cc], errors="coerce") - pd.to_numeric(df[cb], errors="coerce")
            out[f"ACCEL__{root}__v{va}-{vb}-{vc}__dd{dd}"] = r2-r1
    return out

def build_features(df: pd.DataFrame, gate: str) -> tuple[pd.DataFrame, dict[str, str]]:
    master_cols = [c for c in df.columns if gate_allows_master(c, gate) and pd.api.types.is_numeric_dtype(df[c])]
    exante_cols = [c for c in df.columns if gate_allows_exante(c, gate) and pd.api.types.is_numeric_dtype(df[c])]
    base = list(dict.fromkeys(master_cols + exante_cols)); data = {}; fmap = {}
    for c in base: data[c] = pd.to_numeric(df[c], errors="coerce"); fmap[c] = family(c)
    for name, ser in revision_features(df, master_cols).items(): data[name] = ser; fmap[name] = family(name)
    for c in base[:50]:
        z = pd.to_numeric(df[c], errors="coerce")
        data[f"D1__{c}"] = z.groupby(df["gb_delivery_date"]).diff(1); fmap[f"D1__{c}"] = family(c)
        data[f"D4__{c}"] = z.groupby(df["gb_delivery_date"]).diff(4); fmap[f"D4__{c}"] = family(c)
    return pd.DataFrame(data, index=df.index), fmap

def sign_test_p(vals: np.ndarray) -> float | None:
    vals = vals[np.isfinite(vals) & (vals != 0)]; n = len(vals)
    if n < 8: return None
    pos = int((vals > 0).sum()); k = min(pos, n-pos)
    tail = sum(math.comb(n, i) for i in range(k+1)) / (2**n)
    return float(min(1.0, 2*tail))

def _fast_effect(target: np.ndarray, valid: np.ndarray, hit: np.ndarray) -> tuple[int, float]:
    h = valid & hit; n = int(h.sum())
    if n == 0: return 0, np.nan
    return n, float(np.nanmean(target[h]) - np.nanmean(target[valid]))

def _autopsy(df, feat, target, threshold, op, split_date, direction):
    valid = feat.notna() & target.notna() & (df["gb_delivery_date"] >= split_date)
    cond = (feat <= threshold) if op == "<=" else (feat >= threshold)
    q = pd.DataFrame({"d": df.loc[valid, "gb_delivery_date"], "t": target.loc[valid], "h": cond.loc[valid]})
    monthly = []
    for _, z in q.groupby(q["d"].dt.to_period("M")):
        a = z.loc[z.h, "t"]
        if len(a) >= 5: monthly.append(float(a.mean() - z.t.mean()))
    consistency = float(np.mean([np.sign(v) == direction for v in monthly])) if monthly else np.nan
    daily_rows = []
    for d, z in q.groupby("d"):
        a, b = z.loc[z.h, "t"], z.loc[~z.h, "t"]
        if len(a) and len(b): daily_rows.append((str(d.date()), float(a.mean()-b.mean())))
    arr = np.asarray([v for _, v in daily_rows], float); p = sign_test_p(arr); no_best = np.nan
    if len(arr) >= 2:
        no_best = float(np.delete(arr, int(np.argmax(arr*direction))).mean())
    worst = sorted(daily_rows, key=lambda z: z[1]*direction)[:3]
    return consistency, p, no_best, len(daily_rows), json.dumps(worst, separators=(",", ":"))

def scan(df: pd.DataFrame, gate: str, targets: list[str], split: str) -> pd.DataFrame:
    feats, fmap = build_features(df, gate); split_date = pd.Timestamp(split)
    dev = (df["gb_delivery_date"] < split_date).to_numpy(); oos = (df["gb_delivery_date"] >= split_date).to_numpy()
    prelim = []; target_arrays = {t: pd.to_numeric(df[t], errors="coerce").to_numpy(float) for t in targets if t in df}
    for name in feats.columns:
        ser = pd.to_numeric(feats[name], errors="coerce"); x = ser.to_numpy(float); train = x[dev & np.isfinite(x)]
        if len(train) < 300 or len(np.unique(train)) < 10: continue
        for op, qv in [("<=",.10),("<=",.25),(">=",.75),(">=",.90)]:
            th = float(np.nanquantile(train, qv)); hit = (x <= th) if op == "<=" else (x >= th); xvalid = np.isfinite(x)
            for tname, y in target_arrays.items():
                yvalid = np.isfinite(y); nd, ed = _fast_effect(y, dev & xvalid & yvalid, hit); no, eo = _fast_effect(y, oos & xvalid & yvalid, hit)
                if nd < 100 or no < 30 or not np.isfinite(ed) or not np.isfinite(eo) or ed == 0: continue
                same = bool(np.sign(ed) == np.sign(eo)); scale = float(np.nanstd(y[oos & yvalid])) or 1.0
                score = (3.0 if same else 0.0) + min(3.0, abs(eo)/scale*10.0) + min(2.0, math.log10(no+1)/2)
                prelim.append({"feature":name,"family":fmap.get(name,family(name)),"target":tname,"op":op,"threshold":th,"dev_n":nd,"dev_effect":ed,"oos_n":no,"oos_effect":eo,"direction":1 if ed>0 else -1,"same_sign":same,"pre_score":score})
    if not prelim: return pd.DataFrame()
    pre = pd.DataFrame(prelim).sort_values(["same_sign","pre_score","oos_n"], ascending=[False,False,False])
    selected = pre.groupby("target", group_keys=False).head(250).copy(); rows = []
    for _, r in selected.iterrows():
        consistency, p, no_best, daily_n, worst = _autopsy(df, feats[r.feature], pd.to_numeric(df[r.target], errors="coerce"), r.threshold, r.op, split_date, int(r.direction))
        robust = bool(r.same_sign and consistency >= .60 and np.isfinite(no_best) and np.sign(no_best) == int(r.direction))
        z = r.to_dict(); z.update({"monthly_consistency":consistency,"daily_sign_p":p,"no_best_day_effect":no_best,"oos_days":daily_n,"worst_case_dates":worst,"robust":robust})
        z["score"] = float(r.pre_score) + (3 if robust else 0) + (consistency if np.isfinite(consistency) else 0); rows.append(z)
    return pd.DataFrame(rows).sort_values(["robust","score","oos_days","oos_n"], ascending=[False,False,False,False])

def write_summary(out, path, gate, split, audit):
    lines=[f"# GB Alien Scanner — {gate}","",f"Version: `{VERSION}`  ",f"OOS starts: `{split}`","",f"Certified master days: **{audit['master']['certified_days']}**",""]
    if out.empty: lines.append("No candidate passed minimum support.")
    else:
        lines += [f"Candidates in autopsy set: **{len(out)}**",f"Robust V1 candidates: **{int(out.robust.sum())}**","","## Top candidates","","|feature|target|state|dev effect|OOS effect|OOS days|monthly consistency|","|---|---|---|---:|---:|---:|---:|"]
        for _,r in out.head(20).iterrows():
            mc=f"{r.monthly_consistency:.1%}" if pd.notna(r.monthly_consistency) else "NA"
            lines.append(f"|{r.feature}|{r.target}|{r.op} {r.threshold:.3g}|{r.dev_effect:.4g}|{r.oos_effect:.4g}|{int(r.oos_days)}|{mc}|")
    path.write_text("\n".join(lines)+"\n",encoding="utf-8")

def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("--master",required=True); p.add_argument("--exante",default=""); p.add_argument("--gate",choices=["DA","IDA1","IDA2"],default="IDA1"); p.add_argument("--targets",default="short_flag,spread_ida1"); p.add_argument("--oos-from",default="2026-01-01"); p.add_argument("--output-dir",default="alien_output"); p.add_argument("--niv-source",choices=[NIV_SOURCE_MASTER_INTERNAL_INVERTED,NIV_SOURCE_ELEXON_OFFICIAL],default=NIV_SOURCE_MASTER_INTERNAL_INVERTED); a=p.parse_args()
    df,audit=canonical_merge(read_table(Path(a.master)),read_table(Path(a.exante)) if a.exante else None); df=add_targets(df,a.niv_source); targets=[z.strip() for z in a.targets.split(",") if z.strip()]
    out=scan(df,a.gate,targets,a.oos_from); od=Path(a.output_dir); od.mkdir(parents=True,exist_ok=True); out.to_csv(od/f"candidates_{a.gate}.csv",index=False); (od/"time_audit.json").write_text(json.dumps(audit,indent=2,default=str)+"\n",encoding="utf-8"); write_summary(out,od/f"SUMMARY_{a.gate}.md",a.gate,a.oos_from,audit)
    print(json.dumps({"version":VERSION,"gate":a.gate,"niv_source":a.niv_source,"rows":len(df),"features_tested":int(out.feature.nunique()) if len(out) else 0,"candidates":int(len(out)),"robust":int(out.robust.sum()) if len(out) else 0},sort_keys=True)); return 0
if __name__ == "__main__": raise SystemExit(main())
