#!/usr/bin/env bash
set -euo pipefail

source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/pilot_common.sh"

ROOT_DIR="$(pilot_root_dir)"
INSTALL_TORCH="${H5_INSTALL_TORCH:-0}"
TORCH_INDEX_URL="${H5_TORCH_INDEX_URL:-https://download.pytorch.org/whl/cu121}"

pilot_activate_venv "${ROOT_DIR}"
cd "${ROOT_DIR}"

python -m pip install --upgrade pip setuptools wheel

if [[ "${INSTALL_TORCH}" == "1" ]]; then
  echo "Installing torch from ${TORCH_INDEX_URL}"
  python -m pip install --index-url "${TORCH_INDEX_URL}" torch torchvision torchaudio
else
  echo "Skipping torch install. Set H5_INSTALL_TORCH=1 if torch is missing."
fi

python -m pip install -r "${ROOT_DIR}/requirements-h5-sft.txt"

if ! python - <<'PY'
from transformers import Qwen3VLForConditionalGeneration  # noqa: F401
PY
then
  echo "Installed transformers does not expose Qwen3VLForConditionalGeneration."
  echo "Installing the latest Hugging Face transformers from GitHub..."
  python -m pip install -U "git+https://github.com/huggingface/transformers.git"
fi

python - <<'PY'
import torch
import transformers
import peft
print("torch:", torch.__version__)
print("cuda_available:", torch.cuda.is_available())
print("transformers:", transformers.__version__)
print("peft:", peft.__version__)
from transformers import Qwen3VLForConditionalGeneration  # noqa: F401
print("Qwen3VLForConditionalGeneration: ok")
PY
