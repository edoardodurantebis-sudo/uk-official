from datetime import date
import pandas as pd
from gb_legacy_canonicalizer import canonicalize, expected_periods


def test_normal_days_certify():
    # Need surrounding Rome-wall-clock rows because GB day boundaries are shifted.
    dt = pd.date_range("2026-01-14 00:00", periods=48*3, freq="30min").astype(str)
    out, audit = canonicalize(pd.DataFrame({"datetime_tz": dt}))
    assert audit["certified_days"] >= 2
    cert = out[out.gb_time_certified]
    assert cert.gb_sp.notna().all()
    assert set(cert.groupby("gb_delivery_date").size().unique()).issubset({48})


def test_autumn_dst_fold_fails_closed():
    dt = pd.date_range("2025-10-25 00:00", periods=48*3, freq="30min").astype(str)
    _, audit = canonicalize(pd.DataFrame({"datetime_tz": dt}))
    bad = {x["gb_delivery_date"]: x for x in audit["bad_or_partial_days"]}
    assert "2025-10-26" in bad
    assert bad["2025-10-26"]["expected"] == 50
    assert expected_periods(date(2025, 10, 26)) == 50
