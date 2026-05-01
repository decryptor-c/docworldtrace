#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"

ROLLOUT_DIR="${1:-${ROOT_DIR}/data/h2/rollouts_diverse_v2}"
DOCVERIFY_JSON="${2:-${ROOT_DIR}/data/h3/docverify_plus_diverse_v2/docverify_review.json}"
SFT_DIR="${3:-${ROOT_DIR}/data/h5/sft_diverse_v2}"
RUN_DIR="${4:-${ROOT_DIR}/runs/h5_qwen3_vl_diverse_v2}"

MODEL_DIR="${H5_MODEL_DIR:-${ROOT_DIR}/models/Qwen3-VL-8B-Instruct}"
HELDOUT_PER_TASK="${H5_HELDOUT_PER_TASK:-1}"
KEEP_ALL="${H5_KEEP_ALL:-auto}"
FORCE_TRAIN="${H5_FORCE_TRAIN:-0}"

MAX_LENGTH="${H5_MAX_LENGTH:-4096}"
EPOCHS="${H5_EPOCHS:-2}"
LR="${H5_LR:-2e-4}"
BATCH_SIZE="${H5_BATCH_SIZE:-1}"
EVAL_BATCH_SIZE="${H5_EVAL_BATCH_SIZE:-1}"
GRAD_ACCUM="${H5_GRAD_ACCUM:-8}"
DTYPE="${H5_DTYPE:-bf16}"
DEVICE_MAP="${H5_DEVICE_MAP:-auto}"
LORA_R="${H5_LORA_R:-16}"
LORA_ALPHA="${H5_LORA_ALPHA:-32}"
LOAD_IN_4BIT="${H5_LOAD_IN_4BIT:-0}"
LIMIT_EVAL="${H5_LIMIT_EVAL:-0}"

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

pilot_require_dir "${MODEL_DIR}" "Qwen3-VL model directory"
pilot_require_dir "${ROLLOUT_DIR}" "H2 rollout directory"
mkdir -p "${SFT_DIR}" "${RUN_DIR}"

json_ok=0
if [[ -f "${DOCVERIFY_JSON}" ]]; then
  if python - "${DOCVERIFY_JSON}" <<'PY'
import json
import sys
with open(sys.argv[1], "r", encoding="utf-8") as handle:
    json.load(handle)
PY
  then
    json_ok=1
  fi
fi

build_args=(
  python -m docworldtrace.pilot.h5_sft
  --rollout-dir "${ROLLOUT_DIR}"
  --out-dir "${SFT_DIR}"
  --heldout-per-task "${HELDOUT_PER_TASK}"
)

if [[ "${KEEP_ALL}" == "1" || ( "${KEEP_ALL}" == "auto" && "${json_ok}" == "0" ) ]]; then
  echo "Building H5 SFT data with --keep-all."
  echo "Reason: H5_KEEP_ALL=${KEEP_ALL}, docverify_json_valid=${json_ok}."
  build_args+=(--keep-all)
else
  pilot_require_file "${DOCVERIFY_JSON}" "DocVerify++ JSON"
  build_args+=(--docverify "${DOCVERIFY_JSON}")
fi

"${build_args[@]}"

train_adapter() {
  local name="$1"
  local train_file="$2"
  local eval_file="$3"
  local out_dir="${RUN_DIR}/${name}_adapter"

  if [[ -f "${out_dir}/adapter_config.json" && "${FORCE_TRAIN}" != "1" ]]; then
    echo "Skipping ${name} training because ${out_dir}/adapter_config.json exists."
    echo "Set H5_FORCE_TRAIN=1 to retrain."
    return
  fi

  local args=(
    python -m docworldtrace.pilot.h5_qwen_sft
    --model-name-or-path "${MODEL_DIR}"
    --train-file "${train_file}"
    --eval-file "${eval_file}"
    --output-dir "${out_dir}"
    --max-length "${MAX_LENGTH}"
    --num-train-epochs "${EPOCHS}"
    --learning-rate "${LR}"
    --per-device-train-batch-size "${BATCH_SIZE}"
    --per-device-eval-batch-size "${EVAL_BATCH_SIZE}"
    --gradient-accumulation-steps "${GRAD_ACCUM}"
    --dtype "${DTYPE}"
    --device-map "${DEVICE_MAP}"
    --lora-r "${LORA_R}"
    --lora-alpha "${LORA_ALPHA}"
  )
  if [[ "${LOAD_IN_4BIT}" == "1" ]]; then
    args+=(--load-in-4bit)
  fi
  "${args[@]}"
}

eval_adapter() {
  local adapter_name="$1"
  local eval_name="$2"
  local eval_file="$3"
  local out_dir="${RUN_DIR}/eval/${adapter_name}_on_${eval_name}"
  local args=(
    python -m docworldtrace.pilot.h5_qwen_eval
    --model-or-adapter "${RUN_DIR}/${adapter_name}_adapter"
    --base-model "${MODEL_DIR}"
    --eval-file "${eval_file}"
    --output-dir "${out_dir}"
    --max-length "${MAX_LENGTH}"
    --dtype "${DTYPE}"
    --device-map "${DEVICE_MAP}"
  )
  if [[ "${LIMIT_EVAL}" != "0" ]]; then
    args+=(--limit "${LIMIT_EVAL}")
  fi
  "${args[@]}"
}

train_adapter \
  "answer_only" \
  "${SFT_DIR}/answer_only_train.jsonl" \
  "${SFT_DIR}/answer_only_eval.jsonl"

train_adapter \
  "trajectory" \
  "${SFT_DIR}/trajectory_train.jsonl" \
  "${SFT_DIR}/trajectory_eval.jsonl"

eval_adapter "answer_only" "answer_only_eval" "${SFT_DIR}/answer_only_eval.jsonl"
eval_adapter "answer_only" "trajectory_eval" "${SFT_DIR}/trajectory_eval.jsonl"
eval_adapter "trajectory" "answer_only_eval" "${SFT_DIR}/answer_only_eval.jsonl"
eval_adapter "trajectory" "trajectory_eval" "${SFT_DIR}/trajectory_eval.jsonl"

python - <<'PY' "${RUN_DIR}"
import json
import sys
from pathlib import Path

run_dir = Path(sys.argv[1])
rows = []
for path in sorted((run_dir / "eval").glob("*/summary.json")):
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows.append({"eval": path.parent.name, **payload})
(run_dir / "h5_qwen_eval_summary.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(rows, ensure_ascii=False, indent=2))
PY

echo
echo "H5 Qwen3-VL SFT run complete."
echo "SFT data: ${SFT_DIR}"
echo "Adapters and eval: ${RUN_DIR}"
