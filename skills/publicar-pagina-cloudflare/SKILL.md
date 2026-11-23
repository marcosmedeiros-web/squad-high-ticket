---
name: publicar-pagina-cloudflare
description: >-
  PADRÃO do kit pra publicar QUALQUER página ou site estático feito aqui (landing, página de vendas/ingresso, proposta,
  slides, apostila, guia, painel, relatório em HTML, a pasta out/ do Next estático ou dist/ do Vite): sobe a pasta na
  Cloudflare Pages da conta do PRÓPRIO dono (grátis) e devolve a URL https://<projeto>.pages.dev já conferida de fora
  (HTTP 200 + trecho da página). Use sempre que pedirem "publicar", "colocar no ar", "subir a página", "fazer deploy",
  "hospedar", "gerar o link", "atualizar a página no ar", "publish", "deploy my site", "push this live". A chave fica no
  cofre do kit — nunca em comando, log, tela ou chat; criar a conta e a chave é passo do dono, com o Claude guiando.
  A Vercel saiu do kit (14/10/2026): projeto que precisa de servidor (rota de API) vai pra VPS do dono.
---

# Publicar página — Cloudflare Pages da conta do dono

Desde a v5.2 (T114, pedido do Leo em 25/09/2026) toda página que o kit constrói vai pro ar por aqui: **Cloudflare Pages, na
conta do próprio dono**, com uma URL `https://<projeto>.pages.dev` que eu confiro de fora antes de dizer que está no ar.
A Vercel saiu do kit em 14/10/2026 (dono do kit: "vamos usar o Cloudflare apenas e VPS").

## Regras (não negociáveis)

1. **Conta e chave são do DONO.** Eu nunca crio conta, nunca digito, peço, leio ou mostro a chave. Ela entra no cofre do kit pelo
   terminal do dono (`guardar-chave.sh`, que pergunta sem eco) e chega ao wrangler só pelo ambiente, via `com-cofre.sh`. Chave colada
   no chat, em arquivo ou em comando virou lixo: o dono apaga essa no painel da Cloudflare, gera outra e guarda de novo.
2. **Publicar é ato público.** Antes, mostro ao dono a pasta, o nome do projeto e a URL esperada, e só publico com o OK dele
   (regra do kit: o que sai da máquina pede OK).
3. **A pasta vai INTEIRA pra uma URL pública.** Só o site: nada de `.env`, chave, token, transcrição, planilha ou dado de cliente
   que não é pra ser público. O script recusa pasta com `.env` e com link simbólico (o wrangler publicaria o arquivo de destino do
   link). Página que embute token (ex.: o painel do `lpsg-guiado` com o token
   do n8n) vai com o token VAZIO — a pessoa digita o dela na tela de configurações.
4. **"Está no ar" só com a linha `CONFERIDO`** que o script imprime (HTTP 200 + trecho da página, pedido de fora, anti-cache).
   `PUBLICADO` sem `CONFERIDO` não existe: o script sai com rc 6 e eu digo que NÃO está confirmado.

## Primeira vez — passo do dono (eu guio, uma coisa por vez)

1. **Conta grátis na Cloudflare:** https://dash.cloudflare.com/sign-up — e-mail, senha, confirmar o e-mail. Plano Free.
2. **ID da conta:** depois de entrar, é o código de 32 letras/números que aparece no endereço do navegador logo depois de
   `dash.cloudflare.com/` (também aparece na lateral de "Workers & Pages"). O ID não é segredo, mas mora no cofre junto com a chave.
3. **Chave de publicação SÓ de Pages:** https://dash.cloudflare.com/profile/api-tokens → Create Token → Create Custom Token →
   Permissions: **Account · Cloudflare Pages · Edit** (só essa) → Account Resources: Include a conta dele → Continue → Create
   Token. A chave aparece UMA vez: ele copia e vai direto pro passo 4, sem colar em lugar nenhum.
4. **Guardar no cofre, no Terminal DELE (não no chat):**
   ```bash
   bash ~/.claude/head-turbo/bin/guardar-chave.sh CLOUDFLARE_PAGES_TOKEN --testar nenhum
   bash ~/.claude/head-turbo/bin/guardar-chave.sh CLOUDFLARE_ACCOUNT_ID --testar nenhum
   ```
   Cada comando pergunta o valor sem mostrar na tela. Eu confiro sem ver valor nenhum:
   `bash ~/.claude/head-turbo/bin/guardar-chave.sh --listar` → as duas linhas com o tamanho (a chave tem ~40 caracteres, o ID 32).
   **O servidor MCP `cloudflare` saiu do kit na 5.2.9** (pedia uma segunda chave, `CLOUDFLARE_API_TOKEN`, e não publicava nada). Pra
   publicar página, só a `CLOUDFLARE_PAGES_TOKEN` (Pages · Edit). `CLOUDFLARE_API_TOKEN` com DNS · Edit é outra chave, de outro método
   (subdomínio próprio) — nunca a mesma chave de Pages com permissão a mais.
   **Guiado (5.2.9):** a skill `conectar-servico` diz a página do token e o que marcar; o dono gera, clica em Copy e grava no terminal
   dele (`guardar-chave.sh CLOUDFLARE_PAGES_TOKEN --da-area --testar cloudflare`).
5. **Node 22 ou mais novo com npx** na máquina que publica (o wrangler 4.141.0 pede Node 22+). Mac: `brew install node` (ou o instalador
   LTS de https://nodejs.org). VPS do kit: o `instalar-vps.sh` põe o Node 22 quando não há node; se lá houver Node 20/21, o script
   avisa (`MOTIVO=node-antigo`) e diz como atualizar.

A primeira publicação baixa o wrangler 4.141.0 pelo `npx` (sem instalar nada global; 1 a 3 min) e cria o projeto sozinha (produção = ramo
`main`).

## Publicar

```bash
bash ~/.claude/head-turbo/bin/com-cofre.sh bash ~/.claude/head-turbo/bin/publicar-pagina-cloudflare.sh <pasta> <projeto> [--previa] [--trecho "texto"]
```

- `<pasta>`: a pasta do site, com `index.html` na raiz — HTML single-file (a pasta só com o `index.html` e o que ele usa), `out/` do
  Next estático, `dist/` do Vite. Nunca a pasta de trabalho inteira (transcrição, rascunho, `.env`).
- `<projeto>`: nome na Cloudflare — minúsculas, números e hífen, de 1 a 58 (ex.: `lp-imersao-maio`, `proposta-cliente-x`). Vira
  `https://<projeto>.pages.dev`; se o nome já for de outra conta, a Cloudflare põe um sufixo — a URL certa é a que o script devolve.
- `--previa`: publica numa prévia (`https://previa.<projeto>.pages.dev`) sem tocar a produção — pra aprovação antes de ir pro ar.
- `--trecho "texto"`: o texto que a conferência procura na página (padrão: o `<title>` do `index.html`).
- Atualizar a página = rodar o mesmo comando com a pasta nova (mesmo projeto, mesma URL).

Por dentro: `npx --yes wrangler@4.141.0 pages deploy <pasta> --project-name=<projeto> --branch=main` (versão FIXA — a que o teste real de
25/09/2026 mediu) numa pasta temporária, sem terminal, com `CLOUDFLARE_API_TOKEN` só no ambiente do processo filho e o log em disco do
wrangler desligado; projeto inexistente → `wrangler pages project create <projeto> --production-branch=main --force` e publica de novo
(nessa versão, o create feito por um agente como eu é "delegado" pro Cloudflare Workers e falha; o `--force` é o jeito que o próprio
wrangler indica pra criar direto no Pages, e vai só no create — o deploy seguinte já não delega); depois `curl` de fora na URL final (até 12
tentativas, 10 s entre elas).

| Saída | Significa | O que eu faço |
|---|---|---|
| `0` + `PUBLICADO:` + `CONFERIDO` | no ar e conferido de fora | entrego a URL ao dono |
| `2` (`pasta-*` — inclusive `pasta-com-env` e `pasta-com-link` —, `projeto-invalido`, `sem-trecho`) | entrada errada, nada publicado | corrijo a pasta/o nome e rodo de novo |
| `3` (`sem-chave`, `sem-conta`) | a chave ou o ID não chegaram — cofre sem eles, ou rodei fora do `com-cofre.sh` | guio o dono no passo 4 (ou rodo pelo cofre) |
| `4` (`sem-node`, `node-antigo`) | falta Node 22+ com npx | mostro ao dono o comando de instalar |
| `5` (`wrangler-falhou`, `wrangler-sem-url`) | a Cloudflare recusou (chave errada/sem permissão, conta errada…) | mostro a mensagem (chave e conta já ocultadas) e vejo com o dono |
| `6` (`conferencia-falhou`) | o wrangler publicou, mas a URL não respondeu com a página | digo que NÃO está confirmado no ar; tento de novo depois |

## Next.js, Vite e o que precisa de servidor

A Cloudflare Pages deste caminho serve **arquivos estáticos**. Vite: `npm run build` → publicar `dist/`. Next.js: no `next.config`,
`output: "export"` e `images: { unoptimized: true }` (converta as imagens pra WebP antes) → `next build` → publicar `out/`.
O estático não leva: rota de API (`app/api/...` — ex.: a ficha de interesse do `paginas-lpsg-turbo`), middleware/Edge Config, e
`redirects()`/`headers()` do `next.config` (no lugar deles: `public/_redirects` e `public/_headers`, que a Cloudflare Pages lê).
Página que precisa de servidor não é pasta estática: o dono decide — levar a parte de servidor pra outro lugar (ex.: o formulário
postando direto no webhook do n8n) ou publicar esse projeto pela alternativa Vercel.

## Domínio próprio (opcional, depois do `*.pages.dev`)

Caminho da documentação da Cloudflare — **ainda não medido com uma conta real no kit**; confira cada passo na tela do dono.

1. Painel → Workers & Pages → o projeto → **Custom domains** → Set up a custom domain → `lp.seudominio.com.br`.
2. Domínio com o DNS na própria Cloudflare (mesma conta): o painel cria o registro. DNS em outro lugar (Registro.br, Hostinger,
   GoDaddy): criar lá um **CNAME** `lp` → `<projeto>.pages.dev` (subdomínio; domínio raiz, sem `www`, pede o DNS na Cloudflare).
3. O certificado sai sozinho quando o domínio valida (de minutos a horas).
4. Conferir de fora antes de divulgar:
   `curl -sS -o /dev/null -w '%{http_code}\n' https://lp.seudominio.com.br/` → `200`, e o trecho da página no corpo.

A chave de publicação é só de Pages de propósito: ela não mexe em DNS. DNS é o dono, no painel.

## Projeto que precisa de servidor

Rota de API, banco, processo que fica rodando: vai pra VPS do dono (o kit não tem mais a Vercel, desde 14/10/2026). Passo a passo
de Vercel que ainda apareça num método de referência (landing, proposta, slides…) não vale: troque por esta skill ou pela VPS.

<!-- pacote-pagina:inicio · kit 5.3.8 · fonte única: testes/pacote-pagina/bloco.md · não edite aqui: edite a fonte e rode testes/pacote-pagina/aplicar.py -->
## Pacote padrão de página publicada

Vale para TODA página que vai ao ar (venda, ingresso, captura, obrigado, institucional). Quem faz entrega com os 10 itens; quem audita
(picasso-auditor-turbo) reprova a página que não tiver qualquer um deles. Página sem o pacote não está pronta. Para publicar, use a skill
`publicar-pagina-cloudflare`.

1. **Na raiz do site:** `robots.txt` (com a linha `Sitemap: https://.../sitemap.xml`), `sitemap.xml` e `llms.txt` (o que é a página, para quem,
   a oferta e o contato, em texto simples). Opcional: `llms-full.txt`.
2. **No `<head>`:** `<html lang="pt-BR">` (ou o idioma da página), `<title>`, `<meta name="description">` e `<link rel="canonical">` com a URL final.
3. **Open Graph:** `og:title`, `og:description`, `og:url`, `og:type` e `og:image` (1200×630, URL absoluta, responde 200).
4. **Twitter:** `twitter:card` = `summary_large_image`, `twitter:title`, `twitter:description` e `twitter:image`.
5. **JSON-LD:** Organization + WebPage, e FAQPage se a página tiver FAQ. Product/Course **sem** `offers`/preço, salvo autorização do dono
   (preço no JSON-LD é uma segunda cópia do preço da página e diverge em silêncio). Validado de fora no validator.schema.org (comando abaixo).
6. **404 de verdade:** `404.html` na raiz. No Cloudflare Pages, sem ele todo caminho inexistente responde 200 com a página inteira (soft-404).
7. **`favicon.ico` na raiz**, além do `<link rel="icon">`.
8. **Rodapé padrão completo, com os dados do DONO do negócio:** `{{RAZAO_SOCIAL}}` · CNPJ `{{CNPJ}}` · `{{ENDERECO}}` · `{{EMAIL}}` ·
   WhatsApp `{{WHATSAPP}}` · Política de Privacidade · Termos de Uso · a garantia (`{{GARANTIA}}`) · o aviso de que os resultados variam de
   pessoa para pessoa · © `{{ANO}}` `{{RAZAO_SOCIAL}}`. Rodapé completo faz a Meta considerar a página melhor e distribuir mais os anúncios.
   Os campos saem dos dados do negócio que o dono já deu (memória, conhecimento, páginas anteriores). Faltou um campo: pergunte ao dono antes
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
