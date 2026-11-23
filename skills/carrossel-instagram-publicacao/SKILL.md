---
name: carrossel-instagram-publicacao
description: 'Ciclo completo de criação → geração → publicação → automação de carrossel Instagram, com MÚLTIPLOS ESTILOS visuais. Use sempre que o Chefe pedir "Turbo vamos fazer um carrossel", "pesquise tal notícia e cria um carrossel", "monta carrossel sobre X e posta", ou variações. Estilo padrão (top 1) = render 3D premium com proporções de anime, acabamento fosco, feito de materiais reais e luz de estúdio, com o QUINTETO do dono ({{DONO}} + o personagem de IA do dono + o mascote do dono + Claudinho + Codexzinho, aparências definidas no onboarding). Outros estilos sob demanda: Post do X, Jornal, Notícia, Texto Puro HTML. Cobre as 12 etapas e a regra de geração de imagem (Codex da assinatura do ChatGPT do dono, sem chave de API; sem Codex, HTML/CSS/SVG → PNG). Validado em produção no carrossel "Claude no Instagram = 1,5M views" (post IG DYSRcGFiAFf, 2026-05-13).'
---

# Carrossel Instagram — Ciclo Completo (multi-estilo)

> Skill mestra pra fazer ponta-a-ponta um carrossel IG sem o Chefe orquestrar cada passo.
> **Esta é tarefa operacional: a Turbo NÃO executa, delega pra Juliana**, que roda o ciclo e devolve pra Turbo entregar pro Chefe.

---

## 🎨 ESTILOS DE CARROSSEL (LER PRIMEIRO)

Tem vários estilos. O fluxo das 12 etapas é o MESMO pra todos — muda só o tratamento visual de cada card.

| # | Estilo | Quando usar | Como gerar |
|---|--------|-------------|------------|
| **TOP 1 (PADRÃO)** | **Render 3D premium — Quinteto do dono** | Padrão da marca. Conteúdo educativo, autoridade, branding | Codex da assinatura do ChatGPT, quinteto canônico ({{DONO}} + o personagem de IA do dono + o mascote do dono + Claudinho + Codexzinho — ver `knowledge/personagens/SQUAD-CANON.md`) |
| 2 | **Post do X (tweet)** | Provocação, opinião, "screenshot de tweet viral", thread | Mockup de post do X/Twitter (avatar @{{DONO}}.ai, nome, texto, métricas falsas plausíveis). Pode ser HTML→imagem ou Codex |
| 3 | **Jornal** | Notícia "impressa", autoridade editorial, manchete de jornal antigo/clássico | Layout de jornal (cabeçalho, colunas, serifada, P&B ou sépia). HTML→imagem ou Codex |
| 4 | **Notícia (portal)** | Quebra de notícia tech, "saiu na imprensa", credibilidade | Layout de portal de notícia (logo fictício/real, headline, foto, lide). HTML→imagem ou Codex |
| 5 | **Texto Puro (HTML)** | Densidade de informação, lista, framework, didático limpo | HTML/CSS renderizado pra imagem (tipografia forte, fundo sólido, sem personagem) |

**REGRA DE GATILHO:**
- Chefe diz **"padrão"** ou **"top 1"** → uso o **render 3D premium (quinteto)** direto, sem perguntar estilo.
- Chefe **não especifica** estilo → assumo o padrão (top 1).
- Chefe pede **"me manda os estilos que você tem"** / "quais estilos?" → respondo com a tabela acima (os 5 estilos) e espero ele escolher.
- Chefe nomeia um estilo (ex: "faz estilo jornal") → uso aquele.

> Estilos 2-5 (X, Jornal, Notícia, HTML) podem ser renderizados via HTML→imagem (Playwright screenshot de um template HTML) quando precisarem de texto pixel-perfeito, OU via Codex da assinatura quando quiser estética ilustrada. Texto Puro é SEMPRE HTML.

---

## 🖼️ REGRA DE GERAÇÃO DE IMAGEM (CRÍTICA)

Só ferramenta grátis, nunca chave de API de imagem (ordem do Leo, 21/10/2026, Telegram 5100). A ordem é a do
`COMO-CRIAR-IMAGEM-E-VIDEO.md` do kit:

**Padrão: o Codex da assinatura do ChatGPT do dono** (o gerador de imagem do ChatGPT, o mesmo que fazia os cards quando
eram pedidos ao `gpt-image-2` por API — hoje pela assinatura, sem chave e sem custo extra). Sempre tento primeiro.
- Cota antes: `bash ~/.claude/head-turbo/bin/codex-cota.sh` (rc 0 = PODE; rc 2 = não consegui ler, que **não** é "tem cota").
- Tamanho pedido no prompt: `1024x1280` (4:5 portrait) ou `1536x1024` (paisagem/capa).

**Sem Codex ou sem cota: por código** — HTML/CSS/SVG renderizado em PNG
(`bash ~/.claude/head-turbo/bin/renderizar-html.sh card.html card.png 1080x1350`). Serve para os estilos 2-5 e para capa
tipográfica; personagem com cara de render 3D pede o Codex.
Se o Codex falhar, o protocolo é OBRIGATÓRIO:
1. **Aviso o Chefe** que o Codex falhou.
2. **Explico o porquê** (erro retornado, cota, conteúdo recusado, etc.).
3. Sigo por código nos estilos que cabem, ou espero a cota voltar — o Chefe escolhe.

> Nunca trocar de caminho em silêncio. E nunca pedir chave de API de imagem como saída.

---

## 🎯 QUANDO ATIVAR ESSA SKILL

Triggers:
- "Turbo vamos fazer um carrossel baseado nesse aqui" + link de post
- "Turbo pesquise tal notícia e cria um carrossel"
- "Monta carrossel sobre X e posta"
- "Carrossel novo sobre [tema] e ativa o comment-to-DM"
- Qualquer pedido que envolva criar + postar + automação no mesmo fluxo

---

## 📚 PRÉ-REQUISITOS (ler ANTES de começar)

Referências canônicas (consultar):
- **`knowledge/personagens/SQUAD-CANON.md`** — CANON MESTRE do **QUINTETO** (5 personagens obrigatórios, ordem oficial {{DONO}} + o personagem de IA do dono + o mascote do dono + Claudinho + Codexzinho), descrições exatas + ambientes + paleta + tema padrão (disputa Claudinho vs o mascote do dono). **LER ANTES de qualquer prompt.**
- **`knowledge/personagens/personagens-v2.md`** — detalhamento do personagem de IA do dono, do mascote do dono e do {{DONO}} — a aparência de cada um é definida no onboarding do dono, nunca fixada aqui.
- `feedback_envio_cards_carrossel_ordem.md` — envio 1 por vez sequencial
- `feedback_propostas_sem_promessa_numerica.md` — sem prometer ROI pro leitor (case real do Chefe é OK)
- `feedback_acentuacao_producao.md` — PT-BR perfeito sempre

Skills relacionadas:

---

## 🧭 ETAPAS DO CICLO (12 etapas)

### ETAPA 1 — Captura da referência
Se for "baseado nesse aqui" + link:
1. Identificar URL: Instagram (`/p/{shortcode}/` → Instaloader baixa imagens+caption+métricas), TikTok/Reels (yt-dlp), notícia/artigo (WebFetch).
2. Baixar pra `/tmp/{nome-curto}/card-N.jpg`.
3. Ler cada card com Read (multimodal): estrutura, estilo, densidade, hook+CTA.
4. Capturar caption original + top comments.

Se for "pesquise tal notícia": WebSearch/WebFetch → resumir 3-5 pontos-chave → identificar ângulo viral.

**ENTREGÁVEL:** resumo curto no Telegram (≤300 palavras): o que é a referência, hook, o que vamos pegar, **e qual estilo** (padrão/top 1 ou outro).

---

### ETAPA 2 — Roteiro detalhado

Estrutura padrão (estilo Anime/Quinteto):
| Card | Função |
|---|---|
| 01 | Capa com **quinteto** ({{DONO}} + o personagem de IA do dono + o mascote do dono + Claudinho + Codexzinho) + headline + hook |
| 02-N | Prompts / pilares / insights |
| Meio | **Card CASE** com o quinteto (quebra de ritmo, personagem de IA do dono em destaque) |
| Último | **CTA** + palavra-chave pra comment-to-DM |

Pra cada card: tag superior, título (Inter Black), texto principal denso, **descrição visual completa**, badge de numeração, assinatura `@{{DONO}}.ai`.

Decisões a perguntar ANTES de aprovar:
1. **Estilo** (se não foi dito): padrão/top 1 (anime quinteto) ou outro (X/jornal/notícia/HTML)?
2. **Paleta**: cyber (navy+coral+cyan) ou editorial (creme+terracota)?
3. **Quinteto em quais cards**: só na capa ou em vários?
4. **Palavra-chave do CTA**: "CLAUDE", "EU QUERO", "ACESSO"...?
5. **Destino do botão**: imersao.{{DONO}}.ai? outro link?

**ENTREGÁVEL:** roteiro completo no Telegram + perguntas-chave. **AGUARDAR OK EXPLÍCITO** antes de gerar.

---

### ETAPA 3 — Geração das imagens

**Padrão: Codex da assinatura do ChatGPT** (ver REGRA DE GERAÇÃO DE IMAGEM acima). Tamanho `1024x1280` pedido no prompt.

Template (um prompt por card em `prompts/NN.txt`, cada card numa pasta só dele):
```bash
bash ~/.claude/head-turbo/bin/codex-cota.sh || exit 1          # rc 0 = PODE
for i in 01 02 03 04 05 06; do
  mkdir -p /tmp/cards/$i && codex exec --disable apps --disable plugins -c 'web_search="disabled"' --skip-git-repo-check \
    -s workspace-write -C /tmp/cards/$i "Gere UMA imagem com a ferramenta de geração de imagem, retrato 1024x1280: $(cat prompts/$i.txt). Salve como $i.png nesta pasta e diga o caminho completo." < /dev/null &
done; wait
ls -la /tmp/cards/*/*.png      # card sem PNG = gerar de novo só aquele (a cópia da CLI fica em ~/.codex/generated_images/)
```
Disparar em background, Monitor pros logs.
**Se o Codex falhar → seguir o protocolo (avisar + explicar + código ou esperar a cota).**
**Status pro Chefe a cada 2 min** durante a geração.

**Estilos 2-5 (X/Jornal/Notícia/HTML):** quando o estilo for mockup com texto pixel-perfeito, renderizar via HTML→imagem (`renderizar-html.sh card.html card.png 1080x1350`) em vez do Codex.

---

### ETAPA 4 — Revisão visual contra checklist

Ler cada card com Read (multimodal). Para o estilo Anime/Quinteto, validar contra o **canon do squad** (`SQUAD-CANON.md`):
- [ ] **Personagem de IA do dono**: o personagem do dono que representa a IA, aparência definida no onboarding (traço, cor de cabelo, roupa e pin de marca), postura confiante e idêntica entre todos os cards
- [ ] **{{DONO}}**: aparência definida no onboarding (pele, cabelo ou careca, barba, porte, roupa característica) — conferir contra a referência do próprio dono
- [ ] **Mascote do dono**: o mascote configurável do dono, definido no onboarding (espécie, cor, proporção chibi e roupa), sempre igual entre todos os cards
- [ ] **Claudinho**: cabeça-cubo laranja fosco com olhos em colchete `>‹` (sem boca), MESMA roupa streetwear (hoodie preto com o símbolo da Turbo Academy + corrente, jogger preto listra vermelha, tênis brancos chunky), proporção chibi
- [ ] **Codexzinho**: cabeça = nuvem-flor (gradiente lavanda-roxo→azul) com rosto de terminal branco `>_`, MESMA roupa streetwear, proporção chibi, NUNCA monstro
- [ ] **Os 5 personagens presentes** na(s) cena(s) que pedem o squad (capa + cards-herói)
- [ ] Acentuação PT-BR **pixel-perfeita**
- [ ] Densidade de texto adequada, paleta consistente, badge de numeração, assinatura
- [ ] Sem watermark, sem emoji, sem promessa numérica pro leitor

Card que falhar → regenerar APENAS aquele com prompt ajustado.

---

### ETAPA 5 — Overlay manual de logos oficiais (quando precisar)
O gerador de imagem não faz logo pixel-perfect. Gerar versão SEM o logo (espaço reservado), baixar SVG/PNG oficial, compor via HTML (card como `<img>` de fundo + logo posicionado em CSS) e renderizar com `renderizar-html.sh`. Logo Claude.ai em `/tmp/claude-logo-official.png`.

---

### ETAPA 6 — Envio sequencial pra aprovação
**1 card por vez**, ordem 01→N, esperar `ok:true`, sleep 1s. NUNCA paralelo, NUNCA sendMediaGroup.

Envie por qualquer canal de aprovação que você já tenha configurado com o Chefe (bot de Telegram próprio — ver `metodo-bot-python-telegram` — WhatsApp, ou o que for). Padrão de referência (Telegram, `sendPhoto` com o token do SEU bot lido do SEU `.env`):
```bash
TOKEN=$(grep "TELEGRAM_BOT_TOKEN" .env | cut -d= -f2)
curl -s -X POST "https://api.telegram.org/bot${TOKEN}/sendPhoto" \
  -F "chat_id=$CHAT_ID_DO_CHEFE" -F "photo=@/tmp/cards/01.jpg" \
  -F "caption=*01/06* — descrição curta" -F "parse_mode=Markdown"
```
No último, perguntar: "Aprova o carrossel inteiro? Sigo pra legenda + publicação?" **Aguardar OK explícito.**

---

### ETAPA 7 — Legenda do post
1ª pessoa ({{DONO}}), hook forte na 1ª linha, **sem promessa numérica pro leitor** (case do Chefe = OK), sem palavras de coach, 4-5 bullets (✦), CTA literal com a palavra-chave, 10-12 hashtags balanceadas, acentuação perfeita. Mandar pro Chefe e aguardar OK.

---

### ETAPA 8 — Upload em URL pública
⚠️ NÃO usar Litterbox/Catbox/Imgur (Meta scraper bloqueia essas três).
✅ USAR um host estático seu que sirva HTTPS direto (GitHub Pages, Cloudflare Pages, Vercel, Netlify, um bucket com site estático — qualquer um serve, desde que a URL final seja pública e estável). Padrão de referência (repo próprio + Cloudflare Pages, adapte pro seu):
```bash
GITHUB_TOKEN=$(grep "^GITHUB_TOKEN" .env | cut -d= -f2 | tr -d '\n')
git clone "https://$GITHUB_USER:${GITHUB_TOKEN}@github.com/$GITHUB_USER/$SEU_REPO" /tmp/carrossel-clone
cd /tmp/carrossel-clone && mkdir -p cards-carrossel-{nome} && cp /tmp/cards/*.jpg cards-carrossel-{nome}/
git config user.email "$SEU_EMAIL_DE_COMMIT"; git config user.name "$SEU_NOME"
git add . && git commit -m "feat: carrossel {nome}" && git push origin main
```
⚠️ O email do commit precisa ser o mesmo cadastrado na sua conta de deploy (Vercel e afins rejeitam commit de email não autorizado). Esperar o host publicar (~30-60s), validar com Monitor (`until curl ...200`). Se Meta rejeitar formato: reconverter `ffmpeg -y -i card.png -q:v 2 card.jpg` + `?v=$(date +%s)` na URL.

---

### ETAPA 9 — Publicação via Meta Graph API
⚠️ Usar `graph.instagram.com` (NÃO facebook.com). Token IG começa com `IGAAU...` (Instagram Login, obtido no fluxo OAuth do Meta for Developers).

Carregue esse TOKEN de onde você guarda suas credenciais. Pra uso pessoal, um `.env` local basta:
```bash
TOKEN=$(grep "^IG_ACCESS_TOKEN" .env | cut -d= -f2)
```
Se você atende mais de uma conta/cliente, vale guardar os tokens num banco próprio com a coluna do token encriptada (ex.: `pgp_sym_decrypt` no Postgres com uma chave de encriptação em variável de ambiente) em vez de texto puro — mas isso é escolha de arquitetura sua, não um requisito desta skill.

Fluxo (graph.instagram.com/v23.0): 1) criar N containers `is_carousel_item=true` → 2) esperar cada `status_code=FINISHED` → 3) criar container `media_type=CAROUSEL` com `children` + `caption` → 4) `media_publish` com `creation_id`. Salvar `media_id` + pegar `permalink`.

---


---

### ETAPA 11 — Validar disparo

---


---

## 🧰 GOTCHAS (não repetir)
1. **Token IG ≠ Facebook** — `IGAAU...` roda em `graph.instagram.com`. Sintoma: "Cannot parse access token".
2. **Litterbox/Catbox** bloqueiam scraper Meta. Sintoma: erro 9004. Solução: CF Pages via repo imersao.
3. **Cache CDN CF Pages** serve versão antiga. Solução: `?v=$(date +%s)`.
4. **Imagem gerada às vezes vem num formato que a Meta rejeita** (erro 36001). Solução: reconverter `ffmpeg -y -i card.png -q:v 2 card.jpg`.
5. **Logo via prompt nunca é pixel-perfect** — overlay do PNG oficial via HTML + `renderizar-html.sh`.
6. **Private Reply ≠ DM padrão** — botão anexado JUNTO no payload da Private Reply, nunca em 2ª chamada.
7. **Envio sequencial OBRIGATÓRIO** — 1 por vez, sleep 1s, esperar ok=True.
8. **Troca de caminho de imagem NUNCA em silêncio** — o Codex falhou? Avisa, explica, segue por código ou espera a cota. Chave de API de imagem nunca.

---

## ✅ CRITÉRIOS DE "ENTREGUE"
- [ ] Estilo definido (padrão/top 1 ou outro escolhido pelo Chefe)
- [ ] Roteiro aprovado
- [ ] Cards gerados e enviados em ordem, todos aprovados
- [ ] Legenda aprovada
- [ ] Post publicado (`media_id` salvo)
- [ ] Automação criada (`automation_id`, enabled=true)
- [ ] 1º disparo real com `private_reply_with_buttons: ok=True`
- [ ] Confirmado pro Chefe com permalink + automation_id + log

## 🚨 ESCALAR PRO CHEFE QUANDO
- Referência não encontrável (link quebrado/post deletado)
- o Codex falhar ou faltar cota (avisar e combinar o caminho)
- Meta retornar erro persistente
- Banco/Postgres não responder
