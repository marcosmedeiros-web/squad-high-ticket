#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# instalar.sh · monta o venv do fallback local de transcrição (faster-whisper)
#
# O zip da skill NÃO carrega o venv (218 MB) — quem instala roda isto UMA vez:
#   bash <pasta-da-skill-watch>/whisper-local/instalar.sh
#
# O venv vive FORA da árvore de skills: ~/.local/share/whisper-venv (ou $WHISPER_VENV).
# Dentro da skill ele pesava na instalação: os links bin/python* e os binários atrapalham cópia e varredura da pasta.
# O modelo em si baixa sozinho no primeiro uso do transcrever-local.py
# (medium ≈ 3,5 GB no cache ~/.cache/huggingface · tiny ≈ 75 MB).
# ─────────────────────────────────────────────────────────────────────────────
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="${WHISPER_VENV:-$HOME/.local/share/whisper-venv}"

if [[ -x "$VENV/bin/python" ]] && "$VENV/bin/python" -c "import faster_whisper" 2>/dev/null; then
  echo "✓ venv já pronto em $VENV — nada a fazer."
else
  echo "→ criando venv em $VENV"
  mkdir -p "$(dirname "$VENV")"
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install --quiet --upgrade pip
  "$VENV/bin/pip" install --quiet faster-whisper 'av<19'
  "$VENV/bin/python" -c "import faster_whisper" || { echo "MOTIVO=whisper-venv-incompleto rc=4 (faster_whisper não importa em $VENV)"; exit 4; }
fi

# venv antigo DENTRO da skill: só sai depois que o novo provou que importa (acima). Nunca apaga nada além dele.
if [[ -d "$DIR/venv" ]]; then
  echo "→ removendo o venv antigo de dentro da skill ($DIR/venv): ele atrapalhava a cópia e a varredura da pasta"
  rm -rf "$DIR/venv"
fi

echo "✓ pronto. Teste rápido (baixa o modelo tiny, ~75 MB):"
echo "  bash $DIR/transcrever.sh <video.mp4> --model tiny"
