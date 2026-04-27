from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Set


TERMINAL_ACTIONS = {"answer", "refuse"}
CORE_TOOLS = {"search", "read_page", "parse_table", "compute", "verify", "refuse", "answer"}


def _display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(Path.cwd().resolve()))
    except (OSError, ValueError):
        return str(path)


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> int:
    items = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(item, ensure_ascii=False) for item in items) + ("\n" if items else ""),
        encoding="utf-8",
    )
    return len(items)


def _write_markdown(path: Path, lines: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _kept_files(docverify_path: Path) -> Set[str]:
    payload = _load_json(docverify_path)
    files = set()
    for record in payload.get("records", []):
        if (record.get("docverify") or {}).get("filter_decision") == "keep":
            files.add(record["file"])
    return files


def _load_kept_rollouts(rollout_dir: Path, docverify_path: Path) -> List[Dict[str, Any]]:
    kept = _kept_files(docverify_path)
    rollouts = []
    for path in sorted(rollout_dir.glob("*/*.json")):
        display = _display_path(path)
        if str(path) not in kept and display not in kept:
            continue
        payload = _load_json(path)
        payload["_file"] = display
        rollouts.append(payload)
    return rollouts


def _stable_hash(value: str) -> int:
    return int(hashlib.sha256(value.encode("utf-8")).hexdigest()[:12], 16)


def _split_seed_ids(rollouts: Sequence[Dict[str, Any]], heldout_per_task: int) -> Dict[str, str]:
    by_task: Dict[str, List[str]] = defaultdict(list)
    for rollout in rollouts:
        seed = rollout["seed"]
        seed_id = seed["seed_id"]
        task = seed["task_type"]
        if seed_id not in by_task[task]:
            by_task[task].append(seed_id)

    split: Dict[str, str] = {}
    for task, seed_ids in by_task.items():
        ordered = sorted(seed_ids, key=lambda item: (_stable_hash(f"{task}:{item}"), item))
        heldout = set(ordered[: min(heldout_per_task, max(1, len(ordered) - 1))])
        for seed_id in seed_ids:
            split[seed_id] = "eval" if seed_id in heldout else "train"
    return split


def _tool_schema_text() -> str:
    return (
        "Available actions: overview, search, read_page, crop, ocr, parse_table, compute, verify, answer, refuse.\n"
        "Return exactly one JSON object with keys thought, action, and action_input.\n"
        "Use non-terminal document tools before answer/refuse when evidence is needed."
    )


def _task_prompt(seed: Dict[str, Any]) -> str:
    payload = {
        "seed_id": seed["seed_id"],
        "doc_id": seed.get("doc_id"),
        "task_type": seed.get("task_type"),
        "difficulty": seed.get("difficulty"),
        "answerable": seed.get("answerable"),
        "question": seed.get("question"),
        "tool_hints": seed.get("tool_hints", {}),
    }
    return "Task:\n" + json.dumps(payload, ensure_ascii=False)


def _terminal_json(rollout: Dict[str, Any]) -> str:
    final_action = rollout.get("final_action")
    if final_action == "answer":
        action_input = {
            "text": rollout.get("final_answer", ""),
            "evidence_refs": _final_evidence_refs(rollout),
        }
    elif final_action == "refuse":
        action_input = {"reason": rollout.get("final_answer", "Insufficient document evidence")}
    else:
        action_input = {"reason": "No valid terminal action"}
        final_action = "refuse"
    return json.dumps(
        {
            "thought": "Use the final supervised answer.",
            "action": final_action,
            "action_input": action_input,
        },
        ensure_ascii=False,
    )


def _final_evidence_refs(rollout: Dict[str, Any]) -> List[Dict[str, Any]]:
    for step in reversed(rollout.get("trajectory", [])):
        if step.get("action") == "answer":
            refs = (step.get("action_input") or {}).get("evidence_refs")
            if isinstance(refs, list):
                return refs
    return rollout.get("seed", {}).get("supporting_refs", [])


def _normalized_action_json(step: Dict[str, Any]) -> str:
    return json.dumps(
        {
            "thought": step.get("thought", ""),
            "action": step.get("action"),
            "action_input": step.get("action_input") or {},
        },
        ensure_ascii=False,
    )


def _compact_observation(step: Dict[str, Any]) -> str:
    observation = step.get("observation") or {}
    action = step.get("action")
    result = dict(observation.get("result") or {})
    if action == "search":
        result = {
            "query": result.get("query"),
            "results": result.get("results", [])[:3],
        }
    elif action == "read_page":
        pages = []
        for item in result.get("pages", []):
            pages.append(
                {
                    "page": item.get("page"),
                    "summary": item.get("summary"),
                    "text": (item.get("text") or "")[:1000],
                }
            )
        result = {"pages": pages, "missing": result.get("missing", [])}
    elif action in {"crop", "ocr"}:
        result = {"page": result.get("page"), "bbox": result.get("bbox"), "text": (result.get("text") or "")[:1000]}
    elif action == "parse_table":
        result = {
            "page": result.get("page"),
            "bbox": result.get("bbox"),
            "rows": result.get("rows", [])[:8],
            "markdown": (result.get("markdown") or "")[:1000],
        }
    elif action == "compute":
        result = {"expr": result.get("expr"), "value": result.get("value"), "error": result.get("error")}
    elif action == "verify":
        result = {
            "claim": result.get("claim"),
            "label": result.get("label"),
            "sufficiency": result.get("sufficiency"),
            "evidence_count": result.get("evidence_count"),
        }
    else:
        result = result
    return json.dumps(
        {
            "action": action,
            "status": observation.get("status"),
            "cache_hit": observation.get("cache_hit"),
            "result": result,
        },
        ensure_ascii=False,
    )


def answer_only_rows(rollouts: Sequence[Dict[str, Any]], split: Dict[str, str], split_name: str) -> List[Dict[str, Any]]:
    rows = []
    for rollout in rollouts:
        seed = rollout["seed"]
        if split[seed["seed_id"]] != split_name:
            continue
        rows.append(
            {
                "id": f"{rollout['teacher']['name']}::{seed['seed_id']}::{Path(rollout['_file']).stem}",
                "condition": "answer_only_sft",
                "split": split_name,
                "seed_id": seed["seed_id"],
                "teacher": rollout["teacher"]["name"],
                "task_type": seed["task_type"],
                "target_action": rollout.get("final_action"),
                "is_terminal": True,
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are a document QA model. Return the final answer only as JSON with action answer/refuse. "
                            "Do not emit document tool calls."
                        ),
                    },
                    {"role": "user", "content": _task_prompt(seed)},
                    {"role": "assistant", "content": _terminal_json(rollout)},
                ],
            }
        )
    return rows


def trajectory_rows(rollouts: Sequence[Dict[str, Any]], split: Dict[str, str], split_name: str) -> List[Dict[str, Any]]:
    rows = []
    for rollout in rollouts:
        seed = rollout["seed"]
        if split[seed["seed_id"]] != split_name:
            continue
        history = [
            {"role": "system", "content": "You are a document ReAct agent.\n" + _tool_schema_text()},
            {"role": "user", "content": _task_prompt(seed) + "\nReturn the next action as JSON."},
        ]
        for step in rollout.get("trajectory", []):
            if not step.get("format_valid") or not step.get("execution_valid"):
                break
            target = _normalized_action_json(step)
            rows.append(
                {
                    "id": f"{rollout['teacher']['name']}::{seed['seed_id']}::{Path(rollout['_file']).stem}::step{step['step']:02d}",
                    "condition": "trajectory_sft",
                    "split": split_name,
                    "seed_id": seed["seed_id"],
                    "teacher": rollout["teacher"]["name"],
                    "task_type": seed["task_type"],
                    "step": step["step"],
                    "target_action": step.get("action"),
                    "is_terminal": step.get("action") in TERMINAL_ACTIONS,
                    "messages": [*history, {"role": "assistant", "content": target}],
                }
            )
            history.extend(
                [
                    {"role": "assistant", "content": target},
                    {"role": "user", "content": "Observation:\n" + _compact_observation(step) + "\nReturn the next action as JSON."},
                ]
            )
    return rows


def _summarize_rows(rows: Sequence[Dict[str, Any]], condition: str) -> Dict[str, Any]:
    total = len(rows)
    actions = Counter(row.get("target_action") for row in rows if row.get("target_action"))
    terminal = sum(int(bool(row.get("is_terminal", condition == "answer_only_sft"))) for row in rows)
    nonterminal = total - terminal if condition == "trajectory_sft" else 0
    return {
        "condition": condition,
        "count": total,
        "task_distribution": dict(Counter(row["task_type"] for row in rows)),
        "teacher_distribution": dict(Counter(row["teacher"] for row in rows)),
        "target_action_distribution": dict(actions),
        "terminal_target_rate": round(terminal / total, 4) if total else 0.0,
        "nonterminal_target_rate": round(nonterminal / total, 4) if total else 0.0,
        "core_tool_coverage": sorted(action for action in actions if action in CORE_TOOLS),
    }


def _rollout_summary(rollouts: Sequence[Dict[str, Any]], split: Dict[str, str]) -> Dict[str, Any]:
    by_split = Counter(split[rollout["seed"]["seed_id"]] for rollout in rollouts)
    by_task_split: Dict[str, Counter[str]] = defaultdict(Counter)
    for rollout in rollouts:
        seed = rollout["seed"]
        by_task_split[seed["task_type"]][split[seed["seed_id"]]] += 1
    return {
        "rollout_count": len(rollouts),
        "unique_seed_count": len(set(rollout["seed"]["seed_id"] for rollout in rollouts)),
        "split_rollout_counts": dict(by_split),
        "split_by_task": {task: dict(counter) for task, counter in sorted(by_task_split.items())},
    }


def build_h5_sft(
    rollout_dir: str,
    docverify: str,
    out_dir: str,
    heldout_per_task: int,
) -> Dict[str, Any]:
    rollout_path = Path(rollout_dir)
    docverify_path = Path(docverify)
    out_path = Path(out_dir)
    rollouts = _load_kept_rollouts(rollout_path, docverify_path)
    if not rollouts:
        raise SystemExit(f"No kept rollouts found from {rollout_dir} using {docverify}")
    split = _split_seed_ids(rollouts, heldout_per_task=heldout_per_task)

    datasets = {
        "answer_only_train": answer_only_rows(rollouts, split, "train"),
        "answer_only_eval": answer_only_rows(rollouts, split, "eval"),
        "trajectory_train": trajectory_rows(rollouts, split, "train"),
        "trajectory_eval": trajectory_rows(rollouts, split, "eval"),
    }
    counts = {}
    for name, rows in datasets.items():
        counts[name] = _write_jsonl(out_path / f"{name}.jsonl", rows)

    split_rows = [
        {
            "seed_id": seed_id,
            "split": split_name,
        }
        for seed_id, split_name in sorted(split.items())
    ]
    _write_jsonl(out_path / "seed_split.jsonl", split_rows)

    summary = {
        "rollout_dir": _display_path(rollout_path),
        "docverify": _display_path(docverify_path),
        "out_dir": _display_path(out_path),
        "heldout_per_task": heldout_per_task,
        **_rollout_summary(rollouts, split),
        "dataset_counts": counts,
        "answer_only_train": _summarize_rows(datasets["answer_only_train"], "answer_only_sft"),
        "trajectory_train": _summarize_rows(datasets["trajectory_train"], "trajectory_sft"),
        "answer_only_eval": _summarize_rows(datasets["answer_only_eval"], "answer_only_sft"),
        "trajectory_eval": _summarize_rows(datasets["trajectory_eval"], "trajectory_sft"),
    }
    (out_path / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_h5_report(out_path / "summary.md", summary)
    return summary


def write_h5_report(path: Path, summary: Dict[str, Any]) -> None:
    lines = [
        "# H5 SFT Data Preparation",
        "",
        f"- Rollout dir: `{summary['rollout_dir']}`",
        f"- DocVerify++ source: `{summary['docverify']}`",
        f"- Output dir: `{summary['out_dir']}`",
        f"- Kept rollout count: `{summary['rollout_count']}`",
        f"- Unique seed count: `{summary['unique_seed_count']}`",
        f"- Split rollout counts: `{summary['split_rollout_counts']}`",
        "",
        "## Dataset Counts",
        "",
    ]
    for name, count in summary["dataset_counts"].items():
        lines.append(f"- `{name}.jsonl`: `{count}`")
    lines.extend(["", "## Supervision Signal", ""])
    lines.append(
        f"- Answer-only train terminal target rate: `{summary['answer_only_train']['terminal_target_rate']:.2%}`"
    )
    lines.append(
        f"- Trajectory train non-terminal target rate: `{summary['trajectory_train']['nonterminal_target_rate']:.2%}`"
    )
    lines.append(
        f"- Trajectory train core tool coverage: `{summary['trajectory_train']['core_tool_coverage']}`"
    )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- `answer_only_train.jsonl` supervises only terminal answer/refuse behavior.",
            "- `trajectory_train.jsonl` supervises next-action ReAct behavior, including evidence tools before terminal actions.",
            "- A real H5 SFT run should train identical base models on the two train files and evaluate on the corresponding eval split.",
        ]
    )
    _write_markdown(path, lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare H5 answer-only and trajectory SFT datasets from verified H2 rollouts.")
    parser.add_argument("--rollout-dir", default="data/h2/rollouts_v4")
    parser.add_argument("--docverify", default="data/h3/docverify_plus_v4/docverify_review.json")
    parser.add_argument("--out-dir", default="data/h5/sft_v4")
    parser.add_argument("--heldout-per-task", type=int, default=1)
    args = parser.parse_args()

    summary = build_h5_sft(
        rollout_dir=args.rollout_dir,
        docverify=args.docverify,
        out_dir=args.out_dir,
        heldout_per_task=args.heldout_per_task,
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
