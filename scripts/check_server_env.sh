#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${VENV_DIR:-${ROOT_DIR}/.venv}"

if [[ ! -d "${VENV_DIR}" ]]; then
  echo "Missing virtualenv at ${VENV_DIR}"
  exit 1
fi

source "${VENV_DIR}/bin/activate"

python - <<'PY'
import importlib
import shutil
import sys

python_ok = sys.version_info >= (3, 9)
print(f"python_version: {sys.version.split()[0]} {'OK' if python_ok else 'FAIL'}")

modules = [
    "fitz",
    "pdfplumber",
    "PIL",
    "pytesseract",
]

failed = False
for name in modules:
    try:
        importlib.import_module(name)
        print(f"python_module:{name}: OK")
    except Exception:
        failed = True
        print(f"python_module:{name}: FAIL")

for binary in ["tesseract"]:
    path = shutil.which(binary)
    if path:
        print(f"binary:{binary}: OK ({path})")
    else:
        print(f"binary:{binary}: WARN (missing, born-digital PDFs can still work)")

if not python_ok or failed:
    raise SystemExit(1)
PY

python -m unittest discover -s "${ROOT_DIR}/tests" -p 'test_*.py'

echo "Environment check passed."
