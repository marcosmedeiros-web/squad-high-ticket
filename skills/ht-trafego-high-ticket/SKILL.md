---
name: ht-trafego-high-ticket
description: 'Tráfego pago Meta do Squad High Ticket: monta, sobe PAUSADA, otimiza e diagnostica campanhas que alimentam o HT (sessão 1a1, captação de imersão, aula semanal, Reels, remarketing), pela ferramenta do perfil ou entregando a campanha campo a campo. Use para "sobe a campanha da sessão", "como está o CPL", "qual criativo trocar". Ativar só com OK. NÃO usar para criativo (ht-criativos-high-ticket).'
---

# Tráfego High Ticket (Meta Ads)

## 1. Para que serve e o que entrega

Faz o tráfego pago trazer para o HT **lead que agenda, comparece e compra**, não só lead barato. Cobre os 6 destinos de
tráfego do método: sessão 1a1, imersão (captação e ingresso), aula semanal, distribuição de Reels, minicurso de entrada e
webinário. Executa na conta do expert pela ferramenta de tráfego do perfil (`trafego.ferramenta`); sem ferramenta definida (ou sem perfil), entrega a campanha especificada campo a campo, na ordem das telas do Gerenciador de Anúncios, para a pessoa (ou quem sobe por ela) subir à mão, sem exigir CLI nem acesso; toda campanha nasce **PAUSADA** e só ativa com OK do estrategista.

**Entrega** (em `<raiz_projetos>/<expert>/ht/10-trafego/`, um arquivo por ação, `AAAA-MM-DD-<acao>.md`):
1. **Plano de campanha**: objetivo, destino, metas (leads, CPL máximo, leads/dia, verba/dia), estrutura (campanha → conjuntos →
   anúncios) com nomes prontos, públicos, criativos usados (CPF do criativo), o que exclui, verba proposta e o que fica para o estrategista.
2. **Registro de subida**: IDs criados, status PAUSED conferido por leitura, checklist de conferência preenchido.
3. **Relatório de otimização ou diagnóstico**: números D-1 por nível, gargalo apontado pela régua do método, ações propostas
   com o número que as sustenta e o critério de reverter.
4. **Planilha D-1** atualizada (colunas em `references/nomenclatura-e-planilha-d1.md`).

## 2. Antes de começar

1. Carregar `ht-protocolo` (regras comuns, decisões, portão da Aprovação 1). Tráfego só roda com oferta aprovada.
2. Ler em `<raiz_projetos>/<expert>/ht/`:
   - `00-plano/` (pedido do Diretor, aprovações, decisões), `02-oferta/` (promessa, preço, canal vigente),
   - `04-demanda/` (canal que o tráfego alimenta, metas de agenda), `05-eventos/` (data, formato e entrada da imersão),
   - `07-numeros/` (orçamento aprovado, metas, Central 1x1; **vazio** porque o `ht-controller` ainda não entregou: meta e verba
     ficam `[A CONFIRMAR COM ht-controller]`, o plano sai com 3 cenários e a conta de cada um, e nada sobe), `08-copy/` e
     `09-visual/` (criativos **aprovados**, com CPF),
   - `10-trafego/` (campanhas anteriores, planilha D-1, debriefs) e `13-aprendizados/` (o que já funcionou nesse expert).
3. Conferir acesso pela ferramenta de tráfego do perfil: token válido, escopos, conta de anúncios e IG do expert (o que
   conferir e exemplos com a Meta Ads CLI oficial em `references/execucao-ferramenta-trafego.md`).
4. Entradas obrigatórias: canal/destino, URL de destino testada, criativos aprovados, verba aprovada, meta (leads ou vendas)
   e prazo. Se faltar, no máximo 2 perguntas simples por vez (o resto o agente assume e lista em "Assumi"). As que costumam faltar:
   - "Qual a verba total e o período? (sem verba aprovada, eu entrego o plano com 3 cenários e não subo nada)"
   - "A imersão é gratuita, credencial ou paga?" (sem resposta, o agente assume gratuita, que é a recomendada, e lista em "Assumi"; muda o objetivo da campanha: Leads x Vendas)
   - "Qual a meta: quantas pessoas ao vivo / quantas sessões por semana?"
   O resto (públicos, idade, interesses) sai de `01-pesquisa/` e do histórico da conta; o que não der para inferir vira lacuna.

## 3. Passo a passo

### Passo 1. Fixar destino e meta (conta de trás para frente)
Partir do resultado e calcular o que o tráfego precisa trazer. Fórmulas e exemplos em `references/metas-e-orcamento.md`.
- **Sessão 1a1**: sessões/semana desejadas → leads/semana (pela taxa própria lead→agendamento→comparecimento da Central 1x1;
  sem dado, marcar "estimativa"). Medir custo por **agendamento** e por **venda**, não só CPL.
- **Imersão**: pessoas ao vivo ÷ comparecimento = leads. Para planejar: gratuita 25%, credencial ou paga 70%, entrada no grupo
  50% (padrão de planejamento do squad). Depois: CPL máximo = verba ÷ leads; leads/dia = leads ÷ dias de captação; verba/dia.
- **Aula semanal**: captação contínua; meta de leads/semana e CPL; divisão de verba 80/20 (Passo 4C).
- **Reels**: seguidores/mês = verba ÷ custo por seguidor.
- **Minicurso / webinário**: compras ou inscritos qualificados; o retorno se lê no HT vendido (ver skills 24 e 25).
Se a conta não fecha (CPL máximo abaixo do histórico do nicho), **alertar inviabilidade** em linguagem simples e propor o caminho mais simples (mais dias ou meta menor, listado em "Assumi"; outra fonte de lista ou mais verba pedem "posso seguir?"). A primeira campanha de um expert tende a ser ruim: reservar "verba de guerra".

### Passo 2. Conferir infraestrutura (antes de qualquer subida)
Checklist completo em `references/setup-ativos-e-pixel.md`. Mínimo obrigatório:
- [ ] BM próprio do expert (nunca de terceiro), conta em BRL e fuso São Paulo, pagamento ativo, 2FA por aplicativo.
- [ ] Página do Facebook e Instagram profissional vinculados e atribuídos no BM; domínio verificado.
- [ ] Um pixel por negócio, instalado em **todas** as páginas do funil; **evento Lead só no cadastro real** (página de obrigado
      ou redirecionamento curto), nunca no clique do botão. Compra (Purchase) vem do checkout para minicurso e ingresso.
- [ ] Teste de ponta a ponta feito: preencher, cair no obrigado, ver o evento no Testar eventos/Pixel Helper e o contato com a
      tag na ferramenta de e-mail. Teste registrado com data (é a prova; sem ele, a campanha não sobe).
- [ ] Públicos criados antes da campanha (lista em `references/setup-ativos-e-pixel.md`; como criar e ler o ID, já que a CLI não
      cria público personalizado: `references/execucao-ferramenta-trafego.md` §2.0).
- [ ] Conta em `account_status` 1 e token com os 7 escopos no `check` (status e escopos: `references/execucao-ferramenta-trafego.md` §4).

### Passo 3. Desenhar a campanha do canal
Escolher a estrutura do destino (detalhe, configuração e nomes em `references/campanhas-por-canal.md`):

| Destino | Objetivo / evento | Estrutura de referência do método |
|---|---|---|
| Sessão 1a1 | Leads manual, Site, Lead; sem data de término | 1 campanha contínua; conjuntos 00 visitantes 180d · 01 engajamento IG 365d (exclui 00) · 02 semelhante 1% e 02 interesses (excluem 00 e 01; abertos não se excluem entre si) |
| Imersão gratuita | Leads, Site, Lead; fim na hora do evento | LOW até ~R$ 10 mil (internos · semelhante · interesses); segmentada acima disso (1 conjunto por público interno); presencial: 1 conjunto por região |
| Imersão paga / ingresso | Vendas, Purchase | mesma lógica de públicos; perpétuo de ingresso com criativo raiz (skill 34 cuida da oferta do ingresso) |
| Aula semanal | Leads (captação perpétua) + Reconhecimento (remarketing dos cadastrados) | 4 estágios em 4 conjuntos programados por dia: genérico, é amanhã, é hoje, replay (receita em `references/campanhas-por-canal.md` §D) |
| Live direto ao ponto | Leads, Site, Lead; fim na hora da live | captação de 10 a 11 dias para a página própria da LDP; remarketing dos cadastrados na mesma lógica de estágios |
| Reels | Turbinar com objetivo Visitar o perfil | público sugerido; 2 vídeos no mínimo; nunca parar |
| Minicurso de entrada | Vendas, Purchase | público frio, criativo só com a promessa do minicurso (skill 25) |
| Webinário | Leads qualificados | comunicação qualificadora; anúncios novos a cada 2 webinários (skill 24) |

Regras de montagem que valem para todos:
- Orçamento **no conjunto** na fase de teste e **exclusões em cascata** (regra do squad, escrita para a campanha de sessão;
  o desenho de captação de imersão é o mesmo). Depois de validado, pode migrar para orçamento na campanha com
  limite mínimo de gasto por conjunto. Há duas escolas: orçamento na campanha nas primeiras campanhas (ainda não se sabe qual público performa) ou no
  conjunto (otimiza por conjunto; na campanha a Meta tende a gastar no público maior). Vale o padrão recomendado
  (pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`): no teste, orçamento no conjunto; a outra escola fica só como contexto.
- Gênero: todos por padrão; se o público comprador é muito concentrado (exemplo: ~80% homens), restringir só nos
  conjuntos frios (semelhante e interesses) e manter todos nos quentes.
- Mínimo de 5 criativos antes do segundo conjunto; 6 a 10 anúncios por campanha, no máximo 6 por conjunto.
- **Imagem e vídeo no mesmo conjunto** por padrão (padrão recomendado; pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`; há quem use imagem só em
  remarketing, o padrão do squad é misturar).
- Idade do avatar (de `01-pesquisa/`) **só na segmentação**; localização Brasil (ou região); posicionamentos automáticos; melhorias automáticas do
  criativo desmarcadas; CTA "Saiba mais"; destino = página do funil com UTMs; complementos do navegador: nenhum.
- Público fechado (remarketing, visitantes 180d, cadastrados): conferir que a **expansão de público personalizado** está
  desligada (`targeting_relaxation_types` com `custom_audience: 0` e `lookalike: 0`) e reler o alcance estimado. Alcance muito
  maior que o público = vazou. Isto é regra do squad e vale acima de qualquer outra orientação: há quem deixe o Público
  Advantage ligado no começo para a Meta aprender e teste desligado depois; nos conjuntos abertos (semelhante, interesses)
  pode seguir essa prática.
- Interesses: 3 a 5 principais juntos no começo; depois testar isolado. Termo que só existe no Brasil (MEI, INSS) não aparece
  na busca de interesses: usar o equivalente amplo; interesse que só aparece em inglês pode ser usado.

### Passo 3b. Briefing do criativo: trava de atributo pessoal (compliance Meta)
Todo pedido de criativo que esta skill escreve (ao `ht-criativos-high-ticket` e à copy) leva a trava escrita: **o texto não afirma
nem insinua atributo pessoal do leitor** (idade, condição de saúde, peso, situação financeira, desemprego, religião, etnia,
orientação sexual, deficiência, situação jurídica). A dor do avatar que envolve um atributo (ex.: "acima dos 40", "recomeço depois
da demissão") entra pela **segmentação** ou pelo problema na terceira pessoa, nunca como "você que tem mais de 40" ou "você que
está desempregada". Promessa de emprego, contratação, renda ou cura também fica fora. Anúncio que quebra a trava não sobe, mesmo
aprovado em copy: volta com o trecho e a reescrita sugerida. Checklist completo: `ht-protocolo/references/checklist-revisao-entregavel.md`
§5 e `ht-criativos-high-ticket/references/auditoria-anti-ia-e-compliance.md`.

### Passo 4. Casos específicos
**A. Sessão 1a1.** Campanha perpétua: não pausar, finalizar e recriar à toa (o algoritmo aprende com tempo). Excluir também o
público de quem já é lead (obrigado 180d) dos conjuntos: acréscimo técnico, a aula não demonstra. Criativo com escassez de
horários e segmentação no próprio texto; rotação do nome da sessão (auditoria, análise, diagnóstico) quando esgotar.
**B. Imersão.** Campanha termina na hora do início do evento. Captação curta: olhar 2x/dia, mexer 1x/dia ou em dias alternados.
Conta nova libera gasto devagar. Ritmo de verba (padrão recomendado; pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`): funil novo começa com verba menor por 4 a 5
dias; validado, vai com a verba cheia. Há quem comece cheio desde o
dia 1; o padrão do squad é começar menor.
**C. Aula semanal.** Divisão de verba de referência: 80% nas aulas (captação 80%, lembrete 10%, replay 10%) e 20% em
distribuição de conteúdo (descoberta 70%, relacionamento 30%). Captação nunca para; criativo raiz sem data roda o ano todo.
Remarketing para cadastrados no calendário da aula semanal (detalhe e conflito do replay em `references/campanhas-por-canal.md`).
**D. Distribuição de Reels.** Escolher os 2 melhores pelo orgânico (24 a 48 h depois de postar); turbinar com objetivo
"Visitar o perfil", público sugerido, R$ 6/dia por vídeo (Android ou gerenciador; iPhone cobra ~30% a mais), 3 a 4 dias;
no gerenciador, desligar o Criativo Advantage. Monitorar a cada 3 dias (cartão, bloqueio, custo por seguidor). Manter o mais
barato, trocar o mais caro, **nunca pausar tudo** (mínimo de um vídeo, ~R$ 180/mês). Meta de custo por seguidor até R$ 0,50,
aceitável até R$ 1,50 no início (referência). Bloqueio do Turbinar: vídeo > 90 s, filtro do Instagram, música em alta com
direito autoral, baixa qualidade. Seguidor novo vai para o SLG (`ht-slg`); registrar cada Reels na Central 1x1.
**E. Minicurso e webinário.** Configuração de Vendas/Purchase e captação qualificadora: ver `ht-funil-de-entrada-para-ht` e
`ht-webinario-de-vendas`; esta skill executa a campanha que elas especificarem.

### Passo 5. Nomear e subir PAUSADA
- Nome da campanha no padrão do squad, com o prefixo de campanha do perfil (`trafego.prefixo_campanha`), se houver, colado
  logo após o objetivo: `[<destino>][<OBJETIVO>][PREFIXO] [<PRODUTO/CANAL>] [<estratégia>] - DD.MM.AA`
  (ex.: `[v1][LEADS][PREFIXO] [SESSAO1A1] [00-01-02] - 22.11.26`; sem prefixo no perfil, o bloco sai). Conta com padrão
  próprio segue o padrão da conta, marcando o prefixo (se houver) e a data `dd.mm.aa`. Conjunto: número da hierarquia + público. Anúncio: só o CPF do
  criativo, igual em todas as campanhas. Regras completas em `references/nomenclatura-e-planilha-d1.md`.
- Subir pela ferramenta de tráfego do perfil com status **PAUSED** em campanha, conjunto e anúncio. Comandos, armadilhas da API e roteiro de
  conferência em `references/execucao-ferramenta-trafego.md`.
- **Conferir por leitura** (não pela saída do comando de criação): status, objetivo, evento, pixel, públicos e exclusões,
  expansão de público, orçamento, datas, URL com UTM, Página/IG corretos. Registrar o que foi conferido.
- Entregar o plano + registro de subida ao Diretor e pedir o OK para **ativar** como um "posso seguir?" simples. Ativar é ação separada, com o OK
  dele escrito em `00-plano/aprovacoes.md`.

### Passo 6. Acompanhar e otimizar (rotina D-1)
Régua completa em `references/otimizacao-escala-e-diagnostico.md`. Resumo:
1. **Esperar dado**: 3 a 7 dias conforme a verba antes da primeira decisão de estrutura; depois, olhar todo dia.
2. **Planilha D-1** todo dia: leads, gasto, alcance, impressões, cliques, CPL e desvio da meta, por campanha e por criativo.
3. **Três níveis, nesta ordem**: anúncio (o que traz cadastro mais barato x o que gastou sem trazer), conjunto (qual público
   traz mais por menos), campanha (verba). CPL dentro da meta = **não mexer**.
4. **Ler o funil, não só o CPL**: CPM → CTR (≥ 1%) → taxa de carregamento (≥ 80%) → conversão da página (≥ 40% a 50% em
   captação gratuita; 70% na calculadora do método) → CPL (≈ 3x CPC como referência). O gargalo diz onde mexer: CTR baixo = gancho e
   segmentação do criativo; carregamento baixo = velocidade da página; conversão baixa = alinhamento criativo-página.
   Página antes de criativo e público quando o CTR está bom e a página converte pouco.
5. **Escalar** em degraus de 20% a no máximo 30% por vez; acima disso, duplicar a campanha (escala horizontal).
   Todo plano com escada de verba **mostra a conta**: tabela dia a dia (ou por degrau) com verba/dia, quantos dias em cada degrau
   e o acumulado, fechando com o total aprovado. Se 20% por degrau não fecha com o total e o prazo, dizer qual cede (degrau, dias
   ou total), decidir pelo que cede menos e listar em "Assumi" (total maior pede "posso seguir?"); nunca apresentar "degraus de 20%" e um total que não batem.
   Subir rápido demais derrubou um caso de CPL ~R$ 20 para R$ 45 a 53 (referência).
6. **Medir até a venda**: cruzar com a Central 1x1 (`ht-central-e-kpis`): custo por agendamento, comparecimento, custo por
   venda, somando tráfego de sessão e de Reels. Lead barato que não agenda é problema de criativo ou de qualificação.

### Passo 7. Diagnosticar erro
Sintoma → causa → conserto em `references/erros-comuns-meta.md` (não gasta, rascunho, objetivo errado, lead falso, dois
pixels, vídeo bloqueado, pagamento, conta nova limitada, BM errado, Turbinar bloqueado). Regra de ouro: a Meta não tem
"desfazer"; **duplicar antes de apagar** e não descartar rascunho antes de confirmar a publicação.

## 4. Regras inegociáveis do método

- Toda campanha nasce **PAUSADA**, com o prefixo de campanha do perfil (se houver), e só ativa com OK. Verba e ativação pedem "posso seguir?" simples.
- Evento Lead só no cadastro real; campanha de captação nunca com objetivo Tráfego/Engajamento nem formulário instantâneo
  (o objetivo não muda depois: errou, duplica e recria).
- Criativo e página prometem a mesma coisa; tráfego para sessão 1a1 fala com o perfil que compra e filtra quem não serve.
- Ação de tráfego sai de número, nunca de impressão: toda proposta traz janela, amostra, métrica e critério de reverter.
  Amostra pequena é chamada de pequena e não sustenta decisão.
- Não pausar a distribuição de Reels inteira; não pausar campanha perpétua de sessão por ansiedade.
- Nada de pixel ou público de concorrente; nada de BM de terceiro; token nunca no chat (se aparecer, está queimado).
- Regras do squad que se aplicam: exclusões em cascata e orçamento no conjunto no teste; comparecimento para planejar
  (gratuita 25%, credencial ou paga 70%, grupo 50%); Reels até 90 s como condição para turbinar; a entrada da imersão
  (gratuita, credencial ou paga, assumida pela recomendação e listada em "Assumi") decide o objetivo.
- Número de referência não é meta, não meta do expert: depois do primeiro ciclo, a meta passa a ser o histórico da própria conta.

## 5. O que o agente decide e o que pede OK

**Padrões recomendados** (regra desta skill; a pessoa pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`;
antes de aplicar, ler o perfil e seguir o que estiver lá; não volta como pergunta):
- **Otimização na campanha, não no anúncio**: não pausar anúncio dentro de campanha; mexer na
  campanha (campanha nova isolando o vencedor, pausar ou ativar campanha, verba em degraus de ~20%). Anúncio caro pode estar
  gerando atenção que outro converte: olhar visitas ao perfil antes de qualquer leitura (já houve criativo "sem
  conversão" que gerava lead pelo perfil). O método ensina pausar o anúncio que gastou 2x o CPL meta sem lead; o padrão do squad é
  não pausar.
- **Formato**: imagem e vídeo juntos por padrão. Há quem use imagem só no
  remarketing. Se o CPL da imagem em frio sair muito acima, o número vai à pessoa como leitura simples, sem trocar o padrão.
- **Orçamento no teste**: no conjunto, com exclusões em cascata. Há quem use orçamento na campanha nas primeiras campanhas; o padrão do squad é no conjunto. Validado, pode
  migrar para orçamento na campanha com limite mínimo de gasto por conjunto.
- **Verba na largada**: funil novo começa menor (4 a 5 dias); validado, vai cheio. Há quem comece cheio desde o dia 1.

**Pedem um "posso seguir?" simples** (uma frase com o resumo, sem a/b/c; nada é gasto nem ativado sem o OK): a **verba e o prazo** de cada campanha e **ativar** cada uma.

**O agente decide pela recomendação e lista em "Assumi":**
- **Entrada da imersão**: o agente assume gratuita (a recomendada) e lista em "Assumi". Alternativa, só como referência: gratuita (Leads, mais volume, comparecimento ~25%) x credencial ou paga (Vendas, menos volume,
  comparecimento ~70%, ingresso paga parte do tráfego). Dado de caso de referência para pôr nos prós da gratuita (conferir): depois de duas imersões presenciais, o custo de levar uma pessoa ao programa saiu
  mais barato com lead gratuito do que com ingresso, e o caso passou a captar gratuito; 25% de comparecimento tanto no online
  quanto no presencial (online de 1 dia: ~1.324 leads, pico de 334 ao vivo).
- **Escala acima de 30%** ou dobrar verba de uma vez; abrir campanha de escala horizontal: o agente mantém degraus de ~20 a 30% e lista em "Assumi"; subir a verba é gasto e pede "posso seguir?".
- Inviabilidade da meta (conta que não fecha): o agente diz em linguagem simples que a conta não fecha e propõe o caminho mais simples (mais dias ou meta menor), listado em "Assumi"; mais verba pede "posso seguir?".

## 6. Critério de pronto e auditoria final

**Pronto quando:**
- [ ] Meta calculada de trás para frente com CPL máximo, leads/dia e verba/dia; inviabilidade sinalizada se houver.
- [ ] Teste do funil de ponta a ponta registrado (evento Lead/Purchase visto, contato com tag).
- [ ] Estrutura do canal certo, nomes no padrão, CPF dos criativos aprovados, UTMs.
- [ ] Tudo em PAUSED, conferido **por leitura** depois da criação, com a lista do que foi conferido.
- [ ] Pedido de OK para ativar e de verba feito como um "posso seguir?" simples (sem opções a/b/c), com o "Assumi".
- [ ] Planilha D-1 criada ou atualizada; métrica até a venda ligada à Central 1x1.

**Auditoria (erros típicos dos laboratórios e plantões; rodar antes de entregar):**
1. Objetivo Tráfego/Engajamento ou formulário instantâneo no lugar de Leads/Site?
2. Evento Lead no clique do botão (gerenciador conta mais lead que a base)? Dois pixels na conta ou na página?
3. Campanha em rascunho (barra verde) ou um nível desativado? Data de término errada?
4. Exclusão feita pelo "x" em vez de "Excluir este público"? Padrão de URL genérico ("obrigado") misturando páginas?
5. Público fechado com expansão ligada (alcance >> público)?
6. URL do anúncio apontando para checkout/Hotmart quando devia ser a página, ou telefone no anúncio?
7. Vídeo com música com direito autoral, regravado no Instagram ou acima de 90 s (no caso do Turbinar)?
8. Criativo e página prometendo coisas diferentes? Criativo genérico que não filtra o avatar?
9. Mexeu em quem estava no CPL meta? Escalou mais de 30% de uma vez? Apagou sem duplicar?
10. Relatório que só fala de CPL, sem agendamento, comparecimento e venda?
11. Número do método apresentado como meta garantida, sem "referência"?
12. Orçamento passado em reais na CLI (é em centavos) ou orçamento na campanha e no conjunto ao mesmo tempo?
13. Texto de anúncio afirmando atributo pessoal do leitor (idade, saúde, dinheiro, emprego) ou prometendo contratação ou renda?
14. Escada de verba cuja soma não bate com o total aprovado, ou objetivo Reconhecimento usado para captar?

## 7. Saída e handoff

- Gravar em `10-trafego/` (plano, registro de subida, relatórios, planilha D-1). Debrief de cada campanha encerrada em
  `13-aprendizados/` via handoff (CPL real, custo por agendamento e por venda, criativo campeão, o que muda).
- Handoff: **Diretor** ("posso seguir?" de verba e ativação) · `ht-revisor-metodo-copy` (textos de anúncio, compliance
  Meta) · `ht-revisor-visual` (criativo) · `ht-gestor-automacoes` (tags e eventos do funil) · `ht-controller` (gasto x meta,
  custo por venda) · `ht-criativos-high-ticket` (pedido de criativo novo quando a fadiga aparecer, com o diagnóstico do trecho).
- Formato do bloco de entrega: `ht-protocolo/references/estrutura-pasta-projeto.md`.

## 8. Ferramentas de apoio

- A ferramenta de tráfego do perfil (`trafego.ferramenta`; escrita só com OK e PAUSED) e as skills `meta-ads-cli`
  (sintaxe e armadilhas da API) e `meta-ads-cli-setup` (setup de app e token), usadas como executoras.
- `hotmart-meta-conversao` (pixel/Purchase de checkout Hotmart), `analytics-dashboard` (painel), `anthropic-skills:xlsx`
  (planilha D-1), `instagram-analise-estrategica` (escolher o Reels a turbinar), `page-optimizer` (página lenta).## 9. Limites (não inventar)

Não há meta de CPL, CTR ou taxa de agendamento específica da sessão 1a1 de referência. A planilha de tráfego da imersão e a "colinha"
de colunas não vêm no pacote. Instalação de pixel por plataforma além de Hotmart Pages/Green é só citada; API de conversões só
mencionada; benchmarks de CPM e conversão são de casos específicos (conferir no histórico da conta); método ACE de distribuição só
citado.
