#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${VENV_DIR:-${ROOT_DIR}/.venv}"

source "${VENV_DIR}/bin/activate"
cd "${ROOT_DIR}"

python -m docworldtrace.pilot.exp1_runner \
  --document-json "${ROOT_DIR}/pilot_exp1/sample_document.json" \
  --calls "${ROOT_DIR}/pilot_exp1/sample_calls.json" \
  --report-json "${ROOT_DIR}/artifacts/pilot_exp1/sample_report.json" \
  --report-md "${ROOT_DIR}/artifacts/pilot_exp1/sample_report.md"
