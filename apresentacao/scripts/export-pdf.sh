#!/usr/bin/env bash
# Exporta apresentacao/slides.html para PDF via decktape (Chrome headless).
# Uso:
#   ./scripts/export-pdf.sh              -> build/slides.pdf
#   ./scripts/export-pdf.sh saida.pdf    -> caminho customizado
set -euo pipefail

cd "$(dirname "$0")/.."

SLIDES="slides.html"
OUT="${1:-build/slides.pdf}"
CHROME_BIN="${CHROME_PATH:-/usr/bin/google-chrome}"

mkdir -p "$(dirname "$OUT")"

npx --yes decktape@3 reveal \
  "file://$(pwd)/${SLIDES}" \
  "$OUT" \
  --size 1280x720 \
  --chrome-path "$CHROME_BIN"

echo "PDF gerado em ${OUT}"
