from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from ..docenv import DocEnv
from ..utils import tokenize
from .h2_client import OpenAICompatibleClient, TeacherConfig, load_teacher_configs

ACTION_ALIASES = {
    "overview": "overview",
    "search": "search",
    "read_page": "read_page",
    "readpage": "read_page",
    "read-page": "read_page",
    "crop": "crop",
    "ocr": "ocr",
    "parse_table": "parse_table",
    "parsetable": "parse_table",
    "parse-table": "parse_table",
    "compute": "compute",
    "verify": "verify",
    "answer": "answer",
    "refuse": "refuse",
}

TERMINAL_ACTIONS = {"answer", "refuse"}


def display_path(path: str) -> str:
    path_obj = Path(path).expanduser()
    try:
        resolved = path_obj.resolve()
        cwd = Path.cwd().resolve()
        return str(resolved.relative_to(cwd))
    except (OSError, ValueError):
        return str(path_obj)


def teacher_public_metadata(teacher: TeacherConfig) -> Dict[str, str]:
    return {
        "name": teacher.name,
        "model": teacher.model,
    }


def resolve_pdf_path(path: str) -> str:
    pdf_path = Path(path).expanduser()
    if pdf_path.exists():
        return str(pdf_path)
    fallback = Path("data/raw_pdfs") / pdf_path.name
    if fallback.exists():
        return str(fallback)
    return str(pdf_path)


def load_seeds(path: str) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            clean = line.strip()
            if not clean:
                continue
            items.append(json.loads(clean))
    return items


def _tool_spec_text() -> str:
    return (
        "Available actions:\n"
        "- overview(): get document title, page count, and per-page summaries.\n"
        "- search(query: str, top_k: int=3): return relevant pages and snippets.\n"
        "- read_page(page_ids: list[int]): read one or more pages.\n"
        "- crop(page_id: int, bbox: [x0,y0,x1,y1]): crop a region and get text/image.\n"
        "- ocr(page_id: int, bbox: optional[list[float]]): OCR a whole page or region.\n"
        "- parse_table(page_id: int, bbox: [x0,y0,x1,y1]): parse a table region.\n"
        "- compute(expr: str, vars: dict): evaluate a numeric expression.\n"
        "- verify(claim: str, evidence_refs: list[dict]): judge support using page refs.\n"
        "- answer(text: str, evidence_refs: list[dict]): finish with an answer.\n"
        "- refuse(reason: str): finish when the question is unanswerable.\n"
        "\n"
        "Response format:\n"
        'Return exactly one JSON object with keys "thought", "action", and "action_input".\n'
        "Do not include markdown fences. Do not fabricate observations. Use at least one non-terminal tool before answer/refuse.\n"
        "Keep JSON compact and valid; avoid long explanations inside action_input.\n"
        "For evidence_refs prefer page-level citations such as [{\"page\": 5}] unless you have a bbox.\n"
    )


def _few_shot_text() -> str:
    return (
        "Few-shot example 1:\n"
        "User question: What is the heading on page 3?\n"
        'Assistant: {"thought":"I should read the requested page first.","action":"read_page","action_input":{"page_ids":[3]}}\n'
        "Observation: {\"status\":\"success\",\"result\":{\"pages\":[{\"page\":3,\"summary\":\"Model Overview\"}]}}\n"
        'Assistant: {"thought":"I found the heading and can answer with a page citation.","action":"answer","action_input":{"text":"Model Overview","evidence_refs":[{"page":3}]}}\n'
        "\n"
        "Few-shot example 2:\n"
        "User question: Based on the table on page 5, what is the percentage change from FY2022 to FY2023 revenue?\n"
        'Assistant: {"thought":"I need the table values first.","action":"parse_table","action_input":{"page_id":5,"bbox":[90,280,520,430]}}\n'
        "Observation: {\"status\":\"success\",\"result\":{\"rows\":[[\"Metric\",\"Value\"],[\"FY2022 Revenue\",\"2.8\"],[\"FY2023 Revenue\",\"3.2\"]]}}\n"
        'Assistant: {"thought":"Now I can compute the percent change.","action":"compute","action_input":{"expr":"(fy2023-fy2022)/fy2022*100","vars":{"fy2022":2.8,"fy2023":3.2}}}\n'
        "Observation: {\"status\":\"success\",\"result\":{\"value\":14.2857}}\n"
        'Assistant: {"thought":"The computed value is enough to answer.","action":"answer","action_input":{"text":"14.29%","evidence_refs":[{"page":5}]}}\n'
    )


def _task_guidance_text(seed: Dict[str, Any]) -> str:
    task_type = seed.get("task_type", "")
    required_tools = [tool for tool in seed.get("required_tools", []) if tool not in TERMINAL_ACTIONS]
    acceptable_paths = seed.get("acceptable_paths") or []
    hints = seed.get("tool_hints") or {}
    lines = [
        "Task-specific constraints:",
        f"- Task type: {task_type}.",
    ]
    if required_tools:
        lines.append(f"- You should use these non-terminal tools unless impossible: {', '.join(required_tools)}.")
    if acceptable_paths:
        lines.append(
            "- Acceptable tool paths include: "
            + "; ".join(" -> ".join(path) for path in acceptable_paths)
            + "."
        )
    if task_type == "unanswerable":
        lines.append("- Do not refuse immediately. First use search and read_page to look for negative evidence, then refuse if unsupported.")
    elif task_type == "text_lookup":
        lines.append("- Read the target page and answer with the page summary or first visible leading phrase requested by the question.")
        lines.append("- Do not select a later figure caption, table caption, or section heading if the question asks for the leading phrase.")
    elif task_type == "table_lookup":
        lines.append("- First read the target page to locate the table. Then call parse_table with a bbox covering the full table, not a narrow column strip.")
        lines.append("- If parse_table fails, use read_page or OCR evidence before deciding whether to answer or refuse.")
    elif task_type == "numeric_computation":
        lines.append("- Use compute for the arithmetic step. Do not do final arithmetic only in natural language.")
        lines.append("- If the question asks for a percentage-point difference, answer with '<number> percentage points', not '<number>%'.")
    elif task_type == "cross_page":
        lines.append("- Use search to find the anchor page, then read the next page. Trust read_page text before trying crop/OCR.")
    elif task_type == "verification":
        lines.append("- Use search/read_page to gather evidence, then call verify before answering SUPPORTED or UNSUPPORTED.")
    if hints:
        lines.append(f"- Tool hints: {json.dumps(hints, ensure_ascii=False)}")
    lines.append("- Never use answer/refuse before at least one non-terminal tool observation.")
    return "\n".join(lines)


def build_messages(seed: Dict[str, Any], env: DocEnv, max_steps: int) -> List[Dict[str, str]]:
    overview = env.overview()["result"]
    overview_payload = {
        "doc_id": overview["doc_id"],
        "title": overview["title"],
        "page_count": overview["page_count"],
        "page_summaries": overview["pages"][:6],
    }
    return [
        {
            "role": "system",
            "content": (
                "You are a document reasoning teacher for Pilot Exp-2.\n"
                + _tool_spec_text()
                + "\n"
                + _few_shot_text()
            ),
        },
        {
            "role": "user",
            "content": (
                f"Document profile:\n{json.dumps(overview_payload, ensure_ascii=False)}\n\n"
                f"Task metadata:\n{json.dumps({k: seed[k] for k in ['seed_id', 'task_type', 'difficulty', 'answerable']}, ensure_ascii=False)}\n\n"
                f"{_task_guidance_text(seed)}\n\n"
                f"Question: {seed['question']}\n"
                f"Use at most {max_steps} steps.\n"
                "Start by returning the next action as JSON."
            ),
        },
    ]


def extract_json_object(text: str) -> Dict[str, Any]:
    text = text.strip()
    if text.startswith("```"):
        match = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, flags=re.DOTALL)
        if match:
            text = match.group(1).strip()
    decoder = json.JSONDecoder()
    for start_index, char in enumerate(text):
        if char != "{":
            continue
        try:
            value, _ = decoder.raw_decode(text[start_index:])
            if isinstance(value, dict):
                return value
        except json.JSONDecodeError:
            continue
    raise ValueError("No JSON object found in model output")


def _normalize_evidence_refs(value: Any) -> List[Dict[str, Any]]:
    if value is None:
        return []
    refs: List[Dict[str, Any]] = []
    if isinstance(value, list):
        items = value
    else:
        items = [value]
    for item in items:
        if isinstance(item, dict):
            ref = {}
            if "page" in item:
                ref["page"] = int(item["page"])
            if "bbox" in item and item["bbox"] is not None:
                ref["bbox"] = [float(v) for v in item["bbox"]]
            if ref:
                refs.append(ref)
        elif isinstance(item, int):
            refs.append({"page": int(item)})
        elif isinstance(item, str) and item.isdigit():
            refs.append({"page": int(item)})
    return refs


def normalize_action_call(action: str, action_input: Any) -> Tuple[str, Dict[str, Any]]:
    action_key = action.lower().strip().replace(" ", "_")
    if action_key not in ACTION_ALIASES:
        raise ValueError(f"Unsupported action from teacher: {action}")
    canonical = ACTION_ALIASES[action_key]
    action_input = dict(action_input or {})

    if canonical == "overview":
        return canonical, {}
    if canonical == "search":
        return canonical, {
            "query": str(action_input.get("query", "")),
            "top_k": int(action_input.get("top_k", 3)),
        }
    if canonical == "read_page":
        page_ids = action_input.get("page_ids")
        if page_ids is None and "page_id" in action_input:
            page_ids = [action_input["page_id"]]
        if isinstance(page_ids, int):
            page_ids = [page_ids]
        if isinstance(page_ids, str) and page_ids.isdigit():
            page_ids = [int(page_ids)]
        if not isinstance(page_ids, list):
            raise ValueError("read_page requires page_ids")
        return canonical, {"page_ids": [int(value) for value in page_ids]}
    if canonical in {"crop", "parse_table"}:
        bbox = action_input.get("bbox")
        if bbox is None or len(bbox) != 4:
            raise ValueError(f"{canonical} requires bbox with 4 values")
        return canonical, {
            "page_id": int(action_input["page_id"]),
            "bbox": [float(value) for value in bbox],
        }
    if canonical == "ocr":
        bbox = action_input.get("bbox")
        payload = {"page_id": int(action_input["page_id"])}
        if bbox is not None:
            if len(bbox) != 4:
                raise ValueError("ocr bbox must have 4 values")
            payload["bbox"] = [float(value) for value in bbox]
        return canonical, payload
    if canonical == "compute":
        return canonical, {
            "expr": str(action_input["expr"]),
            "vars": dict(action_input.get("vars", {})),
        }
    if canonical == "verify":
        return canonical, {
            "claim": str(action_input["claim"]),
            "evidence_refs": _normalize_evidence_refs(action_input.get("evidence_refs")),
        }
    if canonical == "answer":
        text = action_input.get("text", action_input.get("answer", ""))
        return canonical, {
            "text": str(text),
            "evidence_refs": _normalize_evidence_refs(action_input.get("evidence_refs")),
        }
    if canonical == "refuse":
        reason = action_input.get("reason", action_input.get("text", "Insufficient evidence"))
        return canonical, {"reason": str(reason)}
    raise ValueError(f"Unhandled action: {canonical}")


def compact_observation(action: str, observation: Dict[str, Any]) -> Dict[str, Any]:
    result = dict(observation.get("result", {}))
    compact = {
        "action": action,
        "status": observation.get("status"),
        "cache_hit": observation.get("cache_hit"),
        "result": result,
    }
    if action == "search":
        compact["result"] = {
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
                    "text": (item.get("text") or "")[:1500],
                }
            )
        compact["result"] = {"pages": pages, "missing": result.get("missing", [])}
    elif action in {"crop", "ocr"}:
        compact["result"] = {
            "page": result.get("page"),
            "bbox": result.get("bbox"),
            "text": (result.get("text") or "")[:1500],
        }
    elif action == "parse_table":
        compact["result"] = {
            "page": result.get("page"),
            "bbox": result.get("bbox"),
            "rows": result.get("rows", [])[:8],
            "markdown": (result.get("markdown") or "")[:1500],
        }
    elif action == "verify":
        compact["result"] = {
            "claim": result.get("claim"),
            "label": result.get("label"),
            "sufficiency": result.get("sufficiency"),
            "evidence_count": result.get("evidence_count"),
        }
    elif action == "compute":
        compact["result"] = {
            "expr": result.get("expr"),
            "value": result.get("value"),
            "error": result.get("error"),
        }
    elif action in TERMINAL_ACTIONS:
        compact["result"] = result
    return compact


def rollout_seed(
    seed: Dict[str, Any],
    teacher: TeacherConfig,
    max_steps: int,
    pdf_cache: Dict[str, DocEnv],
) -> Dict[str, Any]:
    pdf_path = resolve_pdf_path(seed["pdf_path"])
    env = pdf_cache.setdefault(pdf_path, DocEnv.from_pdf(pdf_path))
    client = OpenAICompatibleClient(teacher)
    messages = build_messages(seed, env, max_steps=max_steps)

    trajectory: List[Dict[str, Any]] = []
    status = "budget_exhausted"
    final_action = None
    final_answer = None
    raw_usage: List[Dict[str, Any]] = []

    for step in range(1, max_steps + 1):
        response = client.chat(messages)
        raw_text = response["content"]
        raw_usage.append(response.get("usage", {}))
        step_record: Dict[str, Any] = {
            "step": step,
            "raw_model_output": raw_text,
        }
        try:
            parsed = extract_json_object(raw_text)
            thought = str(parsed.get("thought", "")).strip()
            action_name = str(parsed.get("action", "")).strip()
            normalized_action, normalized_input = normalize_action_call(
                action_name,
                parsed.get("action_input", {}),
            )
            observation = env.execute(normalized_action, **normalized_input)
            step_record.update(
                {
                    "thought": thought,
                    "action": normalized_action,
                    "action_input": normalized_input,
                    "observation": observation,
                    "format_valid": True,
                    "execution_valid": True,
                }
            )
            trajectory.append(step_record)
            messages.append({"role": "assistant", "content": raw_text})
            messages.append(
                {
                    "role": "user",
                    "content": (
                        "Observation:\n"
                        + json.dumps(compact_observation(normalized_action, observation), ensure_ascii=False)
                        + "\nReturn the next action as JSON."
                    ),
                }
            )
            if normalized_action in TERMINAL_ACTIONS:
                status = "completed"
                final_action = normalized_action
                if normalized_action == "answer":
                    final_answer = normalized_input.get("text", "")
                else:
                    final_answer = normalized_input.get("reason", "")
                break
        except Exception as exc:
            step_record.update(
                {
                    "format_valid": False,
                    "execution_valid": False,
                    "error": str(exc),
                }
            )
            trajectory.append(step_record)
            status = "format_error"
            break

    tool_sequence = [item.get("action") for item in trajectory if item.get("action")]
    nonterminal_tools = [action for action in tool_sequence if action not in TERMINAL_ACTIONS]
    result = {
        "seed": seed,
        "teacher": teacher_public_metadata(teacher),
        "status": status,
        "trajectory": trajectory,
        "tool_sequence": tool_sequence,
        "final_action": final_action,
        "final_answer": final_answer,
        "raw_usage": raw_usage,
        "metrics": {
            "format_compliant": status != "format_error" and all(item.get("format_valid") for item in trajectory),
            "terminated_normally": status == "completed" and final_action in TERMINAL_ACTIONS,
            "step_count": len(trajectory),
            "used_verify": "verify" in tool_sequence,
            "used_refuse": final_action == "refuse",
            "direct_answer": bool(final_action in TERMINAL_ACTIONS and not nonterminal_tools),
        },
    }
    return result


def error_rollout(seed: Dict[str, Any], teacher: TeacherConfig, error: str) -> Dict[str, Any]:
    return {
        "seed": seed,
        "teacher": teacher_public_metadata(teacher),
        "status": "teacher_error",
        "error": error,
        "trajectory": [],
        "tool_sequence": [],
        "final_action": None,
        "final_answer": None,
        "raw_usage": [],
        "metrics": {
            "format_compliant": False,
            "terminated_normally": False,
            "step_count": 0,
            "used_verify": False,
            "used_refuse": False,
            "direct_answer": False,
        },
    }


def run_rollouts(
    seed_file: str,
    teacher_config_path: str,
    out_dir: str,
    repeats: int,
    max_steps: int,
) -> Dict[str, Any]:
    seeds = load_seeds(seed_file)
    teachers = load_teacher_configs(teacher_config_path)
    out_root = Path(out_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    pdf_cache: Dict[str, DocEnv] = {}
    outputs = []

    for teacher in teachers:
        teacher_dir = out_root / teacher.name
        teacher_dir.mkdir(parents=True, exist_ok=True)
        for seed in seeds:
            for run_index in range(1, repeats + 1):
                try:
                    rollout = rollout_seed(seed, teacher, max_steps=max_steps, pdf_cache=pdf_cache)
                except Exception as exc:
                    rollout = error_rollout(seed, teacher, str(exc))
                file_name = f"{seed['seed_id']}__run{run_index:02d}.json"
                path = teacher_dir / file_name
                path.write_text(json.dumps(rollout, ensure_ascii=False, indent=2), encoding="utf-8")
                outputs.append(display_path(str(path)))

    summary = {
        "seed_file": display_path(seed_file),
        "teacher_config_path": display_path(teacher_config_path),
        "out_dir": display_path(str(out_root)),
        "rollout_count": len(outputs),
        "files": outputs,
    }
    (out_root / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Run H2 teacher rollouts over DocEnv.")
    parser.add_argument("--seed-file", default="data/h2/seeds/pilot_seeds.jsonl", help="Seed JSONL file")
    parser.add_argument("--teacher-config", default="data/h2/teachers.json", help="Teacher config JSON")
    parser.add_argument("--out-dir", default="data/h2/rollouts", help="Output directory for rollout logs")
    parser.add_argument("--repeats", type=int, default=1, help="Number of rollouts per seed per teacher")
    parser.add_argument("--max-steps", type=int, default=8, help="Maximum steps per rollout")
    args = parser.parse_args()

    summary = run_rollouts(
        seed_file=args.seed_file,
        teacher_config_path=args.teacher_config,
        out_dir=args.out_dir,
        repeats=args.repeats,
        max_steps=args.max_steps,
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
