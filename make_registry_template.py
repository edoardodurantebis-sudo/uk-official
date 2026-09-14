#!/usr/bin/env python3
"""Create a disabled Feature Availability Registry template."""
from pathlib import Path
import pandas as pd

COLUMNS = [
    "feature_id", "column_name", "family", "lineage_root", "source", "unit",
    "resolution", "time_domain", "pit_status", "gate_DA", "gate_IDA1",
    "gate_IDA2", "discovery_enabled", "allow_cross_day", "allow_sequence", "notes",
]


def main() -> None:
    out = Path("FEATURE_AVAILABILITY_REGISTRY.csv")
    row = {
        "feature_id": "EXAMPLE_DISABLED_WIND",
        "column_name": "replace_with_real_column",
        "family": "WIND",
        "lineage_root": "WIND_PROVIDER_EXAMPLE",
        "source": "PROVIDER/DATASET/FIELD",
        "unit": "MW",
        "resolution": "PT30",
        "time_domain": "GB_PHYSICAL",
        "pit_status": "REVIEWED_DECLARED",
        "gate_DA": False,
        "gate_IDA1": False,
        "gate_IDA2": False,
        "discovery_enabled": False,
        "allow_cross_day": False,
        "allow_sequence": False,
        "notes": "Template only; certify lineage and gate availability before enabling.",
    }
    pd.DataFrame([row], columns=COLUMNS).to_csv(out, index=False)
    print(out)


if __name__ == "__main__":
    main()
