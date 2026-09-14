import json
import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import gb_power_runner as runner  # noqa: E402


class RunnerContractTests(unittest.TestCase):
    def test_self_test_contract(self):
        runner.self_test()

    def test_missing_registry_uses_fallback(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            df = runner.pd.DataFrame(
                {
                    "gb_delivery_date": ["2026-01-01"] * 46,
                    "gb_sp": list(range(1, 47)),
                    "delivery_start_utc": runner.pd.date_range(
                        "2026-01-01", periods=46, freq="30min", tz="UTC"
                    ),
                    "gb_time_certified": [True] * 46,
                    "niv": [1.0] * 46,
                    "psbil": [2.0] * 46,
                }
            )
            path = root / "master_wide.csv"
            df.to_csv(path, index=False)
            info = runner.inspect_file(path, "master")
            missing = runner.inspect_file(root / "missing.csv", "registry")
            blockers, _ = runner.validate_contract(
                runner.InputPaths(path, None, root / "missing.csv"),
                info,
                missing,
                require_exante=False,
                niv_col="niv",
                price_col="psbil",
            )
            self.assertTrue(any(x.startswith("FEATURE_REGISTRY_NOT_READ") for x in blockers))

    def test_runtime_hash_ignores_clock(self):
        a = runner.runtime_spec()
        b = dict(a)
        b["utc_now"] = "different"
        self.assertEqual(runner.runtime_hash(a), runner.runtime_hash(b))

    def test_csv_engine_smoke_commits_atomic_run(self):
        """The recovered V1 engine must consume CSV as well as Parquet."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = root / "data"
            out = root / "out"
            state = root / "state"
            data.mkdir()
            rows = []
            for day in runner.pd.date_range("2025-01-01", periods=2, freq="D"):
                for sp in range(1, 47):
                    rows.append(
                        {
                            "gb_delivery_date": day.date().isoformat(),
                            "gb_sp": sp,
                            "delivery_start_utc": day + runner.pd.Timedelta(minutes=30 * (sp - 1)),
                            "gb_time_certified": True,
                            "resolution": "PT30",
                            "niv": (-1.0 if sp % 2 else 1.0),
                            "psbil": float(sp),
                            "x": float(sp),
                        }
                    )
            runner.pd.DataFrame(rows).to_csv(data / "master_wide.csv", index=False)
            (data / "FEATURE_AVAILABILITY_REGISTRY.csv").write_text(
                "feature_id,column_name,family,lineage_root,source,unit,resolution,time_domain,pit_status,gate_DA,gate_IDA1,gate_IDA2,discovery_enabled,allow_cross_day,allow_sequence,notes\n"
                "X,x,X,X,TEST,MW,PT30,GB_PHYSICAL,CERTIFIED,true,true,true,true,false,false,test\n",
                encoding="utf-8",
            )
            cmd = [
                sys.executable,
                str(Path(__file__).resolve().parents[1] / "gb_power_runner.py"),
                "--data-dir",
                str(data),
                "--output-dir",
                str(out),
                "--state-dir",
                str(state),
                "--min-train-months",
                "1",
                "--min-cases",
                "1",
                "--min-days",
                "1",
                "--top-features",
                "2",
                "--per-family-seed-cap",
                "2",
                "--max-pairs",
                "2",
                "--smoke",
            ]
            proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
            self.assertIn(proc.returncode, (0, 2), proc.stdout + proc.stderr)
            runs = list((out / "runs").glob("UKPOWER_*"))
            self.assertEqual(len(runs), 1)
            manifest = json.loads((runs[0] / "RUN_MANIFEST.json").read_text(encoding="utf-8"))
            if importlib.util.find_spec("pyarrow") is None and importlib.util.find_spec("fastparquet") is None:
                self.assertEqual(manifest["status"], "BLOCKED_PRIMARY_WITH_FALLBACK")
                self.assertTrue(any("PARQUET_ENGINE_MISSING" in x for x in manifest["blockers"]))
            else:
                self.assertEqual(manifest["status"], "COMPLETED")
                self.assertTrue((runs[0] / "engine_output").exists())


if __name__ == "__main__":
    unittest.main()
