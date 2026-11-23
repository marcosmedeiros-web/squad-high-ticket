#!/usr/bin/env python
"""Acha o reenquadramento 9:16 de um material novo.

    python enquadrar.py ID SEGUNDOS [--aplicar L A X Y]

Sem --aplicar: mostra a resolução da fonte, propõe um crop 9:16 com os olhos
no terço superior e grava um contato com três variações para você escolher.
Com --aplicar: grava um único quadro com aquele crop, para conferir.

Por que isso existe: câmera parada em 9:16 nativo ainda vem com teto morto e o
rosto no meio do quadro. No feed vertical o rosto tem que ficar ALTO — o terço
de baixo é onde entra a legenda e a interface do app. Um crop errado custa
todos os cortes do lote, então mede antes.
"""
import json
import subprocess
import sys
from pathlib import Path

BASE = Path.cwd()
cfg = json.loads((BASE / "projeto.json").read_text(encoding="utf-8"))
FONTE = Path(cfg["fontes_dir"]).expanduser() / cfg["fontes"][sys.argv[1]]
T = sys.argv[2] if len(sys.argv) > 2 else "60"

info = json.loads(subprocess.run(
    ["ffprobe", "-v", "error", "-select_streams", "v:0",
     "-show_entries", "stream=width,height", "-of", "json", str(FONTE)],
    capture_output=True, text=True).stdout)["streams"][0]
W0, H0 = info["width"], info["height"]
print(f"fonte: {W0}x{H0}")

if "--aplicar" in sys.argv:
    i = sys.argv.index("--aplicar")
    props = [tuple(int(x) for x in sys.argv[i + 1:i + 5])]
    nomes = ["escolhido"]
else:
    # três alturas de corte: quanto maior o corte, mais fechado no rosto
    props, nomes = [], []
    for frac, nome in ((1.00, "cheio"), (0.93, "medio"), (0.85, "fechado")):
        ch = int(H0 * frac) // 2 * 2
        cw = min(W0, int(ch * 9 / 16)) // 2 * 2
        cx = (W0 - cw) // 2
        cy = int((H0 - ch) * 0.35)      # sobra mais embaixo que em cima
        props.append((cw, ch, cx, cy))
        nomes.append(nome)

partes = []
for (cw, ch, cx, cy), nome in zip(props, nomes):
    p = f"_enq-{nome}.jpg"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", T, "-i", str(FONTE),
                    "-frames:v", "1", "-vf",
                    f"crop={cw}:{ch}:{cx}:{cy},scale=270:480,"
                    f"drawbox=0:336:270:1:red@0.8:t=2", p], check=True)
    print(f"{nome:9} crop={cw}:{ch}:{cx}:{cy}   -> {p}")
    partes.append(p)

if len(partes) > 1:
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y",
                    *sum([["-i", p] for p in partes], []),
                    "-filter_complex", f"hstack=inputs={len(partes)}",
                    "_enquadramento.jpg"], check=True)
    print("\ncontato: _enquadramento.jpg")
    print("A linha vermelha marca 70% da altura, onde a legenda vai entrar.")
    print("Escolha aquele em que o rosto fica ACIMA da linha com folga,")
    print("e ponha o crop em projeto.json na chave 'crop'.")
