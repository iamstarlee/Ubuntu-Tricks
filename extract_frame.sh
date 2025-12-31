#!/usr/bin/env bash
set -euo pipefail

IN="${1:-/data2/lxx_datasets/FBD-SV-2024/videos/train/bird_26.mp4}"
FPS="${2:-25}"
OUTDIR="${3:-/data2/lxx_datasets/FBD-SV-2024/VID/images/train/bird_26}"
PATTERN="${4:-image%04d.png}"

mkdir -p "$OUTDIR"

ffmpeg -hide_banner -y \
  -i "$IN" \
  -vf "fps=${FPS}" \
  "${OUTDIR}/${PATTERN}"
