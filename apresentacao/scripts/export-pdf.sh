#!/usr/bin/env bash
# Exporta um slides.html local para PDF via decktape (Chrome headless).
# Uso:
#   ./scripts/export-pdf.sh              -> slides.pdf
#   ./scripts/export-pdf.sh saida.pdf    -> caminho customizado
set -euo pipefail

cd "$(dirname "$0")/.."

SLIDES="slides.html"
OUT="${1:-slides.pdf}"
CHROME_BIN="${CHROME_PATH:-/usr/bin/google-chrome}"

if [[ ! -f "$SLIDES" ]]; then
  echo "slides.html nao encontrado em $(pwd)." >&2
  echo "Recrie o deck primeiro e rode novamente." >&2
  exit 1
fi

mkdir -p "$(dirname "$OUT")"

npx --yes decktape@3 reveal \
  "file://$(pwd)/${SLIDES}" \
  "$OUT" \
  --size 1280x720 \
  --chrome-path "$CHROME_BIN"

echo "PDF gerado em ${OUT}"
