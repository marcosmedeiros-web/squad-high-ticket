# Visual pelo Codex: o desenho vem antes do HTML

Regra do kit (5.3.9) para **toda página nova ou redesenho**: landing, página de vendas, página de ingresso, LPSG, Funil 8, low ticket,
captura, obrigado. Antes de escrever uma linha de HTML, o Codex desenha a página; eu construo conforme o desenho. Não vale para
micro-ajuste numa página que já existe (trocar um texto, um preço, um botão): aí o desenho é a própria página no ar.

Toda skill que cria página tem um **Passo 0** que aponta para cá. A regra mora só neste arquivo.

## 1. Copy primeiro

O desenho é feito em cima da copy aprovada. Se a skill da página tem diagnóstico e copy (escada de crenças, dobras, headline), isso vem
antes. Sem copy aprovada, sem desenho.

## 2. O brief do desenho

Crie a pasta do visual dentro do projeto da página (`<projeto>/visual-codex/`) e escreva `brief.md` nela, com:

- **o que é:** tipo de página, produto, público, objetivo (comprar o ingresso, deixar o e-mail…);
- **as dobras, na ordem,** cada uma com o título, o subtítulo e o texto do botão reais (os textos longos podem ir resumidos);
- **o estilo:** se a skill tem layout fixo (editorial bege e coral, neo-brutalista, linha escura interativa, avelloia…), cole a paleta
  em hex, as fontes e as regras inegociáveis do layout e escreva "dentro deste estilo". Se não tem, a direção de arte que a skill
  mandar (ou as cores da marca do dono);
- **onde vai rodar:** a maioria do tráfego é celular; diga se a página é pensada primeiro para o celular.

Nunca no brief: senha, token, chave, `.env`, CPF, CNPJ, e-mail ou telefone de cliente, nada que não vá estar na página pública.

## 3. Pedir o desenho

```bash
bash ~/.claude/head-turbo/bin/visual-pelo-codex.sh <projeto>/visual-codex <projeto>/visual-codex/brief.md [n]
```

`n` = quantas imagens: **1** (padrão) para página de até ~6 dobras; **2 ou 3** para página longa (cada imagem mostra um grupo de dobras).
Custo: ~1 a 2 minutos por imagem e uma parte da cota semanal do Codex (medido em 19/10/2026: 79 s para 1 imagem; a cota
subiu de 7% para 14%, numa conta que outros também usam). Mais imagens = mais cota.

O script faz sozinho, nesta ordem, e para no primeiro "não":

| Checagem | Como | Se falhar |
|---|---|---|
| Codex instalado | `command -v codex` | rc 3 |
| Codex com login | `codex login status` | rc 5 |
| Cota abaixo de 60% | `codex-cota.sh` (lê o último `rate_limits` em `~/.codex/sessions`). Leitura ilegível: uma chamada curta refresca, uma vez; continuou ilegível = não chama | rc 1 |
| Desenho entregue | PNG em `visual-1.png`… (ou a cópia em `~/.codex/generated_images`) + `visual-notas.md` | rc 4 |

O Codex roda com `-s workspace-write -C <pasta do visual>` (escreve só ali), com apps, plugins e busca web desligados. rc 0 imprime
`VISUAL_PRONTO` e o tamanho de cada imagem.

## 4. Construir conforme o desenho

Leia cada `visual-N.png` (abra a imagem, não só o nome) e o `visual-notas.md`. A página segue o desenho em:

- **ordem e número das dobras;**
- **cores:** fundo, texto, acento e botão (o hex das notas; se a nota divergir da imagem, vale a imagem);
- **hierarquia:** tamanho relativo de título, subtítulo e corpo; o que é maior, o que é menor;
- **composição:** lado da imagem, alinhamento, grade, cartões, respiro entre dobras, onde fica o botão;
- **tipografia:** a família das notas ou a mais parecida do Google Fonts;
- **estilo dos botões e cartões:** canto, borda, sombra, peso.

O que NÃO vem do desenho:

- **o texto:** é a copy aprovada, palavra por palavra (o gerador de imagem erra letra e inventa frase);
- **a imagem do desenho dentro da página:** ele é referência, não arquivo da página. Foto e ilustração seguem o caminho normal da skill;
- **as regras da skill:** fontes proibidas, contraste, acessibilidade, layout fixo, pacote de página publicada continuam valendo. Se o
  desenho bater com uma regra, a regra ganha e o desvio fica anotado na comparação.

## 5. Comparar com o desenho

Capture a página feita na largura do desenho (página inteira) e no celular:

```bash
bash ~/.claude/head-turbo/bin/renderizar-html.sh <projeto>/index.html <projeto>/visual-codex/captura-1280.png 1280x<altura>
```

`<altura>` = a da página: comece alto (ex. 6000) e baixe até não sobrar fundo vazio embaixo. **Celular:** o navegador sem tela não
abre janela com menos de 500 px (pedir 390 dá 500 em silêncio). Capture por uma moldura com a página num `iframe` de 390 px, centrado
numa janela de 500, e corte o centro:

```bash
cd <projeto> && printf '<!doctype html><body style="margin:0"><iframe src="index.html" style="width:390px;height:<altura>px;border:0;display:block;margin-left:55px"></iframe>' > .moldura390.html
bash ~/.claude/head-turbo/bin/renderizar-html.sh .moldura390.html visual-codex/.bruta.png 500x<altura> && sips --cropToHeightWidth <altura> 390 visual-codex/.bruta.png --out visual-codex/captura-390.png
```

(No Linux, sem `sips`: abra a `.bruta.png` assim mesmo; a página está entre 55 e 445 px.) Abra as imagens lado a lado e
grave `visual-codex/comparacao.md` com uma linha por item, `ok` ou `diverge: <o quê>`:

ordem das dobras · cor de fundo, acento e botão · hierarquia do título · composição da primeira dobra · cartões e botões · respiro ·
desvios por regra da skill (quais e por quê).

Cada `diverge` sem motivo de regra é ajuste: corrija e capture de novo (até duas voltas). Na entrega ao dono vão **as duas imagens**,
o desenho do Codex e a captura da página.

## 6. Sem Codex: a página sai do mesmo jeito

rc diferente de 0 **não para nada**: faça a página do jeito normal da skill. No fim da entrega, mande ao dono a linha
`SUGESTAO_PARA_O_DONO` que o script imprimiu, sem mudar. Ela já está em linguagem simples, diz o que ele ganha conectando o Codex
(um desenho da página antes, visual mais caprichado e com menos cara de IA) e o passo para conectar (`bash instalar-codex.sh` na pasta
do kit, com login na conta do ChatGPT dele; o plano grátis serve). Não pergunte se ele quer esperar: a página não depende do Codex.
