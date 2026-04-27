from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

from ..docenv import DocEnv
from .h2_client import load_teacher_configs
from .h2_rollout import display_path, error_rollout, load_seeds, rollout_seed


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _failed_records(eval_path: Path, teacher_name: str) -> List[Dict[str, Any]]:
    payload = _load_json(eval_path)
    records = payload.get("records", [])
    failed = []
    for record in records:
        if record.get("teacher") != teacher_name:
            continue
        status = record.get("status")
        adjusted_ok = bool(record.get("answer_correct_adjusted"))
        format_ok = bool(record.get("format_compliant"))
        terminated = bool(record.get("terminated_normally"))
        if not adjusted_ok or not format_ok or not terminated or status in {"teacher_error", "format_error"}:
            failed.append(record)
    return failed


def _records_from_rollout_dir(rollout_dir: Path, teacher_name: str) -> List[Dict[str, Any]]:
    records = []
    teacher_dir = rollout_dir / teacher_name
    for path in sorted(teacher_dir.glob("*.json")):
        payload = _load_json(path)
        metrics = payload.get("metrics", {})
        status = payload.get("status")
        if status in {"teacher_error", "format_error"} or not metrics.get("format_compliant") or not metrics.get("terminated_normally"):
            records.append(
                {
                    "file": display_path(str(path)),
                    "seed_id": payload.get("seed", {}).get("seed_id"),
                    "teacher": teacher_name,
                    "status": status,
                }
            )
    return records


def rerun_failed(
    rollout_dir: str,
    eval_path: str,
    seed_file: str,
    teacher_config: str,
    teacher_name: str,
    max_steps: int,
    dry_run: bool = False,
) -> Dict[str, Any]:
    rollout_root = Path(rollout_dir)
    eval_file = Path(eval_path)
    seed_by_id = {seed["seed_id"]: seed for seed in load_seeds(seed_file)}
    teacher_by_name = {teacher.name: teacher for teacher in load_teacher_configs(teacher_config)}
    if teacher_name not in teacher_by_name:
        raise SystemExit(f"Teacher not found in config: {teacher_name}")
    teacher = teacher_by_name[teacher_name]

    if eval_file.exists():
        records = _failed_records(eval_file, teacher_name)
    else:
        records = _records_from_rollout_dir(rollout_root, teacher_name)

    missing_seeds = sorted({record.get("seed_id") for record in records if record.get("seed_id") not in seed_by_id})
    if missing_seeds:
        raise SystemExit(f"Missing seeds in {seed_file}: {', '.join(missing_seeds)}")

    pdf_cache: Dict[str, DocEnv] = {}
    outputs = []
    for record in records:
        path = Path(record["file"])
        if not path.is_absolute():
            path = Path.cwd() / path
        seed = seed_by_id[record["seed_id"]]
        if dry_run:
            outputs.append({"file": display_path(str(path)), "seed_id": seed["seed_id"], "status": "dry_run"})
            continue
        try:
            rollout = rollout_seed(seed, teacher, max_steps=max_steps, pdf_cache=pdf_cache)
        except Exception as exc:
            rollout = error_rollout(seed, teacher, str(exc))
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(rollout, ensure_ascii=False, indent=2), encoding="utf-8")
        outputs.append(
            {
                "file": display_path(str(path)),
                "seed_id": seed["seed_id"],
                "old_status": record.get("status"),
                "new_status": rollout.get("status"),
                "final_action": rollout.get("final_action"),
                "tool_sequence": rollout.get("tool_sequence", []),
            }
        )

    summary = {
        "rollout_dir": display_path(str(rollout_root)),
        "eval_path": display_path(str(eval_file)),
        "seed_file": display_path(seed_file),
        "teacher_config": display_path(teacher_config),
        "teacher": teacher_name,
        "max_steps": max_steps,
        "dry_run": dry_run,
        "selected_count": len(records),
        "outputs": outputs,
    }
    summary_path = rollout_root / f"rerun_failed_{teacher_name}.summary.json"
    if not dry_run:
        summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Rerun failed H2 rollout files for one teacher in place.")
    parser.add_argument("--rollout-dir", default="data/h2/rollouts_v4")
    parser.add_argument("--eval", default="data/h2/eval_v4/summary.json")
    parser.add_argument("--seed-file", default="data/h2/seeds/pilot_seeds_v4.jsonl")
    parser.add_argument("--teacher-config", default="data/h2/teachers.json")
    parser.add_argument("--teacher", default="dmxapi_gemini_2_5_flash")
    parser.add_argument("--max-steps", type=int, default=8)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    summary = rerun_failed(
        rollout_dir=args.rollout_dir,
        eval_path=args.eval,
        seed_file=args.seed_file,
        teacher_config=args.teacher_config,
        teacher_name=args.teacher,
        max_steps=args.max_steps,
        dry_run=args.dry_run,
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
