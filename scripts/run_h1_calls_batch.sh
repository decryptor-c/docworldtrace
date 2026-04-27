#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"
PDF_DIR="${1:-${ROOT_DIR}/data/raw_pdfs}"
CALLS_DIR="${2:-${ROOT_DIR}/data/calls}"
OUT_DIR="${3:-${ROOT_DIR}/data/reports/h1_calls}"

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

mkdir -p "${OUT_DIR}"

for pdf in "${PDF_DIR}"/*.pdf; do
  [[ -e "${pdf}" ]] || continue
  stem="$(basename "${pdf}" .pdf)"
  calls="${CALLS_DIR}/${stem}.calls.json"
  if [[ ! -f "${calls}" ]]; then
    echo "Skipping ${stem}: missing ${calls}"
    continue
  fi
  echo "Running ${stem}"
  python -m docworldtrace.pilot.exp1_runner \
    --pdf "${pdf}" \
    --calls "${calls}" \
    --report-json "${OUT_DIR}/${stem}.json" \
    --report-md "${OUT_DIR}/${stem}.md"
done

echo
echo "Batch run complete."
echo "Reports written to ${OUT_DIR}"
