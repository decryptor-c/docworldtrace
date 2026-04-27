from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

from ..docenv import DocEnv
from ..utils import is_close


def _is_numeric_cell(value: Any) -> bool:
    text = str(value).strip()
    if not text:
        return False
    normalized = text.replace(",", "").replace("%", "")
    try:
        float(normalized)
    except ValueError:
        return False
    return True


def _text_cell_count(rows: List[List[Any]]) -> int:
    count = 0
    for row in rows:
        for cell in row:
            text = str(cell).strip()
            if text and not _is_numeric_cell(text):
                count += 1
    return count


def load_calls(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if isinstance(payload, dict):
        return list(payload.get("calls", []))
    return list(payload)


def evaluate_expectations(result: Dict[str, Any], expected: Dict[str, Any]) -> List[Dict[str, Any]]:
    checks = []
    if not expected:
        return checks

    if "status" in expected:
        ok = result.get("status") == expected["status"]
        checks.append({"name": "status", "passed": ok, "expected": expected["status"]})

    if "contains_pages" in expected:
        pages = [
            item.get("page")
            for item in result.get("result", {}).get("results", [])
        ]
        required = list(expected["contains_pages"])
        ok = all(page in pages for page in required)
        checks.append({"name": "contains_pages", "passed": ok, "expected": required, "actual": pages})

    if "text_contains" in expected:
        haystack = json.dumps(result.get("result", {}), ensure_ascii=False)
        needle = expected["text_contains"]
        ok = needle in haystack
        checks.append({"name": "text_contains", "passed": ok, "expected": needle})

    if "value_equals" in expected:
        actual = result.get("result", {}).get("value")
        tolerance = float(expected.get("value_tolerance", 1e-6))
        ok = isinstance(actual, (int, float)) and is_close(float(actual), float(expected["value_equals"]), tolerance)
        checks.append(
            {
                "name": "value_equals",
                "passed": ok,
                "expected": expected["value_equals"],
                "actual": actual,
            }
        )

    if "support_label" in expected:
        actual = result.get("result", {}).get("label")
        ok = actual == expected["support_label"]
        checks.append(
            {
                "name": "support_label",
                "passed": ok,
                "expected": expected["support_label"],
                "actual": actual,
            }
        )

    if "cache_hit" in expected:
        actual = bool(result.get("cache_hit"))
        ok = actual == bool(expected["cache_hit"])
        checks.append(
            {
                "name": "cache_hit",
                "passed": ok,
                "expected": bool(expected["cache_hit"]),
                "actual": actual,
            }
        )

    if "table_rows_min" in expected:
        actual_rows = len(result.get("result", {}).get("rows", []))
        ok = actual_rows >= int(expected["table_rows_min"])
        checks.append(
            {
                "name": "table_rows_min",
                "passed": ok,
                "expected": expected["table_rows_min"],
                "actual": actual_rows,
            }
        )

    if "table_text_cells_min" in expected:
        rows = result.get("result", {}).get("rows", [])
        actual_cells = _text_cell_count(rows)
        ok = actual_cells >= int(expected["table_text_cells_min"])
        checks.append(
            {
                "name": "table_text_cells_min",
                "passed": ok,
                "expected": expected["table_text_cells_min"],
                "actual": actual_cells,
            }
        )
    return checks


def build_summary(executions: List[Dict[str, Any]]) -> Dict[str, Any]:
    total = len(executions)
    successes = sum(1 for item in executions if item["result"].get("status") == "success")
    total_checks = 0
    passed_checks = 0
    retrieval_checks = 0
    retrieval_passed = 0
    cache_checks = 0
    cache_passed = 0

    for item in executions:
        for check in item["checks"]:
            total_checks += 1
            if check["passed"]:
                passed_checks += 1
            if check["name"] == "contains_pages":
                retrieval_checks += 1
                retrieval_passed += int(check["passed"])
            if check["name"] == "cache_hit":
                cache_checks += 1
                cache_passed += int(check["passed"])

    return {
        "total_calls": total,
        "success_calls": successes,
        "success_rate": round(successes / total, 4) if total else 0.0,
        "expectation_checks": {
            "passed": passed_checks,
            "total": total_checks,
            "rate": round(passed_checks / total_checks, 4) if total_checks else 0.0,
        },
        "retrieval_checks": {
            "passed": retrieval_passed,
            "total": retrieval_checks,
            "rate": round(retrieval_passed / retrieval_checks, 4) if retrieval_checks else 0.0,
        },
        "cache_checks": {
            "passed": cache_passed,
            "total": cache_checks,
            "rate": round(cache_passed / cache_checks, 4) if cache_checks else 0.0,
        },
    }


def write_markdown_report(path: str, source_label: str, summary: Dict[str, Any], executions: List[Dict[str, Any]]) -> None:
    report_path = Path(path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Pilot Exp-1 Report",
        "",
        f"- Source: `{source_label}`",
        f"- Total calls: `{summary['total_calls']}`",
        f"- Success rate: `{summary['success_rate']:.2%}`",
        f"- Expectation pass rate: `{summary['expectation_checks']['rate']:.2%}`",
        f"- Retrieval pass rate: `{summary['retrieval_checks']['rate']:.2%}`",
        f"- Cache pass rate: `{summary['cache_checks']['rate']:.2%}`",
        "",
        "## Execution Details",
        "",
    ]
    for item in executions:
        result = item["result"]
        lines.append(f"### {item['name']}")
        lines.append(f"- Action: `{item['action']}`")
        lines.append(f"- Status: `{result.get('status')}`")
        lines.append(f"- Cache hit: `{result.get('cache_hit')}`")
        if item["checks"]:
            for check in item["checks"]:
                lines.append(
                    f"- Check `{check['name']}`: "
                    f"{'PASS' if check['passed'] else 'FAIL'}"
                )
        else:
            lines.append("- Checks: none")
        lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Pilot Exp-1 feasibility checks.")
    parser.add_argument("--pdf", help="Path to a PDF document")
    parser.add_argument("--document-json", help="Path to a prepared JSON document")
    parser.add_argument("--calls", required=True, help="Path to call spec JSON")
    parser.add_argument("--report-json", help="Where to write JSON report")
    parser.add_argument("--report-md", help="Where to write Markdown report")
    args = parser.parse_args()

    if bool(args.pdf) == bool(args.document_json):
        raise SystemExit("Provide exactly one of --pdf or --document-json")

    if args.pdf:
        env = DocEnv.from_pdf(args.pdf)
        source_label = args.pdf
    else:
        env = DocEnv.from_json(args.document_json)
        source_label = args.document_json

    calls = load_calls(args.calls)
    executions = []
    for index, call in enumerate(calls, start=1):
        action = call["action"]
        params = dict(call.get("params", {}))
        result = env.execute(action, **params)
        checks = evaluate_expectations(result, call.get("expected", {}))
        executions.append(
            {
                "index": index,
                "name": call.get("name", f"call_{index:02d}"),
                "action": action,
                "params": params,
                "result": result,
                "checks": checks,
            }
        )

    summary = build_summary(executions)
    payload = {
        "source": source_label,
        "summary": summary,
        "executions": executions,
    }

    if args.report_json:
        report_json = Path(args.report_json)
        report_json.parent.mkdir(parents=True, exist_ok=True)
        report_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.report_md:
        write_markdown_report(args.report_md, source_label, summary, executions)

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
