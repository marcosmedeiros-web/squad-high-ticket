---
name: ht-palestras-e-pitch
description: 'Escreve e audita tudo que vai ao palco de um evento que vende HT: estrutura de palestra, talk de abertura, seeding e pré-pitch, pitch P1 a P10, repeat, re-pitch, palestra de decisões, downsell, laser coaching, break de vendas e ensaio de voz. Use para "escreve o pitch da imersão", "monta a talk de abertura", "faz a pré-pitch", "roteiro do re-pitch". NÃO usar para sessão 1a1 (ht-roteiro-sessao-1a1).'
---

# Palestras e pitch (palco do evento de venda de HT)

## 1. Para que serve e o que entrega

Transforma a oferta aprovada do expert em tudo o que é falado no palco de um evento que vende o HT, na ordem do método:
cada palestra com função na venda, o seeding plantando os entregáveis, a pré-pitch que vende sem parecer venda, o pitch
descritivo P1-P10, o pós-pitch que quebra objeções e os fechamentos. A venda começa na primeira palavra do evento.

**Entrega** (em `experts/<slug>/ht/05-eventos/<evento>/palco/`):
1. `grade-de-palestras.md`: tabela palestra × dia × palestrante × duração × 4 perguntas respondidas.
2. Um mapa mental por peça (Markdown em árvore ou link do MindMeister/Whimsical), na ordem: talk de entrada, palestras de
   conteúdo, pré-pitch, pitch, re-pitch/repeat, palestra de decisões, downsell, encerramentos.
3. Roteiro falado de cada peça (blocos com tempo, falas-guia, deixas de vídeo e de slide).
4. `briefing-de-slides.md` para o ht-diretor-arte (uma frase por slide no pitch; provas e fotos indicadas por slide).
5. `operacao-de-palco.md`: laser coaching (formulário e pré-seleção), break de vendas e mesa de fundo (papéis e posições), lobby
   ou breakout no online.
6. `checklist-de-ensaio.md` preenchido e `auditoria-palco.md` com o resultado da auditoria final.

## 2. Antes de começar

1. Carregar `ht-protocolo` (regras comuns, decisões vigentes).
2. Ler em `experts/<slug>/ht/`:
   - `02-oferta/` (oferta vigente aprovada: nome, definição, pilares, entregáveis, duração, preço, entrada, parcelas, bônus,
     garantia, dupla). **Nenhum número de preço sai de outro lugar.**
   - `05-eventos/<evento>/` (formato, big idea, grade de horários do produtor, público esperado, cronograma).
   - `01-pesquisa/` (avatar, 4 âncoras, objeções) e a árvore de objeções (ht-objecoes, em `03-sessao/` ou `01-pesquisa/`).
   - `06-entrega/` e o catálogo de provas e cases (ht-provas-e-cases): casos com evidência, Toque de Midas gravados, depoimentos autorizados.
   - `13-aprendizados/` de eventos anteriores (o que mudar; mudar uma variável por vez).
3. Entradas obrigatórias: oferta aprovada (Aprovação 1), formato e grade do evento (de ht-decisao-de-evento /
   ht-imersao-presencial / ht-imersao-aprendizado / ht-imersao-implementacao), lista de provas por entregável, quem fala.
4. Se faltar, não abrir questionário: assumir o padrão (o expert faz a talk e o pitch; variante de CTA pelo padrão da seção 5) e
   listar em "Assumi". Perguntar só o impossível de adivinhar, no máximo 2 coisas por vez e em linguagem simples (por exemplo:
   quais provas o expert tem autorização para mostrar). O resto vira `[FALTA: …]` ou `[SUPOSIÇÃO: …]`.

## 3. Passo a passo

### Passo 1. Avatar do evento e árvore de objeções
1. Ler o avatar de quem estará na sala (não o do produto): composição, nível, renda, tempo de casa, gênero. Resumo em 4 a 6 linhas.
2. Listar aspirações e objeções em duas colunas: para ENTRAR no programa e para EXECUTAR o resultado.
3. Montar ou atualizar a árvore de objeções: antes, durante e depois do pitch, e a palestra que quebra cada uma.
   Durante o pitch, cada entregável quebra uma objeção ("não sei por onde começar" → plano de ação). Depois: tempo, dinheiro,
   "não estou pronto", "vou tentar sozinho".
Detalhe: `references/pitch-p1-a-p10.md` seção 0.

### Passo 2. Grade de palestras
1. Distribuir o método em palestras por dia (P1 a P24 no presencial de 3 dias; menos no de 2 e 1 dia). Reservar: talk (dia 1),
   pré-pitch e pitch (dia 2), decisões e re-pitch (dia 3). No online de 1 dia: talk → conteúdo → CTA do laser coaching antes do
   almoço → conteúdo → pré-pitch → pitch → pausa → laser coaching → repeat → encerramento.
2. Para cada palestra, preencher as 4 perguntas (valor, objeção, entregável em seeding, prova em seeding) e a prioridade de
   função pela posição (tabela em `references/estrutura-de-palestra.md` seção 3).
3. Palestrante por afinidade; exercício ou perguntas e respostas entre blocos; online enxuga (manhã presencial vira cerca de 1h15).

### Passo 3. Palestras de conteúdo
Para cada uma: mapa mental com Roma → prova → procedência → conteúdo (um framework: Ajustes, Ação-segredo, Ação direta ou 4 Es)
→ fechamento; provas no nível mais alto disponível (Toque de Midas > vídeo > imagem > "no gogó"), todas com os 3 As.
Mapa mental aprovado antes de qualquer slide. Detalhe: `references/estrutura-de-palestra.md`.

### Passo 4. Talk de abertura e talks de entrada
Base: o modelo oficial de 7 pontos (recepcionar, reforçar a promessa, por que esta imersão, alinhar expectativa, antecipar
quem apresenta com o expert, antecipar a existência da mentoria, motivar com o "imagine"), escrito em bullets e falado com
história (cerca de 35 min no presencial; cerca de 45 min no online). Roteiro expandido do dia 1 com prova primeiro, versão online
com ciclo dos 4 Es, talk do dia 2 (insights, antecipação da tarde por causa do pitch) e do dia 3 ("meu time me disse", preparada
na reunião de objeções das 7h às 9h). Sem oferta, sem curso, sem networking. Detalhe: `references/talk-de-abertura.md`.

### Passo 5. Seeding e pré-pitch
1. Seeding em todas as palestras antes do pitch (menções desapegadas aos entregáveis e ao programa).
2. Pré-pitch de 1h30 a 2h30 logo antes do pitch, no Tipo 1 (apresentação de entregáveis: promessa "uma variável",
   história, a variável e seus pilares, cada entregável com o que é, benefício, como fazemos, prova e **como replicar**,
   fechamento com a soma dos pilares). Tipo 2 (case de aluno) e Tipo 3 (quick money) só se o Tipo 1 não encaixar.
   Em cada entregável: "como faço com meus alunos" → "como você faz sozinho na sua casa"; sem "o que não é"; a história é a da
   descoberta da variável, não a biografia do expert.
Referência: com pré-pitch o método foi de 7% para 14% de conversão. Detalhe: `references/pre-pitch-e-seeding.md`.

### Passo 6. Pitch P1 a P10
P1 anunciação → P2 vídeo de case (opcional) e silêncio → P3 história de quem faz o pitch e procedência do método (obrigatórios,
com similaridade com o avatar) → transição "ponta do iceberg" → P4 o que é → P5 resultados → imagine → P6 para quem é e não é
→ P7 entregáveis por pilar narrados como vivência → P8 duração em mês/ano → P9 valor, ancoragem e preço (entrada, parcelado, à vista) → P10 bônus
depois do preço, dupla, garantia de 02-oferta, CTA 1 fácil, escassez honesta, CTA 2 emocional, instrução da pausa.
Horário: dia 2 por volta de 16h30-17h (máx. 18h) no presencial; até 16h (máx. 17h) no online. Duração 1h a 1h30.
Quem faz a talk faz o pitch; expert faz o pitch. Uma frase por slide, um entregável por slide. O pitch de imersão não é o da sessão
1a1 copiado: abre com história e procedência do método e tem "para quem não é". Vídeos de prova produzidos antes do evento.
Detalhe, roteiro preenchível e vídeos: `references/pitch-p1-a-p10.md`.

### Passo 7. Operação pós-pitch
1. Break de vendas: no mínimo 2 h no presencial (30 min a 1h30 no online); equipe na mesa de fundo desde o meio do pitch;
   papéis (mentores, alunos como prova viva, navegadores na ficha, financeiro, flancos nas saídas).
2. Laser coaching (online e IMI): CTA e formulário antes do almoço, 3 a 5 pré-selecionados, depois do pitch, 1 h a 2 h, sem PPT,
   com o nome do entregável.
3. Repeat: "meu time trouxe estas dúvidas", nova CTA. Objeções do break registradas para o dia seguinte.
Detalhe: `references/laser-coaching-e-break-de-vendas.md`.

### Passo 8. Dia 3: re-pitch, decisões, downsell e encerramentos
Re-pitch (vídeo emocional, chamada emocional, acompanhamento e feedback, "chega de desculpas", desapego, pausa obrigatória de
40 min a 1 h, estendida se estiver vendendo) logo cedo;
palestra de decisões nos 3 As; vendas até o almoço de celebração e depois o "pinga-pinga"; downsell 2 a 3 h antes do fim, ticket
baixo (de preferência ingresso do próximo evento), página que "vira abóbora"; encerramentos de cada dia.
Detalhe: `references/repitch-decisoes-downsell-encerramentos.md`.

### Passo 9. Slides e ensaio
1. Briefing de slides para o ht-diretor-arte (regras visuais em `references/estrutura-de-palestra.md` seção 9).
2. Ensaio cronometrado e gravado de talk, pré-pitch e pitch; checklist de voz e entrega em `references/voz-ensaio-e-auditoria.md`.

### Passo 10. Auditoria e handoff
Rodar a auditoria de palco (seção 6) e a do `references/voz-ensaio-e-auditoria.md` seção 3; gravar resultado; passar para revisão.

## 4. Regras inegociáveis do método

1. Palestra só sobre o que gerou resultado, com prova; nada de teoria ou celebridade.
2. Mapa mental aprovado antes do slide; um documento por peça.
3. Dia 1 sem pitch; seeding sem oferta; nunca nome de curso ou produto barato no palco do HT.
4. Pré-pitch antes do pitch, com todos os entregáveis e "como replicar".
5. Pitch na ordem P1-P10: abre com emoção e indignação com a situação atual e segue racional e descritivo (padrão recomendado; a pessoa pode
   mudar em `padroes` do perfil), com história no começo e "para quem não é". Sem perguntas durante o pitch.
6. Preço, entrada, parcelas, bônus, garantia, dupla e duração copiados de `02-oferta/` (padrões recomendados: ordem de preço
   entrada, parcelado, à vista; garantia condicional e mensurável, ligada à execução; duração de 12 meses, ajustável de 11 a 13;
   dupla +50%; ancoragem 10x, depois 5x, depois a emocional). Divergência = vale `02-oferta/` e a diferença vai em "Assumi".
7. Escassez verdadeira: só a condição do evento e o início real do programa. "O programa começa no almoço" não significa
   "inscrição encerra no almoço": continua vendendo.
8. Downsell nunca de graça; muito pitch no fim tira valor.
9. Recusar venda só quando sincero; acordo e desapego sem a metáfora "em cima do muro" (padrão recomendado, quando a fala usar acordo).
10. Nenhum número de referência vira número do expert; caso e depoimento só com evidência e autorização (ht-protocolo, regras 3 e 14).
11. Proibido usar estrutura de aula ou pitch de outro método (lançamento pago de evento): fora do escopo deste squad.

## 5. O que a skill decide e lista em "Assumi"

Decidir pelo padrão ou pela recomendação, sem lote de perguntas, e listar em "Assumi: X, Y, Z (é só pedir para mudar)"; vira oficial na aprovação do plano.
- **Variante de CTA do pitch**: padrão do presencial de 3 dias = venda direta com entrada no evento (mais caixa no evento, exige
  mesa de fundo e financeiro); padrão do online de 1 dia para ticket alto = pitch para sessão de avaliação gratuita (mais
  sessões e quebra de objeção individual, exige time comercial na mesma semana); sessão de avaliação paga só quando há 150 a 200
  interessados e pouco time (com 30 a 40, não compensa). Escolher pelo formato do evento e listar em "Assumi".
- **Valor da entrada/aplicação no evento** se 02-oferta não trouxer (propor pelo padrão e listar em "Assumi"; fontes divergem; na sessão 1a1 o padrão é sinal de R$ 500 a R$ 1.000, até 10%).
- **Produto e preço do downsell**: propor pelo padrão e listar em "Assumi".
- **Expor alunos no palco** (case de aluno, depoimento, nome e número): exige autorização registrada; sem ela, não usa.
- **Garantia no pitch** além da garantia condicional de 02-oferta e qualquer bônus novo: só com nova versão de `02-oferta/`, que pede o OK simples na Aprovação 1.
- Oferecer produto mais barato no mesmo evento para "não perder interessado": padrão = não (recomendação do método); negociar parcelas.

## 6. Critério de pronto e auditoria final

**Pronto quando:**
- [ ] Avatar do evento e árvore de objeções registrados; cada objeção tem palestra dona.
- [ ] Grade com as 4 perguntas respondidas em todas as palestras.
- [ ] Mapa mental de todas as peças, aprovado antes dos slides.
- [ ] Talk sem oferta, com prova antes da promessa, combinados e procedências separadas.
- [ ] Pré-pitch cobre 100% dos entregáveis de 02-oferta com "como replicar".
- [ ] Pitch P1-P10 completo, números idênticos a 02-oferta, horário dentro do limite, CTA com caminho e equipe definidos.
- [ ] Operação do break, laser coaching (se houver) e repeat descritos com papéis.
- [ ] Dia 3 (re-pitch, decisões, downsell) e encerramentos escritos (se o formato tiver).
- [ ] Ensaio feito e checklist de voz preenchido; tempos reais anotados.
- [ ] Toda prova com fonte no catálogo de `06-entrega/provas/` (autorizada); nada inventado; `[FALTA]` listados.

**Auditoria (erros típicos dos laboratórios):**
1. Pitch sem história no começo. 2. Slide com textão ou várias frases. 3. Falta "para quem não é". 4. Pitch com cara de
sessão 1a1. 5. Pôr no pitch, como entregável, o que é a própria sessão de venda. 6. Nome sem ganho claro (sobretudo o da sessão do CTA). 7. Ancoragem financeira em nicho emocional.
8. Sigla solta. 9. Prova que é comentário, não resultado. 10. Pré-pitch sem "como replicar" ou com jogo de palavras que esconde a
rota. 11. Promessa da pré-pitch com 3 nomes no lugar de número compilado. 12. Talk que cita curso ou propõe networking.
13. Procedência do expert misturada com a do método. 14. Pitch tarde ou cronograma estourado. 15. "Carrinho fecha no almoço".
16. Downsell caro ou grátis, ou que não leva a um HT. 17. Expert lendo roteiro. 18. Pitch da sessão 1a1 copiado no evento.
19. Re-pitch sem pausa logo depois. 20. Pré-pitch com biografia do expert, "o que não é" ou sem o gancho "como você faz sozinho".
21. Obstáculo da talk sem caso de aluno (foto, nome, idade, cidade, número). 22. Depoimento em que o aluno vende ou com objeção
velada. Lista completa: `references/voz-ensaio-e-auditoria.md` seção 3.

## 7. Saída e handoff

- Grava em `05-eventos/<evento>/palco/` (dono: ht-roteirista-palco; o ht-produtor-eventos é dono da grade de horários e da
  operação geral do evento).
- Texto → **ht-revisor-metodo-copy** (método, copy, compliance de promessa). Slides → **ht-diretor-arte** / ht-designer →
  **ht-revisor-visual**. Vídeos de case/abertura → ht-designer. Operação do break → ht-produtor-eventos e ht-closer.
- O "Assumi" da seção 5 vai no bloco de entrega para o ht-diretor juntar ao resumo e ao "posso seguir?".
- Depois do evento: debrief em `13-aprendizados/` (objeções que explodiram, tempos reais, conversão por momento: pitch, dia 3,
  downsell) para a próxima edição.

## 8. Ferramentas de apoio (por nome)

- Slides: `gerador-slides`, `slides-uipm`, `anthropic-skills:pptx`, `designer-senior`.
- Vídeo de case e abertura: `testimonial-video`, `hyperframes`, `remotion`, `countdown-video`, `lower-thirds`, `caption-animation`.
- Texto: `avoid-ai-writing`, `humanizer`, `voice-builder` (voz escrita do expert).
- Ensaio e engenharia reversa de pitch gravado: `watch`, `transcrever-youtube`.
- Página da central da imersão com os botões do CTA: `designer-senior`, `publicar-pagina-cloudflare`.## 9. Limites (não inventar)

Voz e prosódia: só há conceito; o checklist de ensaio é compilado de orientações de pitch e não é método de fonoaudiologia (indicar
profissional). Os PPTs, mapas mentais e o "criador de pré-pitch" não vêm no pacote: os roteiros são reconstrução. Números do método
(7% → 14%, 1/3 das vendas no dia do pitch, cancelamento tipo 1, sessão paga a cerca de R$ 197, dois terços das vendas no dia 3) são
referência a conferir.
