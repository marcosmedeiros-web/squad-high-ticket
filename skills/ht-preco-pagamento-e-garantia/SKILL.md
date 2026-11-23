---
name: ht-preco-pagamento-e-garantia
description: 'Define preço, pagamento e garantia do HT: faixa de 5x a 10x a média do nicho, cenários, teste de 20 sessões, tabela à vista e parcelado, entrada, dupla, P2P, garantia condicional e cobrança. Use com "quanto cobrar", "preço do HT", "monta a garantia". NÃO usar para a oferta inteira (ht-arquiteto-oferta).'
---

# Preço, pagamento e garantia do AR

## 1. Para que serve e o que entrega

Preço de HT não sai de fórmula fechada: sai de um múltiplo do que o nicho já paga, do ganho do cliente, da prova que o expert tem
e do teste em campo. Esta skill transforma isso numa faixa defensável, numa tabela que fecha a conta e que o lead entende de
primeira, e numa garantia que dá segurança para comprar e obriga o aluno a executar.

**Entrega**: `02-oferta/rascunhos/AAAA-MM-DD-preco-pagamento-garantia.md` com:
1. Base de cálculo (média do nicho com fontes, tipo de AR, ganho do cliente, prova, custo de entrega) e a faixa de preço (5x a 10x a média do nicho).
2. 3 cenários de preço com prós e contras e a recomendação (o do meio vai como proposta; vira oficial na Aprovação 1).
3. Tabela final: individual e dupla; à vista, parcelado, entrada (sinal); modalidade especial se houver (P2P ou Fake HT); conta
   conferida linha a linha.
4. Bônus à vista validado (ou "sem bônus à vista").
5. Garantia condicional: texto, condições, prazo, evidência, como acionar.
6. Plano do teste de 20 sessões (o que medir e o que fazer com cada resultado).
7. Checklist de cobrança e estrutura fiscal para o contador; política de inadimplência.
Opcional: aba OUTROS ELEMENTOS da planilha de oferta e uma calculadora em planilha (`anthropic-skills:xlsx`).

## 2. Antes de começar

1. Carregar `ht-protocolo`. Conferir o pedido do Diretor.
2. Ler `<raiz_projetos>/<expert>/ht/`:
   - `02-oferta/`: definição e tipo de AR, jornada, entregáveis e conta de horas, versões anteriores de preço (`historico/`).
   - `01-pesquisa/`: preços praticados no nicho (cursos, mentorias, consultas, procedimentos), poder de compra e objeções do
     avatar, provas do expert (casos, prints), benchmark do `ht-consultor-casos`.
   - `07-numeros/`: Master Plan (meta, número mágico), Central 1x1 (sessões e conversão reais, se já houver). **Pasta vazia**
     (o `ht-controller` ainda não entregou): o preço segue pela média do nicho e pela faixa de 5x a 10x; meta, número mágico e caixa ficam
     `[A CONFIRMAR COM ht-controller]`, o plano do teste de 20 sessões vai sem meta de faturamento, e a lacuna entra no bloco de
     entrega.
   - `00-plano/decisoes.md`: troca de um padrão recomendado para este projeto (e `padroes` do perfil `~/.config/squad-ht/perfil.md`).
3. **Entradas obrigatórias**: média de preço do nicho com pelo menos 3 referências; tipo de AR; o que o cliente ganha ou
   economiza com o resultado; prova disponível; custo da entrega. Pergunto só o que não dá para adivinhar, no máximo 2 por vez e em linguagem simples (por exemplo: "Quanto custa o curso ou a
   consulta do expert hoje?"); o resto eu assumo (concorrentes e referências, CNPJ e conta em plataforma de pagamento) e marco
   `[SUPOSIÇÃO: …]`. Sem média do nicho, pedir a pesquisa ao `ht-pesquisador` (via Diretor) em vez de chutar.

## 3. Passo a passo

### Passo 1. Base de cálculo
Detalhe e referências: `references/metodo-de-precificacao.md`.
1. **Média do nicho**: preço médio dos produtos digitais do nicho (cursos, programas), com fonte de cada número. Se o expert tem
   curso de R$ 1 mil ou mais, ele entra na média (a referência é cerca de 10x o curso; e-book e low ticket muito barato não
   servem de base).
2. **Ganho do cliente**: quanto o resultado vale em 12 meses (faturamento, economia, custo de continuar igual). Quanto mais
   ganho (negócio, carreira), maior o teto; bem-estar e habilidade tendem a ficar abaixo; comparáveis do nicho (cirurgia,
   tratamento, funcionário) limitam.
3. **Tipo de AR**: teto tende a cair de negócio para carreira, habilidade e conquista pessoal. O motivo é a âncora do lead: em negócio e carreira ele compara com o que vai ganhar; em habilidade e conquista pessoal, com a alternativa que já
   conhece (no emagrecimento, a cirurgia ou o remédio mensal), o que limita o preço. Não é regra: autoridade muda isso.
4. **Prova e autoridade**: não cobrar acima do que a prova sustenta; produto novo pode começar mais baixo dentro da faixa.
   Referência prática: assistir diagnósticos de nicho parecido e testar em campo; o preço final se acerta
   vendendo, não na planilha.
5. **Custo da entrega**: horas esperadas por aluno x custo/hora do mentor ou especialista (conta do `ht-entregaveis`); margem.
6. **Meta**: com o Master Plan, quantas vendas por mês a cada preço (ticket x volume).

### Passo 2. Faixa de preço e cenários
1. Faixa vigente: **5x a 10x a média do nicho**, validada no teste de 20 sessões (padrão recomendado; a pessoa pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`). Ex.: média de R$ 1.000 → R$ 5.000 a R$ 10.000.
2. As referências vão de 3x a 20x. Acima de 10x só com prova forte, e então listo em "Assumi"; abaixo de 5x
   provavelmente não é HT para aquele nicho (considerar Fake HT ou rever o avatar).
3. Teste do "resultado garantido": quanto seria justo cobrar se o resultado fosse certo? Serve de teto mental.
4. Ancorar no resultado: o preço tem de ser pequeno perto do que a promessa entrega no ano (exemplo: R$ 18 mil prometendo
   R$ 25 mil/mês).
5. Montar 3 cenários dentro da faixa (entrada no mercado, alvo, alto), cada um com: preço à vista, nº de vendas para a meta,
   conversão necessária, risco. Recomendação na a).

### Passo 3. Tabela de pagamento (conta fechada)
Template, fórmulas e exemplos: `references/tabela-e-modalidades.md`.
1. **À vista**: com o desconto escrito (o lead não faz conta).
2. **Parcelado**: cerca de 20% acima do à vista; mostrar a parcela ("pense em parcela") e o total. **Número de parcelas: sem
   padrão no squad**; proponho um número pelas referências abaixo e listo em "Assumi" (registro em `00-plano/decisoes.md`; padrão recomendado: parcelamento definido por expert, editável em `padroes` do perfil `~/.config/squad-ht/perfil.md`). Referências,
   só como contexto: 8 (sobram meses para negociar atraso dentro dos 12) e 8 a 10; 12 aparece na
   negociação ou em nicho em que 12x é o costume. Parcela abaixo de R$ 1.000 "parece real"
   para públicos de menor renda (referência).
3. **Entrada = sinal da sessão** (padrão recomendado; a pessoa pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`): R$ 500 a R$ 1.000, até 10% do valor, a mesma no à vista e no parcelado e na dupla, paga
   com a call aberta. Saldo do à vista em até cerca de 1 semana (referência). Esse sinal vale para a sessão 1a1. Em venda um
   para muitos (imersão, live), o método recomenda aplicação de no máximo R$ 2 mil e menor (R$ 500) para avatar de renda mais
   baixa: o valor de cada evento vem da skill do evento (proposto pelo padrão e oficial na aprovação do plano), nunca desta tabela.
4. **Dupla** (padrão recomendado; a pessoa pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`): +50% sobre o individual, à vista e parcelado; entrada igual. É +50% e não +100% porque a dupla é do mesmo
   negócio ou família e consome o mesmo plano (um diagnóstico para os dois). Trio: sem decisão vigente, fora do padrão; só se pedirem.
5. **Conferir a conta** de cada linha: entrada + parcelas = total; total parcelado > à vista; dupla = individual x 1,5;
   terminação comercial (os exemplos usam 997, 4.997, 11.997) só depois da conta, sem mudar a lógica.
6. **Piso de negociação** (definido antes da sessão, para o closer): até onde a parcela ou a entrada pode cair sem mudar o preço.
   Antes de baixar preço, perguntar "qual parcela cabe?".
7. **Ordem de apresentação na sessão** (padrão recomendado; a pessoa pode mudar em `padroes` do perfil `~/.config/squad-ht/perfil.md`): entrada → parcelado → à vista. Registrar para o `ht-closer`.

### Passo 4. Modalidades para avatar sem caixa (recomendo uma e listo em "Assumi")
- **P2P (dois passos)**: aplicação agora (o sinal) e o restante à vista ou na primeira parcela recorrente em 10 a 15 dias; o prazo
  dá tempo de o cliente se organizar. Quem não for aceito recebe a aplicação de volta.
- **Fake HT**: o programa anual comunicado pela mensalidade (sistema faculdade), com desconto para quem antecipa; cobrança
  recorrente (não tudo no cartão); deixar claro que o programa é anual e só o pagamento é mensal. Não esconder o total por esconder.
- Ticket alto: link de aplicação ou Pix, não cartão de valor cheio; oferecer também o limite do cartão quando houver (antecipa caixa).

### Passo 5. Bônus à vista (validação)
Recebe a proposta do `ht-oferta-matadora` e valida: estimula o à vista sem fazer adiar a compra; não é essencial nem parece faltar
no programa; custo calculado. Segunda cadeira equivale a uma dupla grátis (comparar com o +50% da dupla). Desconto não é bônus.

### Passo 6. Garantia condicional (padrão recomendado: condicional e mensurável, ligada à execução)
Modelos, condições e casos: `references/garantia-modelos.md`.
1. Estrutura obrigatória: **resultado mínimo mensurável** + **condições de execução** + **prazo igual ao do programa** +
   **evidência exigida** + **como acionar** + **o que é devolvido**.
2. Condições usam os entregáveis reais e são verificáveis: fez o diagnóstico; executou o plano de ação; solicitou e fez as
   análises; compareceu aos encontros; registrou os números mensais; pagou em dia.
3. Resultado mínimo calibrado ao ticket e ao avatar (ex.: faturar pelo menos o valor investido; perder o peso combinado; +X% de
   faturamento). Garantia pequena demais para o ticket do cliente perde força.
4. Resultado abstrato (bem-estar, autoconhecimento): não forçar garantia de resultado; escolho pela recomendação da seção 5 e listo em "Assumi".
5. Garantia legal de 7 dias para compra online existe por lei; não é argumento de venda (na UE a plataforma usa 15 dias). Garantia em dobro: não (foi improviso
   desaconselhado). Texto final validado com advogado (vai no termo ou contrato).
6. Pré-requisito operacional: medir investimento e resultado do aluno todo mês (planilha no drive do aluno ou SNA), senão não há
   como honrar nem negar a garantia.

### Passo 7. Plano do teste de 20 sessões (validação da faixa de preço)
1. Não mexer no preço antes de 20 sessões (regra do squad).
2. Ler a conversão (régua do squad): 10% a 20% = preço e oferta de pé; conversão muito alta (referência: 70%) = sinal de preço baixo;
   abaixo de 5% = diagnóstico de conversão (avatar, oferta ou execução da sessão) antes de culpar o preço. Resultado é multifatorial.
3. Registrar na Central 1x1 (`07-numeros/`, dono `ht-controller`): sessões, ofertas feitas, vendas, objeção principal, condição
   usada (à vista, parcelado, dupla).
4. Preço de fundador (fora do padrão; só se pedirem): primeiras vagas mais baratas, subir conforme chegam cases.

### Passo 8. Cobrança, inadimplência e estrutura fiscal inicial
Checklist para o contador e política de cobrança: `references/cobranca-e-estrutura-fiscal.md`. Pontos que sempre entram:
CNPJ (não MEI, pelo faturamento) e limite de saque com CPF na plataforma; aplicação pela plataforma (acesso automático, taxa maior)
e parcelas por gateway com boleto ou cartão recorrente; cobrança da parcela antes do vencimento; termo ou contrato de compra;
previsão de recebimento (referência: receber cerca de 70% a 80% do vendido; o Master Plan usa a premissa de recebimento do squad).
Não é orientação contábil nem jurídica: tudo vira pergunta ao contador e ao advogado do expert.

### Passo 9. Auditoria e entrega
Rodar a seção 6, gravar e fazer o handoff (seção 7).

## 4. Regras inegociáveis do método

- Preço só em `02-oferta/`; nenhum outro agente cria, muda ou arredonda.
- Padrões recomendados (editáveis em `padroes` do perfil): preço de 5x a 10x a média do nicho, validado em 20 sessões; garantia
  condicional mensurável, com prazo do programa; ordem entrada, parcelado, à vista; sinal de R$ 500 a R$ 1.000, até 10% do
  valor, pago com a call aberta; programa de 12 meses; dupla +50% sobre o individual.
- Sempre à vista e parcelado, individual e dupla. Desconto à vista escrito. Conta conferida.
- Entrada alta trava a compra na hora da oferta (erro de laboratório: entrada de R$ 8 mil); manter o sinal de R$ 500 a R$ 1.000, até 10% do valor.
- HT não se define por valor absoluto e sim pelo múltiplo do nicho; a referência "R$ 2 a 5 mil não é HT" do glossário vale
  como alerta, não como regra contra o múltiplo (caso viola 60+).
- Garantia só mensurável e ligada à execução; nunca abstrata, nunca em dobro, nunca a legal como argumento.
- Comprador de HT é o mais comprometido, não o mais rico: facilitar a forma de pagamento antes de baixar o preço.
- Preço da renovação não é decidido aqui (proposto pelo padrão, por projeto, via `ht-renovacao`).
- Nada inventado: preço de concorrente sem fonte não entra; número de referência é "referência, conferir".

## 5. O que decido pelo padrão e o que fica para a Aprovação 1

Não abro lote de perguntas. Decido pela recomendação, sigo e listo em "Assumi: X, Y, Z (é só pedir para mudar)". Preço e
garantia propostos valem só como proposta e viram oficiais na Aprovação 1, como um "posso seguir?" simples:
- **Preço final** entre os 3 cenários (proponho o do meio); **preço acima de 10x** a média (só com prova forte); **preço de fundador** para as primeiras vagas.
- **Modalidade**: tabela padrão; P2P ou Fake HT só se o avatar não tiver caixa.
- **Garantia**: resultado mínimo e condições; em nicho abstrato, recomendo a garantia condicional ligada só à execução e a um
  indicador observável (as outras saídas: sem garantia de resultado, só a legal, ou aplicação reembolsável após o diagnóstico).
- **Garantia incondicional estendida** (ex.: 30 dias, citada como mais forte que a de 7): fora do padrão de garantia condicional; só como
  opção, nunca padrão.
- **Trio** (fora do padrão) e piso de negociação: proponho o piso.
- **Número de parcelas** (sem padrão fixo no squad; parcelamento definido por expert): proponho um número pelas referências do Passo 3 e listo em "Assumi".
- **Bônus à vista** (segunda cadeira ou outro): recomendo um.
- **Estrutura fiscal** (quem fatura, divisão entre o expert e você ou a agência do perfil, se houver): só deixo a pergunta pronta para o contador.

## 6. Critério de pronto e auditoria final

**Critério de pronto**
- [ ] Média do nicho com 3+ fontes citadas; faixa de 5x a 10x calculada.
- [ ] 3 cenários com vendas necessárias para a meta e risco; recomendação.
- [ ] Tabela individual e dupla, à vista e parcelado, entrada (sinal) dentro do padrão; conta conferida linha a linha.
- [ ] Ordem entrada → parcelado → à vista e piso de negociação registrados para o closer.
- [ ] Bônus à vista validado ou ausência justificada.
- [ ] Garantia com os 6 elementos, condições ligadas a entregáveis reais, prazo do programa (ou ausência de garantia de resultado, registrada no "Assumi").
- [ ] Plano do teste de 20 sessões e o que fazer com cada faixa de conversão.
- [ ] Checklist de cobrança e fiscal com as perguntas para o contador.
- [ ] "Assumi" no fim da entrega e "posso seguir?" simples para a Aprovação 1.

**Auditoria (erros dos laboratórios e das lives)**
1. Preço chutado sem média do nicho nem prova; preço fora da faixa sem estar no "Assumi".
2. Conta que não fecha (total parcelado menor que o à vista; parcelas x valor diferente do total; placeholders da planilha).
3. Entrada alta ou diferente entre à vista e parcelado.
4. Desconto à vista pequeno ou não escrito; lead obrigado a fazer conta.
5. Preço sem garantia e sem estar no "Assumi"; garantia abstrata; garantia legal usada como argumento; garantia em dobro; garantia mal calibrada ao ticket.
6. Bônus à vista que faz adiar a compra, que é essencial, ou que é desconto disfarçado.
7. Mudança de preço antes de 20 sessões; preço baixado por objeção de dinheiro que era medo ou prioridade.
8. Cobrança de ticket alto só no cartão cheio; Fake HT que esconde o compromisso anual.
9. Copiar o preço de um caso de outro contexto (resultado é multifatorial).
10. Preço da renovação decidido aqui.

## 7. Saída e handoff

- Gravar `02-oferta/rascunhos/AAAA-MM-DD-preco-pagamento-garantia.md` (+ planilha, se pedida) e o bloco de entrega do `ht-protocolo`.
- Revisão: `ht-revisor-metodo-copy` (método e texto da garantia); a conta é conferida também pelo `ht-controller`.
- Próximo: `ht-oferta-matadora` (integra na oferta para a Aprovação 1). Depois de aprovado: `ht-closer` (ordem entrada → parcelado → à vista, sinal,
  piso, garantia na fala), `ht-controller` (Master Plan e Central 1x1 com o ticket), `ht-gestor-automacoes` (links de pagamento e
  cobrança recorrente, só com OK da pessoa).

## 8. Ferramentas de apoio (por nome)

- `anthropic-skills:xlsx`: calculadora de preço e tabela (à vista, parcelado, dupla, P2P, Fake HT).
- `leitura-web`, `niche-research`: levantar preços do nicho quando o `ht-pesquisador` pedir apoio (fonte citada).
- `hotmart-meta-conversao`: só se for preciso ligar a compra da aplicação ao pixel (tarefa do `ht-gestor-trafego`).
- `avoid-ai-writing`, `humanizer`: texto da garantia.

## 9. Lacunas (não inventar)

Não há fórmula de preço além dos múltiplos e faixas citadas; a taxa da plataforma para HT não foi dada; o texto oficial da garantia condicional não existe (só exemplos); a rotina de cobrança e inadimplência só tem "receber 70% a 80%" e "cobrar antes do vencimento"; contratos e termos não têm modelo: validar com o advogado e o contador do expert; o preço de um programa de referência varia entre R$ 80 mil e R$ 100 mil conforme o caso (conferir).
