#!/usr/bin/env python
"""Produz um corte vertical pronto para o TikTok a partir de uma gravação longa.

Faz, em um passo só:
  1. corte + reenquadramento 9:16 + grade de cor medida trecho a trecho
  2. troca de fundo (segmentação MediaPipe) — opcional
  3. bipe em cima de nome e número específico, no áudio E na legenda
  4. legenda queimada Montserrat 74 a 70% de altura
  5. áudio normalizado a -14 LUFS

Uso:
    python produzir.py ID TRECHOS SAIDA.mp4 [opções]

    python produzir.py 01 "01:13-01:58" cortes/01-regra.mp4

TRECHOS aceita vários, e a ORDEM DADA é a ordem final — é assim que se põe o
gancho no segundo zero e o contexto depois:

    "08:11-08:16,07:56-08:11,08:16-08:24"

Um trecho pode vir de outra fonte, com o prefixo FONTE@:

    "12:08-12:18,02@05:30-05:34"

Opções:
    --fundo IMG      troca o fundo por essa chapa (ver fundo.py)
    --bipar "a,b"    palavras extras além das de bipar.json
    --so-legenda     gera só o .txt de revisão. RODE SEMPRE ANTES DE RENDERIZAR
    --exposicao G    força o gamma em vez de medir
    --preto P        força o ponto preto
    --saturacao S    força a saturação

Configuração do projeto em projeto.json na pasta atual (ver SKILL.md).
"""
import argparse
import json
import math
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

BASE = Path.cwd()
CFG = BASE / "projeto.json"
if not CFG.exists():
    sys.exit(
        "falta projeto.json na pasta atual. Modelo:\n"
        + json.dumps({
            "fontes_dir": "caminho/para/os/videos",
            "fontes": {"01": "GRAVACAO_A.MP4", "02": "GRAVACAO_B.MP4"},
            "crop": {"A": [1440, 2560, 58, 399]},
            "sessao": {"01": "A", "02": "A"},
            "contraste": {"A": [1.10, 0.5]},
        }, indent=2, ensure_ascii=False))

_cfg = json.loads(CFG.read_text(encoding="utf-8"))
CORTES_DIR = Path(_cfg["fontes_dir"]).expanduser()
CORRECOES = BASE / "correcoes.json"
BIPAR = BASE / "bipar.json"
MODELO = BASE / "modelos" / "selfie_multiclass_256x256.tflite"

FONTES = _cfg["fontes"]
# (largura, altura, x, y) do reenquadramento 9:16, medido por sessão de gravação.
# Rodar `python enquadrar.py ID SEGUNDOS` para achar os números de um material novo.
CROP = {k: tuple(v) for k, v in _cfg["crop"].items()}
SESSAO = _cfg["sessao"]

# contraste e nitidez por sessão. O brilho NÃO entra aqui: quem equaliza a
# exposição é o gamma medido por trecho, e um gamma somado a um brightness
# fixo é exatamente o que leiteia a imagem.
GRADE = {k: tuple(v) for k, v in _cfg.get("contraste", {}).items()}
for _s in set(SESSAO.values()):
    GRADE.setdefault(_s, (1.08, 0.5))

W, H, FPS = 1080, 1920, 30

def _vinheta():
    import numpy as np
    yy, xx = np.mgrid[0:H, 0:W]
    d = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    return np.clip(1.0 - 0.30 * np.clip(d - 0.45, 0, None) / 0.9, 0.62, 1.0)[..., None].astype("float32")

_VIN = None
PALAVRAS_POR_BLOCO = 4
ALTURA_LEGENDA = 0.70
MARGEM_BIPE = 0.06          # respiro antes/depois de cada palavra bipada


# ---------------------------------------------------------------- utilidades
def parse_segmentos(spec, fid_padrao):
    """'01:17-01:31,0040@12:08-12:18' -> [('0041',77.0,91.0),('0040',728.0,738.0)].

    Duas coisas de uma vez:
      - a ordem dada é a ordem final, então o trecho de maior impacto pode virar
        o segundo 0 e o contexto entrar depois. É o que separa um corte que
        retém de um corte linear;
      - o prefixo `FONTE@` deixa um corte cruzar arquivos de origem. Serve pra
        casar dois trechos do mesmo assunto gravados em momentos diferentes.
    """
    segs = []
    for parte in spec.split(","):
        parte = parte.strip()
        if not parte:
            continue
        fid = fid_padrao
        if "@" in parte:
            fid, parte = parte.split("@", 1)
        a, b = parte.split("-")
        segs.append((fid, para_segundos(a), para_segundos(b)))
    return segs


def para_segundos(v):
    v = str(v)
    if ":" in v:
        s = 0.0
        for p in v.split(":"):
            s = s * 60 + float(p)
        return s
    return float(v)


def ass_tempo(s):
    h, r = divmod(max(0.0, s), 3600)
    m, s = divmod(r, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def sem_acento(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn").lower()


def carregar_json(p, padrao):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else padrao


# ---------------------------------------------------------------- censura
def carregar_regras(extra):
    cfg = carregar_json(BIPAR, {"nomes": [], "padroes": []})
    nomes = {sem_acento(n) for n in cfg.get("nomes", []) if n}
    nomes |= {sem_acento(n.strip()) for n in (extra or "").split(",") if n.strip()}
    padroes = [re.compile(p, re.IGNORECASE) for p in cfg.get("padroes", [])]
    return nomes, padroes


def deve_bipar(palavra, nomes, padroes):
    limpa = sem_acento(re.sub(r"[^\wÀ-ÿ]", "", palavra))
    if not limpa:
        return False
    if limpa in nomes:
        return True
    return any(p.search(palavra) for p in padroes)


# ---------------------------------------------------------------- legenda
def montar_blocos(segmentos, nomes, padroes):
    """Junta as palavras de todos os trechos, remapeando para a linha do tempo
    do corte final (cada trecho entra em sequência a partir de 0). Cada trecho
    lê a transcrição da sua própria fonte, porque um corte pode cruzar
    arquivos."""
    corr = carregar_json(CORRECOES, {})
    frases = corr.get("_frases", {})
    mapa = {k.lower(): v for k, v in corr.items() if not k.startswith("_")}

    trans = {}
    censura, saida = [], []
    deslocamento = 0.0
    for fid, ini_s, fim_s in segmentos:
        if fid not in trans:
            dados = json.loads((BASE / "transcricoes" / f"{fid}.json")
                               .read_text(encoding="utf-8"))
            trans[fid] = [w for seg in dados for w in seg["words"]
                          if w["start"] is not None]
        for w in trans[fid]:
            if not (ini_s <= w["start"] < fim_s):
                continue
            t0 = w["start"] - ini_s + deslocamento
            t1 = w["end"] - ini_s + deslocamento
            texto = w["word"]
            if deve_bipar(texto, nomes, padroes):
                censura.append((max(0.0, t0 - MARGEM_BIPE), t1 + MARGEM_BIPE))
                texto = re.sub(r"[\wÀ-ÿ]+", "———", texto)
            saida.append({"start": t0, "end": t1, "word": texto})
        deslocamento += fim_s - ini_s
    if not saida:
        return [], []

    # correções de transcrição depois da censura, para não desfazer o ———
    texto_todo = "".join(x["word"] for x in saida)
    for errado, certo in frases.items():
        texto_todo = re.sub(re.escape(errado), certo, texto_todo, flags=re.IGNORECASE)
    if mapa:
        pad = r"\b(" + "|".join(re.escape(p) for p in mapa) + r")\b"
        texto_todo = re.sub(pad, lambda m: mapa.get(m.group(0).lower()) or m.group(0),
                            texto_todo, flags=re.IGNORECASE)
    # remontar trechos fora de ordem deixa minúscula depois de ponto na costura
    texto_todo = re.sub(r"([.!?])(\s+)([a-zà-ÿ])",
                        lambda m: m.group(1) + m.group(2) + m.group(3).upper(),
                        texto_todo)
    tokens = texto_todo.split()

    blocos = []
    passo = max(1, round(len(tokens) / max(1, len(saida) / PALAVRAS_POR_BLOCO)))
    for i in range(0, len(tokens), passo):
        grupo = tokens[i:i + passo]
        ii = min(int(i * len(saida) / max(1, len(tokens))), len(saida) - 1)
        jj = max(min(int((i + len(grupo)) * len(saida) / max(1, len(tokens))) - 1,
                     len(saida) - 1), ii)
        blocos.append((saida[ii]["start"], saida[jj]["end"], " ".join(grupo)))
    return blocos, uniao(censura)


def uniao(spans):
    if not spans:
        return []
    spans = sorted(spans)
    out = [list(spans[0])]
    for a, b in spans[1:]:
        if a <= out[-1][1] + 0.02:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return [tuple(x) for x in out]


def escrever_ass(blocos, destino):
    mv = int(H * (1 - ALTURA_LEGENDA))
    cab = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Legenda,Montserrat,74,&H00FFFFFF,&H00000000,&H90000000,-1,1,6,0,2,90,90,{mv},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    linhas = [f"Dialogue: 0,{ass_tempo(a)},{ass_tempo(b)},Legenda,,0,0,0,,{t}"
              for a, b, t in blocos if t]
    destino.write_text(cab + "\n".join(linhas) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- vídeo
ALVO_MEDIANA = 0.48        # mediana de luma que todo corte deve atingir
_GRADE_CACHE = {}


def medir_grade(fid, a, b):
    """Mede o trecho e devolve (gamma, ponto preto, saturação).

    O sol se pôs no meio da gravação de 08/08: a mediana de luma vai de 0,19 a
    0,66 entre os trechos. Sem medir e equalizar, os cortes postados em
    sequência parecem vídeos diferentes. Mede por TRECHO, não por corte, porque
    um corte remontado costuma juntar momentos com luz bem diferente.
    """
    import numpy as np
    chave = (fid, round(a, 1), round(b, 1))
    if chave in _GRADE_CACHE:
        return _GRADE_CACHE[chave]
    cw, ch, cx, cy = CROP[SESSAO[fid]]
    fonte = CORTES_DIR / FONTES[fid]
    quadros = []
    for t in (a, (a + b) / 2, max(a, b - 0.5)):
        out = subprocess.run(
            ["ffmpeg", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", str(fonte),
             "-frames:v", "1", "-vf", f"crop={cw}:{ch}:{cx}:{cy},scale=240:426",
             "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
            capture_output=True).stdout
        if len(out) == 240 * 426 * 3:
            quadros.append(np.frombuffer(out, np.uint8).reshape(426, 240, 3))
    if not quadros:
        return 1.0, 0.0, 1.14
    arr = np.stack(quadros).astype(np.float32)
    lum = arr[..., 0] * .299 + arr[..., 1] * .587 + arr[..., 2] * .114
    # só o miolo: é onde ele está. A borda entra no fundo trocado e não importa.
    miolo = lum[:, int(.15 * 426):int(.95 * 426), int(.20 * 240):int(.80 * 240)]
    med = float(np.median(miolo)) / 255.0
    p1 = float(np.percentile(lum, 1)) / 255.0
    g = math.log(max(med, 0.02)) / math.log(ALVO_MEDIANA)
    g = max(0.72, min(2.15, g))
    # o gamma levanta a sombra junto com o meio-tom; sem devolver o preto
    # pra baixo o resultado é véu leitoso na imagem inteira
    preto = min(0.35, p1 ** (1 / g) * 0.85)
    sat = 1.10 + 0.16 * max(0.0, g - 1.0)
    _GRADE_CACHE[chave] = (round(g, 3), round(preto, 4), round(sat, 3))
    return _GRADE_CACHE[chave]


def filtro_video(fid, expo=1.0, preto=0.0, sat=1.14):
    """Grade em três etapas, nesta ordem — a ordem é o que evita o véu.

    1. gamma: levanta o meio-tom até a mediana-alvo (o sol se pôs no meio da
       gravação; sem isso os cortes parecem vídeos diferentes na timeline);
    2. colorlevels: devolve o ponto preto pra baixo. O gamma sozinho levanta a
       sombra junto com o meio-tom e o resultado é um véu leitoso na imagem
       inteira — foi o defeito da primeira leva;
    3. contraste/saturação/nitidez: só depois, sobre a faixa já correta.
    """
    cw, ch, cx, cy = CROP[SESSAO[fid]]
    con, nit = GRADE[SESSAO[fid]]
    et = [f"crop={cw}:{ch}:{cx}:{cy}"]
    if abs(expo - 1.0) > 0.01:
        et.append(f"eq=gamma={expo:.3f}")
    if preto > 0.001:
        # colorlevels só aceita RGB e a conversão automática a partir do HLG
        # 10-bit desta fonte devolve QUADRO PRETO, sem erro nenhum. Converter
        # explicitamente. Não remover: o defeito é silencioso e só aparece
        # quando o passo de gamma acima não entra (gamma ~1.0), o que esconde
        # o problema na maioria dos trechos.
        et.append("format=gbrp")
        et.append(f"colorlevels=rimin={preto:.4f}:gimin={preto:.4f}:bimin={preto:.4f}")
    et += [f"eq=contrast={con}:saturation={sat:.3f}", f"unsharp=5:5:{nit}",
           f"scale={W}:{H}:flags=lanczos", f"fps={FPS}", "format=rgb24"]
    return ",".join(et)


def render(entrada_raw, saida_raw, blocos, fundo_path, nframes, desfoque=False):
    """Laço único: troca o fundo (se pedido) e desenha a legenda.

    A legenda é desenhada com PIL porque esta build do ffmpeg não tem libass
    nem libfreetype (sem filtro `ass`, `subtitles` ou `drawtext`). Renderizar
    aqui também dá controle melhor: contorno real, quebra por largura e
    pastilha escura atrás do texto quando o fundo é claro.
    """
    import numpy as np, cv2
    from PIL import Image, ImageDraw, ImageFont
    global _VIN
    if _VIN is None:
        _VIN = _vinheta()
    VINHETA = _VIN

    fonte = ImageFont.truetype(str(BASE / "fontes" / "Montserrat-var.ttf"), 74)
    try:
        fonte.set_variation_by_name("ExtraBold")
    except Exception:
        pass

    seg = None
    bg_rgb = None
    if fundo_path or desfoque:
        import mediapipe as mp
        from mediapipe.tasks import python as mpy
        from mediapipe.tasks.python import vision
        globals()["_mp"] = mp
        if fundo_path:
            bg = cv2.imread(str(fundo_path))
            if bg is None:
                sys.exit(f"não consegui abrir o fundo: {fundo_path}")
            bh, bw = bg.shape[:2]
            e = max(W / bw, H / bh)
            bg = cv2.resize(bg, (int(bw * e + 0.5), int(bh * e + 0.5)))
            y0 = (bg.shape[0] - H) // 2; x0 = (bg.shape[1] - W) // 2
            bg_rgb = cv2.cvtColor(bg[y0:y0 + H, x0:x0 + W], cv2.COLOR_BGR2RGB).astype(np.float32)
        opts = vision.ImageSegmenterOptions(
            base_options=mpy.BaseOptions(model_asset_path=str(MODELO)),
            running_mode=vision.RunningMode.VIDEO,
            output_category_mask=True, output_confidence_masks=True)
        seg = vision.ImageSegmenter.create_from_options(opts)
        import mediapipe as _mp
        globals()["_mp"] = _mp

    def quebrar(texto, largura):
        palavras, linhas, atual = texto.split(), [], ""
        d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
        for p in palavras:
            t = (atual + " " + p).strip()
            if d.textlength(t, font=fonte) <= largura or not atual:
                atual = t
            else:
                linhas.append(atual); atual = p
        if atual:
            linhas.append(atual)
        return linhas

    # pré-renderiza cada bloco de legenda uma vez (não por quadro)
    cache = []
    for a, b, txt in blocos:
        if not txt:
            continue
        linhas = quebrar(txt, W - 180)
        alt = len(linhas) * 92
        cam = Image.new("RGBA", (W, alt + 40), (0, 0, 0, 0))
        d = ImageDraw.Draw(cam)
        for k, ln in enumerate(linhas):
            lw = d.textlength(ln, font=fonte)
            x, y = (W - lw) / 2, 20 + k * 92
            d.text((x, y), ln, font=fonte, fill=(255, 255, 255, 255),
                   stroke_width=7, stroke_fill=(0, 0, 0, 235))
        cache.append((a, b, np.array(cam), alt + 40))

    quadro = W * H * 3
    kc = np.ones((9, 9), np.uint8); ke = np.ones((5, 5), np.uint8)
    alpha_ant = None
    n = 0
    _fe = []

    # fundo desfocado: calculado UMA vez, antes do laço, com um segmentador
    # em modo IMAGE (o de vídeo exige timestamp crescente e já é usado abaixo).
    if desfoque and not fundo_path:
        from mediapipe.tasks.python import vision as _v
        from mediapipe.tasks import python as _p
        with open(entrada_raw, "rb") as f0:
            rgb0 = np.frombuffer(f0.read(W * H * 3), np.uint8).reshape(H, W, 3)
        o = _v.ImageSegmenterOptions(
            base_options=_p.BaseOptions(model_asset_path=str(MODELO)),
            output_category_mask=False, output_confidence_masks=True)
        with _v.ImageSegmenter.create_from_options(o) as s0:
            r0 = s0.segment(_mp.Image(image_format=_mp.ImageFormat.SRGB,
                                      data=np.ascontiguousarray(rgb0)))
        a0 = 1.0 - cv2.resize(r0.confidence_masks[0].numpy_view(), (W, H),
                              interpolation=cv2.INTER_LINEAR)
        m0 = ((a0 > 0.25) * 255).astype(np.uint8)
        m0 = cv2.dilate(m0, np.ones((45, 45), np.uint8), 1)
        bgr = cv2.cvtColor(rgb0, cv2.COLOR_RGB2BGR)
        peq = cv2.resize(bgr, (W // 4, H // 4))
        mpq = cv2.resize(m0, (W // 4, H // 4))
        limpo = cv2.inpaint(peq, mpq, 12, cv2.INPAINT_TELEA)
        limpo = cv2.resize(limpo, (W, H), interpolation=cv2.INTER_LINEAR)
        limpo = cv2.GaussianBlur(limpo, (0, 0), 22)
        _fe.append(cv2.cvtColor(limpo, cv2.COLOR_BGR2RGB).astype(np.float32)
                   * 0.86 * VINHETA)

    with open(entrada_raw, "rb") as fin, open(saida_raw, "wb") as fout:
        while True:
            buf = fin.read(quadro)
            if len(buf) < quadro:
                break
            rgb = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy()
            t = n / FPS

            if seg is not None:
                r = seg.segment_for_video(
                    _mp.Image(image_format=_mp.ImageFormat.SRGB,
                              data=np.ascontiguousarray(rgb)), int(t * 1000))
                a = 1.0 - cv2.resize(r.confidence_masks[0].numpy_view(), (W, H),
                                     interpolation=cv2.INTER_LINEAR)
                # endurece: sem isso sobra ~10% de fundo por cima dele e a
                # camisa branca fica acinzentada
                a = np.clip((a - 0.30) / 0.16, 0, 1)
                # a máscara de categoria (0=fundo) pega mão sobre o corpo, que a
                # de confiança perde. União das duas resolve o gesto perto do peito.
                cat = cv2.resize(r.category_mask.numpy_view(), (W, H),
                                 interpolation=cv2.INTER_NEAREST)
                a = np.maximum(a, (cat > 0).astype(np.float32))
                a8 = (np.clip(a, 0, 1) * 255).astype(np.uint8)
                a8 = cv2.morphologyEx(a8, cv2.MORPH_CLOSE, kc)
                a8 = cv2.erode(a8, np.ones((3, 3), np.uint8), 1)
                a8 = cv2.GaussianBlur(a8, (0, 0), 2.2)
                a = a8.astype(np.float32) / 255.0
                alpha_ant = a if alpha_ant is None else 0.65 * a + 0.35 * alpha_ant
                m = alpha_ant[..., None]
                if bg_rgb is not None:
                    atras = bg_rgb
                else:
                    atras = _fe[0]
                rgb = (rgb.astype(np.float32) * m + atras * (1 - m)).astype(np.uint8)

            for a0, b0, cam, alt in cache:
                if a0 <= t < b0:
                    y = int(H * ALTURA_LEGENDA) - alt // 2
                    y = max(0, min(y, H - alt))
                    reg = rgb[y:y + alt]
                    al = (cam[..., 3:4].astype(np.float32) / 255.0)[:reg.shape[0]]
                    rgb[y:y + alt] = (reg * (1 - al) +
                                      cam[:reg.shape[0], :, :3] * al).astype(np.uint8)
                    break

            fout.write(rgb.tobytes())
            n += 1
            if n % 300 == 0:
                print(f"   render: {n}/{nframes} quadros", flush=True)
    if seg is not None:
        seg.close()
    return n


def extrair_segmentos(segmentos, destino, expo=None, preto=None, sat=None):
    """Recorta cada trecho da SUA fonte, com a SUA grade, e concatena."""
    partes = []
    for i, (fid, a, b) in enumerate(segmentos):
        g, pb, st = medir_grade(fid, a, b)
        if expo is not None:
            g = expo
        if preto is not None:
            pb = preto
        if sat is not None:
            st = sat
        vf = filtro_video(fid, g, pb, st).replace(",format=rgb24", "")
        p = f"{destino}-{i}.mkv"
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y",
                        "-ss", str(a), "-t", str(b - a),
                        "-i", str(CORTES_DIR / FONTES[fid]),
                        "-vf", vf, "-c:v", "libx264", "-preset", "veryfast",
                        "-crf", "16", "-pix_fmt", "yuv420p",
                        "-c:a", "pcm_s16le", "-ar", "48000", "-ac", "2",
                        p], check=True)
        print(f"   trecho {i+1}: {fid} {a:.1f}-{b:.1f}s  gamma {g:.2f} preto {pb:.3f}")
        partes.append(p)
    lista = f"{destino}-lista.txt"
    Path(lista).write_text("".join(f"file '{Path(x).resolve()}'\n" for x in partes))
    saida = f"{destino}-join.mkv"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat",
                    "-safe", "0", "-i", lista, "-c", "copy", saida], check=True)
    return saida, partes + [lista]


# ---------------------------------------------------------------- áudio
def filtro_audio(censura):
    """Muta a fala nas janelas censuradas e põe um bipe de 1 kHz no lugar."""
    if not censura:
        return None, "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000"
    janelas = "+".join(f"between(t,{a:.3f},{b:.3f})" for a, b in censura)
    fala = f"[0:a]volume=0:enable='{janelas}'[fala]"
    bip = (f"sine=frequency=1000:sample_rate=48000[s];"
           f"[s]volume=0.16,volume=0:enable='not({janelas})'[bip]")
    mix = ("[fala][bip]amix=inputs=2:duration=first:dropout_transition=0,"
           "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]")
    return f"{fala};{bip};{mix}", None


# ---------------------------------------------------------------- principal
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id")
    ap.add_argument("segmentos", help="'01:17-01:31' ou '01:17-01:31,01:13-01:17'")
    ap.add_argument("saida")
    ap.add_argument("--fundo", default=None)
    ap.add_argument("--bipar", default="")
    ap.add_argument("--so-legenda", action="store_true")
    ap.add_argument("--exposicao", type=float, default=None,
                    help="força o gamma; por padrão é medido trecho a trecho")
    ap.add_argument("--preto", type=float, default=None)
    ap.add_argument("--saturacao", type=float, default=None)
    ap.add_argument("--desfoque", action="store_true",
                    help="profundidade de campo usando o próprio fundo")
    a = ap.parse_args()

    segs = parse_segmentos(a.segmentos, a.id)
    dur = sum(b - x for _, x, b in segs)
    saida = Path(a.saida); saida.parent.mkdir(parents=True, exist_ok=True)
    saida = saida.resolve()

    nomes, padroes = carregar_regras(a.bipar)
    blocos, censura = montar_blocos(segs, nomes, padroes)

    rev = saida.with_suffix(".txt")
    cab = [f"# {saida.name}  ({dur:.0f}s, {len(segs)} trecho(s))"]
    cab += [f"#   trecho {i+1}: {f} {x:.2f}s-{y:.2f}s"
            for i, (f, x, y) in enumerate(segs)]
    cab += [f"# bipes: {len(censura)}"]
    cab += [f"#   bipe em {x:.2f}s-{y:.2f}s" for x, y in censura]
    rev.write_text("\n".join(cab) + "\n\n" +
                   "\n".join(f"[{x:6.2f}] {t}" for x, _, t in blocos),
                   encoding="utf-8")
    print(f"legenda para conferir: {rev.name}  ({len(censura)} bipes)")
    if a.so_legenda:
        return

    tmp = str((saida.parent / f".tmp-{saida.stem}").resolve())
    inter, lixo = extrair_segmentos(segs, tmp, a.exposicao, a.preto, a.saturacao)

    raw_in, raw_out = f"{tmp}-in.raw", f"{tmp}-out.raw"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", inter,
                    "-f", "rawvideo", "-pix_fmt", "rgb24", raw_in], check=True)
    n = render(raw_in, raw_out, blocos, a.fundo, int(dur * FPS), a.desfoque)
    print(f"   {n} quadros renderizados" + (" (fundo trocado)" if a.fundo else (" (desfoque)" if a.desfoque else "")))
    lixo += [raw_in, raw_out]

    af_complex, af_simples = filtro_audio(censura)
    cmd = ["ffmpeg", "-loglevel", "error", "-y",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
           "-r", str(FPS), "-i", raw_out, "-i", inter]
    if af_complex:
        cmd += ["-filter_complex", af_complex.replace("[0:a]", "[1:a]"),
                "-map", "0:v", "-map", "[aout]"]
    else:
        cmd += ["-af", af_simples, "-map", "0:v", "-map", "1:a"]
    cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", "20",
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
            "-movflags", "+faststart", str(saida)]
    subprocess.run(cmd, check=True)

    for f in lixo + [inter]:
        Path(f).unlink(missing_ok=True)
    print(f"pronto: {saida.name}  ({dur:.0f}s, {len(segs)} seg, {len(censura)} bipes)")


if __name__ == "__main__":
    main()
