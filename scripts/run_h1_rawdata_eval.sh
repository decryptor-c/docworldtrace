#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"
PDF_DIR="${1:-${ROOT_DIR}/data/raw_pdfs}"
OUT_DIR="${2:-${ROOT_DIR}/data/reports/rawdata_eval}"

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

python -m docworldtrace.pilot.exp1_auto_runner \
  --pdf-dir "${PDF_DIR}" \
  --out-dir "${OUT_DIR}"

echo
echo "Reports written to ${OUT_DIR}"
echo "Summary: ${OUT_DIR}/summary.json"
