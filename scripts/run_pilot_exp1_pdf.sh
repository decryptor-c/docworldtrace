#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <pdf_path> <calls_json> [report_prefix]"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${VENV_DIR:-${ROOT_DIR}/.venv}"
PDF_PATH="$1"
CALLS_PATH="$2"
REPORT_PREFIX="${3:-${ROOT_DIR}/artifacts/pilot_exp1/pdf_run}"

source "${VENV_DIR}/bin/activate"
cd "${ROOT_DIR}"

python -m docworldtrace.pilot.exp1_runner \
  --pdf "${PDF_PATH}" \
  --calls "${CALLS_PATH}" \
  --report-json "${REPORT_PREFIX}.json" \
  --report-md "${REPORT_PREFIX}.md"
