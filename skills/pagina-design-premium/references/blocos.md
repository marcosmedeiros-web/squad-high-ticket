# Biblioteca de blocos

Blocos estruturais. Os blocos de **prova** (mocks, gráficos, tabelas) estão em `prova-visual.md`.

Todo bloco assume as classes de `assets/base.html`. Nenhum bloco depende de CSS extra além do que já está lá — se precisar, escreva inline no próprio elemento, não crie classe nova.

**Regra de uso:** nenhum bloco aparece duas vezes seguidas com a mesma forma. Consulte `sequencias.md` para a ordem.

Índice: [hero-oferta](#hero-oferta) · [hero-evento](#hero-evento) · [hero-editorial](#hero-editorial) · [agitacao](#agitacao) · [split-argumento](#split-argumento) · [lista-densa](#lista-densa) · [timeline](#timeline) · [modulos](#modulos) · [pra-quem](#pra-quem) · [autoridade](#autoridade) · [stack-de-valor](#stack-de-valor) · [oferta-final](#oferta-final) · [garantia](#garantia) · [faq](#faq) · [transparencia](#transparencia)

---

## hero-oferta

Para low ticket e venda direta. Assimétrico: argumento à esquerda, cartão de oferta à direita fixo.

```html
<section class="tight">
  <div class="wrap split">
    <div>
      <span class="tag">{{CATEGORIA}}</span>
      <h1 class="mt">{{HEADLINE}}</h1>
      <p class="lead mt">{{SUBHEADLINE}}</p>
      <ul class="list check mt-l">
        <li>{{PONTO_1}}</li><li>{{PONTO_2}}</li><li>{{PONTO_3}}</li>
      </ul>
    </div>
    <aside class="card sticky">
      <div class="between">
        <span class="tag on">{{CONDICAO}}</span>
        <span class="xs num">{{ID}}</span>
      </div>
      <div class="mt">
        <div class="xs">{{ANCORA}}</div>
        <div class="num" style="font-size:2.6rem;font-weight:700;line-height:1">{{PRECO}}</div>
        <div class="xs mt-s">{{PARCELAMENTO}}</div>
      </div>
      <a href="{{CTA_URL}}" class="btn block lg mt">{{CTA}}</a>
      <p class="xs mt-s center">{{MICROCOPY_ABAIXO_DO_BOTAO}}</p>
    </aside>
  </div>
</section>
```

O `{{MICROCOPY_ABAIXO_DO_BOTAO}}` é obrigatório e quase sempre esquecido: "Acesso imediato · 7 dias de garantia" derruba objeção no ponto exato de decisão.

---

## hero-evento

Para ingresso de evento e lançamento. Datas e formato precisam estar acima da dobra.

```html
<section class="tight">
  <div class="wrap">
    <span class="eyebrow" style="margin-bottom:.8rem">{{TAGLINE}}</span>
    <h1 style="max-width:16ch">{{HEADLINE}}</h1>
    <p class="lead mt" style="max-width:52ch">{{PROMESSA}}</p>

    <div class="grid g3 mt-l">
      <div><div class="xs">Datas</div><div class="num" style="font-size:1.25rem;font-weight:600">{{DATAS}}</div></div>
      <div><div class="xs">Horário</div><div class="num" style="font-size:1.25rem;font-weight:600">{{HORARIO}}</div></div>
      <div><div class="xs">Onde</div><div style="font-size:1.25rem;font-weight:600">{{PLATAFORMA}}</div></div>
    </div>

    <div class="card mt" style="display:flex;flex-wrap:wrap;gap:1.25rem;align-items:center;justify-content:space-between">
      <div class="stack" style="gap:.1rem">
        <span class="xs">{{LOTE}}</span>
        <span class="num" style="font-size:2.1rem;font-weight:700;line-height:1">{{PRECO}}</span>
      </div>
      <a href="{{CTA_URL}}" class="btn lg">{{CTA}}</a>
    </div>
    <p class="xs mt-s">{{ESCASSEZ_HONESTA}}</p>
  </div>
</section>
```

---

## hero-editorial

Para high ticket e autoridade pessoal. Foto grande é o elemento principal.

```html
<section class="air">
  <div class="wrap">
    <span class="eyebrow">{{CONTEXTO}}</span>
    <h1 style="max-width:18ch">{{HEADLINE}}</h1>
    <div class="split mt-l">
      <p class="lead">{{PARAGRAFO_DE_ABERTURA}}</p>
      <div>
        <a href="{{CTA_URL}}" class="btn block lg">{{CTA}}</a>
        <p class="xs mt-s">{{QUALIFICACAO}}</p>
      </div>
    </div>
  </div>
  <div class="wrap mt-xl">
    <img src="{{FOTO}}" alt="{{ALT}}" style="width:100%;border-radius:var(--radius)" loading="eager">
  </div>
</section>
```

Se não houver foto, troque a `<img>` por `<div class="ph">FOTO {{PROPORCAO}}</div>` e liste o ativo pendente na entrega.

---

## agitacao

O problema, antes da solução. Use lista densa de itens **específicos**, nunca 3 cards genéricos.

```html
<section class="alt">
  <div class="wrap">
    <span class="eyebrow"><span class="n">01</span> · {{TITULO_CURTO}}</span>
    <h2 style="max-width:20ch">{{TITULO}}</h2>
    <div class="cols mt-l">
      <p class="lead">{{CONTEXTUALIZACAO}}</p>
      <ul class="list neg">
        <li>{{SINTOMA_1}}</li><li>{{SINTOMA_2}}</li>
        <li>{{SINTOMA_3}}</li><li>{{SINTOMA_4}}</li>
      </ul>
    </div>
  </div>
</section>
```

---

## split-argumento

O bloco de trabalho pesado. Um argumento por vez, alternando o lado da imagem/mock a cada uso.

```html
<section>
  <div class="wrap split">        <!-- alterne .split e .split.rev -->
    <div>
      <span class="eyebrow"><span class="n">0{{N}}</span> · {{EYEBROW}}</span>
      <h2 style="max-width:18ch">{{TITULO}}</h2>
      <p class="lead mt">{{DESENVOLVIMENTO}}</p>
      <ul class="list check mt">
        <li>{{PONTO_1}}</li><li>{{PONTO_2}}</li><li>{{PONTO_3}}</li>
      </ul>
    </div>
    <div>
      <!-- aqui entra um mock de prova-visual.md, uma foto, ou nada -->
    </div>
  </div>
</section>
```

---

## lista-densa

Substitui os "3 cards com ícone". Nove itens específicos convencem mais que três vagos.

```html
<section class="tight">
  <div class="wrap">
    <div class="between">
      <h2 style="max-width:22ch">{{TITULO}}</h2>
      <span class="xs num">{{CONTAGEM}} itens</span>
    </div>
    <div class="cols mt-l">
      <ul class="list">
        <li>{{ITEM_1}}</li><li>{{ITEM_2}}</li><li>{{ITEM_3}}</li><li>{{ITEM_4}}</li>
      </ul>
      <ul class="list">
        <li>{{ITEM_5}}</li><li>{{ITEM_6}}</li><li>{{ITEM_7}}</li><li>{{ITEM_8}}</li>
      </ul>
    </div>
  </div>
</section>
```

---

## timeline

Para evento de N dias, cronograma, ou sequência de etapas.

```html
<section class="alt">
  <div class="wrap">
    <span class="eyebrow"><span class="n">0{{N}}</span> · {{EYEBROW}}</span>
    <h2 style="max-width:20ch">{{TITULO}}</h2>
    <div class="stack mt-l" style="gap:0;border-top:var(--border)">
      <!-- repetir por etapa -->
      <div class="split" style="padding-block:1.75rem;border-bottom:var(--border);gap:1.5rem">
        <div class="row" style="align-items:flex-start;gap:1.25rem">
          <span class="num" style="font-size:2rem;font-weight:700;line-height:1;color:var(--accent);flex:none">0{{I}}</span>
          <div>
            <div class="xs num">{{DATA}} · {{HORARIO}}</div>
            <h3 class="mt-s">{{TITULO_ETAPA}}</h3>
            <p class="sm mt-s">{{RESUMO}}</p>
          </div>
        </div>
        <ul class="list check">
          <li>{{ENTREGA_1}}</li><li>{{ENTREGA_2}}</li><li>{{ENTREGA_3}}</li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

---

## modulos

Para curso/área de membros. Numeração + entregáveis.

```html
<section>
  <div class="wrap">
    <span class="eyebrow"><span class="n">0{{N}}</span> · {{EYEBROW}}</span>
    <h2 style="max-width:20ch">{{TITULO}}</h2>
    <div class="grid g2 mt-l">
      <div>
        <div class="between"><span class="xs num">MÓD-01</span><span class="tag">{{DURACAO}}</span></div>
        <h3 class="mt-s">{{NOME_MODULO}}</h3>
        <p class="sm mt-s">{{DESCRICAO}}</p>
      </div>
      <!-- repetir -->
    </div>
  </div>
</section>
```

---

## pra-quem

Duas colunas opostas. Nove de cada lado — a densidade é o ponto: quanto mais específico, mais o leitor se reconhece.

```html
<section class="alt">
  <div class="wrap">
    <span class="eyebrow"><span class="n">0{{N}}</span> · Antes de decidir</span>
    <h2 style="max-width:22ch">{{TITULO}}</h2>
    <div class="cols mt-l">
      <div>
        <div class="between"><span class="tag on">É pra você se</span><span class="xs num">09</span></div>
        <ul class="list check mt">
          <li>{{PERFIL_1}}</li><li>{{PERFIL_2}}</li><li>{{PERFIL_3}}</li>
          <li>{{PERFIL_4}}</li><li>{{PERFIL_5}}</li>
        </ul>
      </div>
      <div>
        <div class="between"><span class="tag">Não é pra você se</span><span class="xs num">09</span></div>
        <ul class="list neg mt">
          <li>{{ANTI_1}}</li><li>{{ANTI_2}}</li><li>{{ANTI_3}}</li>
          <li>{{ANTI_4}}</li><li>{{ANTI_5}}</li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

Os itens de "não é pra você" precisam ser reais, não elogios disfarçados. "Não é pra quem não quer sucesso" é vazio. "Não é pra quem não pode estar ao vivo nos três dias" filtra de verdade — e por isso constrói confiança.

---

## autoridade

Foto + credenciais em números. Nunca card de estatística solto: os números vão dentro da prosa ou em uma faixa de rodapé do bloco.

```html
<section>
  <div class="wrap split rev">
    <div>
      <img src="{{FOTO}}" alt="{{NOME}}" style="width:100%;border-radius:var(--radius)" loading="lazy">
    </div>
    <div>
      <span class="eyebrow"><span class="n">0{{N}}</span> · Quem ensina</span>
      <h2>{{NOME}}</h2>
      <p class="lead mt">{{PARAGRAFO_1}}</p>
      <p class="sm mt">{{PARAGRAFO_2}}</p>
      <div class="grid g2 mt-l">
        <div><div class="num" style="font-size:1.6rem;font-weight:700">{{N1}}</div><div class="xs">{{LABEL1}}</div></div>
        <div><div class="num" style="font-size:1.6rem;font-weight:700">{{N2}}</div><div class="xs">{{LABEL2}}</div></div>
      </div>
    </div>
  </div>
</section>
```

---

## stack-de-valor

Itens com preço individual, soma, e o preço final. Só use se os preços individuais forem defensáveis — stack inflado é a coisa mais "cara de infoproduto ruim" que existe.

```html
<section class="alt">
  <div class="wrap" style="max-width:760px">
    <span class="eyebrow"><span class="n">0{{N}}</span> · O que está incluso</span>
    <h2>{{TITULO}}</h2>
    <div class="mt-l" style="border-top:var(--border)">
      <!-- repetir por item -->
      <div class="between" style="padding:1rem 0;border-bottom:var(--border);align-items:flex-start">
        <div style="max-width:60ch">
          <strong>{{ITEM}}</strong>
          <p class="xs mt-s">{{DESCRICAO}}</p>
        </div>
        <span class="num sm" style="flex:none">{{VALOR}}</span>
      </div>
      <div class="between" style="padding:1rem 0;border-bottom:var(--border)">
        <span class="sm">Valor se comprado separado</span>
        <span class="num sm" style="text-decoration:line-through;color:var(--ink-3)">{{SOMA}}</span>
      </div>
    </div>
  </div>
</section>
```

---

## oferta-final

Sempre em `section.dark`. É o ponto de virada visual da página.

```html
<section class="dark air" id="oferta">
  <div class="wrap" style="max-width:820px">
    <span class="eyebrow">{{EYEBROW}}</span>
    <h2 style="max-width:20ch">{{TITULO_FECHAMENTO}}</h2>
    <ul class="list check mt-l" style="border-color:color-mix(in srgb,var(--bg) 18%,transparent)">
      <li>{{ENTREGA_1}}</li><li>{{ENTREGA_2}}</li><li>{{ENTREGA_3}}</li>
      <li>{{ENTREGA_4}}</li><li>{{ENTREGA_5}}</li>
    </ul>
    <div class="mt-l" style="border:1px solid color-mix(in srgb,var(--bg) 22%,transparent);border-radius:var(--radius);padding:clamp(1.25rem,4vw,2rem)">
      <div class="between">
        <div class="stack" style="gap:.15rem">
          <span class="xs">{{ANCORA}}</span>
          <span class="num" style="font-size:clamp(2.2rem,6vw,3rem);font-weight:700;line-height:1">{{PRECO}}</span>
          <span class="xs">{{PARCELAMENTO}}</span>
        </div>
        <a href="{{CTA_URL}}" class="btn lg">{{CTA}}</a>
      </div>
    </div>
    <div class="row mt" style="gap:1.5rem">
      <span class="xs">→ {{BENEFICIO_1}}</span>
      <span class="xs">→ {{BENEFICIO_2}}</span>
      <span class="xs">→ {{BENEFICIO_3}}</span>
    </div>
  </div>
</section>
```

---

## garantia

Não use selo com fita. Use um bloco sóbrio — sobriedade transmite mais segurança que medalha.

```html
<section class="tight">
  <div class="wrap card" style="max-width:760px">
    <div class="row" style="gap:1.25rem;align-items:flex-start">
      <span class="num" style="font-size:2.4rem;font-weight:700;color:var(--accent);line-height:1;flex:none">{{DIAS}}</span>
      <div>
        <h3>{{TITULO_GARANTIA}}</h3>
        <p class="sm mt-s">{{TEXTO_GARANTIA}}</p>
      </div>
    </div>
  </div>
</section>
```

---

## faq

Acordeão numerado. O JS de "um aberto por vez" já está em `base.html`.

```html
<section class="alt">
  <div class="wrap" style="max-width:820px">
    <span class="eyebrow">FAQ</span>
    <h2 style="max-width:18ch">{{TITULO}}</h2>
    <div class="acc mt-l">
      <details>
        <summary><span class="q">01</span>{{PERGUNTA}}</summary>
        <div class="a">{{RESPOSTA}}</div>
      </details>
      <!-- repetir; 8 a 11 perguntas -->
    </div>
  </div>
</section>
```

Ordene por peso: as três primeiras são as objeções que mais matam a venda, não as mais fáceis de responder.

---

## transparencia

Bloco curto antes ou depois da oferta, dizendo o que vai acontecer. Custa pouco e paga muito em confiança — especialmente em evento que termina em pitch.

```html
<div class="panel mt" style="max-width:680px">
  <span class="tag">Aviso de transparência</span>
  <p class="sm mt-s">{{O_QUE_VAI_ACONTECER}}</p>
</div>
```
