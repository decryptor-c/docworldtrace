#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"
SOURCE_ROLLOUT_DIR="${1:-${ROOT_DIR}/data/h2/rollouts_v5}"
OUT_DIR="${2:-${ROOT_DIR}/data/h3/negative_v5}"
NEGATIVE_ROLLOUT_DIR="${H3_NEGATIVE_ROLLOUT_DIR:-${OUT_DIR}/corrupted_rollouts}"
TOP_K="${H3_DOCVERIFY_TOP_K:-5}"
MAX_PER_TYPE="${H3_NEGATIVE_MAX_PER_TYPE:-}"
INCLUDE_MISSING_EVIDENCE="${H3_INCLUDE_MISSING_EVIDENCE:-1}"

pilot_require_dir "${SOURCE_ROLLOUT_DIR}" "source rollout directory"

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

ARGS=(
  --source-rollout-dir "${SOURCE_ROLLOUT_DIR}"
  --negative-rollout-dir "${NEGATIVE_ROLLOUT_DIR}"
  --out-dir "${OUT_DIR}"
  --top-k "${TOP_K}"
)

if [[ "${INCLUDE_MISSING_EVIDENCE}" == "1" ]]; then
  ARGS+=(--include-missing-evidence)
fi

if [[ -n "${MAX_PER_TYPE}" ]]; then
  ARGS+=(--max-per-type "${MAX_PER_TYPE}")
fi

python -m docworldtrace.pilot.h3_negative "${ARGS[@]}"

echo
echo "H3 negative-control outputs written to ${OUT_DIR}"
