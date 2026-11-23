---
name: ht-afiliados-e-consultores
description: 'Monta o programa de afiliados de evento (quem já recomenda o expert convida compradores do HT e ganha comissão) e o de consultores HT certificados. Use com "afiliados pro evento", "comissão por indicação", "alunos convidando", "consultor do HT". NÃO usar para vender ingresso nem time comercial interno.'
---

# Afiliados de evento e consultores HT

## 1. Para que serve e o que entrega

O maior obstáculo de todo evento de venda do HT é pôr gente na sala. Muita gente já recomenda o expert por reciprocidade
(alunos, clientes, parceiros); a estratégia de afiliados transforma isso em canal: o afiliado convida pessoas com potencial de
comprar o HT para o evento (de graça ou com credencial), o expert converte no pitch e o afiliado recebe comissão sobre o HT
vendido e sobre as renovações. Num caso de referência do método, o canal trouxe cerca de metade dos presentes e cerca de 1/3 das
vendas de um evento, sem custo de tráfego. O consultor HT é a versão profissional: pessoa certificada que gera lead
e vende o HT por comissão, com perfil e posição oficiais.

**Entrega** (em `05-eventos/<evento>/afiliados/`, e `06-entrega/` não é tocado):
1. `diagnostico.md`: pode abrir afiliados agora? (produto estável, prova, capacidade de operar).
2. `regulamento.md`: quem pode ser afiliado, aprovação, o que pode e o que não pode, atribuição, filiação, pagamento.
3. `tabela-comissao.md`: faixas, valores por projeto com o piso proposto, crédito x dinheiro, renovações, exemplos de cálculo.
4. `kit-afiliado/`: página de captação de afiliados, roteiro do webinário de regras, scripts de convite (direto e com
   qualificação), notificações, formulário de afiliado, página individual por afiliado.
5. `controle-afiliados.xlsx`: cadastro, link, convidados, confirmados, presentes, compradores, comissão devida e data de pagamento.
6. `consultores.md` (se pedido): desenho do programa de consultor HT certificado.

## 2. Antes de começar

1. Carregar `ht-protocolo`.
2. Ler `<raiz_projetos>/<expert>/ht/`: `02-oferta/oferta-vigente.md` (ticket, entrada, parcelado, duração: a comissão é calculada sobre
   ele); `05-eventos/<evento>/` (formato, data, capacidade, entrada do evento, captação); `06-entrega/` (provas e taxa de
   renovação real, se houver); `07-numeros/` (conversão de eventos anteriores, margem); `00-plano/decisoes.md` (regra de comissão do projeto, se a pessoa trocou o padrão).
3. Entradas obrigatórias: evento (ou sessão 1a1) para onde os convidados vão; ticket e forma de pagamento do HT; capacidade;
   quem opera o programa no time. Não perguntar piso, quem acompanha nem quem pode ser afiliado: propor pelo padrão (piso pela
   tabela do passo 3, acompanhante `[A CONFIRMAR]`, afiliados = alunos e parceiros do expert) e listar em "Assumi"
   (regra 16 do `ht-protocolo`). Só perguntar, no máximo 2 coisas e em linguagem simples, o que for impossível de adivinhar.
4. Portão do método: **só abrir afiliados com produto minimamente estável** (oferta validada, entrega rodando, conversão em
   evento conhecida). Produto novo: registrar "não é o momento" e propor outra estratégia de atração (`ht-captacao-e-presenca`).

## 3. Passo a passo

### Passo 1. Diagnóstico de prontidão
Conferir e escrever em `diagnostico.md`: oferta aprovada e vendida em 1a1 (20+ sessões); evento com pitch já rodado ou
conversão de referência; entrega com resultado (as pessoas sabem que estão "pondo o convidado em boas mãos"); taxa de
renovação real (se não houver, a comissão de renovação é promessa sobre o futuro: dizer isso ao estrategista); alguém do time para o
trabalho manual (o método avisa que dá muito trabalho: num caso de referência foram 156 páginas de afiliado feitas à mão e contato individual
pelo WhatsApp a cada 2 ou 3 dias). O método é explícito: para quem está começando um produto novo, não é o momento. Saída:
abrir / abrir em escala menor / não abrir.

### Passo 2. Proposta ao afiliado (a "Roma" do programa)
A proposta precisa ser forte o bastante para a pessoa sentir que vale mais que revender qualquer produto barato. Três razões que
o método dá ao afiliado: **margem de comissão alta** sem se preocupar com venda e entrega; **conversão alta** do evento;
**renovação alta** (a comissão continua) e a certeza de pôr o convidado em boas mãos. Escrever a proposta em uma frase com o
valor por HT e o benefício de renovação, usando os números próprios do expert.

### Passo 3. Tabela de comissão (padrão recomendado; a pessoa pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`)
- **Valor por projeto, com piso**: a skill propõe um piso por HT vendido pelo padrão do projeto, monta a tabela e lista o valor em "Assumi"; vira oficial na aprovação do plano.
- **Comissão gamificada em faixas** (modelo do método): 1 a 5 vendas = comissão inicial por venda; 6 a 10 = comissão inicial +
  comissão nas próximas 2 renovações de cada aluno; mais de 10 = comissão inicial + comissão nas próximas 4 renovações. Cada
  faixa dá ganho desproporcional para motivar a próxima.
- **Crédito x dinheiro** (opção do método): comissão em crédito interno (abater parcela, renovação, upgrade) vale o dobro da
  comissão em dinheiro. Só faz sentido quando o afiliado é aluno com parcela a pagar.
- **Pagamento: 45 dias após o recebimento** (padrão recomendado). À vista: comissão 45 dias após o recebimento. Parcelado: o modelo do método paga 50% após a
  1ª parcela e 50% após a última, e não paga a 2ª metade se o aluno não quitar; aplicar o D+45 a cada metade, ou outra divisão
  que a pessoa pedir (seção 5).
- **Filiação de 30 dias** (padrão recomendado): conta a venda fechada até 30 dias depois do evento (ou da sessão 1a1 indicada), desde que o
  convidado tenha entrado pelo link do afiliado. Primeiro cadastro vale.
- Pix/transferência só contra nota (o material cita "CNPJ para CNPJ"; conferir com o contador do expert).
- Referências do método (só referência, ver Conflitos na seção 9): R$ 10 mil por HT em dinheiro ou R$ 20 mil em crédito;
  R$ 10 mil em crédito ou R$ 5 mil em dinheiro; renovações por 4 a 5 anos; filiação de 90 dias x 30
  dias. Exemplos de cálculo em `references/tabela-de-comissao.md`.

### Passo 4. Regulamento
Modelo completo em `references/regulamento-afiliado.md`. Núcleo do método:
- **Pode**: convidar 1 a 1 pessoas com potencial de compra do HT (não precisa comprar, precisa ter potencial); usar os
  templates do kit; ir ao evento ajudar a fechar seus convidados (opcional, papel de closer); indicar para a sessão 1a1 quem já
  tem consciência (preferir o evento, que converte melhor).
- **Não pode**: se passar pelo expert ou pelo time; usar imagem do expert ou da marca fora do material liberado; pedir para o
  convidado trocar de afiliado; convidar aluno ativo dos programas do expert (ex-aluno pode); prometer resultado, preço ou
  comissão ao convidado; repassar comissão.
- **Aprovação manual** de cada afiliado (pode negar). Não se cadastrar "por curiosidade": custa operação manual; dúvida sobre o
  programa vira conversa com o time antes do cadastro.
- **Número de convites por afiliado** limitado pela capacidade do evento (referência: 15 convites numa edição, até 30 nas seguintes, por
  imersão; o número do projeto sai da capacidade dividida pelo número esperado de afiliados ativos).
- **Benefício do afiliado** no caso de referência: além da comissão, o próprio afiliado ganhava o ingresso do evento (a skill propõe o mesmo e lista em "Assumi").
- Venda sem link não conta; indicação anterior ao programa: o time atribui manualmente se comprovada.
- Troca de afiliado: o afiliado não pede; se o **próprio convidado** pedir para mudar de lista, o time avalia (regra de referência). Afiliado não indica a si mesmo nem repassa comissão ao convidado.
- Aviso no regulamento: as regras podem mudar, sempre com comunicação prévia aos afiliados.
- O regulamento é modelo: validar com o jurídico do expert antes de publicar.

### Passo 5. Abrir o programa (recrutar afiliados)
Fluxo do método, em ordem: (1) criativo ou convite convidando para "ouvir a oportunidade de afiliado";
(2) página de inscrição; (3) grupo de WhatsApp; (4) chamada da base de alunos e parceiros; (5) lembretes; (6) **webinário com
as regras**; (7) formulário de afiliado durante o webinário; (8) aprovação e **página de inscrição individual por afiliado**;
(9) grupo de afiliados com o drive de materiais. Atalhos do método: oferecer no offboarding do desafio ou no fim de uma live
(campo "quer ser afiliado?" na última pergunta do NPS). Roteiro do webinário e do convite ao afiliado em `references/kit-do-afiliado.md`.

### Passo 6. Kit do afiliado
Tudo "mastigado": página do evento com a marca do afiliado rastreada; **roteiro de convite** escrito para o afiliado
usar (estrutura: gancho de oportunidade, gratidão ao expert, prova, escassez de convites, convite pessoal); notificações;
formulário de confirmação de presença; drive; grupo. Dois scripts: **convite direto** (para quem o afiliado já sabe que tem
perfil) e **convite com qualificação** (perguntas antes de oferecer o convite). Regra de copy do convite: vender a ideia de ir
ao evento, sem falar de mentoria nem de preço.

### Passo 7. Atribuição e presença
- Link único por afiliado (página individual ou UTM); confirmação de presença do convidado cai na lista do afiliado.
- **Numerar cada afiliado** e marcar o crachá do convidado com o número ou adesivo discreto: o afiliado encontra os seus
  convidados no evento e o time sabe a origem de cada comprador.
- Presença, confirmação e lembretes dos convidados seguem `ht-captacao-e-presenca` (o convidado de afiliado passa pela mesma
  confirmação dupla). Se o evento tiver credencial (a entrada do evento segue `entrada_imersao`), o convidado do afiliado segue a mesma regra; a skill propõe e lista em "Assumi".

### Passo 8. Operação e acompanhamento
- **Contato individual com cada afiliado a cada 2 ou 3 dias** (padrão do método): quantos convidou, quantos confirmaram, dúvidas.
- Ranking e relatório no grupo (sem expor dado pessoal de convidado).
- Planilha de controle em `references/operacao-e-atribuicao.md`.
- Afiliado que pergunta "posso mandar para a sessão 1a1?": sim, se o convidado já tem consciência; o time faz a sessão
  (`ht-agendamento-e-follow-up`).

### Passo 9. Conversão, comissão e pagamento
- Depois do evento: cruzar compradores x afiliado (link + crachá), aplicar a janela de 30 dias, calcular faixa e comissão,
  registrar a data prevista de cada pagamento (recebimento + 45 dias).
- Afiliado no evento pode ajudar a quebrar objeção dos próprios convidados; quem vende é o closer do expert.
- Relatório final ao estrategista: presentes por afiliado, vendas, conversão do canal x conversão geral, comissão total, % das vendas.
  Referência do método, com variação: numa imersão, convidados de afiliado converteram mais que a média (18,98% x 15%); em outra,
  quem não veio de afiliado converteu um pouco mais, mas o afiliado trouxe gente de fora da base. Conferir.
- Debrief em `13-aprendizados/`.

### Passo 10. Programa de consultores HT (quando pedido)
Desenho em `references/programa-de-consultores.md`. Diferença do afiliado: **posição profissional oficial** ("consultor do
programa X"), com perfil próprio administrado sob regras; responsabilidade de **gerar lead e fazer a venda** (sessão 1a1 ou
evento); o expert cuida da entrega. Componentes do método: processo de certificação (que o programa cobra, como franquia);
treinamento de produto e de vendas; materiais (slides, quebra de objeção, link de checkout); ferramentas (automação, disparo);
acompanhamento para otimizar. Números citados (referência): conversão média de 25%, comissão de até R$ 10 mil por venda,
consultores com 4 a 5 vendas por semana. Pré-requisitos: produto validado com conversão alta, margem para comissão, roteiro de
sessão treinável (`ht-treino-comercial`), vagas restritas.

## 4. Regras inegociáveis do método

1. Só com produto estável e entrega que gera resultado: afiliado não conserta oferta fraca.
2. Convidado entra para um evento (ou sessão) de venda do HT; afiliado não vende ingresso nem HT, só convida.
3. Comissão paga sobre HT efetivamente recebido; parcela não paga, comissão não paga.
4. Atribuição só por link/cadastro do afiliado; primeiro cadastro vale; troca só se o próprio convidado pedir.
5. Afiliado não se passa pelo expert, não usa a marca fora do kit, não convida aluno ativo, não promete resultado.
6. Proposta de comissão forte e gamificada; valores e faixas por projeto.
7. **Comissão (padrão recomendado)**: definida por projeto com piso, paga 45 dias após o recebimento, filiação de 30 dias.
8. **Entrada do evento**: se o evento tem credencial ou ingresso, a regra para o convidado do afiliado é a mesma da entrada do evento (a skill propõe e lista em "Assumi").
9. Mensagem a afiliado ou a convidado sai como rascunho e só com OK da pessoa ("posso enviar?"); disparo em massa só pela API oficial.

## 5. O que a skill decide e lista em "Assumi"

A skill decide pelo padrão ou pela recomendação, sem lote de perguntas, e lista tudo em "Assumi: X, Y, Z (é só pedir para mudar)". Vira oficial na aprovação do plano. Itens:
- Abrir ou não o programa neste evento (e em que escala).
- Piso e tabela de comissão: valor inicial por HT, faixas, quantas renovações por faixa.
- Crédito interno x dinheiro (e a proporção), e se vale para não alunos.
- Divisão do pagamento no parcelado: padrão = metade após a 1ª e metade após a última, cada uma D+45 (modelo do método adaptado ao
  padrão de D+45); alternativas (proporcional a cada parcela, ou tudo após a quitação) só se a pessoa pedir.
- Quem pode ser afiliado e quantos convites cada um tem.
- Convidado do afiliado paga credencial ou não: segue a regra de entrada do evento.
- Abrir programa de consultores: preço da certificação, comissão, vagas.

## 6. Critério de pronto e auditoria final

**Critério de pronto**
- [ ] Diagnóstico de prontidão escrito, com a recomendação.
- [ ] Tabela com faixas, piso proposto (em "Assumi"), D+45, filiação de 30 dias e exemplos de cálculo com o ticket de 02-oferta.
- [ ] Regulamento com pode / não pode, aprovação, convites por afiliado, atribuição; marcado "validar com jurídico".
- [ ] Kit: página de afiliados, webinário, convite direto e com qualificação, notificações, formulário, página individual.
- [ ] Atribuição definida (link + número no crachá) e ligada à confirmação de presença.
- [ ] Planilha de controle e cadência de 2 a 3 dias com responsável nomeado.
- [ ] Nenhum número de referência usado como promessa sem o número próprio do expert.

**Auditoria final (erros típicos)**
1. Programa aberto com produto novo ou sem conversão conhecida?
2. Comissão fraca ou confusa (o afiliado não consegue explicar em uma frase)?
3. Promessa de comissão de renovação sem taxa de renovação real, sem avisar?
4. Venda contada sem link, ou troca de afiliado feita a pedido do afiliado?
5. Convite que fala de preço ou de mentoria em vez de vender a ida ao evento?
6. Convidados de afiliado fora da confirmação dupla de presença?
7. Ninguém nomeado para o contato a cada 2 ou 3 dias?
8. Comissão paga antes do recebimento ou sem regra para parcela não paga?
9. Regulamento publicado sem jurídico, ou aluno ativo convidado?
10. Afiliado usando a imagem do expert ou se apresentando como do time?

## 7. Saída e handoff

- Grava em `05-eventos/<evento>/afiliados/` (agente `ht-ingressos-e-patrocinio`); programa de consultores em
  `05-eventos/_programas/consultores/` ou onde o Diretor indicar. Comissão a pagar vai para o `ht-controller` (`07-numeros/`).
- Textos (regulamento, convites, webinário, página) → `ht-revisor-metodo-copy`; página e kit visual → `ht-web-designer` →
  `ht-revisor-visual`.
- Formulários, grupo, notificações e rastreio → `ht-gestor-automacoes` (nada liga sem OK).
- Presença dos convidados → `ht-captacao-e-presenca`; convidados para sessão → `ht-agendamento-e-follow-up`.

## 8. Ferramentas de apoio

`anthropic-skills:xlsx` (controle e cálculo de comissão), `anthropic-skills:docx` (regulamento e termo), `automacao-fluxos`
(formulário, grupo, notificações), `email-marketing-mautic` (comunicação com afiliados), `hotmart-meta-conversao` e
`analytics-dashboard` (atribuição e painel do canal), `avoid-ai-writing` e `humanizer` (scripts de convite).

## 9. Conflitos e lacunas do método

**Valores que variam por projeto** (o padrão recomendado de comissão resolve no que cobre): valor e moeda da comissão (dinheiro x crédito); renovações pagas por vários anos x por faixa; filiação de 90 dias x 30 dias x data fixa; conversão de referência entre 15% e 25%; conversão do convidado de afiliado maior ou um pouco menor que a do público geral. Conferir sempre com o número do expert.

**Lacunas (não inventar)**: (1) o drive de materiais, o vídeo de convite e os scripts completos são modelos reconstruídos a partir da estrutura do método; (2) não há modelo jurídico de termo de afiliado nem regra fiscal: validar com o jurídico e o contador; (3) o programa de consultor tem só o desenho, sem currículo de certificação, sem preço e sem regras de perfil; (4) números de resultado de eventos de referência são indicativos: conferir.
