#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"
ROLLOUT_DIR="${1:-${ROOT_DIR}/data/h2/rollouts_v5}"
OUT_DIR="${2:-${ROOT_DIR}/data/h3/docverify_plus_v5}"
MANUAL_LABELS="${H3_MANUAL_LABELS:-}"
TOP_K="${H3_DOCVERIFY_TOP_K:-5}"

pilot_require_dir "${ROLLOUT_DIR}" "rollout directory"

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

ARGS=(
  --rollout-dir "${ROLLOUT_DIR}"
  --out-dir "${OUT_DIR}"
  --top-k "${TOP_K}"
)

if [[ -n "${MANUAL_LABELS}" ]]; then
  pilot_require_file "${MANUAL_LABELS}" "manual labels file"
  ARGS+=(--manual-labels "${MANUAL_LABELS}")
fi

python -m docworldtrace.pilot.h3_docverify "${ARGS[@]}"

echo
echo "DocVerify++ outputs written to ${OUT_DIR}"
