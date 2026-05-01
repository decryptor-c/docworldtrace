#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODEL_ID="${MODEL_ID:-Qwen/Qwen3-VL-8B-Instruct}"
MODEL_DIR="${MODEL_DIR:-${ROOT_DIR}/models/Qwen3-VL-8B-Instruct}"
PYTHON_BIN="${PYTHON_BIN:-python3}"

cd "${ROOT_DIR}"

if [[ -d "${ROOT_DIR}/.venv" ]]; then
  # shellcheck disable=SC1091
  source "${ROOT_DIR}/.venv/bin/activate"
else
  echo "Warning: ${ROOT_DIR}/.venv not found; using ${PYTHON_BIN} from PATH."
fi

mkdir -p "${MODEL_DIR}"

echo "Model ID: ${MODEL_ID}"
echo "Target directory: ${MODEL_DIR}"
echo
df -h "${ROOT_DIR}" || true
echo

if ! python -c "import modelscope" >/dev/null 2>&1; then
  echo "Installing modelscope into the active Python environment..."
  python -m pip install -U modelscope
fi

echo "Downloading model with ModelScope..."
modelscope download \
  --model "${MODEL_ID}" \
  --local_dir "${MODEL_DIR}"

echo
echo "Model downloaded to ${MODEL_DIR}"
echo "Top-level files:"
find "${MODEL_DIR}" -maxdepth 1 -type f -print | sort
