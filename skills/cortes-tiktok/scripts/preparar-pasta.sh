#!/bin/bash
# Prepara uma pasta de trabalho nova para a pipeline de cortes.
#   bash preparar-pasta.sh [pasta]
# Copia scripts e modelos-base, baixa o modelo de segmentação e cria o venv.
set -euo pipefail
SKILL="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIR="${1:-.}"
mkdir -p "$DIR"/{transcricoes,cortes,fundos,modelos,fontes}
cd "$DIR"

cp -n "$SKILL"/scripts/*.py .
cp -n "$SKILL"/scripts/correcoes.json "$SKILL"/scripts/bipar.json .
cp -n "$SKILL"/fontes/Montserrat-var.ttf fontes/

# modelo de segmentação (16 MB) — só necessário para trocar o fundo
M=modelos/selfie_multiclass_256x256.tflite
[ -s "$M" ] || curl -fsSL -o "$M" \
  "https://storage.googleapis.com/mediapipe-models/image_segmenter/selfie_multiclass_256x256/float32/latest/selfie_multiclass_256x256.tflite"

# venv próprio: o Python do sistema não tem cv2 nem mediapipe, e a falha
# só aparece na hora do render, depois de já ter gasto tempo
[ -d .venv ] || python3 -m venv .venv
./.venv/bin/pip install -q --upgrade pip
./.venv/bin/pip install -q faster-whisper 'av<19' mediapipe opencv-python numpy Pillow

[ -f projeto.json ] || cat > projeto.json <<'JSON'
{
  "fontes_dir": "CAMINHO/PARA/OS/VIDEOS",
  "fontes": {"01": "GRAVACAO.MP4"},
  "crop":   {"A": [1080, 1920, 0, 0]},
  "sessao": {"01": "A"},
  "contraste": {"A": [1.08, 0.5]}
}
JSON

echo "pronto em $(pwd)"
echo "1. edite projeto.json com o caminho e os nomes dos seus vídeos"
echo "2. ./.venv/bin/python enquadrar.py 01 60     (achar o crop)"
echo "3. ./.venv/bin/python transcrever.py audio.wav transcricoes/01"
