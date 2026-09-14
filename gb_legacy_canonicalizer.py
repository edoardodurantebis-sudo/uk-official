#!/usr/bin/env python3
"""Convert legacy UNDER THE BID wall-clock timestamps into certified GB physical identity.

Legacy `datetime_tz` is Europe/Rome wall-clock time (naive). The old `date` and
`settlement_period` columns are commercial/legacy labels and MUST NOT be reused
as GB physical identity. Ambiguous autumn-DST rows cannot be uniquely recovered
from the legacy wide file and are excluded fail-closed.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

LONDON = ZoneInfo("Europe/London")
UTC = ZoneInfo("UTC")
ROME = "Europe/Rome"


def expected_periods(day) -> int:
    start = datetime.combine(day, time(0), tzinfo=LONDON).astimezone(UTC)
    end = datetime.combine(day + timedelta(days=1), time(0), tzinfo=LONDON).astimezone(UTC)
    return int((end - start).total_seconds() // 1800)


def canonicalize(df: pd.DataFrame, ts_col: str = "datetime_tz") -> tuple[pd.DataFrame, dict]:
    if ts_col not in df.columns:
        raise RuntimeError(f"MISSING_TIMESTAMP_COLUMN:{ts_col}")
    x = df.copy()
    naive = pd.to_datetime(x[ts_col], errors="coerce")
    rome = naive.dt.tz_localize(ROME, ambiguous="NaT", nonexistent="NaT")
    x["delivery_start_utc"] = rome.dt.tz_convert("UTC")
    london = x["delivery_start_utc"].dt.tz_convert("Europe/London")
    x["gb_delivery_date"] = pd.to_datetime(london.dt.date)
    valid = x["delivery_start_utc"].notna() & x["gb_delivery_date"].notna()
    counts = x.loc[valid].groupby(x.loc[valid, "gb_delivery_date"].dt.date)["delivery_start_utc"].nunique()
    complete = {d for d, n in counts.items() if int(n) == expected_periods(d)}
    x["gb_time_certified"] = valid & x["gb_delivery_date"].dt.date.isin(complete)
    x["gb_sp"] = pd.Series(pd.NA, index=x.index, dtype="Int64")
    ordered = x.loc[x.index[x["gb_time_certified"]]].sort_values(["gb_delivery_date", "delivery_start_utc"])
    sp = ordered.groupby("gb_delivery_date").cumcount() + 1
    x.loc[ordered.index, "gb_sp"] = sp.astype("Int64")
    x["resolution"] = "PT30"
    bad = []
    for d, n in counts.items():
        exp = expected_periods(d)
        if int(n) != exp:
            bad.append({"gb_delivery_date": str(d), "observed": int(n), "expected": exp})
    audit = {
        "rows": int(len(x)),
        "certified_rows": int(x["gb_time_certified"].sum()),
        "certified_days": int(len(complete)),
        "uncertified_rows": int((~x["gb_time_certified"]).sum()),
        "bad_or_partial_days": bad,
        "policy": "ROME_WALL_CLOCK_TO_UTC_TO_LONDON; AUTUMN_DST_AMBIGUITY_FAIL_CLOSED",
    }
    return x, audit


def read_table(path: Path) -> pd.DataFrame:
    return pd.read_parquet(path) if path.suffix.lower() == ".parquet" else pd.read_csv(path, low_memory=False)


def write_table(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix.lower() == ".parquet":
        df.to_parquet(path, index=False)
    else:
        df.to_csv(path, index=False)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("output")
    p.add_argument("--audit", default="")
    p.add_argument("--timestamp-column", default="datetime_tz")
    p.add_argument("--certified-only", action="store_true")
    a = p.parse_args()
    out, audit = canonicalize(read_table(Path(a.input)), a.timestamp_column)
    if a.certified_only:
        out = out[out["gb_time_certified"]].copy()
    write_table(out, Path(a.output))
    if a.audit:
        Path(a.audit).write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(audit, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
