#!/usr/bin/env bash
set -euo pipefail

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "This installer currently supports Ubuntu/Debian-style Linux servers only."
  exit 1
fi

if ! command -v apt-get >/dev/null 2>&1; then
  echo "apt-get not found. This installer expects Ubuntu/Debian."
  exit 1
fi

if [[ "${EUID}" -ne 0 ]]; then
  SUDO="sudo"
else
  SUDO=""
fi

${SUDO} apt-get update
${SUDO} apt-get install -y \
  build-essential \
  git \
  libgl1 \
  libglib2.0-0 \
  poppler-utils \
  python3 \
  python3-dev \
  python3-pip \
  python3-venv \
  tesseract-ocr \
  tesseract-ocr-eng

echo "System dependencies installed."
