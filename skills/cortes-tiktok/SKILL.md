---
name: cortes-tiktok
description: 'Transforma gravação longa (aula, live, podcast) em cortes 9:16 prontos para postar: gancho no segundo zero, legenda queimada, grade de cor, troca de fundo, bipe de nome. Gatilhos: "fazer cortes", "cortes para TikTok", "transformar aula em reels", "legenda queimada". NÃO usar para roteiro de Reels (ht-reels-com-cta) nem vídeo de terceiro (watch).'
---

# Cortes para TikTok — produção, edição e publicação

## O que esta skill resolve

Gravação longa vira corte vertical que retém. Não é "cortar em pedaços de 60s" —
clipper automático já faz isso e o resultado é fraco porque corta linear.

O que faz diferença aqui: **o gancho é remontado para o segundo zero**, a imagem
é equalizada entre cortes que foram gravados com luz diferente, e nome de cliente
não vaza.

## Princípios

1. **A escolha do trecho decide, a edição só executa.** Corte mal escolhido não é
   salvo por grade, fundo ou legenda. Ver `references/selecao-de-cortes.md`.

2. **O gancho tem que abrir o vídeo.** Se a frase forte está aos 14 segundos, o
   corte está errado. Remonte fora de ordem: impacto primeiro, contexto depois.

3. **Buscar na transcrição de palavra, nunca na compactada.** Janela tirada de
   transcrição em blocos sempre começa no meio da frase.

4. **Ler a legenda antes de queimar.** `--so-legenda` primeiro, sempre. Número
   errado na transcrição vira número errado queimado no vídeo.

5. **Equalizar a exposição por trecho.** Gravação longa muda de luz no meio.
   Cortes com brilho diferente parecem vídeos de dias diferentes na timeline.

6. **Não expor ninguém, mesmo com autorização.** Bipar nome e número que
   identifica. Melhor ainda: escolher a janela que não tem nome nenhum.

7. **Assistir um corte antes de entregar.** Não negociável. Ver
   `references/armadilhas.md` — todo defeito grave desta pipeline foi encontrado
   assistindo, não conferindo quadro.

8. **Falha silenciosa é a regra, não a exceção.** ffmpeg devolve quadro preto sem
   erro, pipe engole código de saída, máscara zera sem avisar. Auditar por
   medição, não por confiança.

## Fluxo

### 1. Preparar o projeto

Um comando monta a pasta inteira — scripts, venv com as dependências, fonte,
modelo de segmentação (baixa os 16 MB) e um `projeto.json` em branco. Antes de
rodar, diga o que ele vai instalar (venv com faster-whisper, mediapipe, opencv,
numpy, Pillow) e espere o OK:

```bash
bash <pasta-desta-skill>/scripts/preparar-pasta.sh ~/cortes-agosto
```

Depois edite `projeto.json`:

```json
{
  "fontes_dir": "~/Videos/gravacao-2026-08",
  "fontes": {"01": "AULA_A.MP4", "02": "AULA_B.MP4"},
  "crop":   {"A": [1440, 2560, 58, 399]},
  "sessao": {"01": "A", "02": "A"},
  "contraste": {"A": [1.10, 0.5]}
}
```

`sessao` agrupa arquivos que compartilham enquadramento e luz. Para achar o crop:

```bash
python enquadrar.py 01 60
```

Copie `correcoes.json` e `bipar.json` da skill para a pasta e preencha com o que é
do **seu** material. Baixe o modelo de segmentação para `modelos/` se for trocar
fundo (link no cabeçalho de `fundo.py`).

### 2. Transcrever

```bash
python transcrever.py audio.wav transcricoes/01
```

`faster-whisper` modelo `medium`, int8, CPU, com `word_timestamps=True`. Em
máquina de muitos núcleos, rode 3 processos em paralelo com `OMP_NUM_THREADS=4`.

Gera o `.json` com timestamp por palavra — é ele que permite cortar na fronteira
exata da frase e casar o bipe.

### 3. Escolher os trechos

Leia a transcrição, encontre as falas fortes, e monte a especificação de cada
corte. Ver `references/selecao-de-cortes.md`.

### 4. Conferir a legenda

```bash
python produzir.py 01 "08:11-08:16,07:56-08:11" cortes/06-burnout.mp4 --so-legenda
```

Leia o `.txt`. Corrija `correcoes.json` e repita até o texto estar certo.

### 5. Renderizar

```bash
python produzir.py 01 "08:11-08:16,07:56-08:11,08:16-08:24" \
    cortes/06-burnout.mp4 --fundo fundos/sala.jpg
```

Trecho de outro arquivo-fonte no mesmo corte: `"12:08-12:18,02@05:30-05:34"`.

A grade é medida trecho a trecho automaticamente. Só passe `--exposicao` para
forçar.

### 6. Auditar

Antes de entregar, nesta ordem:

- presença do sujeito quadro a quadro (a máscara zera em silêncio)
- mediana de luma de cada corte (desvio acima de 10 = parecem vídeos diferentes)
- os 7 primeiros segundos de cada `.txt` lado a lado
- contato visual com um quadro de cada corte
- **assistir um**, com a skill `watch`

Os comandos estão em `references/armadilhas.md`.

### 7. Publicar

Ver `references/publicacao-tiktok.md`. Resumo: pela Zernio (plano grátis
com Instagram + TikTok), ou o expert publica pelo app com o arquivo e a legenda revisada.
Publicar sai para fora: só com o seu OK.

Para série agendada, monte uma fila em disco com as legendas já escritas e
revisadas. Nunca deixe um agente inventar legenda pública sem revisão.

## Referências

| Arquivo | Quando ler |
| --- | --- |
| `references/selecao-de-cortes.md` | Escolher trecho, montar gancho, fundir cortes |
| `references/edicao-imagem-e-som.md` | Grade, máscara de fundo, legenda, bipe, áudio |
| `references/armadilhas.md` | Antes de entregar. E quando algo falhar sem erro |
| `references/publicacao-tiktok.md` | Postar, cota, declarações, série agendada |

## Dependências

`ffmpeg` (conferir se tem `libass`; se não tiver, a legenda vai em PIL — já
tratado), `faster-whisper`, `mediapipe`, `opencv-python`, `numpy`, `Pillow`.

Fonte Montserrat variável em `fontes/`. Modelo `selfie_multiclass_256x256.tflite`
em `modelos/`.

Use um venv do projeto. O Python do sistema não vai ter `cv2` nem `mediapipe`, e
a falha só aparece na hora do render. Faltou algo (ex.: `ffmpeg`)? A skill confere
e, com o seu OK, instala na hora (`brew install ffmpeg`; o resto vai no venv pelo
`preparar-pasta.sh`). Sem instalar nada, ela ainda entrega a seleção dos cortes
com os tempos, o gancho e a legenda revisada, para editar à mão no editor que você usa.
