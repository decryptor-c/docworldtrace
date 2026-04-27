#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ABSOLUTE_ROOT_MARKERS = (
    "/home/kimilabra/DocWorldTrace/",
    "/Users/decryptor/Desktop/DocWorldTrace/",
)


def sanitize_string(value: str) -> str:
    for marker in ABSOLUTE_ROOT_MARKERS:
        if value.startswith(marker):
            return value[len(marker) :]
        value = value.replace(marker, "")
    return value


def sanitize_payload(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: sanitize_payload(item)
            for key, item in value.items()
            if not (key == "api_base" and isinstance(item, str))
        }
    if isinstance(value, list):
        return [sanitize_payload(item) for item in value]
    if isinstance(value, str):
        return sanitize_string(value)
    return value


def sanitize_json_file(path: Path) -> bool:
    if path.name == "teachers.json":
        return False
    try:
        original = path.read_text(encoding="utf-8")
        payload = json.loads(original)
    except (UnicodeDecodeError, json.JSONDecodeError):
        return False
    sanitized = json.dumps(sanitize_payload(payload), ensure_ascii=False, indent=2) + "\n"
    if sanitized == original:
        return False
    path.write_text(sanitized, encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Remove local/API paths from H2 result JSON files.")
    parser.add_argument("roots", nargs="*", default=["data/h2"], help="Files or directories to sanitize")
    args = parser.parse_args()

    changed = []
    for root_arg in args.roots:
        root = Path(root_arg)
        candidates = [root] if root.is_file() else sorted(root.rglob("*.json"))
        for path in candidates:
            if sanitize_json_file(path):
                changed.append(str(path))

    print(json.dumps({"changed_count": len(changed), "changed_files": changed}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
