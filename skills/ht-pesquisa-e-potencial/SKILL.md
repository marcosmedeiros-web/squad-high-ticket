---
name: ht-pesquisa-e-potencial
description: 'Abre todo projeto de HT: pesquisa o avatar (com ou sem audiência), monta Market Fit, âncoras e Roma, avalia potencial HT e legitimidade do expert e responde às objeções dele. Use para "esse expert tem potencial pra HT?", "pesquisa o avatar", "qual a Roma". NÃO use para escolher o HT (ht-portfolio-e-escolha-do-ht) nem para preço.'
---

# Pesquisa e potencial HT (etapa 0 da rota)

## 1. Para que serve e o que entrega

Responde, com evidência, a três perguntas antes de qualquer oferta: **existe gente no mercado do expert que precisa de ajuda
para implementar?**, **esse expert é capaz de gerar e acompanhar esse resultado?** e **quem é o avatar, na voz dele?**. É o
ponto zero do ciclo "criar" do método: tudo que sai daqui alimenta o portfólio, a definição do AR, o Raio-X e a sessão 1a1.

**Entrega** (em `experts/<slug>/ht/01-pesquisa/`):
1. `AAAA-MM-DD-dossie-pesquisa-e-potencial.md` no modelo de `references/template-dossie.md`, com: fontes e amostra da pesquisa,
   Market Fit completo, 4 âncoras (mínimo 5 cada, em 1ª pessoa), Roma (3 opções + a recomendada), média de preço do nicho,
   parecer de potencial (sim / ajustar direção / não agora, sem nota), objeções do expert com resposta, papéis e minuta de acordo
   (só a estrutura; números são do estrategista), benchmark de casos e lacunas.
2. `bruto/` com o material coletado (prints, exportações, respostas, transcrições), sem nome de lead em material público.
3. Planilha Market Fit (cópia do modelo de 4 abas, opcional) quando o estrategista quiser esse formato.

## 2. Antes de começar

- Carregar `ht-protocolo` (regras, decisões, pasta). Conferir o pedido do Diretor em `00-plano/pedidos/`.
- Ler: `00-plano/README.md` e `estado.md` (quem é o expert, nicho, o que já existe), qualquer coisa já em `01-pesquisa/`,
  `02-oferta/` se houver HT antigo, e qualquer pasta de cliente que você já tenha para esse expert em `<raiz_projetos>/<expert>/` (só leitura).
- **Nada nasce do zero**: pedir ao `ht-consultor-casos` o benchmark do nicho (ou nicho vizinho) antes de escrever o parecer.
  Se o banco ainda não cobre o nicho, usar `references/biblioteca-casos.md` e registrar "sem precedente no banco". Todo caso usado
  passa pelas 3 fases de engenharia reversa (análise, desconstrução, o que replicar) descritas no mesmo arquivo.
- Entradas obrigatórias. O que dá para tirar dos arquivos do projeto, tira; o que faltar vira, no máximo, 2 perguntas simples por vez
  (sem lote de opções). Sem resposta, faz a primeira versão com `[SUPOSIÇÃO: …]` e segue:
  1. **Quem é o expert e o que ele já fez** (formação, resultado próprio, resultado de clientes/pacientes com prova). Sem isso
     não há parecer de legitimidade: pergunte, em linguagem simples, "Que resultado comprovado o expert já gerou, para si ou para clientes?"
  2. **Que audiência e que dados existem** (perfil, lista, alunos, pacientes, curso já vendido, NPS, formulários). Pergunte
     "A que dados de audiência temos acesso (Instagram, lista, alunos, pesquisas)?" A resposta decide o modo A ou B; sem resposta, assuma
     o modo B e marque `[SUPOSIÇÃO: …]`.
  3. **Quem faz o quê no projeto** (o expert entrega? você ou sua agência é o estrategista? há outro sócio?). Se não estiver
     em `00-plano/`, assuma o padrão (o expert entrega, você é o estrategista) e liste em "Assumi".

## 3. Passo a passo

### Passo 1. Ficha de avaliação do projeto (30 min)
Preencher a ficha de 6 blocos da sessão de aprovação (`references/potencial-legitimidade-e-objecoes.md`, seção 4) com o
que já se sabe: dados básicos; ideia e histórico (já vendeu? quanto?); capacidade de cada envolvido e papel; comprometimento;
recursos e fluxo de caixa; potencial de faturamento **por último** (de propósito: ele atrai quem busca dinheiro fácil).
Lacuna vira `[FALTA: …]`, nunca suposição.

### Passo 2. Escolher o modo de pesquisa
- **Modo A, com audiência**: o expert tem seguidores engajados, lista, alunos, pacientes ou clientes. Coletar da audiência real.
- **Modo B, sem audiência** (ou audiência que não é o avatar): pesquisar por conversas com pessoas do avatar, lista de 50,
  primeiras sessões como pesquisa e fontes externas. Ter pouca audiência **não** reprova o projeto (os fundadores venderam com
  cerca de 500 seguidores).
- Os dois modos podem se somar. Roteiros, perguntas e quantidades: `references/pesquisa-com-e-sem-audiencia.md`.

### Passo 3. Coletar (modo A)
Fontes, na ordem do que mais rende (detalhe e regras de coleta no arquivo de referência):
1. **Clientes e alunos que já tiveram resultado**: entrevista individual gravada (o que fez decidir, o que foi difícil, o que
   funcionou, o que mais gostou). É a base da oferta e da renovação.
2. **Dúvidas recorrentes**: DMs, comentários, caixinhas de pergunta, chat de aula/live, WhatsApp de atendimento.
3. **Enquete e caixinha nos stories** feitas para a pesquisa (dor, faixa, desejo), com print em até 48 h.
4. **Formulários existentes**: NPS de live (nota 0 a 10 + "quer falar com o time?"), pesquisa na página de obrigado (resposta
   de cerca de 90% citada numa palestra, conferir), pré e pós-sessão, antes de evento, NPS pós-imersão.
5. **Dados de venda** (Hotmart/Central): quem comprou e quem não comprou; separar comprador de não comprador.
Ferramentas: a ferramenta do perfil que lê o Instagram do expert (por exemplo, a Graph API da Meta: lista de posts e insights por
post, só leitura) para achar os posts com mais comentários; texto dos comentários e DMs vem por exportação ou print fornecido pelo
estrategista; `instagram-analise-estrategica` para leitura do perfil; `transcrever-youtube` ou `watch` para lives e
aulas gravadas do expert.

### Passo 4. Coletar (modo B)
1. **Lista de 50** potenciais clientes nas 6 fontes da aba 3 do Market Fit (profissional, social, grupos, eventos, redes, alunos)
   mais prospecção fria (Google Meu Negócio, LinkedIn). Ela serve para pesquisa e depois para a sessão 1a1 (`ht-slg`).
2. **Conversas de descoberta** com 5 a 10 pessoas do avatar dessa lista (roteiro no arquivo de referência). Objetivo: ouvir as
   palavras dele (caso da fisioterapeuta de escoliose: a promessa mudou para a palavra que os clientes usavam).
3. **Pesquisa externa**: perguntas reais de busca (AlsoAsked, planejador de palavras-chave, busca do YouTube em aba anônima),
   concorrentes e **média de preço dos produtos digitais do nicho** (`niche-research`, `leitura-web`).
4. **As primeiras sessões 1a1 são a pesquisa que valida**: o método manda vender em 1a1 antes de ir de um para muitos porque
   cada sessão mostra objeção e ajusta a oferta. Registrar isso como próximo passo, não como lacuna.

### Passo 5. Market Fit (aba 2 da planilha)
Detalhe, rótulos e exemplos: `references/market-fit-e-ancoras.md`.
1. **Matriz CS**: até 10 problemas que o expert tem **certeza** que resolve e até 10 que **supõe** (sem filtro, sem pensar em
   promessa). Cada item de certeza precisa de uma prova ou de um caso; sem prova, desce para suposição.
2. Escolher os **3 principais** da coluna certeza, cruzando com a frequência na pesquisa.
3. **Nicho e subnicho** (subnicho dá menos concorrência e autoridade mais rápida; não precisa acertar de primeira).
4. **Avatar**: idade, gênero, estado civil e profissão/renda (os dois últimos só se fizer sentido), mais as 6 perguntas de dores
   e desejos, sob a ótica de **quem decide e paga** (dono, não operador). Se quem paga não é quem consome (pais que pagam o
   vestibular do filho), registrar os dois.
5. **Resumo do avatar** em 1 a 2 frases, escrito antes da Roma.
6. **Dor passa no teste "acorda pensando nisso?"**; problema que o avatar não sabe que tem é entregável, não dor.

### Passo 6. 4 âncoras
Dores, desejos, objeções e oportunidades, **mínimo 5 de cada, em 1ª pessoa, na frase do avatar**, cada uma com a fonte (print,
resposta, entrevista) ou marcada "hipótese". Dor não é ação nem solução; "preciso de alto investimento" é objeção. A IA
pode acelerar, com curadoria; nunca colar saída de IA sem fonte.

### Passo 7. Roma (promessa do projeto)
Framework: **Ajudo [avatar] a [resultado]**. Escrever 3 opções e recomendar 1. Regras: destino, não veículo (exceto quando o
veículo é o desejo); palavras do avatar; número, prazo ou faturamento só com base; trocar termo vago ("liberdade") por algo
palpável; entre duas promessas, preferir a de resultado mensurável para público que já paga caro.
A Roma do projeto não é a definição do AR (essa é da `ht-definicao-e-jornada`); no HT a estrutura da oferta pesa mais que a Roma.

### Passo 8. Parecer de potencial (sem nota, sem fórmula)
Aplicar os **4 critérios** e a legitimidade (`references/potencial-legitimidade-e-objecoes.md`):
1. Existe público que precisa de **ajuda para colocar em prática**, não só aprender? (cadeia: muitos desejam, muitos ensinam,
   muitos compram, muitos não conseguem sozinhos.)
2. O expert é **capaz de gerar o resultado** que promete? Legitimidade = chegou lá **ou** levou outros a chegar, com prova.
3. É **capaz de acompanhar** essas pessoas até o resultado?
4. Tem **comprometimento** para executar?
Depois: **direção** (o que acelera: negócio, carreira, habilidade ou conquista; muitas vezes a direção certa é contraintuitiva,
como enxugar em vez de acrescentar), **recursos e fluxo de caixa** (plano que se autofinancia) e, por último, potencial de
faturamento. A combinação decide: ideia boa sem comprometimento = não; ideia fraca com pessoa forte e comprometida = mostrar
caminho (outra direção, ou a pessoa como estrategista e outro como mentor). Saída: **sim / ajustar direção / não agora**, com os
motivos e o que precisaria mudar. Se faltar legitimidade, o parecer é "não agora" (não criar HT em área sem resultado).

### Passo 9. Média de preço do nicho
Levantar 5 a 10 produtos digitais do nicho com preço (curso, mentoria, consulta) e registrar a média com fonte. **Não define o
preço do HT** (isso é `ht-preco-pagamento-e-garantia`, sob o padrão recomendado de 5x a 10x a média, validado em 20 sessões); só entrega o dado.

### Passo 10. Objeções do próprio expert
Listar o que o expert diz ("meu nicho não dá", "meu público não tem dinheiro", "não tenho audiência", "não sou famoso", "não estou
pronto", "não tenho tempo", "vou começar com um produto barato", "é coisa demais para entregar") e responder cada uma com o
argumento do método e uma evidência do banco de casos. Investigar a objeção real (medo, insegurança) antes de responder. Roteiro
de respostas: `references/potencial-legitimidade-e-objecoes.md`, seção 5.

### Passo 11. Papéis e acordo
Definir quem é **mentor** (método e resultado, o "motor") e quem é **estrategista** (vendas, marketing, operação), mais executor
e consultor quando houver. Montar a **estrutura** do acordo por escrito: funções, metas, responsabilidades, quem decide o quê,
um produto por vez. Divisão de lucro, pró-labore e prazo são do estrategista (seção 5).

### Passo 12. Montar o dossiê e rodar a auditoria (seção 6)

## 4. Regras inegociáveis do método

- Sem legitimidade (resultado próprio ou de clientes, com prova), **não se cria HT** naquela direção. Conhecimento não é capacidade.
- Potencial não se mede com nota ou fórmula; avalia-se caso a caso.
- Audiência, fama e autoridade **não** são pré-requisito; resultado e capacidade de acompanhar são.
- Quem paga HT é o **mais comprometido**, não o mais rico (Pareto do avatar). Nunca descartar nicho por "público sem dinheiro"
  sem antes olhar modalidade de pagamento (é do `ht-preco-pagamento-e-garantia`).
- Avatar e Roma vêm da voz do avatar: cada âncora tem fonte ou é marcada hipótese. Saída de IA colada sem curadoria é erro comum.
- Um projeto e um avatar por vez; nicho único até o programa ter 5 a 10 clientes. Dois avatares viram dois HTs
  (decisão na `ht-portfolio-e-escolha-do-ht`).
- HT não é venda de horas nem curso com plantão: o parecer já sinaliza quando a ideia do expert é "mais conteúdo".
- Padrões aplicáveis: preço do HT = 5x a 10x a média do nicho, validado no teste de 20 sessões (a média de preço levantada aqui
  alimenta essa conta; o estrategista pode mudar em `padroes` do perfil), regra 8 do protocolo (nada nasce do zero).

## 5. O que decido pelo padrão e o que vai para a Aprovação 1

Não abro lote de perguntas. Decido pela recomendação, sigo e listo em "Assumi: X, Y, Z (é só pedir para mudar)"; o que pesa de
verdade (seguir ou não com o expert, acordo, Roma) vai no resumo da Aprovação 1, como um "posso seguir?" simples, com a minha
recomendação e uma linha de prós e contras:
- **Seguir ou não com o expert** quando o parecer é "ajustar direção" ou "não agora" (o padrão é seguir na direção com legitimidade;
  as saídas são pausar até haver resultado, ou o expert como mentor de outra direção, ou você como estrategista com outro mentor).
- **Acordo expert x estrategista (ou agência)**: divisão de lucro, fixo x variável, prazo, quem paga tráfego e equipe.
- **Qual Roma** entre as opções, quando duas têm evidência parecida (recomendo uma e sigo).
- **Divergência com caso validado** do banco de casos (o caso faz diferente do método): sigo o método e conto no "Assumi".

## 6. Critério de pronto e auditoria final

**Critério de pronto**
- [ ] Modo de pesquisa declarado (A, B ou ambos) com **amostra contada** ("N comentários de M posts", "7 conversas").
- [ ] Matriz CS com prova em cada item de certeza; 3 principais escolhidos; nicho e subnicho.
- [ ] Avatar com demografia, 6 perguntas respondidas, resumo; pagador x consumidor quando diferirem.
- [ ] 4 âncoras com no mínimo 5 itens cada, em 1ª pessoa, cada um com fonte ou "hipótese".
- [ ] 3 Romas e a recomendada, passando no teste destino x veículo.
- [ ] Parecer pelos 4 critérios + legitimidade + direção + recursos, com sim / ajustar / não agora e os motivos.
- [ ] Média de preço do nicho com 5 a 10 fontes (ou lacuna declarada).
- [ ] Objeções do expert respondidas com evidência; papéis definidos; estrutura do acordo sem números inventados.
- [ ] Benchmark de casos citado com fonte e passado pelas 3 fases (o que fez, o que pesou, o que se replica), ou "sem precedente".
- [ ] "Assumi" no fim da entrega; bloco de entrega preenchido (evidência, números com fonte, o que assumi, lacunas).

**Auditoria final (erros típicos)**
1. Roma descreve o veículo (método) e não o destino; ou usa "pessoas" quando o avatar é específico.
2. Roma escrita antes do resumo do avatar (fica incoerente).
3. Avatar pela ótica do operador e não de quem decide e paga.
4. "Dor" que é ação, solução ou objeção; dor que o avatar não sente (nível de consciência avançado).
5. Âncora inventada, sem fonte, ou saída de GPT colada.
6. Parecer positivo sem legitimidade comprovada (cobaia de aluno) ou negativo só por falta de audiência ou de dinheiro do público.
7. Direção errada aceita por ser a primeira ideia do expert (casos viola caipira e professora de exatas).
8. Potencial de faturamento usado como primeiro critério.
9. Amostra pequena apresentada como o todo; número de referência usado sem "referência/conferir".
10. Dois avatares ou dois projetos tratados no mesmo dossiê como se fossem um.

## 7. Saída e handoff

- Grava em `01-pesquisa/` (dono: `ht-pesquisador`); bruto em `01-pesquisa/bruto/`, dado identificável em `01-pesquisa/privado/`.
- Revisão: `ht-revisor-metodo-copy` (método e texto). Depois o Diretor leva o parecer ao estrategista.
- Próximos: `ht-portfolio-e-escolha-do-ht` (qual HT, ordem) e `ht-definicao-e-jornada` (definição do AR, ponto A/B); a lista de
  50 segue para `ht-slg`; a média de preço para `ht-preco-pagamento-e-garantia`; as âncoras para `ht-reels-com-cta` e
  `ht-aula-semanal`. A pesquisa é metade da **Aprovação 1** (a outra é a oferta).

## 8. Ferramentas de apoio (por nome)

`niche-research` (mercado e concorrência), `instagram-analise-estrategica` (leitura do perfil e dos posts),
`leitura-web` (páginas de concorrentes), `transcrever-youtube` e `watch` (lives, aulas e entrevistas gravadas),
a ferramenta do perfil que lê o Instagram (só leitura), `voice-builder` (voz do avatar a partir das falas coletadas),
`anthropic-skills:xlsx` (cópia da planilha Market Fit), `avoid-ai-writing` e `humanizer` (revisão do texto do dossiê).

## 9. Limites

**Limites**: não há questionário oficial de pesquisa de avatar nem roteiro oficial de entrevista de descoberta (os de `references/pesquisa-com-e-sem-audiencia.md` são modelos do squad, marcados); a taxa de 90% de resposta da página de obrigado é referência de palestra (conferir); a leitura do Instagram pela API não traz texto de DMs e pode não trazer o dos comentários (precisa de exportação ou print); o banco de sacadas do `ht-consultor-casos` ainda não existe.
