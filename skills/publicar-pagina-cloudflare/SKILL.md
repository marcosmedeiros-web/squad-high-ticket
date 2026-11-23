---
name: publicar-pagina-cloudflare
description: 'Publica página ou site estático (HTML, out/ do Next, dist/ do Vite) na Cloudflare Pages da conta do expert e devolve a URL conferida de fora. Use para "publicar", "colocar no ar", "subir a página", "fazer deploy", "gerar o link". Publicar sempre pede OK. NÃO usar para projeto que precisa de servidor (rota de API, banco).'
---

# Publicar página — Cloudflare Pages da conta do expert

Toda página estática feita aqui vai para o ar por este caminho: **Cloudflare Pages, na conta do próprio expert** (grátis), com uma
URL `https://<projeto>.pages.dev` que eu confiro de fora antes de dizer que está no ar.

## Regras (não negociáveis)

1. **Conta e chave são da pessoa.** Eu nunca crio conta, nunca digito, peço, leio ou mostro a chave. A chave fica num gerenciador
   de credenciais ou numa variável de ambiente que a pessoa define no terminal dela; nunca no chat, em arquivo do projeto ou em
   comando. Chave colada no chat virou lixo: apagar no painel da Cloudflare, gerar outra e guardar de novo.
2. **Publicar é ato público.** Antes, mostro a pasta, o nome do projeto e a URL esperada, e só publico com o OK.
3. **A pasta vai INTEIRA para uma URL pública.** Só o site: nada de `.env`, chave, token, transcrição, planilha ou dado de cliente.
   Antes de publicar confiro que a pasta não tem `.env` nem link simbólico (o deploy publicaria o arquivo de destino do link). Página
   que embute token (ex.: painel ligado a um webhook) vai com o token VAZIO — a pessoa digita o dela na tela de configurações.
4. **"Está no ar" só depois da conferência de fora** (HTTP 200 + um trecho da página, com anti-cache). Deploy sem conferência = digo
   que NÃO está confirmado.

## Primeira vez — passo da pessoa (eu guio, uma coisa por vez)

1. **Conta grátis na Cloudflare:** https://dash.cloudflare.com/sign-up — e-mail, senha, confirmar o e-mail. Plano Free.
2. **ID da conta:** depois de entrar, é o código de 32 letras/números que aparece no endereço do navegador logo depois de
   `dash.cloudflare.com/` (também aparece na lateral de "Workers & Pages"). Não é segredo.
3. **Chave de publicação SÓ de Pages:** https://dash.cloudflare.com/profile/api-tokens → Create Token → Create Custom Token →
   Permissions: **Account · Cloudflare Pages · Edit** (só essa) → Account Resources: Include a conta → Continue → Create Token.
   A chave aparece UMA vez: copiar e ir direto para o passo 4, sem colar em lugar nenhum.
4. **Guardar fora do chat:** no terminal da pessoa (ou no gerenciador de credenciais dela), definir
   `CLOUDFLARE_API_TOKEN` (a chave) e `CLOUDFLARE_ACCOUNT_ID` (o ID) como variáveis de ambiente. Ex. no Mac, digitando sem eco:
   `read -s CLOUDFLARE_API_TOKEN && export CLOUDFLARE_API_TOKEN` e `export CLOUDFLARE_ACCOUNT_ID=...`. Eu confiro só que existem
   (`[ -n "$CLOUDFLARE_API_TOKEN" ] && echo ok`), nunca o valor. Para publicar página basta essa chave (Pages · Edit); chave com
   DNS · Edit é outra, para domínio próprio — nunca a mesma chave com permissão a mais.
5. **Node 22 ou mais novo com npx** (o wrangler 4 pede Node 22+). A skill confere com `node -v`; se faltar ou for antigo, pede OK e
   instala (`brew install node` no Mac, ou o instalador LTS de https://nodejs.org). Sem OK: entrego a pasta pronta e o passo manual
   (painel da Cloudflare → Workers & Pages → Create → Pages → Upload assets → arrastar a pasta).

O wrangler não precisa de instalação global: o `npx` baixa na primeira vez (1 a 3 min).

## Publicar (só com OK)

```bash
cd "<pasta>" && [ ! -e .env ] && [ -z "$(find . -type l)" ] || { echo "pasta com .env ou link: parar"; exit 2; }
npx --yes wrangler@4 pages project create <projeto> --production-branch=main 2>/dev/null || true   # só na 1a vez
npx --yes wrangler@4 pages deploy . --project-name=<projeto> --branch=main          # produção
# prévia sem tocar a produção: --branch=previa → https://previa.<projeto>.pages.dev
```

- `<pasta>`: a pasta do site, com `index.html` na raiz — HTML single-file (a pasta só com o `index.html` e o que ele usa), `out/` do
  Next estático, `dist/` do Vite. Nunca a pasta de trabalho inteira (transcrição, rascunho, `.env`).
- `<projeto>`: minúsculas, números e hífen, de 1 a 58 (ex.: `lp-sessao-maio`, `proposta-cliente-x`). Vira `https://<projeto>.pages.dev`;
  se o nome já for de outra conta, a Cloudflare põe um sufixo — a URL certa é a que o deploy devolve.
- Se o `project create` falhar pedindo Workers, repetir com `--force` (cria direto no Pages).
- Atualizar a página = rodar o mesmo deploy com a pasta nova (mesmo projeto, mesma URL).

**Conferência de fora (obrigatória):**
```bash
U="https://<projeto>.pages.dev/"; for i in $(seq 1 12); do
  curl -s "$U?nc=$(date +%s)" | grep -qF "<trecho do title>" && { echo CONFERIDO; break; }; sleep 10; done
```

| Sintoma | Significa | O que eu faço |
|---|---|---|
| `CONFERIDO` | no ar e conferido de fora | entrego a URL |
| erro de autenticação | variável sem a chave/ID, ou chave sem permissão | guio a pessoa no passo 4 |
| `node` ausente ou antigo | falta Node 22+ | passo 5 |
| deploy ok, sem `CONFERIDO` | a URL não respondeu com a página | digo que NÃO está confirmado; tento de novo depois |

## Next.js, Vite e o que precisa de servidor

A Cloudflare Pages deste caminho serve **arquivos estáticos**. Vite: `npm run build` → publicar `dist/`. Next.js: no `next.config`,
`output: "export"` e `images: { unoptimized: true }` (converta as imagens para WebP antes) → `next build` → publicar `out/`.
O estático não leva: rota de API (`app/api/...`), middleware/Edge Config, e `redirects()`/`headers()` do `next.config` (no lugar
deles: `public/_redirects` e `public/_headers`, que a Cloudflare Pages lê). Formulário: postar direto no webhook da ferramenta de
automação (n8n, CRM) em vez de rota de API.

## Domínio próprio (opcional, depois do `*.pages.dev`)

Caminho da documentação da Cloudflare; confira cada passo na tela.

1. Painel → Workers & Pages → o projeto → **Custom domains** → Set up a custom domain → `lp.seudominio.com.br`.
2. Domínio com o DNS na própria Cloudflare (mesma conta): o painel cria o registro. DNS em outro lugar (Registro.br, Hostinger,
   GoDaddy): criar lá um **CNAME** `lp` → `<projeto>.pages.dev` (subdomínio; domínio raiz, sem `www`, pede o DNS na Cloudflare).
3. O certificado sai sozinho quando o domínio valida (de minutos a horas).
4. Conferir de fora antes de divulgar:
   `curl -sS -o /dev/null -w '%{http_code}\n' https://lp.seudominio.com.br/` → `200`, e o trecho da página no corpo.

A chave de publicação é só de Pages de propósito: ela não mexe em DNS. DNS a pessoa faz no painel.

## Projeto que precisa de servidor

Rota de API, banco, processo que fica rodando: não é pasta estática. Vai para um servidor próprio (VPS) ou outra hospedagem com
servidor; esta skill não cobre.

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
