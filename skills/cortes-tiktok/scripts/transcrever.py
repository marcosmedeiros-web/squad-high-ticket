#!/usr/bin/env python
"""Transcreve o áudio da aula em português com timestamps por segmento e por palavra.

Saída: transcricao.json (dados brutos) + transcricao.txt (leitura humana, com timecode).
O JSON com timestamps de palavra é o que permite cortar em 60s no ponto exato
e depois queimar legenda revisada.
"""
import json
import sys
from pathlib import Path

from faster_whisper import WhisperModel

AUDIO = Path(sys.argv[1] if len(sys.argv) > 1 else "fonte/aula1-audio.wav")
BASE = Path(sys.argv[2] if len(sys.argv) > 2 else "transcricao")

model = WhisperModel("medium", device="cpu", compute_type="int8")

segments, info = model.transcribe(
    str(AUDIO),
    language="pt",
    word_timestamps=True,
    vad_filter=True,
    vad_parameters={"min_silence_duration_ms": 500},
    beam_size=5,
)

print(f"duracao detectada: {info.duration:.0f}s", flush=True)

dados = []
with open(f"{BASE}.txt", "w", encoding="utf-8") as ftxt:
    for seg in segments:
        m, s = divmod(int(seg.start), 60)
        ftxt.write(f"[{m:02d}:{s:02d}] {seg.text.strip()}\n")
        ftxt.flush()
        dados.append({
            "start": seg.start,
            "end": seg.end,
            "text": seg.text.strip(),
            "words": [
                {"start": w.start, "end": w.end, "word": w.word}
                for w in (seg.words or [])
            ],
        })
        if len(dados) % 25 == 0:
            print(f"  ...{len(dados)} segmentos ({seg.end:.0f}s)", flush=True)

Path(f"{BASE}.json").write_text(
    json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8"
)
print(f"pronto: {len(dados)} segmentos")
