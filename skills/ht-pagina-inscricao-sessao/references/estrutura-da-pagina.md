# Estrutura e copy da página de inscrição da sessão 1a1

Referência da `ht-pagina-inscricao-sessao`. Estrutura reconstruída de uma página real do método. O modelo de
copy é um esqueleto do squad com [campos]; preencher com `03-sessao`, `01-pesquisa` e `06-entrega`.

## 1. Seções, na ordem

| # | Seção | Conteúdo | Regra |
|---|---|---|---|
| 1 | Topo (cor principal da marca) | Logo · título "para quem" com o nome da sessão gratuita em destaque · texto de apoio (horários liberados, o que a pessoa ganha) · frase-comando · botão CTA · microtexto de urgência leve | Título fala com o avatar; destaque de cor só nas palavras-chave |
| 2 | Para quem é esta sessão | 2 a 3 itens com ícone, cada um descrevendo um tipo de avatar elegível | Itens que afastam quem não é avatar |
| 3 | Formulário (âncora de todos os botões) | Título "preencha com suas informações" · campos · botão com texto de ação | Botão nunca "Enviar"; texto do benefício |
| 4 | Por que participar | 3 itens: o que a pessoa sai sabendo/decidindo | Benefícios da sessão, não do programa |
| 5 | CTA intermediário | Frase curta + botão ancorado | |
| 6 | Resultados | Título de prova · 4 a 5 prints no mesmo formato | Só reais e autorizados; sem prova, a seção sai |
| 7 | CTA final | Frase-comando + botão ancorado | |
| 8 | Rodapé | CNPJ · texto de LGPD · contato institucional | Sem telefone pessoal |

Vários CTAs ao longo da página: se o texto convencer no meio, a pessoa já clica e vai ao formulário.

## 2. Modelo de copy (esqueleto)

```
[TOPO]
Título: Para [avatar] que [situação ou desejo principal, nas palavras das 4 âncoras]:
        [Nome da sessão] gratuito(a)
Apoio:  Liberamos [N / alguns] horários na agenda [do expert / do nosso time] para [nome da sessão]: uma conversa individual
        para você [benefício principal: entender, decidir, enxergar] e sair com direcionamento para [resultado].
Comando: Clique no botão abaixo e solicite seu horário.
Botão:  Quero meu [nome da sessão]
Micro:  *Os horários desta semana são limitados.          (só se for verdade)

[PARA QUEM É]
Título: Para quem é [o/a nome da sessão]?
- Para [avatar tipo 1] que [condição de corte visível + desejo].
- Para [avatar tipo 2] que [já tem X e quer melhorar Y].
- (opcional) Para [avatar tipo 3].

[FORMULÁRIO]
Título: Preencha abaixo para solicitar seu horário
Campos: [e-mail] [WhatsApp] ([nome] opcional) ([melhor período] opcional) ([pergunta de corte] se houver segmentação)
Botão:  Quero receber meu [nome da sessão]

[POR QUE PARTICIPAR]
Título: Por que participar [do/da nome da sessão]?
- Para entender [se/como] [resultado] é possível no seu caso.
- Para enxergar [os pontos que travam / as oportunidades] na sua [área].
- Para sair com os próximos passos claros para [resultado].

[CTA intermediário]
[Frase curta: "Os horários são preenchidos por ordem de solicitação."]  Botão: Quero meu [nome da sessão]

[RESULTADOS]  (somente com provas reais e autorizadas)
Título: Veja resultados de quem já aplicou [o método do expert]
[4 a 5 prints, todos quadrados ou todos verticais]

[CTA FINAL]
Clique no botão abaixo e solicite seu horário.  Botão: Quero meu [nome da sessão]

[RODAPÉ]
[Razão social] · CNPJ [nº] · Ao enviar seus dados, você autoriza [o expert / a empresa] a entrar em contato pelo e-mail e
WhatsApp informados sobre [nome da sessão]. [Link da política de privacidade, se houver.]
```

## 3. Regras de copy

- Mesma palavra da promessa e mesmo nome da sessão usados na bio, nos stories, nas mensagens e no criativo.
- Sem preço, sem nome do programa, sem promessa do HT; a página vende a sessão.
- Escassez só real ("horários limitados" só se forem).
- Benefícios da sessão = o que ela de fato entrega (ler o roteiro em `03-sessao`).
- Copy de saúde, finanças e resultados: sem promessa de resultado garantido (compliance do anúncio e da página caminham
  juntos; o revisor confere).
- Se o funil tiver dois públicos (iniciante e experiente), a copy muda para cada um mesmo com o mesmo criativo; avaliar duas
  páginas ou duas versões de topo (padrão assumido, listado em "Assumi").
- Passar por `avoid-ai-writing` e `humanizer` antes da revisão.

## 4. Regras de design para o briefing

- Cores da marca (código hex), variação de tom para separar seções; não tudo na mesma cor, sem vermelho gritante.
- Botão com cor de destaque, texto de ação, cantos arredondados, bom espaço interno; o mesmo botão repetido nas seções.
- Imagens no tamanho original ou mantendo a proporção (nunca "cobrir" ou "esticar").
- Provas no mesmo formato. Ícones simples.
- Leitura no celular primeiro (a maior parte vem do Instagram).
- Título da aba = nome da sessão; favicon quadrado 32 x 32 px, simples, sem letra miúda.
