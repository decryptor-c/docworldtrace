#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"

ROLLOUT_DIR="${1:-${ROOT_DIR}/data/h2/rollouts_v5}"
DOCVERIFY_JSON="${2:-${ROOT_DIR}/data/h3/docverify_plus_v5/docverify_review.json}"
SFT_OUT_DIR="${3:-${ROOT_DIR}/data/h5/sft_v5}"
EVAL_OUT_DIR="${4:-${ROOT_DIR}/data/h5/eval_v5}"
NO_TOOL_EVAL="${H5_NO_TOOL_EVAL:-}"
TOOL_EVAL="${H5_TOOL_EVAL:-${ROOT_DIR}/data/h2/eval_v5/summary.json}"
PATH_REVIEW="${H5_PATH_REVIEW:-${ROOT_DIR}/data/h2/eval_v5_path/path_review.json}"
HELDOUT_PER_TASK="${H5_HELDOUT_PER_TASK:-1}"

for path in "${ROLLOUT_DIR}" "${DOCVERIFY_JSON}" "${TOOL_EVAL}" "${PATH_REVIEW}"; do
  if [[ ! -e "${path}" ]]; then
    echo "Missing required H5 input: ${path}"
    exit 1
  fi
done
if [[ -z "${NO_TOOL_EVAL}" || ! -e "${NO_TOOL_EVAL}" ]]; then
  echo "Missing H5_NO_TOOL_EVAL. Set it to a no-tool baseline summary JSON before running H5."
  exit 1
fi

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

python -m docworldtrace.pilot.h5_sft \
  --rollout-dir "${ROLLOUT_DIR}" \
  --docverify "${DOCVERIFY_JSON}" \
  --out-dir "${SFT_OUT_DIR}" \
  --heldout-per-task "${HELDOUT_PER_TASK}"

python -m docworldtrace.pilot.h5_proxy_eval \
  --sft-summary "${SFT_OUT_DIR}/summary.json" \
  --no-tool-eval "${NO_TOOL_EVAL}" \
  --tool-eval "${TOOL_EVAL}" \
  --path-review "${PATH_REVIEW}" \
  --docverify "${DOCVERIFY_JSON}" \
  --out-dir "${EVAL_OUT_DIR}"

echo
echo "H5 SFT datasets written to ${SFT_OUT_DIR}"
echo "H5 proxy evaluation written to ${EVAL_OUT_DIR}"
