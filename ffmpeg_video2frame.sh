echo "这是视频转帧"

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


echo "这是帧转视频"

#!/usr/bin/env bash
set -euo pipefail

# 用法：
#   ./png2mp4.sh [图片文件夹] [输出视频名] [帧率]
# 示例：
#   ./png2mp4.sh ./frames out.mp4 30

IMG_DIR="${1:-.}"
OUT_VIDEO="${2:-out.mp4}"
FPS="${3:-30}"

cd "$IMG_DIR"

ffmpeg -y \
  -framerate "$FPS" \
  -pattern_type glob -i "*.png" \
  -c:v libx264 -pix_fmt yuv420p \
  "$OUT_VIDEO"
