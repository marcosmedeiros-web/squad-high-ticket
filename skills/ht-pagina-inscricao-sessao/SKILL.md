---
name: ht-pagina-inscricao-sessao
description: 'Squad High Ticket / método FHT. Monta a infraestrutura de captação da sessão 1a1: copy da página de inscrição (topo, para quem é, formulário ancorado, por que participar, provas, CTA, rodapé), página de obrigado (que marca a conversão), formulário com tag e segmentação pós-clique (pergunta de corte que manda cada lead ao destino certo), domínio/SSL e o teste do fluxo inteiro antes de ligar tráfego. Use quando o estrategista disser "faz a página do diagnóstico", "página de inscrição da sessão", "página de obrigado", "formulário que filtra o lead", "testa o fluxo antes do anúncio". Entrega rascunho e especificação; publicar e ligar tráfego só com OK do estrategista. NÃO usar para página de venda de lançamento LPSG, ingresso de evento pago 5+1 ou Funil 8 (Turbo), nem para página de imersão (ht-captacao-e-presenca) ou da aula semanal (ht-aula-semanal).'
---

# Páginas de inscrição e de obrigado da sessão 1a1

## 1. Para que serve e o que entrega

A página de inscrição recebe quem clicou no anúncio, no link da bio ou no story e quer a sessão 1a1 (diagnóstico, análise,
reunião estratégica: o nome é o de `03-sessao/nome-da-sessao.md`, definido pelo `ht-closer`; esta skill **só lê e cita**, nunca
propõe nome). Objetivos, em ordem: deixar claro para quem é a sessão, mostrar o benefício,
mostrar prova se houver e, acima de tudo, **captar o contato**. A página de obrigado confirma ao lead que a equipe vai chamar e
marca a conversão para o tráfego. O formulário identifica o lead (tag) e, quando preciso, separa quem vai para a sessão de quem
vai para outro destino.

**Entrega** (rascunho para o estrategista, dividido pelas pastas donas):
1. `08-copy/paginas-e-emails/pagina-sessao/AAAA-MM-DD-copy.md`: copy completa da inscrição e do obrigado, seção a seção, com os [campos]
   preenchidos pelo material do expert e os `[FALTA]` marcados.
2. `11-automacoes/pagina-sessao/AAAA-MM-DD-formulario.md`: campos, tag, regra de segmentação (se houver), destino do
   obrigado, para onde vai o contato (e-mail marketing/CRM) e quem é avisado.
3. `09-visual/briefs/AAAA-MM-DD-pagina-sessao-briefing.md` (Diretor de arte): briefing para o web designer (estrutura, CTAs ancorados, URLs, título da
   aba, favicon, identidade, requisitos de pixel).
4. `11-automacoes/pagina-sessao/AAAA-MM-DD-teste-de-fluxo.md`: relatório do teste ponta a ponta com a prova observada.
5. Bloco de entrega do protocolo e as decisões para o estrategista.

Pasta com dono (protocolo, regra 5): cada arquivo é gravado pelo agente dono da subpasta (copy pelo Diretor de copy, briefing
pelo web designer, formulário e teste pelo gestor de automações). Quem roda esta skill escreve só na sua subpasta e pede as
outras peças via Diretor, com esta skill como referência.

## 2. Antes de começar

1. Carregar `ht-protocolo`.
2. Ler em `experts/<slug>/ht/`:
   - `03-sessao/nome-da-sessao.md`: **nome e promessa da sessão** (dono único: `ht-closer`) e, no resto de `03-sessao/`, o que
     acontece nela (a página promete só o que a sessão entrega). Arquivo ausente: o título fica `[A CONFIRMAR COM ht-closer]` e o
     Diretor pede o nome ao Closer; a página não inventa nem escolhe nome.
   - `02-oferta/` (pela regra de leitura da oferta do protocolo): avatar e promessa do HT; corte de perfil (a pergunta de segmentação conversa com a parcela).
   - `01-pesquisa/`: 4 âncoras (dores e desejos na voz do avatar), subnicho.
   - `04-demanda/vitrine/` e `04-demanda/slg/`: a mesma palavra da promessa e o mesmo nome da sessão já usados.
   - `06-entrega/` (provas e cases): só resultados reais e autorizados.
   - `10-trafego/`: se haverá campanha (define pixel, evento Lead e padrão de URL).
3. Entradas obrigatórias: nome da sessão, avatar, 3 benefícios, provas disponíveis, domínio do expert, ferramenta de página e
   de e-mail/CRM em uso, CNPJ para o rodapé, cores e logo. Se faltar, até 3 perguntas ao estrategista, por exemplo:
   - "O expert já tem domínio próprio? Em que ferramenta publicamos (Hotmart Pages, página estática própria ou outra)?"
   - "Vai haver segmentação (lead pequeno para outro produto)? Qual o corte?"
   - "Quais provas podemos mostrar, com autorização?"

## 3. Passo a passo

**Passo 1. Definir o fluxo.** Desenhar em uma linha o caminho do lead:
`origem (anúncio/bio/story/SLG) → página de inscrição → formulário (tag) → página de obrigado (evento Lead) → contato da equipe
→ agendamento (ht-agendamento-e-follow-up)`. Com segmentação: o formulário divide para sessão, produto de entrada ou repasse.

**Passo 2. Copy da página de inscrição** (estrutura e modelo em `references/estrutura-da-pagina.md`). Ordem do método:
topo (título para o avatar com o nome da sessão gratuita, texto de apoio, CTA, microtexto) → para quem é → **formulário**
(ponto de ancoragem) → por que participar → CTA → provas (4 a 5) → CTA final → rodapé com CNPJ e texto de LGPD. Todos os
botões levam ao formulário. Mesma palavra da promessa e mesmo nome da sessão de todas as outras peças.

**Passo 3. Página de obrigado** (`references/pagina-de-obrigado.md`). Curta: confirmação e o que acontece agora (a equipe vai
entrar em contato). Sem botão, sem cronômetro, sem nova tarefa para o lead. URL própria e específica (ex.:
`/obrigado-sessao-1a1`) para medir a conversão e montar público.

**Passo 4. Formulário e tag** (`references/formulario-e-segmentacao.md`). Mínimo: e-mail e telefone (WhatsApp); nome opcional;
sem dupla confirmação; tag do tipo "solicitou diagnóstico"; obrigado próprio como confirmação. Campo opcional de melhor
período (manhã, tarde, noite) ajuda o agendamento. Formulário curto: cada campo a mais derruba conversão.

**Passo 5. Segmentação pós-clique (se aplicável).** Mesmo criativo e mesmo formulário; uma pergunta de corte (gasto,
faturamento, situação) decide o destino: acima do corte → sessão; abaixo → produto de entrada do expert ou outro funil. O
valor do corte é decisão do estrategista. Modelo na mesma referência, seção 3.

**Passo 6. Domínio, URLs e itens técnicos** (`references/dominio-e-teste-de-fluxo.md`, seção 1). Domínio próprio com SSL
(propagação de até 24 h, aviso de até 72 h: fazer com antecedência); URLs com hífen, nunca underline; título da aba; favicon
quadrado 32 x 32 px; remover selo da ferramenta quando o plano permitir; imagens sem distorção.

**Passo 7. Briefing ao web designer** com a copy aprovada, a estrutura, as URLs e os requisitos de pixel (pixel na página,
evento Lead disparando só na página de obrigado). Tradução para a ferramenta em uso em `references/adaptacao-ao-stack.md`.

**Passo 8. Teste de fluxo ponta a ponta, antes de qualquer tráfego** (`references/dominio-e-teste-de-fluxo.md`, seção 2).
Preencher com dados de teste, cair no obrigado, ver o contato com a tag e o telefone na ferramenta, ver o evento Lead no
gerenciador (quando houver pixel), testar no celular, testar todos os botões. Registrar a prova (print ou saída). Sem prova,
o item é "feito, não testado".

**Passo 9. Auditoria final** (seção 6) e handoff.

## 4. Regras inegociáveis do método

- O objetivo da página é captar o contato; tudo leva ao formulário (CTA ancorado, vários CTAs ao longo da página).
- Clareza de para quem é a sessão: a página também afasta quem não é avatar.
- Promessa da página = promessa da sessão e da vitrine, com as mesmas palavras; a página não promete o que a sessão não entrega.
- Gratuidade é benefício, não rótulo ("sessão de diagnóstico gratuita" sim; "consulta grátis" como nome, não).
- Sem preço, sem oferta do HT, sem nome do programa na página da sessão: a venda acontece na sessão.
- Provas só reais, do método do expert, coerentes com a promessa e autorizadas; 4 a 5 no mesmo formato. Sem prova, a seção
  sai (nunca depoimento inventado ou "ilustrativo").
- Formulário curto (e-mail e telefone; nome opcional), sem dupla confirmação. Não perguntar quanto a pessoa quer investir nem
  se prefere grupo ou individual.
- Obrigado sem CTA e sem cronômetro: quem age agora é a equipe.
- URL de obrigado específica (não só "obrigado"), para não misturar públicos e conversões de outras páginas.
- Rodapé com CNPJ e texto de LGPD (consentimento de contato).
- Teste do fluxo inteiro antes de ligar o tráfego; domínio configurado com antecedência; uma aba do editor por página (duas
  abas abertas desfizeram o formulário na aula).
- Nada vai ao ar sem OK do estrategista; campanha nasce pausada (`ht-gestor-trafego`, nomenclatura com o prefixo de campanha do perfil (`trafego.prefixo_campanha`), se houver).

## 5. Quando a decisão é do estrategista

Formato do protocolo (decisão numerada, a/b/c, prós, contras, custo; recomendação na a).
- **Ferramenta e hospedagem:** a) página estática própria (publicada por você ou pela agência, campo `agencia` do perfil, se houver, + formulário ligado ao e-mail/CRM
  do projeto) (recomendo, se o expert não tem ferramenta); b) Hotmart Pages + Send, como na aula (se o expert já usa Hotmart); c) ferramenta que o expert já paga.
- **Domínio:** comprar domínio ou usar subdomínio do expert (gasto e acesso ao registro são do expert).
- **Segmentação e corte:** fazer ou não; qual pergunta e qual valor; para onde vai quem fica abaixo (produto de entrada,
  aula semanal, repasse).
- **Provas na página:** quais depoimentos usar (autorização) ou publicar sem a seção.
- **Publicar** e **ligar tráfego** (só depois do teste com prova).

## 6. Critério de pronto e auditoria final

**Pronto quando:**
- [ ] Copy da inscrição com todas as seções do método, nome da sessão citado de `03-sessao/nome-da-sessao.md` (com o estado dele)
      e a promessa idêntica à da vitrine.
- [ ] Todos os botões com texto de ação e ancorados no formulário; pelo menos 3 CTAs na página.
- [ ] Seção de provas só com provas reais e autorizadas (ou removida, com registro).
- [ ] Obrigado curto, sem CTA nem cronômetro, com URL específica.
- [ ] Formulário com e-mail e telefone, tag definida, obrigado próprio como destino, sem dupla confirmação.
- [ ] Segmentação especificada (pergunta, corte, destinos) ou dispensada com motivo.
- [ ] Domínio com SSL, URLs com hífen, título da aba, favicon 32 x 32.
- [ ] Rodapé com CNPJ e texto de LGPD.
- [ ] Teste ponta a ponta feito com prova (inscrição de teste → obrigado → contato com tag e telefone → evento Lead, se houver
      pixel), inclusive no celular.
- [ ] Nada publicado nem tráfego ligado sem OK registrado.

**Auditoria (erros típicos da aula e dos alunos):** botão que não leva ao formulário; formulário longo; formulário com página
de confirmação padrão esquecida no lugar do obrigado; underline na URL; obrigado com o mesmo padrão de URL de outras páginas
(público misturado); "salvou e não publicou"; duas abas do editor abertas; favicon esticado ou com letra miúda; imagem
distorcida ("cobrir/esticar"); tudo na mesma cor ou vermelho gritante; domínio configurado em cima da hora; provas fora do
formato ou que não sustentam a promessa; página prometendo o programa ou citando preço; pixel ausente ou duplicado na conta;
evento Lead não disparando (aviso de "sem atividade de conversão" no gerenciador).

## 7. Saída e handoff

- Copy → `08-copy/paginas-e-emails/pagina-sessao/` (`ht-copy-paginas-e-emails`, aprovada pelo Diretor de copy) → `ht-revisor-metodo-copy`.
- Briefing → `09-visual/briefs/` (`ht-diretor-arte`); página → `09-visual/paginas/pagina-sessao/` (`ht-web-designer`) → `ht-revisor-visual`.
- Formulário, tag, destino dos contatos e teste de fluxo → `11-automacoes/pagina-sessao/` (`ht-gestor-automacoes`).
- Pixel, evento Lead, públicos por URL e campanha → `10-trafego/` (`ht-gestor-trafego`), só depois do teste aprovado.
- Contato que chegou → `ht-agendamento-e-follow-up` (contato em minutos, 2 horários, sessão em até 2 dias).
- Sem parecer dos revisores e sem OK do estrategista, a página não vai ao ar.

## 8. Ferramentas de apoio (por nome)

- Página: `frontend-design:frontend-design`, `pagina-design-premium`, `ui-ux-pro-max`, `design-tokens-turbo`,
  `designer-senior-turbo`; otimização depois de aprovada: `page-optimizer-turbo`.
- Publicação: `publicar-pagina-cloudflare` (com OK do estrategista).
- Formulário e e-mail: `email-marketing-mautic`; fluxos: `automacao-fluxos`.
- Pixel e conversão: `meta-ads-cli-turbo`, `meta-ads-cli-setup-turbo`, `hotmart-meta-conversao` (a ferramenta de tráfego do
  perfil, `trafego.ferramenta`, para leitura; campanha nasce pausada).
- Texto: `avoid-ai-writing`, `humanizer`.

## 9. Fontes e lacunas

**Fontes:** trilha 12 (bootcamp "Ferramentas para Sessão 1:1", aulas 02 a 11 lidas por inteiro na revisão R3: domínio, tag, formulário, modelo da
página de inscrição, modelo do obrigado, integração, dúvidas); trilha 13 (RESUMO-trafego: pixel, evento Lead na obrigado,
públicos por URL, padrão de URL; RESUMO-criativos 3.12 e 4.6: rotação do nome e segmentação pós-clique); parte B
(construtor-pagina-inscricao-sessao-1a1, construtor-pagina-obrigado-sessao, configurador-tag-formulario-send,
configurador-dominio-pagina, testador-fluxo-inscricao-sessao, desenhista-segmentacao-pos-clique, depurador-evento-lead-e-pixel);
desafio jan/2026 plantão 132 (pedir só o período no formulário; não perguntar investimento); palestras do encontro FHT jun/2026
(formulário de agendamento imediato, encaminhamento condicional); padrões do squad.

**Lacunas (não inventar):** o mapa mental da trilha 12 não foi lido; a demonstração é em Hotmart Pages/Send e a interface pode
ter mudado; o bootcamp de tráfego não tem aula de instalação do pixel nem de verificação de domínio no BM (só citados);
nenhuma fonte trata API de conversões nem envio do agendamento ou da venda como evento; não há meta de taxa de conversão da
página de sessão nas aulas (a "Calc FHT" da Central traz conversão de página acima de 70% como métrica esperada, sem contexto,
conferir); limites e preços de plano da Hotmart foram ditos de memória pela instrutora.
