---
name: ht-provas-e-cases
description: 'Squad High Ticket / método FHT. Transforma a entrega do HT em prova: NPS por entregável com ação em nota baixa, formulário de solicitação com perguntas coringa, catálogo de resultados por aluno ligado às objeções, Toque de Midas (estudo de caso Antes → feedback do mentor → Depois, com mapa TM001 e instruções de corte, apresentado com os 3 As), entrevista e depoimento (inclusive em grupo), engenharia reversa do resultado de aluno para evoluir o método, prova quando o HT ainda é novo e reengajamento de aluno travado (consumo e termo de comprometimento). Use quando o estrategista disser "monta o Toque de Midas", "catálogo de resultados", "NPS dos entregáveis", "entrevistar aluno que deu resultado", "não tenho prova social", "aluno sumiu". NÃO usar para podcast e consultoria ao vivo (ht-conteudo-de-prova) nem para LPSG da Turbo.'
---

# Provas e cases do HT

## 1. Para que serve e o que entrega

O resultado do aluno é o resultado do expert, e no FHT ele é a matéria-prima de tudo: pitch, palco, Reels, página, renovação e
evolução do método. Esta skill monta o sistema que captura o resultado a cada entrega, comprova, organiza e transforma em caso
apresentável, e cuida do aluno que não está gerando resultado (porque é ele que derruba NPS, renovação e prova).

**Entrega** (conforme o pedido), em `experts/<slug>/ht/06-entrega/provas/`:
1. `nps-e-solicitacao.md`: formulários de NPS por entregável e de solicitação (com perguntas coringa) + protocolo de nota baixa.
2. `catalogo-de-resultados.xlsx` (ou base Notion): estrutura por aluno e por ação de venda, com ligação às objeções.
3. `toque-de-midas/TM0NN-<aluno>.md`: mapa do caso + roteiro do vídeo/palestra + instruções de corte + falas dos 3 As.
4. `entrevistas/<aluno>-roteiro.md`: roteiro de entrevista ou de depoimento em grupo.
5. `engenharia-reversa/<caso>.md`: análise, desconstrução, compreensão e o que muda no método.
6. `reengajamento.md`: lista de travados por consumo, plano e termo de comprometimento.
7. `plano-prova-ht-novo.md`: quando ainda não há caso.

## 2. Antes de começar

- Carregar `ht-protocolo`. Pedido do Diretor conferido.
- Ler: `02-oferta/` (promessa, jornada, faixas: a prova tem de provar ESTA promessa), `06-entrega/` (lista de entregáveis, NPS
  existente, gravações, base de alunos), `03-sessao/` (planilha de objeções de ht-objecoes, Central 1x1),
  `13-aprendizados/`.
- Entradas obrigatórias por pedido: para Toque de Midas, a gravação da interação mentor-aluno (não dá para gravar depois) e a
  evidência do resultado; para catálogo, a lista de alunos; para NPS, a lista de entregáveis. Se faltar, no máximo 3 perguntas:
  1. As sessões com alunos são gravadas e onde estão as gravações?
  2. Qual aluno teve o resultado (com evidência) e ele autorizou o uso?
  3. Quais objeções mais travam a venda hoje (para escolher qual caso montar primeiro)?
- **Autorização**: depoimento, imagem, nome e números de aluno só com autorização registrada em `06-entrega/provas/autorizacoes.md`
  (regra 14 do protocolo). Sem autorização, o caso pode ser usado internamente (método), nunca em material público.
  **Arquivo ainda não existe** (projeto novo, `06-entrega/` vazia): vale como "nenhuma autorização". Quem cria é o `ht-cs`
  (dono de `06-entrega/provas/`), com uma linha por pessoa: código (nunca o nome no material), o que foi autorizado (nome, rosto,
  número, depoimento), canal, data e onde está a prova do aceite. Até lá, prova de aluno em peça pública fica
  `[A CONFIRMAR COM ht-cs: autorização]` e o Diretor pede ao `ht-cs` a criação do arquivo.

## 3. Passo a passo

### Passo 1. NPS por entregável
Modelo completo em `references/nps-solicitacao-e-catalogo.md`.
- Ao fim de **cada** entregável (individual e em grupo): nome, e-mail, entregável, mentor, nota 0 a 10, motivo da nota, "maior
  sacada" (evita o "gostei de tudo"). Lives também citam incluir o faturamento do mês anterior.
- Indicadores: média dos últimos 30 dias e o NPS oficial (promotores − detratores). Referência do FHT: NPS acima de 95% e
  cancelamento de 34% para 15% depois de implantar (trilha 19, números de aula).
- **Nota abaixo de 6**: ligação no mesmo dia ou no seguinte, ouvir, resolver ou explicar, nova entrega se for o caso, pedido de
  desculpas. Reclamação é chance de vínculo.
- Quem não consome nada também recebe ligação.
- NPS alimenta a planilha de Problemas e Oportunidades e a oferta de renovação (ht-renovacao).
- Disparo do formulário: automação só com OK do estrategista (ht-gestor-automacoes).

### Passo 2. Formulário de solicitação com perguntas coringa
- Todo entregável individual é pedido por formulário (informações de preparo do mentor + perguntas coringa a partir do 2º
  entregável). Perguntas coringa do FHT (adaptar à métrica do nicho): progresso no objetivo, total faturado até agora, total
  investido em tráfego, maior desafio. Versão da planilha: "o que já evoluiu", "se já teve resultado, conte", "maior desafio".
- Resultado: a cada pedido o catálogo ganha um dado novo, sem esforço extra.

### Passo 3. Catálogo de resultados
- **Registrar** o resultado (mesmo sem prova ainda) e **catalogar a evidência** depois; não confundir os dois. Resultado sem
  evidência não vale como prova pública.
- Estrutura por **conta do aluno** (individual, dupla, trio): nicho, tipo de AR, ponto de partida, faturamento/métrica mês a mês,
  investimento, entregáveis consumidos e não consumidos, resumo do caso, link da pasta de evidências.
- Estrutura por **ação de venda** (o FHT registra cada ação separada): aluno, data, tipo de ação (1a1, imersão, live...), produto,
  investimento, resultado, link da evidência.
- Pasta de evidências por aluno no Drive, arquivos numerados e com nome autoexplicativo (prints, áudios, entrevistas em vídeo).
- Ligar cada caso às **objeções** que ele quebra (engenharia reversa: aluno com resultado → qual objeção ele tinha antes).
- Grupo só de resultados (Telegram citado) com print, áudio e fonte, e alguém responsável por catalogar tudo o que é celebrado.
- Erros da casa citados: linha duplicada por aluno, catálogo desatualizado.

### Passo 4. Toque de Midas (o caso padrão)
Roteiro e mapa em `references/toque-de-midas.md`.
1. **Gravar SEMPRE** as interações mentor-aluno (diagnóstico, reunião estratégica, análises). Sem gravação do feedback, não há
   Toque de Midas.
2. Escolher o caso pela objeção que mais trava a venda e pela força da evidência.
3. Mapa do caso **TM0NN + nome**: nicho, faturamento, histórico de consumo, resumo (mentores, ações recomendadas e implementadas,
   resultado, como replicar), passo a passo replicável, instruções de corte (arquivo, início e fim com as primeiras e últimas
   palavras do trecho).
4. Estrutura do vídeo/palestra em 3 partes: **Antes** (história, obstáculos, ponto de partida e números), **Feedback** (o corte da
   gravação em que o mentor dá a recomendação que gerou o resultado, com a evidência), **Depois** (como ficou, resultado).
5. Cada corte prova um ponto do resumo. Curadoria por alguém sênior; o editor só corta depois do roteiro aprovado. Fazer o melhor
   estudo primeiro e só depois condensar.
6. Duração: 7 a 15 min (6 a 7 em casos curtos).
7. Não aceitar só "cheguei em X" do aluno: precisa da evidência e do feedback gravado.
8. Apresentar com os **3 As**: Antecipa (o que prestar atenção, sem contar o fim), Apresenta (dá o play), Aterrissa (o que a pessoa
   devia extrair, ligado à objeção).
9. Usos: pitch (P2 do P1-P10, vídeo de case opcional), palestra de aluno na IMR, renovação ("faltam só dois metros"), Reels densos, transferência de
   autoridade ao mentor, página. Termômetro: se não há Toque de Midas disponível, o problema pode ser método ou engajamento.
10. Nunca falar mal de concorrente; mostrar o resultado gerado.

### Passo 5. Entrevista e depoimento
Roteiros em `references/entrevista-e-depoimento.md`.
- **Entrevista individual** (Zoom, fechada): qual resultado teve (o MESMO que o método promete, dito com número), qual era a maior
  objeção ou obstáculo antes, o que o expert disse que convenceu, onde travou, o que fez diferente, o que mais ajudou. Puxar a
  pessoa a repetir os trechos fortes. Microfone do expert mudo nas respostas (facilita o corte).
- **Depoimento em grupo** (desafio fev/26): Zoom com 3 alunas, sem anunciar a gravação como "depoimento"; nome, resultado, por que
  duvidava, como é a vida hoje. Editar intercalando as histórias; ter 3 a 4 histórias; cortar trecho que levanta objeção velada ou
  que parece pago.
- Entrevista pode ser ponto de contato da própria entrega. Também entrevistar na renovação ("o que faltou?").
- Produção do vídeo: `testimonial-video` (formato), com o roteiro desta skill.

### Passo 6. Engenharia reversa do resultado de aluno (evoluir o método)
Modelo em `references/engenharia-reversa-e-reengajamento.md`.
- Três fundamentos: **análise** (história, resumo do negócio, métricas), **desconstrução** (redes, captação, evento, oferta,
  produto), **compreensão** (por que deu resultado) → passo a passo replicável.
- Fonte: assistir às gravações das calls, ver o que foi implementado, entrevistar o aluno ("o que funcionou, o que não").
- Meta-análise periódica de todos os casos do catálogo (ordenar por resultado e estudar os maiores).
- Processo de evolução do método em 8 passos: ideia, testar, ensinar, acompanhar, analisar, engenharia reversa, formalizar,
  evoluir. O que muda vai para o manual de entregáveis e para a planilha de Problemas e Oportunidades.
- Ensinar só o que de fato está gerando avanço (premissa da live 058).

### Passo 7. HT novo, sem caso ainda
- Turma inicial pequena posicionada como piloto/pioneira; entrevistar os 3 primeiros resultados.
- Usar "resultados que eu tive" (do expert) no lugar de "resultados do programa".
- Sem nenhum resultado (nem do expert): não vender. Segurar com volume de conteúdo até o primeiro caso.
- Hierarquia de prova (do mais forte): Toque de Midas, vídeo, imagem, "no gogó" (desafio out/25).

### Passo 8. Reengajar aluno travado
- O problema real do HT é pagar e não consumir: sem consumo não há resultado nem renovação.
- Medir consumo médio por entregável (ex. citado: 1,8 de 12 análises) e criar projetos para subir.
- Contato proativo; "chacoalhão" sem grosseria; over delivery de entregável que ajuda e não vende.
- Aluno travado: **termo de comprometimento** com datas fechadas e acompanhamento semanal (caso citado: primeira ação do zero
  rendeu ~60 mil, conferir).
- Mentalidade (quando trava por comparação ou medo): foco, coragem, ambiente, resiliência; não concluir antes de 20 a 25 sessões
  (padrão do squad).
- Mensagens e termo saem como rascunho; envio só com OK do estrategista.

## 4. Regras inegociáveis do método

1. Gravar todas as interações com aluno (com aviso ao aluno, conforme o contrato do programa).
2. NPS em todo entregável, com motivo; nota baixa tem ação no mesmo dia ou no seguinte.
3. Prova é resultado do aluno com evidência; elogio não é prova (resultado, não elogio).
4. A prova tem de provar a promessa do HT (mesma métrica), não outra coisa.
5. Toque de Midas tem Antes, Feedback do mentor e Depois; sem o feedback gravado é só depoimento.
6. Nada inventado: número, caso, print, nome. Faltou: `[FALTA: …]`.
7. Uso público só com autorização registrada; dado sensível (CPF, faturamento) nunca sai da pasta do projeto.
8. Material para anúncio passa pelo compliance Meta (renda, saúde, antes/depois) no ht-revisor-metodo-copy.

## 5. Quando a decisão é do estrategista

Qual caso vai para material público e anúncio; uso de nome, rosto e números do aluno; contrapartida ao aluno pelo depoimento (se
houver); termo de comprometimento com efeito na garantia; categoria de prova em nicho de saúde (antes/depois). Formato: decisão
numerada com opções e riscos.

## 6. Critério de pronto e auditoria final

**Pronto quando**:
- [ ] NPS cobre 100% dos entregáveis, com motivo e "maior sacada", e há protocolo de nota baixa com responsável.
- [ ] Todo formulário de solicitação a partir do 2º entregável tem as perguntas coringa.
- [ ] Catálogo separa registro de resultado e evidência; cada caso tem objeção ligada e link da evidência.
- [ ] Toque de Midas tem mapa TM0NN, corte do feedback identificado (arquivo, início, fim), roteiro em 3 partes e falas dos 3 As.
- [ ] Autorização registrada para todo uso público.
- [ ] Números marcados com fonte; nada inventado.

**Auditoria (erros típicos)**:
1. NPS só de "satisfação geral", sem entregável e sem motivo.
2. Nota baixa sem ligação.
3. "Gostei de tudo" aceito como resposta.
4. Catálogo com linha duplicada por aluno ou desatualizado.
5. Resultado sem evidência usado como prova pública.
6. Caso que não prova a promessa do HT.
7. Toque de Midas sem o feedback do mentor (vira depoimento comum).
8. Contar o fim antes do play (quebra o 3 As).
9. Editor cortando sem roteiro aprovado.
10. Depoimento com objeção velada ou cara de pago.
11. Aluno travado tratado com mensagem em massa em vez de 1 a 1.

## 7. Saída e handoff

- Grava em `06-entrega/provas/` (escreve o ht-cs; ht-arquiteto-entrega, ht-roteirista-palco e ht-gestor-renovacao leem).
- Roteiros, falas dos 3 As e textos → **ht-revisor-metodo-copy**. Vídeo e slides do caso → ht-designer / ht-diretor-arte →
  **ht-revisor-visual**.
- Casos para pitch e palco → ht-roteirista-palco (ht-palestras-e-pitch, ht-imersao-de-resultados). Casos para anúncio e Reels →
  ht-diretor-copy e ht-gestor-trafego. Automação de NPS → ht-gestor-automacoes (liga só com OK do estrategista).
- Mudança no método vinda da engenharia reversa → ht-arquiteto-entrega (manual) e Diretor.

## 8. Ferramentas de apoio

`testimonial-video`, `capcut-edit`, `caption-animation`, `lower-thirds`, `short-form-video`, `cortes-tiktok-turbo` (produção e cortes
do caso), `watch` e `transcrever-youtube-turbo` (achar o trecho do feedback na gravação), `anthropic-skills:xlsx` (catálogo),
`gerador-slides-turbo` (slides de prova), `humanizer` / `avoid-ai-writing` (textos), `ht-avaliacao-de-reunioes-por-ia` (gravação e
transcrição de 100% das reuniões).

## 9. Fontes e lacunas

**Fontes**: trilha 19 (RESUMO: NPS entregáveis, perguntas coringa, catálogo, Notion, 34% → 15%, NPS > 95%); lives FHT 001, 002, 011,
012, 015, 022 (Toque de Midas inteira), 025 (termo de comprometimento), 026, 028 (Toque de Midas, 3 As), 036 e 037 (acervo,
entrevista), 041 (engenharia reversa), 050, 053, 055, 058 (catálogo e meta-análise, transcrita hoje), 061 (engenharia reversa e
entrevistas, transcrita hoje); parte-B (curador de provas), parte-G (depoimento em grupo, 4 níveis de prova), parte-H (blocos de NPS,
reengajamento, catálogo, Toque de Midas, entrevista), parte-I (toque de Midas, 3 As, acervo, entrevista, primeiros casos,
engenharia reversa).

**Lacunas**: (1) o template do Notion do catálogo e o mapa mental do Toque de Midas não foram abertos (estrutura reconstruída das
falas); (2) os 8 passos de evolução do método só aparecem nomeados, sem detalhe de cada um; (3) não há script de autorização de
uso de imagem no material (o squad usa registro próprio); (4) números de caso (60 mil do termo, 34% → 15%, NPS > 95%) são de aula,
conferir antes de material público.
