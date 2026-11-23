#!/usr/bin/env python
"""Extrai uma chapa de fundo limpa de um vídeo em que a pessoa aparece.

    python fundo.py VIDEO SAIDA.jpg [--amostras 128] [--desfoque 9]

Serve para reaproveitar um cenário bom (a sala do expert, com estante, placas,
identidade visual) como fundo de cortes gravados em outro lugar.

MEDIANA SIMPLES NÃO FUNCIONA. Se a pessoa fica parada — e numa aula ela fica —
a mediana temporal de cada pixel É o rosto dela. O que funciona: segmentar cada
quadro amostrado e compor o pixel apenas a partir dos quadros em que AQUELE
pixel é fundo. Onde nunca é fundo (atrás do corpo, o tempo todo), preencher com
inpaint. Cobertura típica: 85-90% real, o resto reconstruído.

Depois desfoca. O fundo desfocado faz três coisas: esconde a costura do
inpaint, cria profundidade que separa a pessoa do cenário, e não compete com
a legenda.

Requer: mediapipe, opencv-python, numpy. Modelo em modelos/selfie_multiclass_256x256.tflite
(https://storage.googleapis.com/mediapipe-models/image_segmenter/selfie_multiclass_256x256/float32/latest/selfie_multiclass_256x256.tflite)
"""
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks.python import vision, BaseOptions

W, H = 1080, 1920
VIDEO = Path(sys.argv[1])
SAIDA = Path(sys.argv[2] if len(sys.argv) > 2 else "fundo.jpg")
N = int(sys.argv[sys.argv.index("--amostras") + 1]) if "--amostras" in sys.argv else 128
SIGMA = float(sys.argv[sys.argv.index("--desfoque") + 1]) if "--desfoque" in sys.argv else 9.0
MODELO = Path.cwd() / "modelos" / "selfie_multiclass_256x256.tflite"

dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                            "format=duration", "-of", "csv=p=0", str(VIDEO)],
                           capture_output=True, text=True).stdout)
print(f"vídeo de {dur:.0f}s, amostrando {N} quadros")

seg = vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(
    base_options=BaseOptions(model_asset_path=str(MODELO)),
    running_mode=vision.RunningMode.IMAGE, output_category_mask=True))

soma = np.zeros((H, W, 3), np.float64)
peso = np.zeros((H, W), np.float64)
for i in range(N):
    t = dur * (i + 0.5) / N
    raw = subprocess.run(
        ["ffmpeg", "-loglevel", "error", "-ss", f"{t:.2f}", "-i", str(VIDEO),
         "-frames:v", "1", "-vf", f"scale={W}:{H}", "-f", "rawvideo",
         "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    if len(raw) != W * H * 3:
        continue
    rgb = np.frombuffer(raw, np.uint8).reshape(H, W, 3)
    r = seg.segment(mp.Image(image_format=mp.ImageFormat.SRGB,
                             data=np.ascontiguousarray(rgb)))
    cat = cv2.resize(r.category_mask.numpy_view(), (W, H),
                     interpolation=cv2.INTER_NEAREST)
    # dilata a pessoa antes de descartar: a borda da máscara ainda tem halo dela
    pessoa = cv2.dilate((cat > 0).astype(np.uint8), np.ones((25, 25), np.uint8), 1)
    ehfundo = (pessoa == 0)
    soma[ehfundo] += rgb[ehfundo]
    peso[ehfundo] += 1
    if (i + 1) % 20 == 0:
        print(f"  {i+1}/{N}  cobertura {100*(peso>0).mean():.0f}%")
seg.close()

cob = (peso > 0)
print(f"cobertura final: {100*cob.mean():.1f}% real, o resto vai de inpaint")
placa = np.zeros((H, W, 3), np.uint8)
placa[cob] = (soma[cob] / peso[cob, None]).astype(np.uint8)
placa = cv2.inpaint(placa, (~cob).astype(np.uint8), 15, cv2.INPAINT_TELEA)

placa = cv2.GaussianBlur(placa, (0, 0), SIGMA)
placa = cv2.convertScaleAbs(placa, alpha=1.16, beta=10)
# vinheta: escurece a borda e empurra o olho para o centro, onde a pessoa fica
yy, xx = np.mgrid[0:H, 0:W]
d = np.sqrt(((xx - W/2)/(W/2))**2 + ((yy - H/2)/(H/2))**2)
vin = np.clip(1.0 - 0.30*np.clip(d - 0.45, 0, None)/0.9, 0.62, 1.0)[..., None]
placa = (placa * vin).astype(np.uint8)

cv2.imwrite(str(SAIDA), cv2.cvtColor(placa, cv2.COLOR_RGB2BGR),
            [cv2.IMWRITE_JPEG_QUALITY, 95])
print(f"pronto: {SAIDA}")
