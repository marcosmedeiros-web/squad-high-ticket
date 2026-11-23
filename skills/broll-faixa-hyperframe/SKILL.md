---
name: broll-faixa-hyperframe
description: >
  Pega um vídeo/reels vertical 9:16, recorta o conteúdo em QUADRADO no topo e preenche a FAIXA de
  baixo em 100% do vídeo com b-roll Hyperframe ILUSTRADO (um por take de 10s). Use quando o pedido for
  "corta quadrado e bota faixa de hyperframe embaixo", "preenche a faixa preta com b-roll",
  "barra de baixo com motion graphics do início ao fim". Formato quadrado-em-cima + faixa-embaixo.
metadata:
  { "tags": "reels, b-roll, faixa, barra, hyperframe, lower-third, video" }
---

# VSL FAIXA HYPERFRAME (quadrado em cima + faixa Hyperframe embaixo, 100% do vídeo)

Formato: vídeo 9:16 com o conteúdo (rosto do Chefe) num **quadrado em cima** e uma **faixa embaixo
preenchida 100% com b-roll Hyperframe ILUSTRADO**, do início ao fim. Um b-roll novo a cada **10s**.

## REGRA QUE O CHEFE BRIGOU (NÃO ESQUECER)
**NUNCA queimar a frase falada como legenda na faixa.** Cada b-roll da faixa tem que ILUSTRAR a ideia
do trecho: **kicker curto + headline punchy (3-7 palavras, resumo, NÃO a frase) + elementos visuais**
(número contando, barra crescendo/encolhendo, ícones, comparação lado a lado, carimbo back.out, seta,
checklist, gauge). Igual aos b-rolls de uma VSL profissional. (A 1ª versão só queimou a frase = lixo,
o Chefe xingou. A 2ª, ilustrada, ele aprovou.)

## FLUXO
1. **Medir a faixa:** `cropdetect` em vários pontos do vídeo (`ffmpeg -ss T -t 1 -i v -vf cropdetect=24:2:0 -f null -`). A região com conteúdo dá o quadrado de cima; a faixa = `altura_total - altura_conteúdo` na base. (No caso real: vídeo 1080x1920, conteúdo top 1076px, faixa = **1080x844 começando em y=1076**.) Se o vídeo ainda NÃO veio cortado, cortar: conteúdo quadrado 1080x1080 em cima, faixa embaixo.
2. **Transcrever LOCAL** com timestamp por palavra (faster-whisper `medium`, sem API paga; o áudio não sai da máquina): `~/.local/share/head-turbo/whisper-venv/bin/python ~/.claude/skills/cortes-tiktok-turbo/scripts/transcrever.py audio.wav transcricao` → `transcricao.json` (segmentos + palavras). Sem o venv: `bash ~/.claude/skills/watch/whisper-local/instalar.sh` (1x). Copie o áudio pra caminho ASCII antes (acento/vírgula no caminho atrapalham).
3. **Quebrar em takes de 10s:** N = ceil(duração/10). Gerar specs `{id, dur, fala}` por take (a fala = texto da transcrição naquela janela, pro agente saber o que ilustrar). Gerar `specs<N>.json`.
4. **Gerar os N b-rolls (paralelo):** Workflow `assets/workflow-bar-ilustrado.js` (1080x844), em lotes (~4 takes/agente). Cada agente LÊ o specs.json, pega a fala dos seus takes e **desenha** a barra ilustrando (kicker+headline+elementos), valida e renderiza pra `brolls/bar/bar-<id3>.mp4`. Args não são usados (agente lê o specs do disco) — relançar via `scriptPath`.
5. **Montar:** `assets/montar_faixa.sh` — espera os N renders, **concatena** as barras na ordem (`concat` → bar-track 1080x844), **sobrepõe** na faixa: `overlay=0:<y_da_faixa>` mantendo a faixa preta coberta 100% e o **áudio do vídeo** (`-map 0:a`). Salva (no Mac também abre o vídeo; no Linux/WSL só diz onde salvou).

## GOTCHAS
- **Verificar frame:** sampleie no MEIO de cada take (start+5s), NUNCA no início do take (multiplo de 10) — lá a barra está entrando (opacity 0) e parece preta. Já me enganei 2x assim.
- **Concatenar exige mesmos params** (todas as barras saem do mesmo render → ok). A última barra é mais curta (resto da duração).
- **Subagentes + hook RTK:** `npx hyperframes@x` quebra; usar caminho absoluto do npx do nvm + dangerouslyDisableSandbox, ou `npm run`.
- **Esperador de verdade:** waiters em background com `sleep` real (o truque `ffmpeg anullsrc -t 5` roda instantâneo, NÃO espera). O arquivo de saída aparece parcial durante o encode → só considerar pronto quando o log de montagem disser "PRONTO" (não pela mera existência do arquivo).
- Template da barra: `assets/template-bar-1080x844.html` (placeholders). Mas o AGENTE deve AUTORAR ilustrado, não só trocar texto no template (template é só base de estilo/dimensão).

## ASSETS
- `template-bar-1080x844.html` — base de estilo/dimensão da barra (1080x844, dark).
- `workflow-bar-ilustrado.js` — workflow que desenha N barras ilustradas em paralelo (lê specs.json).
- `montar_faixa.sh` — espera os renders, concatena a faixa e sobrepõe no vídeo (ajustar `N`, `Y`, `SRC` e `BROLL_DIR` no topo do script). Roda no Mac e no Linux/WSL.
