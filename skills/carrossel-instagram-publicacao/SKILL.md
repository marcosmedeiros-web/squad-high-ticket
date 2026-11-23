---
name: carrossel-instagram-publicacao
description: 'Ciclo completo de carrossel do Instagram: referência, roteiro, imagens, aprovação, legenda e publicação, em vários estilos visuais. Use para "vamos fazer um carrossel", "pesquisa essa notícia e cria um carrossel", "monta carrossel sobre X e posta", "carrossel estilo jornal". NÃO usar para post único, story ou anúncio.'
---

# Carrossel Instagram — Ciclo Completo (multi-estilo)

> Skill mestra para fazer de ponta a ponta um carrossel do Instagram sem que você precise orquestrar cada passo.
> O agente roda o ciclo e só para nas aprovações: roteiro, cards, legenda e publicação.

---

## 🎨 ESTILOS DE CARROSSEL (LER PRIMEIRO)

Tem vários estilos. O fluxo das etapas é o MESMO para todos — muda só o tratamento visual de cada card.

| # | Estilo | Quando usar | Como gerar |
|---|--------|-------------|------------|
| **TOP 1 (PADRÃO)** | **Personagens da marca** | Padrão da marca. Conteúdo educativo, autoridade, branding | Ilustração/render dos personagens que o expert usa (o próprio expert, mascote, personagens recorrentes), descritos uma vez num arquivo de canon do projeto |
| 2 | **Post do X (tweet)** | Provocação, opinião, "screenshot de tweet viral", thread | Mockup de post do X/Twitter (avatar e @ do expert, nome, texto, métricas plausíveis). HTML→imagem |
| 3 | **Jornal** | Notícia "impressa", autoridade editorial, manchete de jornal clássico | Layout de jornal (cabeçalho, colunas, serifada, P&B ou sépia). HTML→imagem |
| 4 | **Notícia (portal)** | Quebra de notícia, "saiu na imprensa", credibilidade | Layout de portal de notícia (logo, headline, foto, lide). HTML→imagem |
| 5 | **Texto Puro (HTML)** | Densidade de informação, lista, framework, didático limpo | HTML/CSS renderizado para imagem (tipografia forte, fundo sólido, sem personagem) |

**REGRA DE GATILHO:**
- Pedido diz **"padrão"** ou **"top 1"**, ou não especifica estilo → uso o estilo 1 direto, sem perguntar.
- Pedido "quais estilos você tem?" → respondo com a tabela acima.
- Pedido nomeia um estilo (ex.: "faz estilo jornal") → uso aquele.
- O expert ainda não tem personagens definidos → uso o estilo 5 (Texto Puro) e digo em "Assumi".

> Estilos 2-5 saem sempre por HTML→imagem quando precisam de texto pixel-perfeito. Texto Puro é SEMPRE HTML.

---

## 🖼️ REGRA DE GERAÇÃO DE IMAGEM (CRÍTICA)

Só ferramenta grátis ou que a pessoa já usa; nunca pedir chave de API de imagem. Três caminhos, nesta ordem:

1. **Por código (padrão para os estilos 2-5 e capa tipográfica):** HTML/CSS/SVG renderizado em PNG 1080x1350. Para tirar o
   PNG, a skill confere se o Playwright está disponível; se não estiver, pede o OK e instala na hora
   (`npm i -D playwright && npx playwright install chromium`, dizendo o que vai instalar). Sem OK, entrega o `.html` pronto e o
   passo manual: abrir no navegador em 1080x1350 e salvar a captura.
2. **Gerador de imagem que a pessoa já usa (para o estilo 1):** entrego um prompt por card, pronto para colar (ex.: no ChatGPT ou
   no gerador que ela tiver), com o tamanho `1024x1280` (4:5 retrato) ou `1536x1024` (capa paisagem) escrito no prompt. Se este
   ambiente já tiver um gerador de imagem ligado, uso ele direto.
3. **Foto real:** peço a foto do expert ou do produto e componho por HTML.

Se um caminho falhar: aviso o que falhou e por quê (erro, recusa de conteúdo) e sigo pelo próximo caminho que cabe no estilo.
Nunca troco de caminho em silêncio.

---

## 🎯 QUANDO ATIVAR ESSA SKILL

- "Vamos fazer um carrossel baseado nesse aqui" + link de post
- "Pesquise tal notícia e cria um carrossel"
- "Monta carrossel sobre X e posta"
- "Carrossel novo sobre [tema] e ativa o comment-to-DM"
- Qualquer pedido que envolva criar + postar no mesmo fluxo

---

## 📚 ANTES DE COMEÇAR

- Se o projeto tiver um arquivo de canon dos personagens (aparência exata de cada um, ambiente, paleta), ler ANTES de qualquer
  prompt. Se não tiver e o estilo for o 1, montar o canon a partir de fotos/descrição que a pessoa der e salvar no projeto.
- Regras fixas: envio dos cards 1 por vez, em ordem; sem promessa numérica para o leitor (case real do expert, com prova, é OK);
  português com acentuação perfeita.

---

## 🧭 ETAPAS DO CICLO

### ETAPA 1 — Captura da referência
Se for "baseado nesse aqui" + link:
1. Identificar URL: Instagram (`/p/{shortcode}/`), TikTok/Reels, notícia/artigo (WebFetch). Para baixar imagens e legenda de
   post, a skill confere se `instaloader` ou `yt-dlp` estão disponíveis e, se não, pede OK para instalar
   (`pip install instaloader` / `brew install yt-dlp`); sem OK, pede para a pessoa salvar os prints dos cards.
2. Salvar em `/tmp/{nome-curto}/card-N.jpg`.
3. Ler cada card com Read (multimodal): estrutura, estilo, densidade, hook + CTA.
4. Capturar legenda original + comentários de destaque.

Se for "pesquise tal notícia": WebSearch/WebFetch → resumir 3-5 pontos-chave → identificar o ângulo.

**ENTREGÁVEL:** resumo curto (≤300 palavras): o que é a referência, hook, o que vamos pegar e qual estilo.

---

### ETAPA 2 — Roteiro detalhado

Estrutura padrão:
| Card | Função |
|---|---|
| 01 | Capa com os personagens da marca (ou tipográfica) + headline + hook |
| 02-N | Prompts / pilares / insights |
| Meio | **Card CASE** (quebra de ritmo) |
| Último | **CTA** + palavra-chave para comment-to-DM |

Para cada card: tag superior, título (fonte forte), texto principal denso, **descrição visual completa**, badge de numeração,
assinatura com o @ do expert.

Não pergunto antes; decido pelo padrão e listo no fim do roteiro:
"Assumi: estilo X · paleta Y · personagens na capa e no card case · palavra-chave do CTA Z · link do botão W (é só pedir para mudar)."
O link do botão sai do projeto; se não houver nenhum, deixo `[LINK]` marcado e digo.

**ENTREGÁVEL:** roteiro completo + linha "Assumi". **AGUARDAR OK** antes de gerar.

---

### ETAPA 3 — Geração das imagens

Seguir a REGRA DE GERAÇÃO DE IMAGEM acima. Um prompt ou um HTML por card, cada card numa pasta só dele (`/tmp/cards/NN/`).
Card sem PNG no fim = gerar de novo só aquele. Trabalho longo: dar status a cada poucos minutos.

---

### ETAPA 4 — Revisão visual contra checklist

Ler cada card com Read (multimodal):
- [ ] Personagens idênticos ao canon e entre todos os cards (rosto, cabelo, roupa, proporção)
- [ ] Todos os personagens previstos presentes nas cenas que pedem o grupo (capa + cards-herói)
- [ ] Acentuação PT-BR **pixel-perfeita**
- [ ] Densidade de texto adequada, paleta consistente, badge de numeração, assinatura
- [ ] Sem marca d'água, sem emoji, sem promessa numérica para o leitor

Card que falhar → regenerar APENAS aquele com o prompt ajustado. Para revisão independente, acionar o `ht-revisor-visual`.

---

### ETAPA 5 — Overlay manual de logos oficiais (quando precisar)
Gerador de imagem não faz logo pixel-perfect. Gerar a versão SEM o logo (espaço reservado), baixar o SVG/PNG oficial, compor
via HTML (card como `<img>` de fundo + logo posicionado em CSS) e renderizar em PNG como na Etapa 3.

---

### ETAPA 6 — Envio sequencial para aprovação
**1 card por vez**, ordem 01→N, esperar a confirmação de entrega, pausa de 1s. NUNCA em paralelo, NUNCA em álbum.

Envie pelo canal de aprovação que você já usa (chat aqui, bot de Telegram próprio, WhatsApp). Exemplo com bot de Telegram próprio
(token numa variável de ambiente ou gerenciador de credenciais; nunca colado no chat):
```bash
curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendPhoto" \
  -F "chat_id=$CHAT_ID" -F "photo=@/tmp/cards/01/01.jpg" \
  -F "caption=01/06 — descrição curta"
```
No último: "Aprova o carrossel inteiro? Sigo para legenda e publicação?" **Aguardar OK.**

---

### ETAPA 7 — Legenda do post
1ª pessoa (o expert), hook forte na 1ª linha, **sem promessa numérica para o leitor**, sem palavras de coach, 4-5 bullets (✦),
CTA literal com a palavra-chave, 10-12 hashtags balanceadas, acentuação perfeita. Mostrar e aguardar OK.

---

### ETAPA 8 — Upload em URL pública
⚠️ NÃO usar Litterbox/Catbox/Imgur (o scraper da Meta bloqueia).
✅ Usar um host estático que sirva HTTPS direto (GitHub Pages, Cloudflare Pages, Netlify, bucket com site estático) — a URL final
precisa ser pública e estável. Para Cloudflare Pages, ver a skill `publicar-pagina-cloudflare`. Esperar o host publicar
(~30-60s) e validar com `curl -I` até dar 200. Se a Meta rejeitar o formato: reconverter para JPG
(`ffmpeg -y -i card.png -q:v 2 card.jpg`; se não houver ffmpeg, pedir OK para `brew install ffmpeg` ou exportar em JPG direto
do render) e usar `?v=$(date +%s)` na URL.

---

### ETAPA 9 — Publicação via Meta Graph API (só com OK)
⚠️ Usar `graph.instagram.com` (NÃO facebook.com). Token IG começa com `IGAA...` (Instagram Login, obtido no fluxo OAuth do Meta
for Developers). O token fica numa variável de ambiente ou gerenciador de credenciais; nunca no chat.

Fluxo (graph.instagram.com/v23.0): 1) criar N containers `is_carousel_item=true` → 2) esperar cada `status_code=FINISHED` →
3) criar container `media_type=CAROUSEL` com `children` + `caption` → 4) `media_publish` com `creation_id`. Salvar `media_id` e
pegar o `permalink`.

Sem token configurado: entregar os cards em ordem + a legenda pronta, e o passo manual (postar pelo app do Instagram).

---

### ETAPA 10 — Automação de comentário (opcional)
Se a pessoa usa uma ferramenta de comment-to-DM, configurar a palavra-chave do CTA nela e testar com um comentário real.

---

## 🧰 GOTCHAS (não repetir)
1. **Token IG ≠ Facebook** — `IGAA...` roda em `graph.instagram.com`. Sintoma: "Cannot parse access token".
2. **Litterbox/Catbox** bloqueiam o scraper da Meta. Sintoma: erro 9004. Solução: host estático próprio.
3. **Cache de CDN** serve versão antiga. Solução: `?v=$(date +%s)`.
4. **Imagem num formato que a Meta rejeita** (erro 36001). Solução: reconverter para JPG.
5. **Logo via prompt nunca é pixel-perfect** — overlay do PNG oficial via HTML.
6. **Private Reply ≠ DM padrão** — botão anexado JUNTO no payload da Private Reply, nunca numa 2ª chamada.
7. **Envio sequencial OBRIGATÓRIO** — 1 por vez, pausa de 1s, esperar confirmação.
8. **Troca de caminho de imagem NUNCA em silêncio.** Chave de API de imagem, nunca.

---

## ✅ CRITÉRIOS DE "ENTREGUE"
- [ ] Estilo definido
- [ ] Roteiro aprovado
- [ ] Cards gerados e enviados em ordem, todos aprovados
- [ ] Legenda aprovada
- [ ] Post publicado (`media_id` salvo) ou pacote entregue para postagem manual
- [ ] Confirmado com permalink

## 🚨 PARAR E AVISAR QUANDO
- Referência não encontrável (link quebrado/post apagado)
- Os caminhos de imagem falharem
- A Meta retornar erro persistente
