#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"
ROLLOUT_DIR="${1:-${ROOT_DIR}/data/h2/rollouts_v5}"
DOCVERIFY_JSON="${2:-}"
OUT_DIR="${3:-${ROOT_DIR}/data/h4/diversity_v5}"

pilot_require_dir "${ROLLOUT_DIR}" "rollout directory"

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

ARGS=(
  --rollout-dir "${ROLLOUT_DIR}"
  --out-dir "${OUT_DIR}"
)

if [[ -n "${DOCVERIFY_JSON}" ]]; then
  pilot_require_file "${DOCVERIFY_JSON}" "DocVerify++ JSON"
  ARGS+=(--docverify "${DOCVERIFY_JSON}")
fi

python -m docworldtrace.pilot.h4_diversity "${ARGS[@]}"

echo
echo "H4 diversity outputs written to ${OUT_DIR}"
