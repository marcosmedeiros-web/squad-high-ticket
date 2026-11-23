#!/bin/bash
# montar_faixa.sh — espera os N renders da faixa, concatena e sobrepõe no vídeo. Roda no Mac e no Linux/WSL.
# Ajuste antes: N (quantos takes), Y (onde a faixa começa), SRC (o vídeo de origem) e BROLL_DIR (pasta de trabalho).
set -u
BROLL_DIR="${BROLL_DIR:-$HOME/videos-broll}"; cd "$BROLL_DIR" || { echo "sem a pasta de trabalho $BROLL_DIR"; exit 2; }
N="${N:-130}"; Y="${Y:-1076}"; SRC="${SRC:-$BROLL_DIR/video-cortado.mov}"; OUT="${OUT:-$BROLL_DIR/VSL-FAIXA-HYPERFRAME.mp4}"
FF="$(command -v ffmpeg)" || { echo "sem ffmpeg no PATH"; exit 2; }
if [ "$(uname -s)" = Darwin ]; then VENC=(-c:v h264_videotoolbox -b:v 12M); else VENC=(-c:v libx264 -preset veryfast -crf 18); fi
mkdir -p logs; LISTA="$BROLL_DIR/logs/bar-concat.txt"
for i in $(seq 1 240); do   # espera os N
  ok=1; for n in $(seq 0 $((N-1))); do nnn=$(printf "%03d" $n); [ -s "brolls/bar/bar-$nnn.mp4" ] || ok=0; done
  [ "$ok" = "1" ] && break; sleep 10
done
echo "[bar $(date +%H:%M:%S)] todos renderizados, concatenando" >> logs/auto-bar.log
: > "$LISTA"
for n in $(seq 0 $((N-1))); do nnn=$(printf "%03d" $n); echo "file '$PWD/brolls/bar/bar-$nnn.mp4'" >> "$LISTA"; done
"$FF" -y -f concat -safe 0 -i "$LISTA" -c:v libx264 -preset veryfast -crf 18 -pix_fmt yuv420p -r 30 brolls/bar/bar-track.mp4 >> logs/auto-bar.log 2>&1
echo "[bar $(date +%H:%M:%S)] overlay na faixa preta (y=$Y)" >> logs/auto-bar.log
"$FF" -y -i "$SRC" -i brolls/bar/bar-track.mp4 -filter_complex "[1:v]scale=1080:844,setsar=1,fps=30[bar];[0:v][bar]overlay=0:$Y:shortest=0[v]" -map "[v]" -map 0:a "${VENC[@]}" -c:a aac -b:a 192k -movflags +faststart "$OUT" >> logs/auto-bar.log 2>&1
if [ -s "$OUT" ]; then
  if [ "$(uname -s)" = Darwin ]; then osascript -e 'tell application "QuickTime Player" to quit' 2>/dev/null; open "$OUT"; fi
  echo "[bar $(date +%H:%M:%S)] PRONTO: $OUT" >> logs/auto-bar.log; echo "PRONTO: $OUT"
fi
