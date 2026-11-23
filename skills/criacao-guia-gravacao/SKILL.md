---
name: criacao-guia-gravacao
description: 'Gera o guia de gravação do webinário: a página que o expert deixa aberta durante a aula, com nomes para cumprimentar e perguntas para responder, em HTML parseável. Gatilhos: "guia de gravação", "guia do webinário", "página com os nomes e perguntas da live", "monta o guia da aula". NÃO usar para a página de inscrição do webinário (ht-webinario-de-vendas).'
---

# Criação do Guia de Gravação de Webinário

O guia é USO INTERNO da live: seção 1 traz os nomes que "chegam" na live pro expert cumprimentar, seções 2 e 3 trazem as perguntas que ele responde ao vivo. Depois da gravação, o MESMO HTML pode alimentar um motor de chat da sala do webinário (se você tiver essa peça montada) através de um parser que lê a marcação abaixo. Por isso a estrutura HTML é CONTRATO: não pode divergir do padrão abaixo.

## Exemplar validado (fonte da verdade)

Sempre partir de um exemplar, nunca desenhar do zero:
1. Se já existe um guia anterior do expert que passou no parser (arquivo único `index.html`), ele é o exemplar.
2. Sem guia anterior: o template da seção "Template do index.html" abaixo é o exemplar.

O jeito certo de gerar um guia novo é copiar o `index.html` do exemplar e trocar SÓ o conteúdo (título, hero, pessoas, perguntas, chave do localStorage), preservando CSS, JS e marcação byte a byte.

## O processo

Pergunte o mínimo: só o que não dá para deduzir do material. O que faltar e tiver padrão razoável, assuma e liste em "Assumi: … (é só pedir para mudar)".

1. **Tema e conteúdo.** Perguntar qual o TEMA da aula e pedir o material que existir: roteiro, tópicos, rascunho, transcrição, o que ele vai ensinar. Se a oferta (produto, preço, formato única/mensal, parcelamento, garantia, bônus) não vier junto, buscar na pasta do projeto (02-oferta) antes de perguntar.
2. **Alunos reais.** Perguntar quais ALUNOS REAIS da comunidade incluir (nome a nome ou lista do expert). Sem lista, o guia sai só com fictícios e você avisa isso na entrega; nunca inventar nome de aluno real.
3. **Gerar o elenco e as perguntas** (regras de geração abaixo).
4. **Montar o `index.html`** no padrão exato do exemplar (template abaixo).
5. **Validar com o parser** (checklist abaixo). Só seguir pro deploy com o parser passando.
6. **Publicar** com a skill `publicar-pagina-cloudflare` (Cloudflare Pages da conta do expert ou da agência; a pasta tem só o `index.html`), com o seu OK antes de pôr no ar. A receita Vercel abaixo é a alternativa.
7. **Entregar o link**; se houver motor de chat da sala, este guia é o input dele.

## Regras de geração

**Seção 1, nomes (~74 no total, meta: ~39 reais + ~35 fictícios):**
- Alunos REAIS levam a badge laranja `ALUNO`, classe `person real`, `data-id="rNN"`, e NÃO levam profissão (`p-perfil`).
- Fictícios levam `data-id="pNN"`, handle Instagram realista (padrão nome + sufixo de nicho: `@dra.anabeatriz.odonto`, `@beto.silva.autopecas`, `@lari.fontes.estetica`) e SEMPRE `p-perfil` com a profissão. A profissão é o elo: ela conecta a persona à pergunta que ela vai fazer nas seções 2 e 3.
- Profissões LIGADAS ao tema da aula e aos nichos que compram a oferta (clínicas, imóveis, advocacia, academias, lojas, agências, infoprodutores, agro, energia solar, food service etc). Variar.
- Cidade/UF espalhada pelo Brasil INTEIRO, capitais e interior, todas as regiões (o exemplar cobre de Macapá/AP a Santa Maria/RS). Não repetir a mesma cidade em sequência.
- Intercalar real e fictício na grade (o exemplar alterna r, p, r, p...).

**Seção 2, perguntas de conteúdo (~22):**
- Cada pergunta NASCE do conteúdo que veio: dúvida real de quem vive aquele nicho assistindo aquela aula, nunca pergunta genérica de IA.
- Cada pergunta tem dono: uma persona FICTÍCIA da seção 1, com contexto de vida na fala ("minhas clientes agendam tudo pelo direct", "na advocacia eu tenho sigilo profissional", "eu recebo muito curioso que não compra"). A profissão do dono tem que casar com a pergunta.
- Nunca atribuir pergunta a aluno REAL (não botar palavra na boca de gente de verdade).
- Cobrir os eixos: funciona pro meu nicho?, diferença pra ferramenta que já uso, canais, controle/erro da IA, requisitos técnicos, custo recorrente, personalização de tom, integrações (agenda, pagamento), tempo/dificuldade de setup, segurança/sigilo, qualificação de lead, disponibilidade 24h.

**Seção 3, perguntas de oferta (~10), adaptadas ao preço e formato REAIS da oferta dele:**
preço única vs mensal; parcelado com ou sem juros (citar o valor real, ex. "12x tem juros ou fica menos de R$30 mesmo?"); garantia (vale mesmo depois de usar?); acesso na hora; suporte/grupo; bônus vitalício ou expira; custo extra por fora (servidor, ferramenta); serve pra renda extra/CLT; materiais vitalícios ou com prazo; comprar agora e usar depois. Donos também são fictícios da seção 1, com profissão coerente.

## CONTRATO DE SAÍDA: marcação parseável (INEGOCIÁVEL)

O `parse-guia.mjs` extrai `{ cast: [{name, handle, city, is_alumni, profession?}], questions: [{n, section, text, owner_name, owner_handle}] }` por REGEX. Qualquer desvio abaixo quebra o chat fabricado da sala:

1. **Pessoa** é um `<div class="person">` ou `<div class="person real">` SEM nenhum `<div>` aninhado dentro (só `<span>`), em UMA linha lógica fechada pelo primeiro `</div>`. Classe exatamente `person real` nessa ordem pro aluno real.
2. Dentro da pessoa, os spans com classes exatas: `p-nome` (nome; no real, a badge `<span class="badge-aluno">ALUNO</span>` vai DENTRO do p-nome), `p-arroba` (com `@`), `p-cidade` (formato `Cidade/UF`), `p-perfil` (só fictício). O parser lê o nome como tudo antes de `<span class="p-arroba"` e tira a badge pelo ELEMENTO (o `<span class="badge-aluno">…</span>` inteiro, seja qual for o texto dele), nunca pelo texto do selo; `is_alumni` vem da classe `real` ou da presença de `badge-aluno`. Parser que ainda remove o selo por um texto fixo antigo deixa "ALUNO" colado no nome: ajuste-o antes de validar.
3. **Seções de perguntas** abrem com `<section class="acc" data-sec="conteudo" ...>` e `<section class="acc" data-sec="oferta" ...>`. O atributo `class` vem PRIMEIRO e `data-sec` logo em seguida (regex: `<section class="acc[^"]*" data-sec="...">`). Valores válidos só `conteudo` e `oferta` (a seção de nomes usa `data-sec="nomes"` e não entra nas questions).
4. **Pergunta** segue esta sequência de tags SEM nada entre elas (nem espaço, nem quebra de linha entre o `>` da div e o primeiro span):
```html
<div class="question" data-id="c01"><span class="q-num">01</span><span class="q-texto">Texto da pergunta?<span class="q-quem"><b>Nome Do Dono</b> &middot; @handle.do.dono</span></span></div>
```
   O `q-quem` fica ANINHADO dentro do `q-texto`. O separador é a entidade LITERAL `&middot;` (nunca o caractere `·` direto), com `<b>` no nome e `@` antes do handle. `q-num` numérico ("01", "02"...).
5. `data-id` únicos no documento: `rNN` reais, `pNN` fictícios, `cNN` conteúdo, `oNN` oferta. O JS de riscar e o contador dependem disso.
6. Todo `owner` de pergunta (nome + handle) precisa existir IDÊNTICO na seção 1 (o motor da sala cruza os dois).
7. Zero dependência externa: CSS e JS inline, fontes de sistema, favicon data URI.

## Template do index.html (blocos essenciais)

Copiar o exemplar inteiro e trocar o conteúdo. Estrutura resumida do que existe nele:

```html
<!DOCTYPE html><html lang="pt-BR"><head>
<title>Guia do Webinário · {TEMA}</title>
<meta name="robots" content="noindex, nofollow">
<style>
/* Família visual AVELLOIA, neo-brutalista. Tokens do template:
   --bg:#faf5ec; --bg-alt:#f8f1e7; --surface:#fff; --fg:#1b1714; --fg-muted:#6c6253;
   --ember:#ff5a1f; --ember-dk:#b8380a; --line:#e8dccb; --ink:#160f0a; --gold:#c98a00;
   --danger:#dc2626; --shadow-brutal:5px 5px 0 0 var(--fg);
   fontes: Space Grotesk (display) / DM Sans (body) / Geist Mono (mono), fallback sistema.
   Copiar o <style> COMPLETO do exemplar: header sticky, hero com grid creme,
   acordeão .acc/.acc-head/.acc-body-wrap, .people-grid/.person/.badge-aluno,
   .q-list/.question/.q-num/.q-texto/.q-quem, estado .done (riscado + tag USADO),
   oferta com borda --gold, footer ink, media queries. */
</style></head><body>

<header class="site-header">
  <a class="brand" href="#top"><span class="brand-mark">&rsaquo;&lsaquo;</span>
  <span class="brand-text">GUIA DA LIVE<br>{TEMA}</span></a>
  <span class="head-progress" id="progress">0/{TOTAL} usados</span>
  <button class="btn-reset" id="btn-reset" type="button">Limpar riscados</button>
</header>

<section class="hero" id="top"><div class="container">
  <p class="eyebrow">// GUIA DE APOIO &middot; WEBINARIO AO VIVO &middot; @{handle-do-expert}</p>
  <h1 class="hero-title">GUIA DO WEBINÁRIO<br><span class="ember">{TEMA}</span></h1>
  <p class="hero-sub">Deixa esta página aberta do lado durante a gravação. Seção 1: nomes chegando na live. Seção 2: perguntas de conteúdo. Seção 3: perguntas de oferta.</p>
  <p class="hero-hint">Clique em qualquer nome ou pergunta pra riscar como já usado. Fica salvo mesmo se recarregar a página.</p>
</div></section>

<main><div class="container acc-list">

  <section class="acc open" data-sec="nomes" id="sec-nomes">
    <button class="acc-head" type="button" aria-expanded="true">
      <span class="acc-num">01</span><span class="acc-title">Nomes para cumprimentar</span>
      <span class="acc-count" data-count>{N}</span><span class="acc-toggle" aria-hidden="true">+</span>
    </button>
    <div class="acc-body-wrap"><div class="acc-body"><div class="acc-body-inner">
      <div class="people-grid">
        <div class="person real" data-id="r01"><span class="p-nome">Nome Real <span class="badge-aluno">ALUNO</span></span><span class="p-arroba">@handle.real</span><span class="p-cidade">Cidade/UF</span></div>
        <div class="person" data-id="p01"><span class="p-nome">Nome Fictício</span><span class="p-arroba">@handle.ficticio</span><span class="p-cidade">Cidade/UF</span><span class="p-perfil">profissão ligada ao tema</span></div>
        <!-- ...intercalar reais e fictícios até ~74 -->
      </div>
    </div></div></div>
  </section>

  <section class="acc" data-sec="conteudo" id="sec-conteudo">
    <button class="acc-head" type="button" aria-expanded="false">
      <span class="acc-num">02</span><span class="acc-title">Perguntas de conteúdo</span>
      <span class="acc-count" data-count>{N}</span><span class="acc-toggle" aria-hidden="true">+</span>
    </button>
    <div class="acc-body-wrap"><div class="acc-body"><div class="acc-body-inner">
      <p class="acc-desc">// {eixos do tema da aula}</p>
      <div class="q-list">
        <div class="question" data-id="c01"><span class="q-num">01</span><span class="q-texto">Pergunta nascida do conteúdo, com contexto de vida do dono?<span class="q-quem"><b>Nome Fictício</b> &middot; @handle.ficticio</span></span></div>
        <!-- ...até ~22 -->
      </div>
    </div></div></div>
  </section>

  <section class="acc" data-sec="oferta" id="sec-oferta">
    <button class="acc-head" type="button" aria-expanded="false">
      <span class="acc-num">03</span><span class="acc-title">Perguntas de oferta</span>
      <span class="acc-count" data-count>{N}</span><span class="acc-toggle" aria-hidden="true">+</span>
    </button>
    <div class="acc-body-wrap"><div class="acc-body"><div class="acc-body-inner">
      <p class="acc-desc">// Preço, parcelamento, garantia, entregáveis, acesso, suporte</p>
      <div class="q-list">
        <div class="question" data-id="o01"><span class="q-num">01</span><span class="q-texto">Os R${PRECO} é uma vez só ou eu pago todo mês?<span class="q-quem"><b>Nome Fictício</b> &middot; @handle.ficticio</span></span></div>
        <!-- ...até ~10 -->
      </div>
    </div></div></div>
  </section>

</div></main>

<footer class="site-footer"><div class="container footer-inner">
  <span class="brand-mark">&rsaquo;&lsaquo;</span>
  <p>GUIA DO WEBINÁRIO {TEMA} &middot; uso interno da live &middot; @{handle-do-expert}</p>
</div></footer>

<script>
// Copiar do exemplar. Pontos fixos:
// var KEY = "guia-webinario-{slug-do-tema}-usados";  <- chave NOVA por guia (localStorage)
// clique em [data-id] risca/desrisca (.done) e persiste; #progress mostra "usados/total";
// cada .acc mostra "usados/total" da seção em [data-count]; #btn-reset limpa com confirm;
// .acc-head abre/fecha o acordeão (classe .open + aria-expanded).
</script>
</body></html>
```

Nota: é uma página de uso interno do expert, o guia usa `localStorage` de propósito (não é artifact do claude.ai, a restrição de artifact não se aplica aqui).

## Roster de alunos — exemplo de formato

> Entradas fictícias só pra ilustrar o formato (nome + @handle + Cidade/UF). A lista real vem do expert; sem ela, nenhum nome real é inventado.

Fulano Exemplo @fulano.exemplo Cidade Um/SP · Ciclana Modelo @ciclana.modelo Cidade Dois/PR · Beltrano Teste @beltrano.teste Cidade Três/PE · Aluna Demo @aluna.demo Cidade Quatro/MG · Cliente Amostra @cliente.amostra Cidade Cinco/BA · Pessoa Fictícia @pessoa.ficticia Cidade Seis/RS

## Checklist de validação (rodar ANTES do deploy, entregar a prova)

1. **Parser roda?** Se você tem sua própria cópia do parser (`parse-guia.mjs`, do motor de chat da sala), rode local: `node parse-guia.mjs guia-novo.html guia-novo.json`. Saída esperada no stderr: `parse-guia: cast=74 (alumni=39, ficticios=35) questions=32 (conteudo=22, oferta=10)` com os números do guia novo. Se sair "nada reconhecido no HTML", a marcação divergiu do contrato. Sem o parser à mão, valide manualmente pelos itens 2-6 abaixo (todos dá pra conferir com `grep`/`jq` direto no HTML/no seu editor, sem depender de servidor nenhum).
2. **Badges certos?** No JSON, `is_alumni:true` bate exatamente com a lista de alunos reais (nem um a mais, nem um a menos) e nenhum aluno real tem `profession`.
3. **Profissões casam com as perguntas?** Pra cada question do JSON, achar o dono no cast e conferir que a `profession` sustenta a pergunta (dentista pergunta de agenda, gestor de tráfego pergunta de campanha).
4. **Nenhuma pergunta órfã?** Todo `owner_name` + `owner_handle` existe no cast, é fictício (`is_alumni:false`) e tem `profession`. Conferência rápida no JSON com `jq`.
5. **data-id únicos** (`grep -o 'data-id="[^"]*"' index.html | sort | uniq -d` vazio), contador do header = total de itens, `&middot;` literal em todos os q-quem, chave nova no localStorage.
6. Abrir a página e clicar: risca, persiste no reload, contador anda, "Limpar riscados" zera.

## Publicar

> **Publicar = skill `publicar-pagina-cloudflare` (padrão):** Cloudflare Pages da conta do expert ou da agência, chave guardada num gerenciador de credenciais ou variável de ambiente (nunca em comando, log ou chat), URL `https://<projeto>.pages.dev` conferida de fora antes de dizer que está no ar; domínio próprio é opcional, depois (seção "Domínio próprio" da skill). A pasta publicada tem só o `index.html` do guia. A receita Vercel abaixo é a **alternativa**: só quando você pedir a Vercel.

### Alternativa: Vercel

Na Vercel, o domínio próprio usa A record no Cloudflare apontando pra 76.76.21.21. Guia novo vai pelo padrão acima; este é o caminho da alternativa (precisa das CLIs `gh` e `vercel`; sem elas, a skill oferece instalar com `brew install gh` e `npm i -g vercel`, com o seu OK):

```bash
# suas próprias credenciais, de um gerenciador de credenciais ou variável de ambiente (nunca no chat)
GH_TOKEN=$(grep "^GITHUB_TOKEN" .env | cut -d= -f2)
VERCEL_TOKEN=$(grep "^VERCEL_TOKEN" .env | cut -d= -f2)
CF_TOKEN=$(grep "^CLOUDFLARE_API_TOKEN" .env | cut -d= -f2)

# 1) repo GitHub PRIVADO (conta <GITHUB_USER>, branch master)
cd <pasta-do-guia>   # só o index.html
git init && git add index.html && git commit -m "Guia do Webinário {TEMA} (layout avelloia)"
GH_TOKEN=$GH_TOKEN gh repo create <GITHUB_USER>/guia-{slug} --private --source=. --push

# 2) deploy Vercel (scope <VERCEL_SCOPE>)
vercel --token $VERCEL_TOKEN --yes --prod --scope <VERCEL_SCOPE>
vercel domains add guia-{slug}.<dominio-do-expert> guia-{slug} --token $VERCEL_TOKEN --scope <VERCEL_SCOPE>

# 3) DNS Cloudflare, zona <dominio-do-expert> (<CF_ZONE_ID>):
curl -s -X POST "https://api.cloudflare.com/client/v4/zones/<CF_ZONE_ID>/dns_records" \
  -H "Authorization: Bearer $CF_TOKEN" -H "Content-Type: application/json" \
  --data '{"type":"A","name":"guia-{slug}","content":"76.76.21.21","ttl":1,"proxied":false}'

# 4) VERIFICAR de fora antes de reportar
curl -sI https://guia-{slug}.<dominio-do-expert> | head -5   # HTTP/2 200 + server: Vercel
```

## Entrega

Reportar curto com o link do guia no ar, os números (reais/fictícios/conteúdo/oferta), a prova do parser (linha de resumo do parse-guia) e, se houver motor de chat da sala, o lembrete de apontá-lo para este HTML.
