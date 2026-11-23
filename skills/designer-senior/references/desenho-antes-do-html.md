# Desenho antes do HTML

Regra para **toda página nova ou redesenho**: landing, página de vendas, página de ingresso, página de inscrição, captura, obrigado.
Antes de escrever uma linha de HTML, existe um desenho da página (imagem de referência); eu construo conforme o desenho. Não vale
para micro-ajuste numa página que já existe (trocar um texto, um preço, um botão): aí o desenho é a própria página no ar.

Toda skill que cria página tem um **Passo 0** que aponta para cá. A regra mora só neste arquivo. Ela **nunca bloqueia**: sem
desenho, a página sai do jeito normal da skill (seção 6).

## 1. Copy primeiro

O desenho é feito em cima da copy aprovada. Se a skill da página tem diagnóstico e copy (escada de crenças, dobras, headline), isso
vem antes. Sem copy aprovada, sem desenho.

## 2. O brief do desenho

Crie a pasta do visual dentro do projeto da página (`<projeto>/visual/`) e escreva `brief.md` nela, com:

- **o que é:** tipo de página, produto, público, objetivo (agendar a sessão, comprar o ingresso, deixar o e-mail…);
- **as dobras, na ordem,** cada uma com o título, o subtítulo e o texto do botão reais (os textos longos podem ir resumidos);
- **o estilo:** se a skill tem layout fixo, cole a paleta em hex, as fontes e as regras inegociáveis do layout e escreva "dentro
  deste estilo". Se não tem, a direção de arte que a skill mandar (ou as cores da marca do expert);
- **onde vai rodar:** a maioria do tráfego é celular; diga se a página é pensada primeiro para o celular.

Nunca no brief: senha, token, chave, `.env`, CPF, CNPJ, e-mail ou telefone de cliente, nada que não vá estar na página pública.

## 3. Conseguir o desenho

Use o primeiro caminho disponível:

1. **Gerador de imagem já ligado neste ambiente:** peça 1 imagem (página de até ~6 dobras) ou 2-3 (página longa, cada imagem com um
   grupo de dobras), a partir do `brief.md`, e salve em `visual/visual-1.png`… com um `visual-notas.md` (hex, fontes, observações).
2. **Gerador que a pessoa já usa (ex.: ChatGPT):** entregue o prompt pronto, montado do `brief.md`, e peça para ela salvar a imagem
   gerada em `visual/visual-1.png`. Se ela preferir pular, siga para a seção 6.
3. **Referência que a pessoa mandou** (print, Figma, página que ela gosta): ela vira o desenho.

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

Capture a página feita na largura do desenho (página inteira) e no celular (390 px). Para capturar, a skill confere se há Playwright;
se não houver, pede OK e instala (`npm i -D playwright && npx playwright install chromium`, dizendo o que vai instalar):

```bash
npx playwright screenshot --full-page --viewport-size=1280,800 "file://$PWD/<projeto>/index.html" <projeto>/visual/captura-1280.png
npx playwright screenshot --full-page --viewport-size=390,844  "file://$PWD/<projeto>/index.html" <projeto>/visual/captura-390.png
```

Sem OK para instalar: abra a página no navegador, use o modo responsivo (390 px) e salve as capturas à mão.

Abra as imagens lado a lado e grave `visual/comparacao.md` com uma linha por item, `ok` ou `diverge: <o quê>`:

ordem das dobras · cor de fundo, acento e botão · hierarquia do título · composição da primeira dobra · cartões e botões · respiro ·
desvios por regra da skill (quais e por quê).

Cada `diverge` sem motivo de regra é ajuste: corrija e capture de novo (até duas voltas). Na entrega vão **as duas imagens**, o
desenho e a captura da página.

## 6. Sem desenho: a página sai do mesmo jeito

Não há gerador nem referência, ou a pessoa preferiu pular: faça a página do jeito normal da skill e diga numa linha
"Assumi: sem desenho de referência; segui a direção de arte da skill (é só mandar uma referência para eu ajustar)."
