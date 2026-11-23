---
name: pagina-design-premium
description: 'Transforma briefing, copy ou referência visual em landing page HTML de arquivo único com acabamento de estúdio, sem cara de IA. Use para "deixar a página bonita", "diagramar essa copy", "criar a LP desse briefing", "no estilo dessa página", "ficou com cara de IA". NÃO usar para diagnóstico de conversão nem performance (page-optimizer).'
---

# Página de Design Premium

<!-- desenho-antes-do-html:inicio -->
> **Passo 0 de toda página: desenho antes do HTML.** Antes de escrever HTML, siga
> `designer-senior/references/desenho-antes-do-html.md`: consigo um desenho de referência da página (gerador de imagem disponível,
> o que a pessoa já usa, ou a referência que ela mandou) e construo conforme o desenho (cores, hierarquia, composição e tipografia)
> com a copy aprovada. Sem desenho: faço do jeito normal desta skill e digo em "Assumi". Nunca bloqueia.
<!-- desenho-antes-do-html:fim -->

Skill de **direção de arte + diagramação**. Recebe conteúdo e devolve um HTML único com acabamento que não parece gerado.

## Os dois princípios

> **1.** O que faz uma página parecer cara não é ter mais elementos. É ter menos elementos, com mais intenção, organizados por um conceito que atravessa a página inteira.

> **2.** Não existe "o tema bonito". Existe a direção de arte certa para **este** nicho, **este** público e **este** registro emocional. Aplicar o mesmo visual em tudo é exatamente o que produz cara de IA.

Uma página de tráfego pago para gestor e uma página de emagrecimento para mulher de 45 anos não podem sair do mesmo sistema — muda a paleta, a família tipográfica, a curvatura, a densidade, o tipo de prova que convence e o ritmo. A skill **deriva** isso do briefing.

---

## Workflow

### Passo 0 — Regra de fidelidade

Se o usuário forneceu copy, **100% do texto entregue vem dela**. Não crie seção, microcopy, garantia, depoimento, número ou conteúdo de mock que não esteja no material. Texto inventado não pode ser validado com o cliente e obriga uma auditoria da página inteira.

Blocos que a copy não trouxe (FAQ, garantia, depoimentos, escassez) ficam **disponíveis sob pedido** — ofereça no fim, não encaixe sozinho. Leia `references/fidelidade-de-copy.md` para o que é permitido cortar, os mocks com marcador de preenchimento, e o relatório de fidelidade que fecha toda entrega.

### Passo 1 — Classificar a entrada

| Entrada | Sinal | Caminho |
|---|---|---|
| **Briefing** | descreve produto, público e oferta em prosa | Passo 2 → 3 → 4 → 5 → 6 |
| **Copy pronta** | manda o texto da página com headlines | Pule o Passo 2 |
| **Referência visual** | JPG/PNG/PDF/print de Figma | Leia `references/leitura-de-referencia.md` antes de tudo |

Com briefing puro sem copy: a copy sai antes do `ht-copy-paginas-e-emails` (núcleo de copy do Squad HT); se a pessoa quiser seguir já, escreva uma copy funcional e avise que é rascunho.

### Passo 2 — Extrair os dados obrigatórios

Tire primeiro do que já existe (briefing, copy, projeto, página atual). Pergunte de uma vez só, numa mensagem, apenas o que faltar:

1. **O que é e quanto custa**
2. **Para quem** — sexo, faixa etária, o que já tentou antes
3. **Prova disponível** — números reais, prints, depoimentos, credenciais
4. **Destino do CTA**
5. **Ativos** — logo, cor, fonte, fotos (ou "não tenho, escolhe você")

Se ele disser "não tenho cor nem referência", **não pergunte de novo**. Derive e proponha. É o trabalho da skill.

### Passo 3 — Direção de arte

Leia `references/direcao-de-arte.md`. Derive papel, tinta, destaque, cores de apoio, par tipográfico, curvatura e motivo a partir do registro emocional + público + nível de prova + ticket.

Apresente em 6 linhas (aprovação simples; sem resposta, siga com ela e diga "Assumi: esta direção, é só pedir para mudar"):

```
REGISTRO      acolhimento / alívio
PÚBLICO       feminino 35–55, já tentou outras coisas
PAPEL         creme quente #FBF6F0
DESTAQUE      cranberry #B8484F + 4 apoios dessaturados
TIPOGRAFIA    Fraunces (display) + Inter (corpo)
MOTIVO        grade de progresso de 12 semanas + divisor orgânico
```

Os arquétipos no fim daquele arquivo (`blueprint`, `botanica`, `editorial`, `terminal`, `festival`) são **pontos de partida**, não um menu. Ajuste sempre pelo menos o accent e o motivo ao caso concreto.

### Passo 4 — Conceito

A metáfora que dá coesão. Gere **3 candidatas** internamente, cada uma em duas linhas (qual é a metáfora e como aparece na página), escolha a mais forte e mostre as três com a escolhida marcada: "Assumi: conceito X (é só pedir para trocar por Y ou Z)".

Um conceito só é válido se produz **elementos concretos**: nomenclatura, numeração, forma dos separadores, tipo de moldura. "Moderno e clean" não é conceito.

### Passo 5 — Mapa de blocos

Leia `references/composicao.md` **antes** de `blocos.md`. Ele traz a grade de 12 colunas medida, as contagens de coluna que as referências usam, e a **biblioteca de 7 heróis** — para você escolher deliberadamente em vez de cair sempre no mesmo split com foto à direita.

Preencha o quadro de composição do fim daquele arquivo antes de escrever HTML. Se o hero anterior desta conversa foi *retrato lateral*, o próximo não pode ser.

Depois leia `references/sequencias.md` (ordem por perfil) e `references/blocos.md` (HTML). Quando o usuário fornece copy, a **ordem vem da copy**, não da sequência canônica.

**Densidade mínima — não negocie:**

| Perfil | Seções | Mocks de prova | Formas distintas |
|---|---|---|---|
| Low ticket | 12–16 | 3 | 8 |
| Ingresso de evento | 14–18 | 3 | 9 |
| High ticket | 12–16 | 3 | 8 |
| Captura de lead | 6–8 | 1 | 5 |
| Upsell | 3–5 | 1 | 3 |

Página cara **é** densa. Nove seções magras é o erro mais comum e o mais visível. Se o material do usuário não dá para a densidade mínima, diga isso explicitamente e proponha o que falta — não entregue uma página curta fingindo que está pronta.

Regras do mapeamento:
- **Uma forma nunca se repete em seções consecutivas.** Alterne: grid → lista densa → mock → split assimétrico → tabela → faixa escura → timeline.
- **Todo número relevante vira objeto visual**, não card com número grande. `references/prova-visual.md`.
- **Seção sem função sai.** Se você não sabe que objeção ela derruba, corte.

Mostre o mapa ao usuário — seção → bloco → objeção que resolve. Ele aprova ou corta.

### Passo 6 — Gerar

Partida: `assets/base.html`. Some as três camadas:

1. **Tokens** da direção de arte do Passo 3
2. **Sprite de ícones** de `references/sistema-de-icones.md` — escolha 6–10 ícones coerentes com o nicho e repita esses. Cole o sprite logo após `<body>`.
3. **Movimento** de `references/movimento.md` — no máximo 3 técnicas de scroll + 1 loop. Nada anima acima da dobra.
4. **Dispositivos** de `references/dispositivos.md` — biblioteca dos objetos construídos das duas referências, com o CSS real. **Mínimo 3 por página, e pelo menos 1 de cada família** (A = construídos/tela, B = tangíveis/foto). Escolha pela tabela do fim daquele arquivo, a partir do argumento da seção.
5. **Linguagem visual** de `references/linguagem-visual.md` — profundidade em 3 níveis de sombra, pastéis derivados, marca-texto, CTA em cor diferente do accent, uma seção escura com brilho, e o **elemento-assinatura**.

Não negociáveis:
- **Um arquivo só.** CSS em `<style>`, JS antes de `</body>`. Sem build, sem biblioteca externa além das fontes.
- **Mobile-first, referência 390px.** CSS base para mobile, `@media (min-width:900px)` para subir.
- **Pixel/GTM inline no `<head>`**, antes de tudo. Sem Pixel, deixe `<!-- PIXEL AQUI -->` e avise.
- **Zero imagem inventada.** Falta foto → `<div class="ph">` com proporção marcada, e liste os ativos pendentes com proporção e uso.
- **Todo CTA aponta pro link real** ou `#oferta`, e você lista onde trocar.

Salve em `/mnt/user-data/outputs/` e apresente com `present_files`.

### Passo 6b — Extrair de páginas ao vivo, quando houver

Se o usuário citar uma URL de referência e houver navegador conectado (`list_connected_browsers`), **extraia o sistema do CSS computado** em vez de estimar de screenshot. Amostra de pixel erra o accent; CSS não erra.

```js
// tokens declarados
const vars={};
for(const sh of document.styleSheets){try{for(const r of sh.cssRules){
  if(r.style&&r.selectorText&&/:root/.test(r.selectorText)){
    for(const p of r.style) if(p.startsWith('--')) vars[p]=r.style.getPropertyValue(p).trim();
}}}catch(e){}}
// escala tipográfica real
const g=el=>{const s=getComputedStyle(el);return{f:s.fontFamily,size:s.fontSize,w:s.fontWeight,ls:s.letterSpacing,lh:s.lineHeight,c:s.color,ta:s.textAlign}};
// e o CTA, que é onde mora o detalhe
```

Olhe em especial `font-size` do corpo, `font-weight` do display, e a **sombra do botão** — foi assim que se descobriu que o CTA verde carrega halo laranja. Extraia sistema (tokens, escala, sombras, radius); nunca copy, foto, logo ou ícone.

### Passo 7 — Renderizar e auditar

**Sempre renderize antes de dizer que está pronto.** Erro de espaçamento, quebra de texto e sobreposição só aparecem renderizados.
Se o Playwright não estiver disponível, peça OK e instale (`npm i -D playwright && npx playwright install chromium`); sem OK, abra o
HTML no navegador em 390 px e 1440 px e salve as capturas à mão.

```bash
npx playwright screenshot --viewport-size=390,844 --full-page saida.html mobile.png
npx playwright screenshot --viewport-size=1440,900 --full-page saida.html desktop.png
```

Abra os dois e olhe. Depois rode `references/anti-cara-de-ia.md` item por item, e:

- [ ] Densidade mínima do perfil atingida
- [ ] Cor de destaque em menos de 10% da área
- [ ] Mínimo de mocks atingido
- [ ] Nenhuma forma repetida em seções consecutivas
- [ ] Zero texto inventado; relatório de fidelidade escrito
- [ ] Todo gráfico tem referência (linha de empate, faixa semântica ou anel) **e** legenda de três linhas
- [ ] Pelo menos 4 contagens de coluna diferentes
- [ ] Mínimo 3 dispositivos, com pelo menos 1 de cada família
- [ ] Pelo menos 2 seções têm elemento que **atravessa a borda** de outro (selo pendurado, painel sobreposto, cauda apontando, número vazando)
- [ ] Elemento fixo escolhido entre A/B/C/D e justificado — cabeçalho fixo não é default
- [ ] Escala tipográfica calibrada pelo registro: B2B 36–42px display / 16–17px corpo · consumo 50–60px / 19–20px
- [ ] Tokens trazem `--accent-rgb` em canais separados
- [ ] Não caiu no vocabulário de uma referência só
- [ ] Hero escolhido da biblioteca e diferente do anterior
- [ ] Conceito aparece em 4+ lugares
- [ ] Corpo em 19–20px, display em weight 800 com tracking negativo forte
- [ ] Sombras compostas (rente + difusa), não uma sombra só
- [ ] Existe um elemento-assinatura que vem do assunto
- [ ] CTA está numa cor que não aparece em mais nada
- [ ] Não caiu em nenhum dos 3 defaults de IA (creme+serif+terracota, preto+neon, broadsheet)
- [ ] Ícones: um conjunto só, mesma grade, mesmo traço
- [ ] Movimento: no máximo 3 técnicas, nada animando acima da dobra
- [ ] `prefers-reduced-motion` respeitado
- [ ] Zero emoji, zero gradiente entre dois matizes saturados
- [ ] `scrollWidth === 390` medido no navegador, não estimado
- [ ] Barra fixa inferior com `env(safe-area-inset-bottom)` e `viewport-fit=cover` — senão o botão morre sob a faixa do iPhone
- [ ] Camada defensiva de `mobile.md` aplicada
- [ ] Nenhum `<br>` de desktop quebrando errado no mobile

Relate o que ficou pendente por falta de material dele.

---

## Arquivos

| Arquivo | Quando ler |
|---|---|
| `references/direcao-de-arte.md` | **Passo 3, sempre.** Derivação de paleta, tipografia, curvatura, motivo |
| `references/anti-cara-de-ia.md` | **Sempre.** Antes e depois de gerar. Traz a calibração dos 3 defaults de IA e a lista do que NÃO está proibido |
| `references/linguagem-visual.md` | **Passo 6, sempre.** Sistema medido de páginas reais: profundidade, pastéis, marca-texto, molduras, elemento-assinatura |
| `references/dados-e-leitura.md` | **Sempre que a copy trouxer número ou dado.** Legenda de três linhas, linha de empate, faixa semântica, hub com raios, equação, zonas, radar, tag de estado, dados borrados, pílula na borda, abas |
| `references/prova-visual.md` | Sempre que houver número ou dado na copy |
| `references/fidelidade-de-copy.md` | **Passo 0, sempre que houver copy.** Zero invenção, mocks com marcador, blocos sob pedido |
| `references/composicao.md` | **Passo 5, sempre.** Grade, contagens de coluna e biblioteca de 7 heróis |
| `references/diagramacao.md` | **Passo 5 e 6.** Vocabulário de posicionamento: balão com cauda, glow, marca-d'água, trilha curva, painel sobreposto, nota com fita, anéis, colagem |
| `references/dispositivos.md` | **Passo 6, sempre.** Notebook 3D, órbita, chips, contador, pulso, digitando, selo pendurado, bilhete, pilha de notificações |
| `references/blocos.md` | Passos 5 e 6, biblioteca com HTML |
| `references/sequencias.md` | Passo 5, ordem por perfil |
| `references/sistema-de-icones.md` | Passo 6, sprite SVG e escolha do conjunto |
| `references/movimento.md` | Passo 6, animações, 22 keyframes medidos e armadilhas de CSS |
| `references/mobile.md` | **Passo 6 e 7, sempre.** Breakpoint 760px, camada defensiva, troca de `<br>`, reordenação |
| `references/leitura-de-referencia.md` | Entrada por imagem, PDF ou Figma |
| `assets/catalogo-dados.html` | **Passo 5.** Catálogo vivo dos gráficos que ensinam a ler |
| `assets/catalogo-composicoes.html` | **Passo 5.** Catálogo vivo de diagramação — os 12 recursos de posicionamento |
| `assets/catalogo-dispositivos.html` | **Passo 6.** Catálogo vivo: funil, tabela de gerenciador, medidor, sparkline, toast, bilhete, borda cônica, pulso, digitando, chips. Abra antes de escolher |
| `assets/base.html` | Passo 6, esqueleto de partida |
| `assets/exemplo-evento.html` | **Referência de teto.** Evento pago na linguagem medida: barra de lote, foto com cards sobrepostos, bilhete com entalhe, tiles pastel, moldura de notebook, escura com brilho |
| `assets/exemplo-botanica.html` | Registro acolhedor, saúde/feminino |
| `assets/exemplo-blueprint.html` | Referência do arquétipo técnico |

## Cuidados de conteúdo

- **Não invente prova.** Sem número real, o mock é claramente rotulado como ilustrativo.
- **Saúde, emagrecimento, finanças e ganhos** têm regra de anúncio. Evite promessa de resultado com número e prazo, e antes de subir passe por `auditor-policy-google-ads`.
- **Emagrecimento e alimentação:** não construa a página em cima de meta de peso, contagem de calorias, restrição ou comparação de corpos. Ancore em hábito, consistência, energia e força. É mais responsável, aprova mais fácil no anúncio e converte melhor com quem já tentou e falhou.
- **De uma referência visual, extraia sistema** (paleta, escala, ritmo, tipos de bloco) — nunca copy, foto, logo ou ícone da página original.

## O que esta skill não faz

Não escreve copy do zero, não faz rotas múltiplas, não faz app dinâmico.

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
