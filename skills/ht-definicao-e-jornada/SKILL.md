---
name: ht-definicao-e-jornada
description: 'Escreve o núcleo do Acelerador de Resultados (AR): tipo de AR, definição, ponto A e B, jornada do aluno (4 etapas x 4-5 passos), travas e níveis de resultado. Use para "define o AR do expert", "monta a jornada do aluno", "ponto A e ponto B", "cria os níveis". NÃO use para escolher o HT (ht-portfolio-e-escolha-do-ht) nem entregáveis (ht-entregaveis).'
---

# Definição do AR e jornada do aluno

## 1. Para que serve e o que entrega

O AR é um programa de acompanhamento, não um curso: o expert direciona, acompanha e dá feedback enquanto o aluno implementa.
Antes de pensar em entregável, preço ou bônus, a oferta precisa de um núcleo fixo: para quem é, que resultado entrega, por qual
caminho. Regra do método: quanto melhor a jornada, melhor a oferta (em um caso exemplar, oito horas de jornada e uma de
oferta). Esta skill fixa esse núcleo.

**Entrega** (um arquivo Markdown + a planilha opcional):
- `02-oferta/rascunhos/AAAA-MM-DD-definicao-e-jornada.md` com: tipo de AR e justificativa; definição final + 2 variações;
  ponto de partida e ponto de chegada; jornada (etapas e passos, um por linha, verbo no início); mapa de travas por passo
  (alimenta o `ht-entregaveis`); níveis de resultado (4 x 3); auditoria; "Assumi".
- `02-oferta/niveis-e-faixas.md` (proposta; vira vigente só na Aprovação 1).
- Opcional: a planilha "Jornada do Avatar" preenchida (passo a passo, partida e chegada, travas), via `anthropic-skills:xlsx`.

## 2. Antes de começar

1. Carregar `ht-protocolo` (regras comuns, decisões vigentes, pasta com dono). Conferir o pedido do Diretor.
2. Ler `experts/<slug>/ht/`:
   - `01-pesquisa/`: Market Fit (problemas, subnicho, avatar), Roma/promessa, 4 âncoras, voz do avatar, potencial HT,
     benchmark de casos do `ht-consultor-casos` (regra "nada nasce do zero").
   - `02-oferta/`: `portfolio.md` (qual HT foi escolhido; se não houver e o HT não for AR, devolver ao Diretor) e versões anteriores.
   - `00-plano/decisoes.md` (troca de regra do protocolo, se houver).
3. **Entradas obrigatórias**: avatar (quem compra e paga), resultado que ele quer, método do expert (como ele faz o resultado
   acontecer), legitimidade (resultado próprio ou de clientes). Se faltar, pergunto no máximo 2 coisas por vez, em linguagem simples (por exemplo as de baixo); sem resposta, faço a primeira
   versão com `[SUPOSIÇÃO: …]`:
   - "Qual o caminho que o expert faz com um cliente, do primeiro contato ao resultado, em 5 a 10 passos?"
   - "Que resultado concreto (número ou situação) clientes dele já tiveram?"
   - "Quem paga: o profissional, o dono da empresa ou a pessoa física?"
   Sem resultado próprio nem de cliente, o método não cria HT onde o expert não tem legitimidade (erro 6): a primeira versão sai marcada `[SUPOSIÇÃO: …]`, com a recomendação de mudar a direção, e isso entra no "Assumi" e
   no resumo da Aprovação 1 (ver seção 5).

## 3. Passo a passo

Ordem fixa: tipo → definição → ponto A e B → jornada → travas → níveis. Detalhes, modelos e exemplos em `references/`.

### Passo 1. Tipo de AR (5 min)
1. Classificar em **negócio** (avatar tem empresa; criar, gerir, escalar algo que dá lucro), **carreira** (evoluir ou mudar de
   área sem negócio próprio, ou profissional que se vê como carreira mesmo com consultório), **habilidade** (técnica que exige
   repetição, correção e evolução) ou **conquista pessoal** (público final; vida pessoal, bem-estar, relacionamento).
2. Critério: o que mais conecta com o avatar e para onde o expert leva o aluno. Pode misturar dois tipos com um dominante.
3. Registrar o efeito no preço: teto tende a cair na ordem negócio > carreira > habilidade > conquista (não é regra; passa
   para o `ht-preco-pagamento-e-garantia`).
4. Brainstorm de partida quando travar: "que resultado ele geraria dando atenção exclusiva a uma só pessoa?".
5. Dúvida real entre dois tipos não trava o trabalho: escolher o dominante, seguir, e listar a alternativa no "Assumi".
Exemplos de enquadramento: `references/definicao-framework-e-exemplos.md`, seção 2.

### Passo 2. Definição do AR (5 a 10 min por versão)
1. Escrever no framework oficial (texto completo e a versão longa da planilha em `references/definicao-framework-e-exemplos.md`, seção 1):
   programa de acompanhamento personalizado para **[avatar]** que querem **[resultado]**; nesse programa você terá
   direcionamento, acompanhamento e feedback durante o processo de **[etapas do veículo]**.
2. Três partes, três testes:
   - **Avatar** específico, que tem capacidade de investir e é quem paga (no B2B, o dono). Nichar pela dor e pelo perfil que o
     expert mais ajudou, não por profissão quando a dor é comum. Teste do subnicho: dos clientes que o expert já atendeu,
     quantos são desse recorte? Se o recorte corta a maior parte da base (caso de "mães engenheiras": 8 de 27 clientes), ele cobra um "imposto" alto de público; o recorte vira fala de conteúdo, não a definição. Delimitar o que muda
     a dor (faixa de faturamento, idade do filho, porte da empresa), porque a mesma profissão em outro momento tem outra dor
     (advogado que fatura até 4 mil quer técnica; acima de 20 mil quer não perder prazo e escalar).
   - **Resultado** atrativo e concreto (número ou situação reconhecível), sem palavra negativa, sem duas promessas, na
     linguagem do avatar. "Liberdade financeira" vira valor por mês. Teste da dor: o avatar pagaria R$ 10 a 20 mil para
     resolver isso? (referência, ajustar ao nicho).
   - **Veículo** em etapas específicas e compiladas, em segunda pessoa, que mostram o "como" (o método usa criar, vender, entregar,
     renovar). "Estudo, aplicação e desenvolvimento" é amplo demais: reprovado. Compilar em cerca de 3 blocos: cinco ou mais
     itens confundem na hora de explicar. Não escrever na frase o tipo de AR nem "de todos os nichos".
   - **Teste da fala**: a definição é o que o closer diz ao lead na venda. Ler em voz alta como fala: precisa ficar
     "gostosa de ouvir" e fazer o avatar pensar "eu tenho esse problema e isso resolve".
3. Verbo do expert é **acompanhar** ou **ajudar**, nunca "ensinar" (ensinar é o curso; acompanhar é o AR).
4. Conferir a atração do resultado contra o bolso do avatar (caso do vendedor de ouro): uma promessa de "ganhar
   R$ 10 mil/mês" só atrai quem ganha menos que isso; se o HT custa mais do que o avatar ganha, o avatar está errado.
5. Vender o que o cliente quer, entregar o que ele precisa: o resultado da definição é o desejo; o veículo carrega o que ele
   precisa fazer.
6. Entregar a definição final + 2 variações (uma mais curta, uma com outra formulação do resultado), cada uma com o teste aplicado.
Se usar IA: só depois de tentar à mão, e lapidar a saída.
Saída de IA colada sem revisão é erro comum.

### Passo 3. Ponto de partida e ponto de chegada (2 a 5 min)
1. **Ponto de partida**: o que o aluno precisa SER ou QUERER ao entrar (pré-requisito real: "ser terapeuta formado"; "querer
   construir para vender"). Não é desejo genérico nem dor solta.
2. **Ponto de chegada**: o resultado da definição já conquistado, específico, com número quando o avatar quer dinheiro
   ("faturou R$ 10 mil/mês com terapia"; "estúdio montado com clientes recorrentes"). É o **troféu**: o que o avatar mostraria
   como prova de que deu certo. Teste: "eu gostaria de chegar nesse lugar?"
3. Coerência: quem parte querendo X chega em X. Mudar o ponto A muda a jornada inteira.

### Passo 4. Jornada de sucesso do aluno (15 a 20 min no rascunho; refinar depois)
1. Dividir o caminho em **4 etapas** (3 ou 5 aceitáveis; nunca 19). Nomear em linguagem do aluno ("Fase 1: entender o seu
   cenário atual"), não no jargão do expert. Não misturar ciclo, fase, etapa e pilar na mesma jornada.
2. Dentro de cada etapa, **4 a 5 passos**. Cada passo:
   - começa com verbo e é ação **do aluno** (nunca entregável do mentor, nunca módulo ou tema de aula);
   - é **autoexplicativo** (lendo a frase, sabe-se o que fazer, sem precisar do "como");
   - é **auditável**: dá para responder sim ou não ("fez ou não fez"). Teste do juiz: alguém de fora, lendo o
     passo, consegue dizer se foi feito? "Fiz pela metade" é não.
   - não depende de existir o expert: teste "se você não existisse no processo, o que o aluno teria de fazer?".
     A ferramenta do expert vira entregável e a ação fica na jornada (ex.: "fazer a sessão de hipnoterapia" sai; "trabalhar as
     crenças limitantes sobre dinheiro" fica, e a hipnoterapia entra no `ht-entregaveis` como o que acelera esse passo).
3. Nível de detalhe: nem tutorial (o aluno faria sozinho só lendo) nem genérico (não entende o que fazer).
4. Formato: sequencial na maioria dos nichos; **por áreas** quando o avatar não segue ordem (ex. gestão de empresa: raio-x do
   negócio, financeiro, equipe, liderança). Em AR de negócio B2B, pode haver passos que outra pessoa da empresa executa.
5. Bifurcação (presencial ou online, canal A ou B) não vira "você escolhe": vira escolha do expert, tomada numa sessão
   individual. Recomendar 1 caminho principal + 2 ou 3 secundários, não "tudo".
6. Conferir ordem lógica (depoimento antes de escalar; organização financeira depois de começar a vender) e lacunas (faltou
   geração de demanda, faltou escala, faltou técnica). Lacuna mais comum: pular de "estruturar a oferta" para
   "fechar na reunião" sem a etapa de gerar demanda para a reunião.
   Coerência com a definição: toda etapa precisa caber na promessa e a promessa precisa aparecer nas etapas. Etapa que a
   definição não promete (liderança num AR de finanças) ou promessa que some da jornada (o "escolar" num AR de comportamento
   infantil) exige mexer numa das duas.
7. Teste final: lendo de cima a baixo, vê-se o avatar chegando no ponto de chegada? Pergunta-guia do estrategista: "se o aluno
   fizer todos esses passos, ele chega lá?"
8. IA de apoio: mandar só "Ponto de partida: ..." e "Ponto de chegada: ..." ao GPT de jornada (ou reconstrução própria), depois
   corrigir com o caminho real do expert ("não uso esse caminho, uso tal"; "falta escala"). O expert valida: desenhar a jornada
   costuma expor falhas do método, e isso é esperado.
Template, exemplos e erros: `references/jornada-template-e-exemplos.md`.

### Passo 5. Mapa de travas (onde o aluno trava)
Para cada passo, responder (perguntas por passo, em `references/jornada-template-e-exemplos.md`, seção 4):
onde trava, o que procrastina, onde acha que faz certo mas erra, onde falta coragem, onde errar custa caro, que recurso pronto
aceleraria, que conexão ajudaria. Classificar cada trava em um dos **4 problemas universais** do consumidor: compra e
não consome; consome e não implementa; implementa errado sem feedback; tem resultado e estagna. Marcar os 3 a 6 **pontos
críticos** (maior travamento ou maior custo de erro). Essa tabela é a entrada obrigatória do `ht-entregaveis`.

### Passo 6. Níveis de resultado (padrão do squad: 4 níveis x 3 graus)
1. 12 critérios, do mais simples (1º grau do nível 1) ao mais avançado (resultado acumulado), podendo passar do ponto de chegada.
2. Regras: nível é **resultado**, nunca atividade ("alterou uma crença", não "identificou"); consumo de conteúdo só nos primeiros
   graus, para dar movimento; 1º grau é uma atividade básica; redação que sirva a vários perfis do avatar; consistência entre
   "uma vez" e "30 dias seguidos"; critério de faturamento é acumulado na vida.
3. Nome temático do nicho (faixa, joias, estrelas); cada marco da jornada tende a virar um grau.
4. Uso a registrar: reconhecimento (faixa, certificado), próximo passo do aluno, calibrar cobrança, segurar o aluno, gatilho de
   upgrade, regra de quem entra no encontro presencial (ninguém chega faixa branca).
Modelo, exemplo e a alternativa de faixas por faturamento: `references/niveis-de-resultado.md`.

### Passo 7. Auditoria e entrega
Rodar a seção 6, corrigir, gravar e fazer o handoff (seção 7).

## 4. Regras inegociáveis do método

- AR é acompanhamento da implementação de um método; curso ensina e tira dúvida. A definição foca no **veículo**, não só no
  destino (Roma). Roma do projeto e definição do HT são coisas diferentes.
- Um avatar por AR. Dois avatares (ex.: projetista e dono de loja) pedem dois HTs; escolher um, de preferência o que paga mais
  e o que o expert mais ajudou.
- Jornada só com ações do aluno, com verbo, auditáveis. Entregável, módulo ou tema de aula na jornada reprova.
- Quem direciona o caminho é o expert. "Você escolhe" é proibido.
- Não criar HT onde o expert não tem resultado nem cliente com resultado.
- Nível de resultado é resultado. Consumo de aula só nos graus iniciais.
- IA ajuda, não decide: tentar à mão, depois lapidar a saída; nunca colar cru.
- Nada inventado: resultado e número de caso sem fonte viram `[FALTA: ...]`; número de referência só como referência ("conferir").
- Padrões que se aplicam: 4 níveis da planilha como padrão do squad; ciclo do programa de 11 a 13 meses (em geral 12) só como contexto do ponto de
  chegada (o resultado precisa caber em um ano de acompanhamento).

## 5. O que decido pelo padrão (e listo em "Assumi")

Não abro lote de perguntas. Decido pela recomendação, sigo e listo em "Assumi: X, Y, Z (é só pedir para mudar)"; vira oficial
na Aprovação 1:
- **Avatar quando há dois candidatos** (ex.: profissional x dono): escolho um pelo ticket, dor, legitimidade e volume e conto no "Assumi".
- **Tipo de AR quando a escolha muda o preço** (ex.: carreira x negócio para dono de consultório): escolho e conto no "Assumi".
- **Expert sem legitimidade clara** naquele resultado: recomendo mudar a direção para onde ele tem resultado (as outras saídas: ele vira
  estrategista e se busca um expert com resultado para parceria, ou não fazer o HT agora); vai no resumo da Aprovação 1. Resultado próprio que pode ter sido
  sorte de mercado (demanda que estourou num período) passa antes pelo teste de replicação: aplicar o método com 2 ou 3
  pessoas e ver se elas têm o resultado. Tema da moda sem nenhuma venda ainda (o exemplo de referência foi uma norma
  nova) não é legitimidade: empacotar o que o expert já fez.
- **Promessa com número** (faturamento, quilos): só com base; sem base, redijo sem número e listo em "Assumi".
- **Divergência entre caso validado do nicho e o método** (vinda do `ht-consultor-casos`): sigo o método e conto no "Assumi".
- **Sistema de níveis**: uso o padrão 4 x 3 da planilha; faixas por faturamento só se pedirem.

## 6. Critério de pronto e auditoria final

**Critério de pronto**
- [ ] Tipo de AR escolhido com 1 frase de justificativa e o efeito esperado no preço.
- [ ] Definição no framework, com avatar específico que paga, resultado concreto e atrativo, veículo em etapas compiladas, em
      segunda pessoa, verbo "acompanhar/ajudar"; + 2 variações.
- [ ] Ponto de partida = quem o aluno é ou quer ao entrar; ponto de chegada = resultado conquistado, com número quando cabe.
- [ ] Jornada com 3 a 5 etapas nomeadas na linguagem do aluno e 4 a 5 passos por etapa, um por linha, verbo no início.
- [ ] Mapa de travas por passo, com os pontos críticos marcados e o problema universal de cada um.
- [ ] 12 critérios de nível (4 x 3), todos resultado, nome temático.
- [ ] Toda informação do expert com fonte (arquivo de 01-pesquisa ou fala registrada); lacunas como `[FALTA: ...]`.

**Auditoria (erros típicos; corrigir antes de entregar)**
1. Definição mistura o "como" com o desejo (ex.: "organizar finanças" no lugar de "lucro").
2. Avatar híbrido ou genérico; profissão no lugar da dor; termo técnico fora do vocabulário do avatar.
3. Resultado com palavra negativa ("estagnada"), duas promessas, ou subjetivo sem tradução ("viver a vida que merece").
4. Veículo amplo ("estudo, aplicação, desenvolvimento") ou lista longa sem compilar.
5. "Ensinar" na definição.
6. Ponto de partida escrito como desejo; chegada sem número quando o avatar quer dinheiro; chegada que é meio ("montar o
   estúdio" em vez de "ter o estúdio com clientes").
7. Entregáveis listados como passos ("fazer diagnóstico", "conhecer o programa"); passos divididos em módulos; passo sem verbo;
   tema de aula como passo ("planejar a vida, recordar").
8. Jornada escrita do ponto de vista do aluno do aluno (quem o expert ensina a vender), e não do aluno do AR.
9. Mistura de ciclo, etapa e pilar; ordem ilógica; lacuna de etapa (demanda, escala).
10. "Você escolhe" em bifurcação.
11. Nível que é atividade; consumo de curso em grau avançado; graus inconsistentes ("uma vez" x "30 dias").
12. Saída de IA colada sem lapidar (jornada com um único ponto, passos genéricos).
13. Resultado prometido que o expert nunca gerou, ou resultado que não foi testado como replicável.
14. Ferramenta do expert escrita como passo do aluno (falha no teste "se você não existisse").
15. Etapa da jornada que a definição não promete, ou promessa da definição que não aparece na jornada.
16. Ponto de chegada sem número nem padrão de vida quando o avatar quer dinheiro ("liberdade geográfica" sem renda).
17. Subnicho que corta a maior parte da base atendida; faixa do avatar larga demais (ex.: filhos de 7 a 17 anos).

## 7. Saída e handoff

- Gravar em `02-oferta/rascunhos/` (definição e jornada) e `02-oferta/niveis-e-faixas.md` (proposta). Nada vira vigente sem OK
  do estrategista. Versão anterior vai para `02-oferta/historico/` com data. O `niveis-e-faixas.md` é saída **desta skill** mesmo
  quando o pedido não o cita: listar no bloco de entrega como artefato extra, para o Diretor incluí-lo na Aprovação 1.
- Contratação tardia (aluno que entra no meio do ciclo de 12 meses): o material não traz regra; registrar como lacuna e suposição
  no "Assumi" (`DA-n`), sem inventar prazo ou pró-rata.
- Bloco de entrega no formato do `ht-protocolo` (`ht-protocolo/references/estrutura-pasta-projeto.md`, seção 3.2), com a evidência marcada
  (o que o expert confirmou x o que foi inferido).
- Revisão: `ht-revisor-metodo-copy` (método e linguagem).
- Próximo: `ht-entregaveis` (recebe o mapa de travas e a jornada) → `ht-oferta-matadora`. Os níveis seguem também para
  `ht-arquiteto-entrega` (06-entrega) e `ht-gestor-renovacao` (upgrade).

## 8. Ferramentas de apoio (por nome)

- `anthropic-skills:xlsx`: preencher a planilha da jornada e dos níveis a partir do modelo.
- `avoid-ai-writing` e `humanizer`: limpar a redação da definição (sem cara de IA).
- `voice-builder`: quando já houver amostras de fala do avatar em 01-pesquisa, para escrever o resultado nas palavras dele.
- `niche-research`, `instagram-analise-estrategica`, `leitura-web`: só se faltar contexto de mercado para validar a dor
  (o dono da pesquisa é o `ht-pesquisador`; pedir via Diretor).

## 9. Limites

**Limites**: não existe modelo oficial de prompt de IA para definição de AR e jornada (o prompt de apoio da referência é reconstrução própria); a ordem e os cortes das faixas por faturamento variam, e o padrão é 4 x 3.
