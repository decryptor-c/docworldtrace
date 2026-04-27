#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"
ROLLOUT_DIR="${1:-${ROOT_DIR}/data/h2/rollouts}"
OUT_JSON="${2:-${ROOT_DIR}/data/h2/eval/summary.json}"
OUT_MD="${3:-${ROOT_DIR}/data/h2/eval/summary.md}"

if [[ $# -ge 2 && "${OUT_JSON}" != *.json && ! -f "${OUT_JSON}" ]]; then
  OUT_DIR="${OUT_JSON}"
  OUT_JSON="${OUT_DIR}/summary.json"
  if [[ $# -lt 3 ]]; then
    OUT_MD="${OUT_DIR}/summary.md"
  fi
fi

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

python -m docworldtrace.pilot.h2_eval \
  --rollout-dir "${ROLLOUT_DIR}" \
  --out-json "${OUT_JSON}" \
  --out-md "${OUT_MD}"

echo
echo "H2 evaluation written to ${OUT_JSON} and ${OUT_MD}"
