---
name: paginas-interativas-premium
description: 'Monta página interativa premium na linha escura cinética (React + Vite + Framer Motion, vídeo de fundo discreto, aurora, rastro de mouse, parallax). Use para "página interativa premium", "landing com animação e vídeo de fundo", "que pare o scroll", "versão React animada". NÃO usar para layout editorial claro em HTML estático (pagina-design-premium).'
---

# Páginas Interativas Premium (linha escura cinética)

<!-- desenho-antes-do-html:inicio -->
> **Passo 0 de toda página: desenho antes do HTML.** Antes de escrever HTML, siga
> `designer-senior/references/desenho-antes-do-html.md`: consigo um desenho de referência da página (gerador de imagem disponível,
> o que a pessoa já usa, ou a referência que ela mandou) e construo conforme o desenho (cores, hierarquia, composição e tipografia)
> com a copy aprovada. Sem desenho: faço do jeito normal desta skill e digo em "Assumi". Nunca bloqueia.
<!-- desenho-antes-do-html:fim -->

> Skill pra montar QUALQUER página interativa premium no visual da linha escura cinética: React + Vite + Framer Motion sobre **preto puro**, com **vídeo de fundo do Hyperframes** discreto, **aurora WebGL** sutil, **rastro de mouse pixelado** e animação scroll-driven. É a linha "para o scroll e diz uau", não o editorial bege.
> **Tarefa de código:** quem executa é o `ht-web-designer`, que monta a página, valida com VÍDEO (não só print) e entrega a prévia para aprovação.

O passo a passo detalhado, com as constantes e os snippets prontos, está em `reference.md` (LER antes de montar).

## ⚠️ Qual skill usar (não confundir)

São DUAS linhas de página. Escolher antes de começar:

- **landing-funil-editorial** = editorial impresso: papel **bege** `#efe7d2` + acento **coral** + serifa Playfair, HTML/CSS estático, `base.css` compartilhado. Funil, captura, VSL, carta, upsell.
- **ESTA (paginas-interativas-premium)** = linha **escura cinética**: **preto puro** `#000` + emerald `#1fe07a` + gold `#e8c66b`, React + Vite + Framer Motion + canvas/WebGL + vídeo de fundo. Página-vitrine que precisa de movimento e "uau".

Na dúvida: bege/serifa/jornal = a outra; preto/vídeo de fundo/rastro de mouse/animação = esta.

## 🧠 O FEEL

Fundo **PRETO PURO**. Por cima, três camadas que dão vida SEM roubar a cena — o vídeo é um **detalhe**, nunca o protagonista, e o **texto fica 100% legível** sempre:

1. **VideoBackground** (z-0) — o loop do Hyperframes (rede neural girando LENTO) roda a `opacity ~0.30` e ainda leva um **scrim preto** por cima a `~0.55`, então a rede neural lê bem apagada. Recalibra mudando só essas duas constantes.
2. **AuroraShader** (z-0) — aurora FBM em WebGL (emerald + gold sobre quase-preto), reage ao cursor, a `opacity 0.18` com `mix-blend-mode: screen` → só um respiro de luz.
3. **PixelSpotlight** (z-2) — rastro pixelado que segue o CAMINHO do mouse: pluma espalhada (não fio reto), `PEAK_ALPHA 0.18` (não ofusca o texto), movimento lento, e **some 100% em ~1.5s** quando o mouse para. Emerald no head → gold na cauda.

O conteúdo fica em `main` a `z-10`, acima de tudo. A barra de progresso de scroll no topo (`z-50`) usa o gradiente emerald→gold.

Acima disso, o conteúdo é **cinético**: seções entram com fade + slide + blur (`Reveal`), números fazem **count-up** ao entrar na tela, CTAs são **magnéticos** (puxam pro cursor), cards têm **tilt 3D**, e o hero tem **parallax scroll-driven** (a copy sobe e some, o vídeo desce e escala). Tudo isso é Framer Motion.

## 🧰 STACK / COMBO

Quatro ferramentas, cada uma no seu papel (detalhe e por que em `reference.md`):

- **21st.dev Magic** (MCP `21st-magic`) — usar SÓ a tool de **INSPIRAÇÃO** (busca de componentes/layout), que roda headless. O `component_builder` **NÃO roda headless** no nosso ambiente: não chamar, escrever o componente à mão a partir da inspiração.
- **Framer Motion** (`framer-motion`, pinado `11.3.19`) — toda a cinética: `Reveal` (fade+slide+blur via `whileInView`), parallax (`useScroll`/`useTransform`), tilt 3D (`useTilt`), botão magnético (`useMagnetic`), count-up (`useCountUp`), sticky storytelling.
- **UI/UX Pro Max** — design system: confirmar paleta, tipografia e densidade pra não cair em "AI slop". A paleta da casa nesta linha já é fixa (ver abaixo).
- **Hyperframes** — gera o **VÍDEO DE BACKGROUND** (three.js/shaders → render mp4 via CLI). Depois passa no **ffmpeg** pra DESACELERAR (`setpts`) e comprimir (H.264 CRF alto + `faststart`, sem áudio).

Base do projeto (`package.json`): Vite + **React 18.3.1** + **framer-motion 11.3.19** + **lucide-react 0.383.0** + Tailwind 3.4.7.

## 🎨 PALETA / TIPOGRAFIA (fixas nesta linha)

Tokens do `tailwind.config.js` — não inventar cor solta:

| Token | Hex | Uso |
|---|---|---|
| fundo | `#000` puro (base) / `bg-deep #050806` | corpo, trilhos de scrollbar |
| `emerald` | `#1fe07a` (soft `#7ef0b0`) | acento principal, head do rastro, títulos com glow |
| `gold` | `#e8c66b` | acento secundário, cauda do rastro, palavra de destaque |
| `coral` | `#ff4d4d` | CTA magnético (shimmer + glow coral) |
| `ink` | `#cfe6d8` | corpo de texto |
| `muted` | `#7f9a8a` | texto de apoio, subtítulo |

Fontes: **Geist** (sans, corpo/títulos) + **Fira Code** (mono, labels/eyebrow/contadores). Glow emerald nos títulos (`text-glow`, `shadow-glow`). Vidro fosco (`.glass`: gradiente emerald translúcido + `backdrop-filter: blur`) nos chips e no botão secundário.

## 🛠️ PROCESSO (resumo — o detalhe está em reference.md)

1. **Capturar a oferta 1:1** da página base (produção) num `data.ts` — copy, bullets, preço, FAQ, embed do VSL. **Não inventar conteúdo**; corrigir só a acentuação pra PT-BR correto.
2. **Montar as seções** com o combo (Hero com parallax + VSL em tilt, Problema, Benefícios, Entregáveis, Oferta, FAQ…). Cada seção em seu arquivo; nada de arquivo > 1000 linhas.
3. **Gerar o bg no Hyperframes** (loop 3D na paleta) e **otimizar o mp4** com ffmpeg: desacelerar (`setpts`), 1280×720, H.264 CRF alto, sem áudio, `+faststart`. Alvo: poucos MB (um bg de ~15MB costuma cair pra ~1.8MB).
4. **Calibrar** as 4 constantes (`VIDEO_OPACITY`, `BLACK_SCRIM_OPACITY`, `AURORA_OPACITY`, `PEAK_ALPHA`/`LIFE`/`MAX_SAMPLES` do rastro) até o vídeo virar detalhe e o rastro ficar sutil sem ofuscar.
5. **Publicar em PRÉVIA (com OK)**: `vite build` → `dist/` → skill `publicar-pagina-cloudflare` no ramo de prévia (Cloudflare Pages da conta do expert, `https://previa.<projeto>.pages.dev`, produção intocada). Alternativa, só se a pessoa pedir a Vercel: **Vercel REST API** (`deploy.mjs`: upload por sha + deployment prebuilt, `teamId <VERCEL_TEAM_ID>`, project pinado) — **NUNCA o `vercel` CLI** (já publicou em projeto errado).
6. **Validar com VÍDEO** (Playwright headless — a skill instala com OK se faltar: `npm i -D playwright && npx playwright install chromium`; sem OK, a pessoa grava a tela à mão — grava o scroll + varredura de mouse → webm → mp4): provar que o rastro segue, some ao parar, e o texto fica legível. **Print não prova animação.**
7. **Otimizar MOBILE**: 1ª dobra cheia, sem overflow horizontal, CTA acima da dobra. Auditar em viewport real (390/360, `is_mobile`).

É sempre **uma V2/preview pra aprovar**. NUNCA tocar produção; depois da aprovação, a pessoa decide a promoção/apontamento do domínio.

## 🚫 PEGADINHAS (as que já custaram tempo)

- **Vídeo de fundo pesa.** Sempre otimizar no ffmpeg (CRF alto, 720p, sem áudio, faststart). Sem isso a página trava no carregamento.
- **`component_builder` do 21st NÃO roda headless** no nosso ambiente. Só a tool de inspiração. Escrever o componente à mão a partir da referência.
- **Acentuação correta em produção** (regra da casa). Todo texto público em PT-BR impecável; o `data.ts` corrige a acentuação capturada.
- **Manter a oferta REAL 1:1** — preço, bullets, garantia, FAQ idênticos à base. Não criar promessa nova.
- **O rastro não pode ofuscar** o texto: `PEAK_ALPHA ~0.18`, pluma espalhada, blend screen. Se lavar a copy, está errado (foi o erro da 1ª versão — mancha verde forte parada).
- **Prova SEMPRE em VÍDEO**, não print: animação (rastro, parallax, count-up, vídeo girando) não aparece em foto.
- **Respeitar `prefers-reduced-motion`**: vídeo vira poster, canvas desenha 1 frame e para, rastro não roda.
- **`vercel` CLI proibido** (na alternativa Vercel): só REST API com teamId/project pinados.
- **Não usar a paleta da outra linha** (bege/coral editorial) aqui: esta é preto + emerald + gold.

## 📎 REFERENCE

- `reference.md` é o passo a passo COMPLETO: as 3 camadas de fundo com z-index e constantes verbatim, o rastro (todos os knobs), as primitives Framer (Reveal/Magnetic/Tilt/Counter) com snippet, o `data.ts` (capturar oferta), o `deploy.mjs` (Vercel REST API, alternativa), o pipeline Hyperframes + ffmpeg, o screencast Playwright de prova, e o checklist mobile.

<!-- pacote-pagina:inicio -->
## Pacote padrão de página publicada

Vale para TODA página que vai ao ar (venda, ingresso, captura, obrigado, institucional). Quem faz entrega com os 10 itens; quem audita
(o `ht-revisor-visual`) reprova a página que não tiver qualquer um deles. Página sem o pacote não está pronta. Para publicar, use a skill
`publicar-pagina-cloudflare`.

1. **Na raiz do site:** `robots.txt` (com a linha `Sitemap: https://.../sitemap.xml`), `sitemap.xml` e `llms.txt` (o que é a página, para quem,
   a oferta e o contato, em texto simples). Opcional: `llms-full.txt`.
2. **No `<head>`:** `<html lang="pt-BR">` (ou o idioma da página), `<title>`, `<meta name="description">` e `<link rel="canonical">` com a URL final.
3. **Open Graph:** `og:title`, `og:description`, `og:url`, `og:type` e `og:image` (1200×630, URL absoluta, responde 200).
4. **Twitter:** `twitter:card` = `summary_large_image`, `twitter:title`, `twitter:description` e `twitter:image`.
5. **JSON-LD:** Organization + WebPage, e FAQPage se a página tiver FAQ. Product/Course **sem** `offers`/preço, salvo autorização do expert
   (preço no JSON-LD é uma segunda cópia do preço da página e diverge em silêncio). Validado de fora no validator.schema.org (comando abaixo).
6. **404 de verdade:** `404.html` na raiz. No Cloudflare Pages, sem ele todo caminho inexistente responde 200 com a página inteira (soft-404).
7. **`favicon.ico` na raiz**, além do `<link rel="icon">`.
8. **Rodapé padrão completo, com os dados do dono do negócio:** `{{RAZAO_SOCIAL}}` · CNPJ `{{CNPJ}}` · `{{ENDERECO}}` · `{{EMAIL}}` ·
   WhatsApp `{{WHATSAPP}}` · Política de Privacidade · Termos de Uso · a garantia (`{{GARANTIA}}`) · o aviso de que os resultados variam de
   pessoa para pessoa · © `{{ANO}}` `{{RAZAO_SOCIAL}}`. Rodapé completo faz a Meta considerar a página melhor e distribuir mais os anúncios.
   Os campos saem dos dados do negócio que o expert já deu (memória, conhecimento, páginas anteriores). Faltou um campo: peça só esse dado antes
   de publicar. Nunca invente CNPJ, endereço ou garantia, e nunca use os dados de outra empresa.
9. **Celular:** medido em 320, 390 e 428 px sem rolagem horizontal (`document.documentElement.scrollWidth <= innerWidth` em cada largura).
10. **Conferência de fora antes de dizer "no ar"** (anti-cache; cada linha tem de passar):
```bash
P='https://DOMINIO/caminho/'; S="$(printf '%s' "$P" | cut -d/ -f1-3)/"; n=$(date +%s); T=$(mktemp)
for f in robots.txt sitemap.xml llms.txt favicon.ico; do echo "$f $(curl -s -o /dev/null -w '%{http_code}' "$S$f?nc=$n")"; done  # 200 nos 4
echo "inexistente $(curl -s -o /dev/null -w '%{http_code}' "${S}nao-existe-$n")"                                                 # 404
curl -s "$P?nc=$n" -o "$T"; for t in 'lang="' 'name="description"' 'rel="canonical"' og:title og:description og:url og:type og:image \
  twitter:card twitter:title twitter:description twitter:image application/ld+json CNPJ Privacidade Termos arantia resultados ©; do
  grep -qF "$t" "$T" && echo "ok $t" || echo "FALTA $t"; done
I=$(grep -oE '<meta[^>]*og:image"[^>]*>' "$T" | grep -oE 'content="[^"]+"' | head -1 | cut -d'"' -f2); echo "og:image $(curl -s -o /dev/null -w '%{http_code}' "$I")"
curl -s -X POST https://validator.schema.org/validate --data-urlencode "url=$P" | tail -c +5 \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print('schema fetchError', d.get('fetchError'), 'erros', d.get('totalNumErrors'))"  # None 0
```
Qualquer `FALTA`, código diferente de 200/404 ou erro no schema: a página não está no ar, está quebrada. Conserte e confira de novo.
<!-- pacote-pagina:fim -->
