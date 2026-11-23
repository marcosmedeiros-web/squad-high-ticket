# Campanhas por canal (configuração de referência do método)

Cada bloco: objetivo, estrutura, configuração, nomes de exemplo e cuidados. Tudo sobe **PAUSADO**. Nomes no padrão de
`nomenclatura-e-planilha-d1.md`.

## A. Sessão 1a1 (captação contínua de leads)

Fonte: trilha 13 `RESUMO-trafego.md` §3.4 a §3.10, §4 etapas D e E, §5.4.

- Objetivo **Leads**, campanha **manual** (a automática não deixa escolher público), local de conversão **Site**, conjunto de
  dados = pixel da página, evento **Lead**. Orçamento diário. **Sem data de término** (a sessão é perpétua).
- Hierarquia do mais quente/menor para o mais frio/maior, excluindo os menores dos maiores para não concorrerem:

| Conjunto | Público | Exclui |
|---|---|---|
| 00 | visitantes da inscrição/site 180d | leads (obrigado 180d) |
| 01 | engajamento IG 365d | 00 e leads |
| 02 | semelhante 1% do engajamento 365d | 00, 01 e leads |
| 02 | interesses (3 a 5 do nicho) | 00, 01 e leads (não exclui o semelhante: abertos não se excluem) |

  A exclusão dos leads é acréscimo técnico (a aula cria o público de obrigado mas não o exclui).
- Exclusão pela setinha "Excluir este público" (só tirar da caixa de inclusão não exclui). Para criar 01 e 02, duplicar o
  conjunto anterior "com as configurações atuais" na mesma campanha e trocar nome e público.
- Orçamento: R$ 10/dia por conjunto no teste (regra do squad: orçamento no conjunto e exclusões em cascata). Atenção: a
  aula monta o primeiro conjunto com orçamento no conjunto (R$ 10) e depois **recomenda** orçamento na campanha (R$ 20) nas
  primeiras campanhas, porque ainda não se sabe qual público performa. Vale a regra do squad (padrão recomendado; o estrategista pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`:
  orçamento no conjunto no teste); a recomendação da aula fica só como contexto.
  Mínimo da Meta citado na aula: ~US$ 1 por dia por conjunto (R$ 6,14 no dia da gravação).
- Público Advantage: a aula deixa ligado no começo e manda testar desligado depois; com ele ligado, o Meta pode sair da
  segmentação. Para o conjunto 00 (público fechado), conferir a expansão desligada.
- Idade do avatar (exemplo de aula 25 a 60), Brasil, posicionamentos padrão com prévia conferida em story e feed.
- Anúncio: Página e IG corretos, carregamento manual, versões 9:16 e 1:1, CTA "Saiba mais", destino = página de inscrição
  (testar o botão), complementos do navegador nenhum, rastreamento com eventos do site em verde.
- Riscos a vigiar: orçamento concentrando nos públicos grandes; medir só Lead e não agendamento, comparecimento e venda.

Nomes de exemplo: campanha `[v1][LEADS][PREFIXO] [SESSAO1A1] [00-01-02] - 22.11.26` · conjunto
`00 | Visitantes | Inscrição sessão | 180d` · anúncio = CPF do criativo (`SES-VID-HOOKAUDITORIA-01`).

## B. Captação de imersão

Fonte: trilha 17 `RESUMO-parte-A` §3.3 a §3.5, §5.2 (via `parte-D`); FEV26 §3.8, §5.7, §5.8 e OUT25 aulas 7 e 8 (via
`parte-G`); FEV26 aula 36 (transcrição nova).

- Objetivo **Leads** (imersão gratuita) ou **Vendas** (ingresso); Site, pixel, evento Lead ou Purchase; maximizar conversões.
  A entrada do evento (gratuita, credencial ou paga) é decisão do estrategista por evento; mostrar prós e contras.
- Estruturas:
  - **LOW** (verba até ~R$ 5 a 10 mil): 00 públicos internos · semelhante (exclui internos) · interesses (exclui internos, não
    exclui semelhante).
  - **Segmentada** (acima de ~R$ 10 mil): cada público interno num conjunto próprio (seguidores, envolvimento, visitantes,
    lista de leads, vídeo 75%), mais semelhantes e interesses.
  - **Presencial**: um conjunto por região.
  - Variante FEV26 (alternativa a testar, não padrão): 1 campanha, 4 conjuntos (seguidores, envolvimento 365, semelhante 1%,
    interesses), 3 anúncios (1 imagem, 2 vídeos), sem exclusões, orçamento na campanha; foi mais barato naquela turma. Só
    contexto: no teste, o orçamento fica no conjunto (padrão recomendado; o estrategista pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`).
- Idade do avatar (FHT usa 35 a 55); posicionamentos automáticos; interesses 1 a 3 por conjunto (OUT25; o bootcamp da trilha
  17 põe vários do nicho juntos no LOW); melhorias automáticas do criativo desmarcadas; nome do anúncio = nome do criativo;
  redirecionador com UTMs; CTA "Saiba mais" (performou melhor).
- Orçamento no conjunto (trilha 17): verba diária do plano dividida igual entre os conjuntos (ex.: R$ 126 em 3 conjuntos de
  R$ 42); depois da primeira leitura, mover verba para o conjunto que performa.
- No LOW, o conjunto de semelhante exclui os internos; o de interesses exclui os internos mas não os semelhantes (excluir
  público grande limita demais a entrega).
- **Fim da campanha na hora do início da imersão** (trilha 17 e FEV26 citam isso; usar a hora do evento salvo pedido do estrategista).
- Distribuição de conteúdo durante a captação (trilha 17): só para quem já distribui; referência de ~20% da verba (ex.: R$ 600
  de R$ 3.000); quem não distribui põe tudo na captação.
- Pelo menos 5 criativos antes de abrir o segundo conjunto. Meta de produção da turma: 5 vídeos e 5 estáticos para começar.
- Duplicar conjuntos/anúncios e publicar tudo junto (seleção múltipla).
- Nome de exemplo do método: `IMI | MÊS | ANO | ONLINE | CADASTRO`; no squad, adaptar ao padrão de `nomenclatura-e-planilha-d1.md` (com o prefixo do perfil, se houver):
  `[v2][LEADS][PREFIXO] [IMI-ONLINE-MAR26] [LOW] - 22.11.26`. Fase (captação x distribuição) no bloco de estratégia.

## C. Perpétuo de ingresso

Fonte: trilha 17 `RESUMO-parte-B` §3.3 estratégia 2 e §5.2 (via `parte-D`). A oferta e a página do ingresso são da skill
`ht-venda-de-ingressos`; aqui só a campanha.
- Campanha contínua de Vendas para a página de ingresso, com criativo raiz completo (benefício, data, horário, onde, o que
  aprende) e variações (dor, desejo, quebra de objeção, história pessoal, encenação).
- Meta: custo de aquisição que ao menos empate o custo do evento (ingresso barato que vende o HT costuma valer mais que lucrar
  no ingresso).
- Proteção de checkout (nome, e-mail e telefone antes do checkout) para o comercial recuperar.
- Cuidado quando o expert está em outro lançamento: o criativo pode confundir.

## D. Aula semanal

Fonte: trilha 14 `RESUMO-aula-semanal.md` §5.11, §6, §7 (via `parte-C`); transcrição nova da Parte 2 do bootcamp.
- **Captação perpétua** (nunca para) para a página de inscrição da aula, evento Lead no obrigado. Página roda o tempo todo e
  fica no link da bio. Só Instagram/Facebook na operação FHT.
- **Remarketing** para o público de cadastrados, com 4 estágios de criativo: anúncio direto com foto do expert, dia e hora,
  local (live), promessa e botão de ativar notificação:
  1. genérico/"é {dia}" nos demais dias; 2. "é amanhã" na véspera; 3. "é hoje" no dia; 4. **replay** com thumb da aula passada.
  Exemplo de calendário para aula na terça: "é amanhã" na segunda, "é hoje" na terça, genéricos nos outros dias.
  **Conflito do replay**: a planilha fala em 2 dias após a transmissão; a Parte 2 mostra replay de quarta a domingo. Padrão:
  2 dias; estender se o estrategista pedir.
- Criativo raiz **sem data** (roda o ano inteiro), produção contínua (2 por semana dá mais de 100 no ano).

**Receita dos 4 estágios do remarketing** (montagem técnica do squad sobre a regra da aula; conferir a interface no dia):
- **Campanha**: objetivo **Reconhecimento** (`OUTCOME_AWARENESS`, otimização `REACH`), porque o público já é lead e o objetivo é
  lembrar, não captar. A captação da aula continua em Leads; Reconhecimento nunca é usado para captar. Orçamento no conjunto (ABO).
  Nome: `[YT][RECONHECIMENTO][PREFIXO] [AULASEMANAL-RMKT] [4-ESTAGIOS] - DD.MM.AA` (destino YouTube; `[v1]` se o destino for
  a página da aula).
- **Público** (os 4 conjuntos): cadastrados da aula (evento Lead do obrigado da página da aula, 90 dias, ou a lista do e-mail),
  expansão de público personalizado desligada (`targeting_relaxation_types` com `custom_audience: 0` e `lookalike: 0`), sem
  exclusão entre os conjuntos (a separação é por dia, não por pessoa). Idade e gênero abertos: o público já é o cadastrado.
- **Um conjunto por estágio**, com orçamento vitalício, data de término longa (ex.: 12 semanas) e **programação de anúncios por
  dia da semana** (a CLI aceita `--pacing-type day_parting`, mas não tem flag de programação, na versão conferida: a
  programação é feita no Gerenciador, ou via Graph `adset_schedule` com OK):
  1. `01 | RMKT | Genérico "é <dia>"`: os dias que sobram.
  2. `02 | RMKT | É amanhã`: a véspera da aula, o dia inteiro.
  3. `03 | RMKT | É hoje`: o dia da aula, da 0h até o horário de início.
  4. `04 | RMKT | Replay`: os 2 dias seguintes à aula (padrão; estender só se o estrategista pedir).
  Exemplo, aula na quarta às 20h: replay quinta e sexta; genérico sábado, domingo e segunda; é amanhã na terça; é hoje na quarta
  até 20h.
- **Anúncio**: foto ou vídeo do expert, dia, hora e "ao vivo no YouTube", promessa da aula e CTA para o link da live (ou da página).
  Destino YouTube: o link da transmissão agendada da semana troca a cada aula, então o anúncio aponta para o canal ou a playlist
  fixa, ou é atualizado toda semana (tarefa no cronograma, com OK). CPF no padrão `AS-RMKT-EHOJE-01`.
- **Verba**: dentro dos 20% de lembrete e replay da divisão de referência (lembrete 10%, replay 10% da verba das aulas), dividida
  entre os 4 conjuntos pela quantidade de dias de cada um; a conta aparece no plano, conjunto por conjunto, e fecha com o total.
- **Ler**: alcance e frequência por estágio e presença ao vivo e no replay da semana; frequência acima de ~3,5 no genérico =
  público pequeno, baixar verba.
- Públicos de distribuição: view de página, envolvimento 30d, view de vídeo, semelhantes de cadastrados, interesses.
- Divisão de verba de referência: 80% aulas (captação 80, lembrete 10, replay 10) e 20% distribuição (descoberta 70,
  relacionamento 30).
- Formulário de qualificação no obrigado: se o cadastro não é o avatar, achar o criativo que traz a pessoa errada e trocar.

## E. Distribuição de Reels (Turbinar)

Fonte: trilha 14 `RESUMO-funil-de-reels-parte2.md` §3.5 a §3.11, §4 passos 16 a 26, §5.5, §5.9, §7, §8.
- Escolher os **2 melhores** Reels pelo orgânico depois de 24 a 48 h (visualizações; o GPT "FHT Analisador de Métricas" ranqueia).
- Pelo celular (recomendado): Turbinar post > objetivo **Visitar seu perfil** > público **sugerido** (automático) > R$ 6/dia
  (Android; iPhone ~R$ 11 a 12 por taxa) > 3 dias (configurar 4 para não acabar antes da análise) > concluir. Ignorar a versão
  que combina várias ações.
- Pelo gerenciador: Turbinar > **desativar Criativo Advantage** > visitas ao perfil > automático > mínimo ~R$ 5,47 > 4 dias.
  Seguidores ganhos só aparecem nos insights do Instagram.
- A segmentação vem do que se fala no vídeo (uma palavra muda quem chega).
- Rotina: a cada 3 dias (ex.: segunda e quinta) ver cartão, bloqueio e custo por seguidor; manter o mais barato, pausar o mais
  caro e produzir novos; **nunca pausar tudo** (mínimo um vídeo, ~R$ 180/mês); não pausar por enjoo vídeo que traz seguidor
  qualificado. Avançado mantém os 3 melhores rodando.
- Olhômetro: de cada 10 perfis novos, quantos são do nicho (meta 80%). "Cara de Pix" vai para SLG e sessão; "cara de Serasa"
  vai para a aula semanal.
- Registrar cada Reels na aba "Tráfego Funil de Reels com CTA" da Central 1x1: nome, link, status, estilo (CTA), data,
  seguidores, investimento, visitas ao perfil, alcance, custo por seguidor.
- Execução: o Turbinar é feito pelo expert no celular ou pelo estrategista; pela API, só se o estrategista pedir (anúncio de publicação
  existente, objetivo de visita ao perfil).

## F. Minicurso de entrada e webinário

Especificados por `ht-funil-de-entrada-para-ht` (Vendas/Purchase do minicurso, público frio, criativo só com a promessa do
minicurso, verba fixa com reinvestimento) e `ht-webinario-de-vendas` (Leads com comunicação qualificadora, anúncios novos a cada
2 webinários). Esta skill monta, sobe pausada e otimiza com a mesma régua.
