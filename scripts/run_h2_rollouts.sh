#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"
ENV_FILE="${DMXAPI_ENV_FILE:-${ROOT_DIR}/.env.dmxapi}"
SEED_FILE="${1:-${ROOT_DIR}/data/h2/seeds/pilot_seeds_v5.jsonl}"
TEACHER_CONFIG="${2:-${ROOT_DIR}/data/h2/teachers.json}"
OUT_DIR="${3:-${ROOT_DIR}/data/h2/rollouts_v5}"
REPEATS="${H2_REPEATS:-1}"
MAX_STEPS="${H2_MAX_STEPS:-8}"

pilot_require_file "${SEED_FILE}" "seed file"

if [[ ! -f "${TEACHER_CONFIG}" ]]; then
  echo "Missing teacher config: ${TEACHER_CONFIG}"
  echo "For DMXAPI, run: bash ${ROOT_DIR}/scripts/setup_h2_dmxapi_teachers.sh"
  echo "Or copy pilot_h2/teachers.example.json to data/h2/teachers.json and edit as needed."
  exit 1
fi

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

if [[ -z "${DMXAPI_API_KEY:-}" && -f "${ENV_FILE}" ]]; then
  pilot_load_env_file "${ENV_FILE}"
fi

if grep -q '"api_key_env"[[:space:]]*:[[:space:]]*"DMXAPI_API_KEY"' "${TEACHER_CONFIG}" && [[ -z "${DMXAPI_API_KEY:-}" ]]; then
  echo "Missing DMXAPI_API_KEY."
  echo "Set it with: export DMXAPI_API_KEY=..."
  echo "Or create ${ENV_FILE} from .env.dmxapi.example."
  exit 1
fi

python -m docworldtrace.pilot.h2_rollout \
  --seed-file "${SEED_FILE}" \
  --teacher-config "${TEACHER_CONFIG}" \
  --out-dir "${OUT_DIR}" \
  --repeats "${REPEATS}" \
  --max-steps "${MAX_STEPS}"

echo
echo "H2 rollout logs written to ${OUT_DIR}"
