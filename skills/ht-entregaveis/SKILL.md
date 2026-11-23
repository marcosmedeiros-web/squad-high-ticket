---
name: ht-entregaveis
description: 'Desenha os entregáveis do Acelerador de Resultados: cardápio nos 4 pilares, nome autoral, quantidade "até N" com condição, conta de horas, escala e SNA de 5 semanas. Use para "quais entregáveis?", "monta o cardápio do AR", "isso escala?", "faz o SNA". NÃO usar para roteiro de condução (ht-entregaveis-1a1, ht-entrega-em-grupo) nem para preço (ht-preco-pagamento-e-garantia).'
---

# Entregáveis do AR

## 1. Para que serve e o que entrega

O entregável é o que o aluno recebe para executar a jornada mais rápido. O valor do AR está no acompanhamento (direcionar,
fornecer recursos prontos, destravar, dar feedback), não no volume de coisa. Esta skill transforma a jornada e o mapa de travas
num cardápio enxuto, vendável e escalável: cada entregável existe porque resolve um ponto da jornada, é descrito de forma que o
lead entende na hora, e é prometido em quantidade que o expert consegue cumprir.

**Entrega**: `02-oferta/rascunhos/AAAA-MM-DD-entregaveis.md` com:
1. Matriz jornada x entregável (qual passo ou etapa cada entregável acelera, e com qual função).
2. Cardápio por pilar: nome autoral, o que é, benefício, quantidade "até N", condição de solicitação, quem entrega.
3. Conta de horas e capacidade (teórico x consumo esperado) e o limite de alunos por estrutura de time.
4. O que fica de fora agora (prometer depois) e o que vira overdelivery.
5. Esboço do SNA de 5 semanas (se o SNA entrar no cardápio).
6. Auditoria e linha "Assumi".
Opcional: planilha da oferta (aba ENTREGÁVEIS) preenchida.

## 2. Antes de começar

1. Carregar `ht-protocolo`. Conferir o pedido do Diretor.
2. Ler `experts/<slug>/ht/02-oferta/`: definição, jornada e **mapa de travas** (saída do `ht-definicao-e-jornada`). Sem jornada
   formalizada, monto antes a primeira versão dela pelo `ht-definicao-e-jornada`, marcada como suposição: entregável sem jornada sai "de paraquedas".
3. Ler `01-pesquisa/` (dores, objeções, casos parecidos do `ht-consultor-casos`) e `06-entrega/` (o que o expert já entrega hoje,
   time disponível, materiais prontos). **`06-entrega/` vazia** (projeto novo, sem aluno no squad): o que o expert já entrega sai
   da pasta dele fora de `ht/` (materiais, programa que já vende) e de `01-pesquisa/`; o que não estiver lá vira
   `[A CONFIRMAR COM ht-arquiteto-entrega]` (time e capacidade) ou `[SUPOSIÇÃO: ...]`. Não bloqueia o desenho dos entregáveis.
4. **Entradas obrigatórias**: jornada + pontos críticos; o que o expert já faz com clientes (sessões, materiais, grupos);
   quanto tempo por semana ele tem para entregar; se há time (mentor, navegador). Não abrir questionário: assumir o padrão do squad (horas por semana
   pela capacidade padrão, sem time, 10 alunos no primeiro ciclo) e listar em "Assumi". Perguntar só o que for impossível de
   adivinhar (por exemplo, "Que materiais prontos ele já tem?"), no máximo 2 coisas por vez e em linguagem simples.

## 3. Passo a passo

### Passo 1. Entender o ciclo do acompanhamento (aplicar em todo entregável)
Todo AR repete 4 movimentos em cada coisa que o aluno executa:
1. **Direcionar** de forma personalizada o que, como e quando fazer (às vezes é dar menos informação: "do curso de 300 horas,
   agora só este módulo").
2. **Fornecer recursos pré-construídos** (modelos, templates, mensagens prontas, planilhas): o aluno erra menos.
3. **Destravar** obstáculos de forma passiva (o aluno pede) e **ativa** (o time vai atrás de quem sumiu ou travou sem pedir).
4. **Analisar** o que foi executado e recomendar melhorias.
Extra: gerar conexões entre pessoas (ambiente).

### Passo 2. Cruzar jornada x travas x entregáveis
1. Para cada ponto crítico do mapa de travas, perguntar: qual movimento do ciclo falta aqui? Antes, durante ou depois da execução?
2. Não há regra de "um entregável por passo": um entregável pode acelerar uma etapa inteira (no método, o diagnóstico resolve a
   etapa de criação); três entregáveis podem servir a um passo só (bootcamp + drive + checklist para "construir os elementos de
   venda").
3. Pergunta-pivô: "se o programa custasse 10 vezes mais, o que o expert entregaria?" Revela o que move o resultado (80/20).
4. Começar pelo mínimo que cobre os pontos críticos. Montar a matriz:

| Etapa / passo | Ponto crítico? | Entregável | Função (direcionar, recurso, destravar, analisar, ambiente) | Momento (antes, durante, depois) |
|---|---|---|---|---|

### Passo 3. Escolher no cardápio dos 4 pilares (mínimo 1 por pilar; ninguém usa o cardápio inteiro)
Cardápio completo, com benefício, como replicar, nomes e quando não prometer: `references/cardapio-4-pilares.md`.
- **Direcionamento** (clareza do próximo passo): diagnóstico, plano de ação, SNA. O diagnóstico entra em todo produto (dez/25);
  plano de ação e SNA podem existir juntos, só um deles ou fundidos (há expert que só entrega o documento, sem a reunião). O
  normal é diagnóstico e plano em sessões separadas (analogia do médico: consulta, exames, depois a receita); fundem quando um
  questionário prévio (modelo do Raio-X do método) colhe os dados e a primeira reunião só confirma e já faz o plano (jun/26 SP).
  O questionário enviado logo após a compra também acalma o aluno que acabou de pagar alto. Plano de ação: prometer 1 com
  revisões quando solicitado, ou "até N" se ele é feito por trimestre ("até 4"), porque depende de o aluno cumprir.
  Diagnóstico é entregável de quem já comprou; não confundir com a sessão 1a1 de venda (erro de dez/25).
- **Implementação** (tudo para executar): área de membros, reunião estratégica, bootcamp/implementation day, drive, navegador.
- **Acompanhamento e Feedback** (antes, durante, depois): check-up (antes), real time (durante), análise individual (depois),
  laboratório (grupo), documento de feedbacks, plantão de dúvidas (só com volume).
- **Ambiente** (o diferencial que ninguém copia): comunidade, encontro exclusivo de alunos (canal de renovação), desafio,
  área de parcerias.
Prioridade do método: **análise depois da execução** é o entregável que mais faz o aluno evoluir e vender, e obriga o aluno a
agir.
Profissional complementar (designer, tráfego, psicólogo, nutricionista) entra como consultoria pontual "até N", sem trocar o
método do expert.
Equilíbrio individual x grupo: só entregável individual dá personalização mas não gera ambiente nem escala; oferta sem nenhum
entregável um-para-muitos foi apontada como falha no laboratório de dez/25. Em AR de negócio B2B, considerar um entregável que
o time do aluno também consome (alinhamento da metodologia para a equipe, jun/26 SP).
Análise sempre diz **análise do quê**: um entregável "análise individual" com os temas que podem ser pedidos (oferta, rede
social, atendimento, técnica) dimensiona melhor que vários entregáveis estreitos (exercícios).

### Passo 4. Escrever cada entregável nos 4 campos (+2 operacionais)
Modelos e exemplos: `references/redacao-de-entregavel.md`.
1. **Nome autoral**, do nicho ("Scanner de performance", "Plano de rota", "Mesa do Conselho", "Drive Necessaire"). Nome criativo
   leva explicação ao lado; para o lead entender o programa sem estudar, prefira nomes conhecidos com um toque do nicho
   ("Reunião de diagnóstico de carreira"). Nunca o mesmo nome para coisas diferentes; nunca jargão do método ("SNA") para o lead.
   Se o programa tem nome de marca, derivar os nomes dos entregáveis dele reforça o branding (dez/25).
2. **O que é**: literal, com formato, canal e duração ("uma sessão individual no Zoom de até 1h20 para..."). Na hora do pitch o
   lead não conhece o entregável.
3. **Benefício**: específico, escrito para o aluno (não para o mentor), ligado à dor ("você sai com a oferta pronta para vender").
4. **Quantidade "até N"**, nunca frequência (padrão do squad). Quer entregar um por mês? Escreve "até 12". Frequência fixa só
   em encontro de grupo (ex.: data do encontro anual). Entregável em grupo recorrente (laboratório, plantão) vai como "N por
   ano" ou "ao longo do programa, conforme agenda", nunca "mensal" ou "semanal": feriado e dezembro quebram a promessa (dez/25,
   jun/26 SP). Quando o método exige presença semanal do aluno, a cadência vai no plano de ação e no SNA, não no texto da oferta
   (jun/26 SP). Quantidade de análise acompanha o esforço: análise de 3 minutos por áudio pode ser mais generosa; a que exige
   sentar e estruturar, menos (dez/25). O N ideal só aparece com 1 a 2 anos de dados de consumo; até lá, dar um a mais a quem
   está executando não quebra nada.
5. **Condição de solicitação**: "quando você executar X, pode solicitar Y". Ex.: a cada estratégia de venda
   executada, solicitar uma análise individual de até 2h. Exceção sem condição: reunião estratégica. Condição leve (precisar) para
   não virar "ovo ou galinha". Logística (agendar por link, mandar a demanda antes) não entra no texto da oferta: lá ela parece
   barreira; o aluno descobre como pedir quando entra (jun/26 SP).
6. **Quem entrega** (expert, mentor, navegador, especialista) e **como se solicita** (formulário, prazo de resposta em dias úteis).

### Passo 5. Conta de horas, consumo e capacidade (escala)
Template e referências: `references/escala-e-conta-de-horas.md`.
1. Para cada entregável individual: horas teóricas por aluno = N x duração. Somar.
2. Aplicar o consumo esperado (sem dado próprio, usar a referência marcada "conferir": 20% dos alunos consomem 80%; numa mentoria
   citada, de até 12 análises a média consumida foi de 2 a 3; plantão recebe 5% a 10% dos alunos).
3. Converter em capacidade com o padrão do squad: expert sozinho até 20 alunos; mentor 1:70; navegador 1:100.
4. Teste de escalabilidade: se todos consumissem tudo, o expert aguenta? Se não, trocar frequência por "até N" com condição,
   passar entregável para grupo (laboratório, bootcamp) ou para mentor/navegador com manual.
5. Peixe assado ("faço por você") nunca predomina no AR; no máximo como bônus com teto.

### Passo 6. Cortar o entulho e separar o que fica para depois
1. **Efeito PQP**: oferta com entregável demais assusta ("não vou dar conta", "vou usar só um pedaço"). Entregar o que o
   aluno precisa na hora que precisa. Menos entregáveis, mais claros; unir os repetidos.
2. **Não prometer o que ainda não existe** e depende de volume: comunidade geral, bootcamp gravado, laboratório e plantão com 1
   a 10 alunos. Com poucos alunos: grupo VIP com o expert (padrão do squad: WhatsApp até ~10 alunos, Telegram até ~150, Circle
   a partir daí; vender "comunidade", não a ferramenta; escolher a ferramenta que o avatar já usa, ex.: empresário que não está
   no Facebook). Encontro de alunos pode ser prometido para cerca de 12 meses depois da primeira entrada (o primeiro
   encontro de uma mentoria citada teve 12 a 13 pessoas); há mentor que só passa a prometer depois de ~15 alunos, para já marcar
   a data a um ano (jun/26 SP). Usar o primeiro (prometer já, para cerca de 12 meses) e listar em "Assumi" (seção 5).
3. Área de membros e drive podem ser vendidos antes de existirem desde que descritos como o que são: organizados a partir das
   gravações e materiais das próprias entregas. O que não puder ser cumprido, sai.
4. **Overdelivery** ("na gaveta"): o que se entrega sem prometer (plantão, plantão temático). Vira entregável só quando provar valor.
5. Não criar entregável de "plano de continuidade" que concorra com a renovação. Uma sessão final de
   conquista é o momento natural da oferta de renovação (`ht-renovacao`).
6. Overdelivery não aparece também no cardápio: se está nos dois lugares, sai de um (dez/25).

### Passo 7. SNA de 5 semanas (se entrar no cardápio)
Estrutura completa: `references/sna-5-semanas.md`. Plano de ação é o macro (mês a mês); o SNA é o micro (tarefa, prazo, como
executar, evidência, checkbox, barra de progresso). Criar uma vez e replicar; dar nome comercial claro para o lead.

### Passo 8. Auditoria e entrega
Rodar a seção 6. Gravar e passar adiante (seção 7).

## 4. Regras inegociáveis do método

- Entregável nasce da jornada e das travas, não de "encher linguiça". Arquitetura da oferta pensa primeiro em resultado, depois em venda.
- Mínimo um entregável por pilar; diagnóstico e plano de ação quase sempre presentes.
- Individual sempre "até N" com condição; frequência só em encontro de grupo (padrão do squad). Prometer frequência é "enfiar o HT no
  ralo": o expert vira refém da própria oferta e vende o tempo dele.
- Grupo e individual do mesmo tipo = dois entregáveis distintos.
- Real time só se puder cumprir; navegador sempre com prazo de resposta em dias úteis; plantão só com volume.
- Entregável que só serve ao mentor (boletim de avaliação) não é entregável; vira ferramenta interna ou planilha do aluno.
- Nada se constrói inteiro antes de vender: entregar o que existe, criar por demanda, gravar tudo.
- Gravar todo entregável individual (prova, "toques de Midas", acervo para a área de membros).
- Contrato ou modelo jurídico no drive: avisar que o aluno valida com o advogado dele.
- Diagnóstico: alvo de 1h20, teto de 2 h e parte 2 prevista (padrão recomendado; a pessoa pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`). Capacidade pelo padrão do squad. Comunidade pelo padrão do squad.

## 5. O que a skill decide e lista em "Assumi"

A skill decide pelo padrão ou pela recomendação, sem lote de perguntas, e lista em "Assumi: X, Y, Z (é só pedir para mudar)"; vira oficial na Aprovação 1. Itens:
- **Quantidade N de cada entregável individual** quando mexe na capacidade do expert (ex.: análises até 6 ou até 12): usar o N que cabe na conta de horas.
- **Fundir ou separar diagnóstico e plano de ação** (uma sessão longa x duas sessões): padrão = separar.
- **Prometer ou não** encontro presencial, comunidade, real time e bootcamp no primeiro ciclo; para o encontro: padrão = prometer
  já, para cerca de 12 meses após a primeira entrada; alternativa (só se a pessoa pedir): prometer só depois de ~15 alunos, já com data (jun/26 SP).
- **Especialista terceiro na entrega** (custo e margem): padrão = sem terceiro; contratar um pede o OK simples ("posso seguir?").
- **Entregar via mentor desde o início** ou expert sozinho até 20 alunos: padrão = expert sozinho até 20.
- **Algo que o expert faz hoje por frequência** (ex.: reunião semanal já vendida a alunos atuais): propor como migrar sem quebrar promessa e listar em "Assumi".

## 6. Critério de pronto e auditoria final

**Critério de pronto**
- [ ] Toda linha do cardápio aponta para um passo, etapa ou ponto crítico da jornada (matriz preenchida).
- [ ] Pelo menos 1 entregável por pilar; diagnóstico e plano de ação presentes ou ausência justificada.
- [ ] Cada entregável tem nome, o que é (formato, canal, duração), benefício para o aluno, "até N", condição, quem entrega, como
      solicitar e prazo de resposta quando houver.
- [ ] Conta de horas teórica e com consumo esperado; capacidade em nº de alunos com o time atual.
- [ ] Lista do que não será prometido agora e do overdelivery.
- [ ] Nenhuma frequência fixa em entregável individual.
- [ ] Se há SNA: semanas, tarefas, evidência e nome comercial.

**Auditoria**
1. Entregável na jornada, ou jornada usada como lista de entregáveis.
2. Frequência ("mensal", "toda semana", "ativo de segunda a sexta", "intensivo") no lugar de "até N".
3. Mesmo nome para coisas diferentes; nome criativo sem explicação; jargão do método para o lead.
4. "O que é" sem formato e duração; benefício escrito para o mentor.
5. Pilar errado (encontro presencial em feedback; biblioteca fora de implementação) ou pilares duplicados.
6. Plantão e laboratório duplicados; plantão com poucos alunos; hot seat em turma pequena ou inexperiente.
7. Real time prometido sem capacidade de cumprir.
8. Comunidade, Circle, bootcamp ou laboratório prometidos com 1 aluno; Circle cedo.
9. Entulho (efeito PQP): entregáveis demais, consumo impossível.
10. Kit físico caro sem conta de custo e frete.
11. Navegador ou suporte sem prazo de resposta.
12. Entregável que serve ao mentor; plano de continuidade que mata a renovação.
13. Oferta não escalável: conta de horas estoura a capacidade.
14. Peixe assado predominante.
15. Oferta só com entregáveis individuais, sem nenhum um-para-muitos (dez/25).
16. Análise sem dizer do quê; vários entregáveis de análise que são o mesmo com tema diferente.
17. Logística de pedido no texto da oferta ("mediante agendamento e envio prévio da demanda") soando como barreira.
18. Entregável ao vivo sem duração escrita (gravado não precisa).
19. Mesmo item no cardápio e no overdelivery; dois entregáveis que só diferem pelo momento (mapa x rota, comitê x ciclo).
20. Diagnóstico confundido com a sessão 1a1 de venda.

## 7. Saída e handoff

- Gravar em `02-oferta/rascunhos/AAAA-MM-DD-entregaveis.md` (e a planilha, se pedida). Vira parte de `oferta-vigente.md` só no
  `ht-oferta-matadora`, com OK do estrategista.
- Bloco de entrega do `ht-protocolo`, com evidência (o que o expert confirmou que consegue entregar x inferido).
- Revisão: `ht-revisor-metodo-copy`.
- Próximo: `ht-oferta-matadora` (consolida a oferta). Depois da Aprovação 1: `ht-arquiteto-entrega` usa o cardápio para o manual
  de entregáveis, formulários de solicitação e roteiros (`ht-entregaveis-1a1`, `ht-entrega-em-grupo`, `ht-escala-da-entrega`).

## 8. Ferramentas de apoio (por nome)

- `anthropic-skills:xlsx`: aba ENTREGÁVEIS da planilha de oferta, conta de horas e o SNA.
- `avoid-ai-writing`, `humanizer`: redação de "o que é" e benefício.
- `anthropic-skills:docx`: versão em documento para o expert ler, quando o estrategista pedir.

