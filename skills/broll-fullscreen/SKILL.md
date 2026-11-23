---
name: broll-fullscreen
description: >
  Edita um vídeo talking-head vertical 9:16 (reels, VSL, conteúdo do Chefe falando) inserindo b-roll
  que COBRE a tela inteira a cada ~3 segundos. Use quando o pedido for "põe b-roll no meu vídeo/reels",
  "edita com b-roll", "cada 3s muda a cena", "intercala meu rosto com b-roll". Momentos de IA/agentes
  usam os personagens do canon `knowledge/personagens/SQUAD-CANON.md` (imagem pelo Codex da assinatura do ChatGPT → movimento
  por ffmpeg/HyperFrames); o resto usa Hyperframe. Tudo grátis, sem chave de API.
  É o formato de b-roll por cima, tela cheia, voz contínua por baixo.
metadata:
  { "tags": "reels, vsl, b-roll, video, hyperframe, ffmpeg, codex, edicao" }
---

# B-ROLL FULL-SCREEN (b-roll cobre a tela a cada ~3s — reels e vídeos talking-head)

Formato: vídeo talking-head vertical 9:16 do Chefe. O b-roll cobre a tela inteira por cima, a **voz do
Chefe continua contínua por baixo** o tempo todo. **Regra de ouro: o rosto dele aparece no máximo 3
segundos por vez** — a cada ~3s entra um b-roll. Serve pra reels (o caso mais comum) e pra VSL.

## REGRAS INEGOCIÁVEIS (o Chefe brigou por cada uma)
1. **Rosto ≤3s por vez.** Garantido pelo MODELO JANELADO (abaixo). O vídeo ABRE no t=0 já com b-roll (sem rosto na abertura).
2. **B-roll pinado no timestamp EXATO da fala** (transcrição). Se entrar adiantado/atrasado, fica "deslocado" e o Chefe percebe na hora.
3. **Personagens só com aprovação:** SEMPRE gera a IMAGEM primeiro (Codex da assinatura do ChatGPT, gasta cota dela) → abre pro Chefe aprovar → SÓ ENTÃO vira clipe. NUNCA monta clipe de personagem sem aprovar.
4. **Personagens fiéis ao canon:** ancorar a geração de imagem nas refs de b-rolls aprovados (`codex exec -i` com frames de referência), e seguir `knowledge/personagens/SQUAD-CANON.md` — o elenco ATUAL e a ordem oficial estão lá (o quinteto); nunca um elenco antigo nem uma lista de cabeça.
5. **Velocidade na timeline:** clipe de personagem (gerado + aproveitados) entra a **2x** (`setpts=0.5*PTS`, 8s→4s). Hyperframe a **1x**, **90% de opacidade** (rosto aparece de leve por trás). 9:16 sem faixa preta.
6. **Sem faixa preta:** todo clipe de personagem sai 1080x1920 cheio (`scale=...:force_original_aspect_ratio=increase,crop=...`) e é salvo como `*-fill.mp4`. Montar SEMPRE com os `-fill`.
7. **Preço (se houver oferta):** mostrar "12x R$30,00 / R$297 à vista", NUNCA centavos quebrados (27,25/29,90).

## FLUXO
1. **Transcrever LOCAL** com timestamp por palavra (faster-whisper `medium`, sem API paga; o áudio não sai da máquina): `~/.local/share/head-turbo/whisper-venv/bin/python ~/.claude/skills/cortes-tiktok-turbo/scripts/transcrever.py audio.wav transcricao` → `transcricao.json` (segmentos + palavras). Sem o venv: `bash ~/.claude/skills/watch/whisper-local/instalar.sh` (1x). Copie o áudio pra caminho ASCII antes (acento/vírgula no caminho atrapalham).
2. **Mapear cada b-roll** pinado no timestamp da frase. Momentos de IA/agentes/o-que-os-agentes-fazem → **personagens**; resto → **Hyperframe**. Seja generoso com personagem onde fala de IA. (Não precisa quebrar o vídeo em partes — monta o vídeo inteiro de uma vez. Pra vídeo MUITO longo dá pra fatiar pra trabalhar por pedaço, mas é opcional, não regra.)
3. **Hyperframe (grátis, paralelo):** dispara um Workflow (1 subagente por b-roll) com `assets/workflow-hf-portrait.js` (args = lista de conceitos `{id,dur,text,kicker,concept}`; o script faz `JSON.parse(args)`). Cada agente copia um `_tpl` (clone de `assets/template-hf-portrait.html`, que renderiza limpo) e autora um motion-graphic 9:16, valida e renderiza.
4. **Personagens:** cota primeiro (`bash ~/.claude/head-turbo/bin/codex-cota.sh`, rc 0 = PODE) → `assets/gen_imgs_personagens.py` (Codex da assinatura do ChatGPT, refs aprovadas via `-i`; sai ≠ 0 se faltar imagem) → abre pro Chefe aprovar → vira clipe `-fill` de 8 s **sem API**, de um destes jeitos:
   - **ffmpeg, movimento de câmera lento (padrão):**
     `ffmpeg -y -loop 1 -r 30 -t 8 -i img/img-XX.png -vf "scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,zoompan=z='min(1.12,1.0+0.0005*on)':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,setsar=1" -frames:v 240 -c:v libx264 -pix_fmt yuv420p -an char-XX-fill.mp4`
   - **HyperFrames, quando pede mais vida:** composição 9:16 com a imagem aprovada de fundo + parallax/brilho/partículas por cima (mesmo `template-hf-portrait.html`, render `--quality high`), salva como `char-XX-fill.mp4`.
   Sem Codex ou sem cota: o momento vira b-roll Hyperframe (motion graphic) e eu aviso o Chefe numa linha.
5. **Montar:** `assets/montar_parte.py` — define os inserts `(kind,file,start_abs)` numa única faixa cobrindo o vídeo. MODELO JANELADO: cada b-roll exibe de `start` até `(próximo_start - 2.5s)`, `overlay=eof_action=repeat` segura o último frame → **rosto fixo 2,5s garantido**. hf = 90% opacidade 1x; char = 2x cobrindo 100%. Mantém `[0:a]` (voz). Salvar e abrir pro Chefe ver. (Se tiver fatiado um vídeo longo: `ffmpeg -f concat -c copy` no fim.)

## GOTCHAS (caros, aprendidos na marra)
- **Ken Burns:** `zoompan` com `d=1`, `-t 8`, `-frames:v 240` — NUNCA `d=120` (gera 400 s de vídeo).
- **`eof_action=clone` NÃO existe** no overlay → é `repeat`.
- **Verificar frame de b-roll:** sampleie no MEIO da janela (start+1.5s), nunca no `start` exato (lá o b-roll está em opacity:0 entrando → parece preto/rosto).
- **Subagentes do workflow + hook RTK:** o hook reescreve `npx hyperframes@x` e quebra. Rodar via `npm run` (dentro do projeto) ou caminho absoluto do npx do nvm.
- Nenhuma chave de API (ordem do Leo, 21/10/2026, Telegram 5100: só ferramenta grátis): imagem pelo Codex da assinatura, movimento por ffmpeg/HyperFrames. Pasta de trabalho: `$BROLL_DIR` (padrão `~/videos-broll`). Sem venv: os scripts só usam a biblioteca padrão do Python.
- Hyperframe: `npx hyperframes@0.6.110`. Render `--quality high`. Verificar SEMPRE com ffprobe (1080x1920 + duração) — não confiar no "ok" do agente.

## ASSETS
- `montar_parte.py` — montador (modelo janelado, hf 90% / char 2x). Editar os inserts pro seu vídeo.
- `template-hf-portrait.html` — composição Hyperframe 9:16 de referência (renderiza limpo).
- `workflow-hf-portrait.js` — workflow que autora N b-rolls Hyperframe em paralelo (1 agente cada).
- `gen_imgs_personagens.py` — gera imagens dos personagens do canon (Codex da assinatura do ChatGPT + refs aprovadas).
