# Prova visual

O arquivo que mais separa uma página de estúdio de uma página gerada.

## A regra

> Todo número relevante da copy vira **objeto visual em HTML/CSS**, nunca um card com número grande.

"R$ 100 milhões gerenciados em tráfego" dentro de um card gigante é enfeite: não prova nada, e é exatamente o que um template faz. O mesmo dado dentro de um painel de métricas simulado, com número quebrado, variação percentual e um item ruim no meio, **parece captura de tela** — e vira prova.

Três motivos para fazer em HTML e não em imagem:
1. Fica nítido em qualquer densidade de tela, inclusive retina
2. Pesa quase nada (não infla o LCP como um PNG de 400kb)
3. Você edita o número depois sem abrir editor de imagem

---

## Escolhendo o mock certo

| O que a copy diz | Mock |
|---|---|
| "analiso seus dados e mostro o que fazer" | [Painel de métricas](#1-painel-de-métricas) |
| "você conversa e a IA executa" | [Conversa](#2-conversa) |
| "esse criativo vendeu, esse queimou" | [Barras horizontais](#3-barras-horizontais) |
| "o jeito antigo × o jeito novo" | [Antes/depois lado a lado](#4-antesdepois) |
| "de X impressões só Y compram" | [Funil](#5-funil) |
| "aluno mandou isso no zap" | [Conversa de WhatsApp](#6-depoimento-em-conversa) |
| "somos diferentes de curso/dashboard/IA genérica" | [Tabela comparativa](#7-tabela-comparativa) |
| "você sai com essas 5 peças montadas" | [Entregáveis como peças](#8-entregáveis-como-peças) |

Use **no mínimo dois** por página. Mais de quatro cansa.

---

## As cinco regras de credibilidade

Um mock só funciona se parece real. O que quebra a ilusão:

1. **Número redondo.** `R$ 12.000` é inventado. `R$ 12.753,45` é extrato. Sempre quebre.
2. **Tudo bom.** Se todas as linhas são verdes, ninguém acredita. Inclua 1–2 itens ruins — e é isso que torna o resto crível.
3. **Label genérico.** Use o vocabulário real da ferramenta: "Conjunto de anúncios", "Custo por resultado", "ROAS", "Hook rate", "Connect rate". Nomes reais > nomes bonitos.
4. **Fonte proporcional em número.** Todo número em `var(--font-mono)` com `font-variant-numeric:tabular-nums`. Sem isso as colunas dançam.
5. **Sem cromo demais.** Barra de janela falsa com três bolinhas coloridas é cafona. Uma borda hairline e um cabeçalho discreto bastam.

E um aviso de responsabilidade: **não invente resultado de cliente.** Se o usuário não tem número real, o mock ilustra o *tipo* de leitura que a ferramenta faz, com dados claramente ilustrativos e um rótulo `Exemplo ilustrativo` visível. Isso continua sendo bom design e evita problema de policy e de confiança.

---

## 1. Painel de métricas

```html
<div class="card flush">
  <div class="between" style="padding:.85rem 1.15rem;border-bottom:var(--border)">
    <span class="tag"><span class="dot ok"></span>Conta ativa</span>
    <span class="xs num">Últimos 7 dias</span>
  </div>
  <div class="grid g4" style="border:0">
    <div>
      <div class="xs">Investimento</div>
      <div class="num" style="font-size:1.35rem;font-weight:600">R$ 12.753,45</div>
      <div class="xs" style="color:var(--ok)">↑ 18,6%</div>
    </div>
    <div>
      <div class="xs">Faturamento</div>
      <div class="num" style="font-size:1.35rem;font-weight:600">R$ 38.942,10</div>
      <div class="xs" style="color:var(--ok)">↑ 24,3%</div>
    </div>
    <div>
      <div class="xs">ROAS</div>
      <div class="num" style="font-size:1.35rem;font-weight:600">3,05x</div>
      <div class="xs" style="color:var(--ok)">↑ 15,1%</div>
    </div>
    <div>
      <div class="xs">CPA</div>
      <div class="num" style="font-size:1.35rem;font-weight:600">R$ 48,72</div>
      <div class="xs" style="color:var(--bad)">↓ 7,4%</div>
    </div>
  </div>
</div>
```

Opcional: sparkline SVG embaixo. Nunca use biblioteca de gráfico — 7 pontos em `<polyline>` resolvem.

```html
<svg viewBox="0 0 300 60" preserveAspectRatio="none" style="width:100%;height:60px">
  <polyline points="0,48 50,42 100,45 150,30 200,33 250,18 300,12"
    fill="none" stroke="var(--accent)" stroke-width="2" vector-effect="non-scaling-stroke"/>
</svg>
```

---

## 2. Conversa

Mostra o produto em uso. Muito mais convincente que descrever a interface.

```html
<div class="card flush" style="max-width:520px">
  <div class="between" style="padding:.8rem 1.1rem;border-bottom:var(--border)">
    <span class="tag"><span class="dot"></span>Assistente</span>
    <span class="xs num">10:42</span>
  </div>
  <div class="stack" style="padding:1.1rem;gap:.85rem">
    <div style="align-self:flex-end;max-width:82%;background:var(--accent-soft);border:var(--border);border-radius:var(--radius-lg);padding:.7rem .9rem;font-size:var(--t-sm)">
      Como estão minhas campanhas hoje?
    </div>
    <div style="max-width:88%;background:var(--bg-2);border:var(--border);border-radius:var(--radius-lg);padding:.85rem .95rem;font-size:var(--t-sm)">
      <strong>Leitura concluída.</strong>
      <ul class="stack mt-s" style="gap:.35rem">
        <li class="xs">→ 3 campanhas acima do ponto de empate</li>
        <li class="xs">→ 2 queimando verba sem venda</li>
        <li class="xs">→ Próxima ação: aprovar o plano de corte</li>
      </ul>
    </div>
  </div>
  <div style="padding:.7rem 1.1rem;border-top:var(--border)" class="xs muted">Pergunte ou peça algo…</div>
</div>
```

---

## 3. Barras horizontais

O gráfico mais útil e o mais fácil. Cada linha é um item real, a largura é `width:%`.

```html
<div class="stack" style="gap:.55rem">
  <!-- repita por item; verde = passou da meta, vermelho = não passou -->
  <div>
    <div class="between" style="margin-bottom:.28rem">
      <span class="sm">VSL — Eu quero te fazer vender</span>
      <span class="num sm">3,8x</span>
    </div>
    <div style="height:10px;background:var(--bg-2);border:var(--border);border-radius:2px;overflow:hidden">
      <div style="width:76%;height:100%;background:var(--ok)"></div>
    </div>
  </div>
  <div>
    <div class="between" style="margin-bottom:.28rem">
      <span class="sm">Depoimento — cliente</span>
      <span class="num sm muted">0,7x</span>
    </div>
    <div style="height:10px;background:var(--bg-2);border:var(--border);border-radius:2px;overflow:hidden">
      <div style="width:14%;height:100%;background:var(--bad)"></div>
    </div>
  </div>
</div>
<p class="xs mt">Acima da linha de empate (1,0x) = investir mais. Abaixo = gastou mais do que trouxe.</p>
```

Sempre inclua a legenda de leitura abaixo. Gráfico sem "como ler" é decoração.

---

## 4. Antes/depois

Duas colunas, a da esquerda deliberadamente feia (é o problema), a da direita limpa (é a solução).

```html
<div class="cols">
  <div class="card" style="opacity:.72">
    <span class="tag">O jeito antigo</span>
    <h3 class="mt-s">Planilha e achismo</h3>
    <ul class="list neg mt">
      <li>Métricas soltas, difíceis de cruzar</li>
      <li>Decisão por impressão, não por lucro</li>
      <li>Horas analisando pra chegar em nada</li>
    </ul>
    <div class="panel mt" style="display:flex;gap:1.5rem">
      <div><div class="xs">ROAS</div><div class="num" style="font-size:1.2rem">0,68</div></div>
      <div><div class="xs">Lucro</div><div class="num" style="font-size:1.2rem;color:var(--bad)">−23%</div></div>
    </div>
  </div>
  <div class="card hi">
    <span class="tag on">O jeito novo</span>
    <h3 class="mt-s">Decisão guiada por lucro</h3>
    <ul class="list check mt">
      <li>Dados cruzados: custo, margem, retorno</li>
      <li>Campanhas separadas por zona de decisão</li>
      <li>Gargalos priorizados por impacto</li>
    </ul>
    <div class="panel mt" style="display:flex;gap:1.5rem">
      <div><div class="xs">ROAS</div><div class="num" style="font-size:1.2rem">2,8x</div></div>
      <div><div class="xs">Lucro</div><div class="num" style="font-size:1.2rem;color:var(--ok)">+42%</div></div>
    </div>
  </div>
</div>
```

---

## 5. Funil

Largura decrescente proporcional ao número. Cada etapa carrega a taxa e a meta.

```html
<div class="stack" style="gap:.4rem">
  <!-- width proporcional ao volume; nunca menos de 18% pra continuar legível -->
  <div style="width:100%;border:var(--border);border-left:3px solid var(--accent);padding:.75rem .95rem;background:var(--surface)">
    <div class="between"><span class="sm">Impressões</span><span class="num">3.642.890</span></div>
  </div>
  <div style="width:74%;border:var(--border);border-left:3px solid var(--accent);padding:.75rem .95rem;background:var(--surface)">
    <div class="between"><span class="sm">Cliques no link</span><span class="num">95.172</span></div>
    <div class="xs">2,61% das impressões · meta ≥ 1,5% ✓</div>
  </div>
  <div style="width:52%;border:var(--border);border-left:3px solid var(--warn);padding:.75rem .95rem;background:var(--surface)">
    <div class="between"><span class="sm">Visitas à página</span><span class="num">56.107</span></div>
    <div class="xs" style="color:var(--warn)">58,9% de connect rate · meta 80% · −21 p.p.</div>
  </div>
  <div style="width:30%;border:var(--border);border-left:3px solid var(--accent);padding:.75rem .95rem;background:var(--surface)">
    <div class="between"><span class="sm">Compras</span><span class="num">66</span></div>
  </div>
</div>
```

O item em `--warn` no meio é o que faz o funil valer: ele mostra onde vaza. Um funil todo verde não ensina nada.

---

## 6. Depoimento em conversa

Substitui o card com aspas gigantes. Se o usuário tem print real, o print ganha — use o mock só quando não tiver.

```html
<div class="card flush" style="max-width:460px">
  <div class="row" style="padding:.8rem 1rem;border-bottom:var(--border)">
    <div style="width:34px;height:34px;border-radius:50%;background:var(--bg-2);border:var(--border)"></div>
    <div class="stack" style="gap:0">
      <strong style="font-size:.92rem">{{NOME}}</strong>
      <span class="xs" style="color:var(--ok)">online</span>
    </div>
  </div>
  <div class="stack" style="padding:1rem;gap:.6rem">
    <div style="max-width:88%;background:var(--bg-2);border-radius:var(--radius-lg);padding:.65rem .85rem;font-size:var(--t-sm)">
      {{FALA_1}}
      <div class="xs" style="text-align:right;margin-top:.2rem">09:22</div>
    </div>
    <div style="max-width:88%;background:var(--bg-2);border-radius:var(--radius-lg);padding:.65rem .85rem;font-size:var(--t-sm)">
      {{FALA_2}}
      <div class="xs" style="text-align:right;margin-top:.2rem">09:23</div>
    </div>
  </div>
</div>
```

Mantenha as marcas de fala real: erro de digitação, frase cortada, parêntese. Depoimento gramaticalmente perfeito parece escrito pela empresa — porque geralmente foi.

---

## 7. Tabela comparativa

Você × as alternativas. Sua coluna é a última e a única destacada.

```html
<table class="tbl">
  <thead><tr>
    <th></th><th>Curso</th><th>Dashboard</th><th>IA genérica</th><th style="color:var(--accent)">{{PRODUTO}}</th>
  </tr></thead>
  <tbody>
    <tr><td>Olha a sua conta real</td><td class="muted">×</td><td>✓</td><td class="muted">×</td><td style="color:var(--accent)">✓</td></tr>
    <tr><td>Diz o que fazer</td><td class="muted">×</td><td class="muted">×</td><td class="muted">×</td><td style="color:var(--accent)">✓</td></tr>
    <tr class="hi"><td>Prioriza por lucro</td><td class="muted">×</td><td class="muted">×</td><td class="muted">×</td><td style="color:var(--accent)">✓</td></tr>
  </tbody>
</table>
```

Regra de honestidade que também é regra de credibilidade: dê **pelo menos um ✓ para os concorrentes**. Tabela onde só a sua coluna tem check é propaganda, e o leitor sente.

---

## 8. Entregáveis como peças

Transforma "o que você recebe" em inventário técnico. Combina especialmente com o tema `blueprint`.

```html
<div class="between mt">
  <span class="eyebrow" style="margin:0"><span class="n">07</span> · O que você leva</span>
  <span class="xs num">5 peças · rev. 01 · folha 1/1</span>
</div>
<div class="grid g3 mt">
  <div>
    <div class="between"><span class="xs num">PÇ-01</span><span class="tag">Pronta</span></div>
    <h3 class="mt-s">{{NOME_DA_PECA}}</h3>
    <p class="sm mt-s">{{O_QUE_E}}</p>
  </div>
  <!-- repetir PÇ-02 … PÇ-05 -->
</div>
```

O código de peça e o "rev. 01 · folha 1/1" custam nada e são exatamente o tipo de detalhe que faz a página parecer feita por alguém.
