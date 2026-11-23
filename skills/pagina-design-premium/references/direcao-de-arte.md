# Direção de arte

Substitui a ideia de "escolher um tema". A skill **deriva** a direção de arte do nicho, do público e do registro emocional da oferta. Os arquétipos no fim do arquivo são pontos de partida, não um menu fechado.

## Por que derivar e não escolher

Uma página de tráfego pago para gestor e uma página de emagrecimento para mulher de 45 anos não podem sair do mesmo sistema. Não é só a cor: muda a família tipográfica, a curvatura, a densidade, o tipo de prova que convence, o ritmo. Skill que aplica o mesmo tema em tudo produz exatamente a uniformidade que faz a página parecer gerada.

---

## Fase 1 — Ler o briefing em quatro eixos

Antes de escolher qualquer cor, responda estas quatro perguntas. Elas determinam tudo o que vem depois.

**1. Registro emocional** — o que a pessoa sente ao chegar?

| Registro | Sinal no briefing | Consequência visual |
|---|---|---|
| Urgência / performance | dinheiro, escala, concorrência, tempo perdido | alto contraste, denso, sans condensada, accent vibrante |
| Alívio / acolhimento | cansaço, frustração acumulada, tentativas falhas | baixo contraste, arejado, serif humanista, paleta quente dessaturada |
| Autoridade / seriedade | investimento alto, decisão de carreira, saúde grave | neutro quase monocromático, serif de texto, muito espaço |
| Descoberta / entusiasmo | novidade, tecnologia, "ninguém faz isso ainda" | escuro, accent único vibrante, mono, mocks técnicos |
| Pertencimento | comunidade, identidade, "gente como eu" | fotografia de pessoas, cor viva, formas orgânicas |

**2. Público** — sexo, faixa etária, familiaridade digital

| Público | Ajuste |
|---|---|
| Feminino 30–55, tema de vida pessoal | Serif com contraste (Fraunces, Newsreader), curvatura maior (radius 12–20px), paleta quente e **colorida sem ser infantil**, formas orgânicas, foto de pessoa real. Evitar rosa-bebê e tipografia script |
| Masculino 25–45, negócios | Grotesk, radius baixo, paleta fria ou monocromática, números e dashboards |
| 55+ | Corpo em 17–18px mínimo, contraste AAA, botões maiores, menos elemento por dobra |
| Técnico / dev | Escuro, mono presente, densidade alta, zero decoração |
| Misto / amplo | Neutro quente, serif de display + sans de corpo, deixar a foto carregar a identidade |

**3. Nível de prova disponível** — muda a arquitetura, não só o visual

- **Tem número e print** → a página se organiza em torno de mocks e dados
- **Tem depoimento e história** → a página se organiza em torno de pessoas e narrativa
- **Não tem nada** → a página se organiza em torno de clareza e método. É a mais difícil e a que mais precisa de tipografia boa

**4. Ticket** — quanto mais caro, mais sóbrio. R$ 47 pode ser colorido e enérgico. R$ 15.000 não.

---

## Fase 2 — Construir a paleta

Nunca comece pela cor de destaque. Comece pelo **papel**.

### 2.1 O papel (o fundo)

Este é o token que mais define se a página parece cara. Branco puro `#FFFFFF` é o default de template e achata tudo.

| Papel | Hex | Quando |
|---|---|---|
| Creme quente | `#FBF6F0` `#FAF7F2` | acolhimento, saúde, feminino, educação |
| Off-white frio | `#F7F7F5` `#F6F7F8` | técnico, produto, B2B |
| Areia | `#F5F0E8` | artesanal, terroso, comida |
| Quase-preto | `#0B0C0E` `#101216` | tecnologia, noturno, premium jovem |
| Tinta profunda colorida | `#141018` `#0F1614` | quando o nicho pede cor mas não pode ser claro |

Regra: o `--bg-2` é o papel escurecido 3–5%, não uma cor diferente.

### 2.2 A tinta (o texto)

Preto puro `#000` quase nunca. Use um preto tingido da mesma família do papel:

- Papel quente → tinta quente: `#2A1F1C`, `#241E19`
- Papel frio → tinta fria: `#14161A`, `#0F1419`
- Papel escuro → tinta clara tingida: `#F2EDE6` (quente), `#F2F4F7` (frio)

Isso é sutil e é exatamente o tipo de coisa que separa design de template.

### 2.3 O destaque

Escolha **uma** cor. Ela precisa passar 4.5:1 contra o papel.

Famílias por registro:

| Registro | Família | Exemplos |
|---|---|---|
| Performance / dinheiro | azul elétrico, verde-limão sobre escuro | `#1B4DFF` `#3DF08C` |
| Acolhimento / saúde | terracota, cranberry, ocre, sálvia | `#B8484F` `#C4653A` `#4A6B52` |
| Autoridade | vinho escuro, azul-petróleo, quase-neutro | `#7A2233` `#1F4A54` |
| Descoberta | violeta profundo, âmbar | `#5B3DF0` `#F0A93D` |
| Pertencimento | coral, magenta profundo, laranja queimado | `#E0574F` `#B33A6B` |

### 2.4 As cores de apoio (isto é o que dá "colorido sem ser feio")

Aqui está a resposta para "quero algo colorido": **não é o accent que fica colorido, é o sistema de apoio.**

Defina 2–4 cores de apoio da mesma temperatura do papel, **todas dessaturadas para o mesmo nível** (é a dessaturação uniforme que faz um conjunto de cores parecer intencional). Elas não competem com o accent porque aparecem em áreas grandes e claras, nunca em elementos de ação.

Exemplo de sistema quente e colorido, para saúde/feminino:

```css
--accent:#B8484F;                       /* cranberry — só ação */
--sup-1:#E8D9C4;  --sup-1-ink:#6B4A22;  /* areia */
--sup-2:#D9E2D3;  --sup-2-ink:#3C5540;  /* sálvia */
--sup-3:#F0D8CE;  --sup-3-ink:#8A4433;  /* rosa queimado */
--sup-4:#E4DCEA;  --sup-4-ink:#4F3F63;  /* lilás acinzentado */
```

Como usar: cada seção temática, cada card de módulo, cada etapa de cronograma pega uma cor de apoio como fundo, com o `-ink` correspondente no texto. A página fica colorida e coesa, e o accent continua sendo só o botão.

Teste de sanidade: converta as cores de apoio para escala de cinza mentalmente. Se todas ficarem no mesmo tom de cinza, o sistema está certo.

### 2.5 Semânticos

`--ok` `--warn` `--bad` sempre existem, mas puxados para a temperatura do papel. Verde `#3C6E47` num papel quente, não `#00FF00`.

---

## Fase 3 — Tipografia

Sempre **dois** tipos (às vezes três com mono). Nunca um só.

### Pares que funcionam

| Par | Registro | Google Fonts |
|---|---|---|
| Fraunces + Inter | acolhimento, saúde, feminino, artesanal | `Fraunces:opsz,wght@9..144,400..800` + `Inter` |
| Instrument Serif + Inter | editorial, autoridade, high ticket | `Instrument Serif` + `Inter` |
| Newsreader + Inter | educação, conteúdo denso, 45+ | `Newsreader:wght@400..700` + `Inter` |
| Inter Tight + Inter + IBM Plex Mono | técnico, método, sistema | os três |
| Space Grotesk + Inter + Space Mono | tecnologia, IA, dado | os três |
| Bricolage Grotesque + Inter | jovem, energia, criativo | `Bricolage Grotesque` + `Inter` |
| Archivo + Archivo Narrow | esportivo, urgência, evento | os dois |

Fraunces merece nota: tem eixo óptico e eixo `SOFT`/`WONK`. Em tamanho grande use `font-variation-settings:'SOFT' 40,'WONK' 1` para ganhar a curvatura que faz a diferença no registro acolhedor.

### Regras de escala

- Contraste h2 ÷ corpo ≥ **2,4×**. Abaixo disso a página achata.
- Display sempre com `letter-spacing` negativo (−.02 a −.04em). Serif menos que sans.
- Labels sempre com `letter-spacing` positivo (+.12 a +.16em) e caixa alta.
- Corpo entre 60 e 72 caracteres por linha. Nunca mais.
- Público 45+: corpo em `1.0625rem` mínimo, `line-height` 1.7.

---

## Fase 4 — Curvatura e forma

O radius carrega registro tanto quanto a cor.

| Radius | Registro |
|---|---|
| 0–4px | técnico, blueprint, seriedade |
| 6–10px | neutro, produto |
| 14–24px | acolhimento, saúde, feminino, jovem |
| Orgânico (`border-radius:40% 60% 55% 45%/50% 45% 55% 50%`) | wellness, natureza, humano |

Formas orgânicas — blob de fundo, máscara de imagem, divisor curvo — funcionam **muito bem** no registro acolhedor e são péssimas no técnico. Quando usar, use com consistência: se a foto tem máscara orgânica, o card também tem.

---

## Fase 5 — O motivo

O elemento gráfico repetido que dá assinatura. É o passo que ninguém faz e que mais entrega acabamento.

| Motivo | Como aparece |
|---|---|
| Numeração de peça | `PÇ-01`, `rev. 02`, `folha 1/1` |
| Grade de progresso | quadradinhos preenchendo ao longo do scroll (ver heatmap em `prova-visual.md`) |
| Traço manuscrito | sublinhado SVG irregular sob palavras-chave |
| Selo circular | texto curvado em círculo, girando devagar |
| Fita / marquee | faixa horizontal em movimento com os pontos-chave |
| Divisor orgânico | onda SVG separando seções |
| Moldura de filete duplo | borda 1px + offset 4px, estilo papelaria |
| Marcador de etapa | círculo numerado conectado por linha vertical |

Escolha **um** motivo principal e use em 4+ lugares. Um segundo motivo é permitido se for discreto.

---

## Arquétipos de partida

Sistemas já resolvidos. Use como base e ajuste pela derivação acima — não como resposta pronta.

### `blueprint` — técnico, método, sistema
```css
--bg:#F7F7F5;--bg-2:#EFEFEC;--surface:#FFF;
--ink:#14161A;--ink-2:#4A4F57;--ink-3:#82888F;
--line:#DDDDD6;--line-strong:#C2C2B9;
--accent:#1B4DFF;--accent-ink:#FFF;--accent-soft:#E8EDFF;
--radius:4px;--radius-lg:6px;
```
Fontes: Inter Tight + Inter + IBM Plex Mono. Motivo: numeração de peça.

### `botanica` — saúde, bem-estar, feminino, transformação pessoal
```css
--bg:#FBF6F0;--bg-2:#F4EBE1;--surface:#FFF;
--ink:#2A1F1C;--ink-2:#5C4B44;--ink-3:#8E7C73;
--line:#E7DACD;--line-strong:#CDB9A6;
--accent:#B8484F;--accent-ink:#FFF;--accent-soft:#F7E5E3;
--sup-1:#E8D9C4;--sup-1-ink:#6B4A22;
--sup-2:#D9E2D3;--sup-2-ink:#3C5540;
--sup-3:#F0D8CE;--sup-3-ink:#8A4433;
--sup-4:#E4DCEA;--sup-4-ink:#4F3F63;
--radius:14px;--radius-lg:20px;
```
Fontes: Fraunces + Inter. Motivo: grade de progresso + divisor orgânico.

### `editorial` — autoridade, high ticket, mentoria
```css
--bg:#FBFAF7;--bg-2:#F2F0EA;--surface:#FFF;
--ink:#101010;--ink-2:#4B4B47;--ink-3:#8A8A82;
--line:#E0DDD4;--line-strong:#BFBBAE;
--accent:#7A2233;--accent-ink:#FFF;--accent-soft:#F5E7EA;
--radius:2px;--radius-lg:2px;
```
Fontes: Instrument Serif + Inter. Motivo: filete duplo.

### `terminal` — IA, tráfego, automação, dev
```css
--bg:#0B0C0E;--bg-2:#131519;--surface:#16181D;
--ink:#F2F4F7;--ink-2:#A2A9B4;--ink-3:#6B7280;
--line:#242830;--line-strong:#343A45;
--accent:#3DF08C;--accent-ink:#07120C;--accent-soft:#12291D;
--radius:6px;--radius-lg:10px;
```
Fontes: Space Grotesk + Inter + Space Mono. Motivo: indicador de status.

### `festival` — evento, lançamento, energia, público jovem
```css
--bg:#12100E;--bg-2:#1B1815;--surface:#211D19;
--ink:#FBF3E8;--ink-2:#BCAE9D;--ink-3:#847767;
--line:#2E2823;--line-strong:#463D35;
--accent:#F0A93D;--accent-ink:#1A1206;--accent-soft:#2D2213;
--sup-1:#E0574F;--sup-2:#4FA88A;--sup-3:#8C6FE0;
--radius:8px;--radius-lg:12px;
```
Fontes: Bricolage Grotesque + Inter. Motivo: marquee + selo circular.

---

## Entrega da direção de arte

Antes de gerar HTML, apresente ao usuário em 6 linhas:

```
REGISTRO      acolhimento / alívio
PÚBLICO       feminino 35–55, já tentou outras coisas
PAPEL         creme quente #FBF6F0
DESTAQUE      cranberry #B8484F  (+ 4 cores de apoio dessaturadas)
TIPOGRAFIA    Fraunces (display, SOFT 40) + Inter (corpo)
MOTIVO        grade de progresso de 12 semanas + divisor orgânico
```

Ele aprova ou ajusta uma linha. Só então gere.
