#!/usr/bin/env python3
"""Fail-closed execution envelope for UNDER THE BID / GB discovery."""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import importlib.util
import json
import os
import platform
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional, Sequence

try:
    import pandas as pd
except Exception as exc:  # pragma: no cover
    pd = None
    _PANDAS_IMPORT_ERROR = repr(exc)
else:
    _PANDAS_IMPORT_ERROR = None

RUNNER_VERSION = "UK_POWER_RUNNER_2.0.1_NIV_LINEAGE"
ALLOWED_GB_PERIOD_COUNTS = {46, 48, 50}


@dataclass(frozen=True)
class InputPaths:
    master: Optional[Path]
    exante: Optional[Path]
    registry: Optional[Path]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def stable_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def atomic_write_json(path: Path, payload: Any) -> None:
    atomic_write_text(path, json.dumps(payload, indent=2, sort_keys=True, default=str) + "\n")


def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(payload, sort_keys=True, default=str) + "\n")
        fh.flush()
        os.fsync(fh.fileno())


def read_table(path: Path):
    if pd is None:
        raise RuntimeError(f"PANDAS_IMPORT_FAILED:{_PANDAS_IMPORT_ERROR}")
    ext = path.suffix.lower()
    if ext == ".parquet":
        return pd.read_parquet(path)
    if ext in {".csv", ".txt"}:
        return pd.read_csv(path)
    if ext == ".json":
        obj = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(obj, list):
            return pd.DataFrame(obj)
        if isinstance(obj, dict):
            for key in ("rows", "data", "features", "records"):
                if isinstance(obj.get(key), list):
                    return pd.DataFrame(obj[key])
            return pd.DataFrame([obj])
    raise RuntimeError(f"UNSUPPORTED_INPUT_FORMAT:{path}")


def runtime_spec() -> dict[str, Any]:
    def ver(name: str):
        try:
            return importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:
            return None
    return {
        "runner_version": RUNNER_VERSION,
        "python": platform.python_version(),
        "platform": platform.platform(),
        "utc_now": now_utc().isoformat(),
        "packages": {k: ver(k) for k in ["numpy", "pandas", "pyarrow", "scikit-learn", "statsmodels"]},
    }


def runtime_hash(spec: dict[str, Any]) -> str:
    x = dict(spec)
    x.pop("utc_now", None)
    return sha256_bytes(stable_json(x).encode())


def choose_file(data_dir: Path, explicit: str, names: Sequence[str]) -> Optional[Path]:
    if explicit:
        return Path(explicit).expanduser()
    for name in names:
        p = data_dir / name
        if p.exists():
            return p
    for name in names:
        stem = Path(name).stem
        for ext in (".parquet", ".csv"):
            hits = sorted(data_dir.glob(f"{stem}*{ext}"))
            if hits:
                return hits[0]
    return None


def resolve_inputs(args) -> InputPaths:
    d = Path(args.data_dir).expanduser()
    return InputPaths(
        choose_file(d, args.master_path, ["master_wide.parquet", "master_wide.csv"]),
        choose_file(d, args.exante_path, ["exante_wide.parquet", "exante_wide.csv"]),
        choose_file(d, args.registry_path, ["FEATURE_AVAILABILITY_REGISTRY.csv", "feature_availability_registry.csv"]),
    )


def _period_summary(df) -> dict[str, Any]:
    if not {"gb_delivery_date", "gb_sp"}.issubset(df.columns):
        return {"available": False, "reason": "GB_IDENTITY_COLUMNS_NOT_PRESENT"}
    d = pd.to_datetime(df["gb_delivery_date"], errors="coerce").dt.date
    sp = pd.to_numeric(df["gb_sp"], errors="coerce")
    counts = pd.DataFrame({"d": d, "sp": sp}).dropna().groupby("d")["sp"].nunique()
    observed = sorted({int(v) for v in counts.tolist()})
    bad = [v for v in observed if v not in ALLOWED_GB_PERIOD_COUNTS]
    return {"available": True, "day_count": int(len(counts)), "observed_period_counts": observed,
            "allowed_period_counts": sorted(ALLOWED_GB_PERIOD_COUNTS), "invalid_period_counts": bad,
            "fixed_48_assumption": False, "status": "PASS" if not bad else "FAIL"}


def inspect_file(path: Optional[Path], role: str) -> dict[str, Any]:
    if path is None or not path.exists():
        return {"role": role, "accessible": False, "error": "NOT_FOUND", "path": str(path) if path else None}
    try:
        df = read_table(path)
        return {"role": role, "accessible": True, "path": str(path.resolve()), "format": path.suffix.lower()[1:],
                "bytes": path.stat().st_size, "sha256": sha256_file(path), "rows": int(len(df)),
                "columns": [str(c) for c in df.columns], "period_summary": _period_summary(df)}
    except Exception as exc:
        return {"role": role, "accessible": False, "path": str(path), "error": f"READ_FAILED:{type(exc).__name__}:{exc}"}


def validate_contract(inputs: InputPaths, master_info: dict[str, Any], registry_info: dict[str, Any], *,
                      require_exante: bool, niv_col: str, price_col: str):
    blockers: list[str] = []
    warnings: list[str] = []
    if pd is None:
        blockers.append(f"PANDAS_IMPORT_FAILED:{_PANDAS_IMPORT_ERROR}")
    elif importlib.util.find_spec("pyarrow") is None and importlib.util.find_spec("fastparquet") is None:
        blockers.append("PARQUET_ENGINE_MISSING:install_pyarrow_or_fastparquet")
    if not master_info.get("accessible"):
        blockers.append(f"MASTER_NOT_READ:{master_info.get('error', 'UNKNOWN')}")
    else:
        cols = set(master_info.get("columns", []))
        for col in (niv_col, price_col):
            if col not in cols:
                blockers.append(f"MASTER_REQUIRED_COLUMN_MISSING:{col}")
        missing = {"gb_delivery_date", "gb_sp", "delivery_start_utc", "gb_time_certified"} - cols
        if missing:
            blockers.append("GB_TIME_KEYS_OR_CERTIFICATION_MISSING:" + ",".join(sorted(missing)))
        if master_info.get("period_summary", {}).get("status") == "FAIL":
            blockers.append("GB_PERIOD_COUNT_INVALID")
        if {"gb_sp", "settlement_period"}.issubset(cols):
            warnings.append("COMMERCIAL_SETTLEMENT_PERIOD_KEPT_SEPARATE_FROM_GB_SP")
    if not registry_info.get("accessible"):
        blockers.append(f"FEATURE_REGISTRY_NOT_READ:{registry_info.get('error', 'UNKNOWN')}")
    if require_exante and (inputs.exante is None or not inputs.exante.exists()):
        blockers.append("EXANTE_REQUIRED_BUT_NOT_FOUND")
    elif inputs.exante is None:
        warnings.append("EXANTE_NOT_PRESENT_OR_NOT_SELECTED")
    return blockers, warnings


def build_engine_command(args, inputs: InputPaths, engine_path: Path, engine_output: Path, state_dir: Path):
    cmd = [sys.executable, str(engine_path), "--master-path", str(inputs.master), "--registry-path", str(inputs.registry),
           "--output-dir", str(engine_output), "--queue-dir", str(state_dir), "--gates", args.gates,
           "--targets", args.targets, "--niv-col", args.niv_col, "--price-col", args.price_col, "--niv-source", args.niv_source,
           "--min-train-months", str(args.min_train_months), "--min-cases", str(args.min_cases),
           "--min-days", str(args.min_days), "--top-features", str(args.top_features),
           "--per-family-seed-cap", str(args.per_family_seed_cap), "--max-pairs", str(args.max_pairs)]
    if inputs.exante and args.join_keys:
        cmd += ["--exante-path", str(inputs.exante), "--join-keys", args.join_keys]
    if args.from_date:
        cmd += ["--from-date", args.from_date]
    if args.to_date:
        cmd += ["--to-date", args.to_date]
    if args.smoke:
        cmd.append("--smoke")
    return cmd


def run_once(args) -> int:
    started = now_utc()
    run_id = f"UKPOWER_{started:%Y%m%dT%H%M%SZ}_{sha256_bytes(started.isoformat().encode())[:8]}"
    out = Path(args.output_dir).expanduser()
    stage = out / ".staging" / run_id
    final = out / "runs" / run_id
    state = Path(args.state_dir).expanduser()
    stage.mkdir(parents=True, exist_ok=False)
    inputs = resolve_inputs(args)
    master = inspect_file(inputs.master, "master")
    exante = inspect_file(inputs.exante, "exante")
    registry = inspect_file(inputs.registry, "feature_availability_registry")
    blockers, warnings = validate_contract(inputs, master, registry, require_exante=args.require_exante,
                                           niv_col=args.niv_col, price_col=args.price_col)
    spec = runtime_spec()
    manifest = {"runner_version": RUNNER_VERSION, "run_id": run_id, "created_at_utc": started.isoformat(),
                "runtime": spec, "runtime_hash": runtime_hash(spec), "inputs": {"master": master, "exante": exante,
                "feature_registry": registry}, "warnings": warnings, "blockers": blockers,
                "niv_source": args.niv_source, "promotion_policy": "MACHINE_MAX_REVIEW_READY_HUMAN_PROMOTION_EXTERNAL",
                "dst_policy": "GB_PHYSICAL_EXPLICIT_IDENTITY_46_48_50_FAIL_CLOSED"}
    atomic_write_json(stage / "INPUT_MANIFEST.json", manifest)
    status = "COMPLETED"
    result = ""
    if blockers:
        status = "DATA_NOT_READ" if not master.get("accessible") else "BLOCKED_PRIMARY_WITH_FALLBACK"
        result = "PRIMARY_BLOCKED; FALLBACK_SCHEMA_LINEAGE_TIME_AUDIT_WRITTEN"
        atomic_write_json(stage / "SCHEMA_LINEAGE_AUDIT.json", {"status": status, "blockers": blockers,
                          "warnings": warnings, "next": "RESTORE_MISSING_PIT_REGISTRY_OR_GB_TIME_KEYS_THEN_RUN_DISCOVERY"})
    else:
        engine = Path(args.engine_path).expanduser()
        if not engine.exists():
            status = "BLOCKED_PRIMARY_WITH_FALLBACK"
            blockers.append(f"ENGINE_NOT_FOUND:{engine}")
            result = "ENGINE_MISSING; INPUT_AUDIT_RETAINED"
        else:
            engine_out = stage / "engine_output"
            proc = subprocess.run(build_engine_command(args, inputs, engine, engine_out, state), text=True,
                                  capture_output=True, check=False)
            atomic_write_text(stage / "ENGINE_STDOUT.log", proc.stdout)
            atomic_write_text(stage / "ENGINE_STDERR.log", proc.stderr)
            if proc.returncode:
                status = "BLOCKED_PRIMARY_WITH_FALLBACK"
                blockers.append(f"ENGINE_EXIT_CODE:{proc.returncode}")
                result = f"ENGINE_FAILED_EXIT_{proc.returncode}"
            else:
                em = list(engine_out.rglob("RUN_MANIFEST.json"))
                if not em:
                    status = "BLOCKED_PRIMARY_WITH_FALLBACK"
                    blockers.append("ENGINE_RUN_MANIFEST_MISSING")
                    result = "ENGINE_EXITED_WITHOUT_RUN_MANIFEST"
                else:
                    e = json.loads(em[-1].read_text(encoding="utf-8"))
                    manifest["engine_manifest"] = e
                    result = f"DISCOVERY_ENGINE_COMPLETED candidates={e.get('candidate_count', 0)} review_ready={e.get('review_ready_count', 0)}"
    manifest.update({"status": status, "result": result, "blockers": blockers})
    atomic_write_json(stage / "RUN_MANIFEST.json", manifest)
    report = (f"RUN_ID={run_id}\nSTATUS={status}\nDATA_READ={'PASS' if master.get('accessible') else 'FAIL'}\n"
              f"RESULT={result}\nPRIMARY_BLOCKER={';'.join(blockers) if blockers else 'NONE'}\n")
    atomic_write_text(stage / "REPORT.txt", report)
    final.parent.mkdir(parents=True, exist_ok=True)
    os.replace(stage, final)
    append_jsonl(state / "heartbeat.jsonl", {"run_id": run_id, "timestamp_utc": now_utc().isoformat(),
                 "status": status, "result": result, "report_path": str(final / "REPORT.txt")})
    print(report, end="")
    print(f"RUN_DIR={final}")
    return 0 if status == "COMPLETED" else 2


def self_test() -> None:
    assert runtime_hash(runtime_spec()) == runtime_hash(runtime_spec())
    if pd is None:
        raise RuntimeError("pandas required")
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "master_wide.csv"
        pd.DataFrame({"gb_delivery_date": ["2026-03-29"] * 46 + ["2026-03-30"] * 48 + ["2026-10-25"] * 50,
                      "gb_sp": list(range(1, 47)) + list(range(1, 49)) + list(range(1, 51)),
                      "delivery_start_utc": pd.date_range("2026-03-29", periods=144, freq="30min", tz="UTC"),
                      "gb_time_certified": [True] * 144, "niv": [1.0] * 144, "psbil": [2.0] * 144}).to_csv(p, index=False)
        info = inspect_file(p, "master")
        assert info["accessible"] and info["period_summary"]["status"] == "PASS"
        assert info["period_summary"]["observed_period_counts"] == [46, 48, 50]
    print("SELF_TEST=PASS")


def parse_args(argv: Optional[Sequence[str]] = None):
    p = argparse.ArgumentParser(description="Canonical UNDER THE BID / Power UK runner")
    p.add_argument("--data-dir", default=os.environ.get("UK_POWER_DATA_DIR", "data"))
    p.add_argument("--output-dir", default=os.environ.get("UK_POWER_OUTPUT_DIR", "runs"))
    p.add_argument("--state-dir", default=os.environ.get("UK_POWER_STATE_DIR", "state"))
    p.add_argument("--engine-path", default=str(Path(__file__).with_name("GB_NIGHTLY_DISCOVERY_V1.py")))
    p.add_argument("--master-path", default=""); p.add_argument("--exante-path", default=""); p.add_argument("--registry-path", default="")
    p.add_argument("--join-keys", default=""); p.add_argument("--gates", default="DA,IDA1,IDA2")
    p.add_argument("--targets", default="SIGN,PRICE_SHORT,PRICE_LONG"); p.add_argument("--niv-col", default="niv"); p.add_argument("--price-col", default="psbil"); p.add_argument("--niv-source", choices=["MASTER_INTERNAL_INVERTED","ELEXON_OFFICIAL"], default="MASTER_INTERNAL_INVERTED")
    p.add_argument("--from-date", default=""); p.add_argument("--to-date", default="")
    p.add_argument("--min-train-months", type=int, default=6); p.add_argument("--min-cases", type=int, default=30); p.add_argument("--min-days", type=int, default=8)
    p.add_argument("--top-features", type=int, default=30); p.add_argument("--per-family-seed-cap", type=int, default=4); p.add_argument("--max-pairs", type=int, default=300)
    p.add_argument("--require-exante", action="store_true"); p.add_argument("--smoke", action="store_true"); p.add_argument("--self-test", action="store_true")
    return p.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    if args.self_test:
        self_test(); return 0
    return run_once(args)


if __name__ == "__main__":
    raise SystemExit(main())
