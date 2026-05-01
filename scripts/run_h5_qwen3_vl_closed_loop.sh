#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"

MODEL_DIR="${H5_MODEL_DIR:-${ROOT_DIR}/models/Qwen3-VL-8B-Instruct}"
RUN_DIR="${H5_RUN_DIR:-${ROOT_DIR}/runs/h5_qwen3_vl_diverse_v2}"
SFT_DIR="${H5_SFT_DIR:-${ROOT_DIR}/data/h5/sft_diverse_v2}"
ROLLOUT_DIR="${H5_ROLLOUT_DIR:-${ROOT_DIR}/data/h2/rollouts_diverse_v2}"
OUT_DIR="${H5_CLOSED_LOOP_OUT_DIR:-${ROOT_DIR}/data/h5/closed_loop_diverse_v2}"
SEED_FILE="${H5_SEED_FILE:-}"

MAX_STEPS="${H5_CLOSED_LOOP_MAX_STEPS:-8}"
MAX_LENGTH="${H5_MAX_LENGTH:-4096}"
MAX_NEW_TOKENS="${H5_MAX_NEW_TOKENS:-256}"
DTYPE="${H5_DTYPE:-bf16}"
DEVICE_MAP="${H5_DEVICE_MAP:-auto}"
LIMIT="${H5_CLOSED_LOOP_LIMIT:-0}"
SPLIT="${H5_CLOSED_LOOP_SPLIT:-eval}"

LOG_DIR="${H5_LOG_DIR:-${ROOT_DIR}/logs}"
mkdir -p "${LOG_DIR}"
LOG_FILE="${H5_CLOSED_LOOP_LOG:-${LOG_DIR}/h5_closed_loop_$(date +%Y%m%d_%H%M%S).log}"
exec > >(tee -a "${LOG_FILE}") 2>&1

echo "H5 closed-loop log: ${LOG_FILE}"

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

pilot_require_dir "${MODEL_DIR}" "Qwen3-VL model directory"
pilot_require_dir "${RUN_DIR}/answer_only_adapter" "answer-only adapter directory"
pilot_require_dir "${RUN_DIR}/trajectory_adapter" "trajectory adapter directory"
pilot_require_dir "${SFT_DIR}" "H5 SFT directory"
pilot_require_dir "${ROLLOUT_DIR}" "H2 rollout directory"
pilot_require_file "${SFT_DIR}/seed_split.jsonl" "H5 seed split"

args=(
  python -m docworldtrace.pilot.h5_closed_loop
  --base-model "${MODEL_DIR}"
  --adapter "answer_only=${RUN_DIR}/answer_only_adapter"
  --adapter "trajectory=${RUN_DIR}/trajectory_adapter"
  --sft-dir "${SFT_DIR}"
  --rollout-dir "${ROLLOUT_DIR}"
  --split "${SPLIT}"
  --out-dir "${OUT_DIR}"
  --max-steps "${MAX_STEPS}"
  --max-length "${MAX_LENGTH}"
  --max-new-tokens "${MAX_NEW_TOKENS}"
  --dtype "${DTYPE}"
  --device-map "${DEVICE_MAP}"
)

if [[ -n "${SEED_FILE}" ]]; then
  pilot_require_file "${SEED_FILE}" "seed JSONL"
  args+=(--seed-file "${SEED_FILE}")
fi

if [[ "${LIMIT}" != "0" ]]; then
  args+=(--limit "${LIMIT}")
fi

"${args[@]}"

echo
echo "H5 closed-loop evaluation complete."
echo "Output: ${OUT_DIR}"
echo "Summary: ${OUT_DIR}/summary.md"
echo "Log: ${LOG_FILE}"
