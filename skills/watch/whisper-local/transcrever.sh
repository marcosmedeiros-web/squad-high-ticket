#!/usr/bin/env bash
# transcrever.sh · acha o venv do faster-whisper e roda transcrever-local.py com ele. Uso:
#   bash <pasta-da-skill-watch>/whisper-local/transcrever.sh <video-ou-audio> [--model medium] [--start MM:SS] [--end MM:SS]
# Ordem de busca: $WHISPER_VENV · ~/.local/share/whisper-venv (padrão desde 21/09/2026) · venv antigo dentro da skill.
# Saídas: rc do transcrever-local.py · 2 = uso · 3 = venv não encontrado (rode instalar.sh)
set -u
DIR="$(cd "$(dirname "$0")" && pwd)"
[ $# -ge 1 ] || { sed -n '2,5p' "$0" | sed 's/^# \{0,1\}//'; exit 2; }
for v in "${WHISPER_VENV:-}" "$HOME/.local/share/whisper-venv" "$DIR/venv"; do
  [ -n "$v" ] && [ -x "$v/bin/python" ] || continue
  exec "$v/bin/python" "$DIR/transcrever-local.py" "$@"
done
echo "MOTIVO=whisper-venv-ausente rc=3 (procurei em \${WHISPER_VENV:-}, ~/.local/share/whisper-venv e $DIR/venv; rode: bash $DIR/instalar.sh)" >&2
exit 3
