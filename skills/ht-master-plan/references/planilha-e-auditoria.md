# A planilha do Master Plan: modelo original, versão do squad e auditoria

## 1. O modelo original (como é)
Duas abas.
- **PRODUTOS HT**: blocos HT 1 a HT 3 (mais um em branco), cada um com O que é, Pra quem é, Roma, Ticket, Canais de venda.
- **PLANEJAMENTO 7 ANOS** (título "MASTER PLAN"): colunas B a I = 8 anos (2026 a 2033 na versão atual). Linhas 5 e 8:
  faturamento acumulado e líquido anual de todos os HTs. Por HT: meta de novos, ticket, faturamento com novos, % de renovação,
  número de renovados, ticket de renovação, faturamento só de renovação, total de clientes, bruto novos + renovação, margem de
  custo (%), previsão de custos, líquido, bruto acumulado. Só as células amarelas são editáveis.
- Regras do modelo: fazer cópia antes de editar; mexer só nas amarelas; se a fórmula quebrar, baixar de novo o modelo;
  compartilhar com "qualquer pessoa com o link pode ler" para feedback.

## 2. Defeitos conhecidos do modelo (conferidos nas fórmulas)
1. HT 1, C19: `C16*70000` (número fixo) em vez de `C18*C16`.
2. HT 1, C16: renovação usa só os novos do ano anterior (`B11*C15`); HT 2 e HT 3 usam o total de alunos do ano anterior.
3. HT 2, D38: `D36+D29` soma o **ticket** em vez do faturamento dos novos (`D36+D30`).
4. Cabeçalhos: HT 2 mostra 2034 no lugar de 2033; HT 3 começa em 2027 e termina em 2034.
5. "Margem de custo" (no modelo, é o % de CUSTO) de 60% pré-preenchida em células do HT 2 (D39:G39) e de 10% no exemplo,
   enquanto a aula usa 40% de custo. No squad vale o padrão do squad: 40% de MARGEM, ou seja, 60% de custo.
6. Linha 5 (acumulado) às vezes só traz os anos; conferir se puxa as fórmulas.
7. A margem é aplicada sobre o bruto em contrato; o modelo não tem linha de recebido.

## 3. Versão do squad (gerada por `gerar_master_plan.py`)
Mantém a lógica e os rótulos do modelo original e corrige:
- renovação sempre sobre o total de clientes do ano anterior, inclusive no HT 1;
- faturamento de renovação = renovados x ticket de renovação em todos os anos;
- novos + renovação soma faturamentos;
- linha de **recebido** (% de recebimento sobre o contrato) e **margem de lucro** de 40% sobre o recebido (padrão do squad), com
  custo = recebido x (1 - margem) = 60%; no modelo original o número da linha "margem de custo" é o % de custo (40% no modelo);
- linha de alunos já ativos antes do ano 1 (quem já tem base pode ter renovação no ano 1);
- anos calculados do ano inicial;
- abas extras: PREMISSAS (com a fonte de cada número), NÚMERO MÁGICO (por mês, por semana, plano por canal, funil reverso 1a1)
  e CAPACIDADE (padrão do squad).
Uso: `python3 gerar_master_plan.py --exemplo > entrada.json`, editar o JSON, `python3 gerar_master_plan.py entrada.json
saida.xlsx`. Testado em 22/11/2026 com 1 e 3 HTs, recalculado no LibreOffice: contas conferidas à mão (ex.: ano 2 com 36 novos a
R$ 10 mil + 12 renovados a R$ 10 mil = R$ 480 mil de contrato; 80% recebido = R$ 384 mil; custo de 60% = R$ 230,4 mil; líquido de 40% = R$ 153,6 mil). Refeito em 23/11/2026 depois da
correção da margem: ano 3 = 52 novos x R$ 10 mil + 24 renovados x R$ 10 mil = R$ 760 mil; recebido R$ 608 mil; custo R$ 364,8 mil;
líquido R$ 243,2 mil; com 10 alunos de base a 50% no ano 1: 5 renovados, R$ 290 mil de contrato e R$ 92,8 mil de líquido.
Se o estrategista preferir o modelo original, copiar o arquivo dele, corrigir os defeitos da seção 2 e registrar.

## 4. Regras de preenchimento (método)
1. Projeção **conservadora**: se o conservador agrada, o resto é lucro. Exemplo de referência: previu 12 mentorias no ano 1 e fez
   32; previu 30 no ano 2 e fez 170.
2. **Ano 1 de pé no chão, dividido por semana** para testar; pergunta-guia: "se eu chegar no fim do ano com esse
   faturamento, estou tranquilo?"; "consigo vender 1 por mês? 2? 1 por semana?".
3. Crescimento realizável de 20% a 25% ao ano; crescimento não é infinito (mesmo um ano de +50% foi chamado de atípico).
   Também se sugere ser mais audacioso nos anos 1 a 3: registrar o cenário usado.
4. Sem referência de ticket: R$ 10 mil e a sequência de novos do exemplo (24, 36, 52, 70, 80, 90, 100), marcados provisórios. No
   squad, ticket real vem de `02-oferta`.
5. **Renovação**: 50% padrão do squad (valores de referência variam de 30% a 90%). Ano 1 sem renovação, salvo base existente.
6. **Ticket de renovação**: sem regra fixa, definido por projeto: assumo o mesmo ticket da venda e listo em "Assumi" (opções: menor, igual, reajuste), marcado "provisório".
7. **Margem (lucro)** de 40% sobre o recebido, custo de 60% (padrão do squad): imposto, equipe de entrega, comissão, tráfego.
   No modelo original o número da linha "margem de custo" é o custo (40%); o squad usa 60% de custo até haver dado próprio. Faturamento não
   é dinheiro no bolso.
8. **Total de clientes** = novos do ano + renovados do ano anterior.
9. **HT 2 e HT 3** começam no ano em que fizer sentido (GIC só depois de o AR gerar resultado; regras e ticket do GIC: em aberto, assumo o padrão e listo em "Assumi").
10. Ler o **acumulado e o líquido** e perguntar se o número em 7 anos é o que o expert quer e se é viável; ajustar meta e ticket.
11. O Master Plan é **vivo**: revisado linha a linha no plano de ação (o mentor alinha expectativa com a realidade) e atualizado
    depois de cada ciclo de 20 sessões, evento ou renovação, com o número real.
12. Duração do programa: 12 meses, ajustável de 11 a 13 para cair no ciclo de renovação.

## 5. Auditoria (erros comuns)
1. Imersão listada como HT (é canal de venda); EHT planejada no ano 1 sem público de topo.
2. Canais de captação (Instagram, LinkedIn, anúncio, palestra sem pitch) listados como canal de venda.
3. Dois públicos ou dois HTs para públicos diferentes.
4. GIC sem gente com resultado, aberto cedo, ticket abaixo de 50% acima do AR, ou curso chamado de GIC.
5. "R$ 997 em 21 dias" ou qualquer produto de entrada tratado como AR.
6. Ticket baixo para público profissional que ganha dinheiro com o tema.
7. Renovação sem motivo (formação não renova: combinar com AR ou GIC).
8. Meta do ano 1 maior que a do ano 2 (metas invertidas) ou irreal frente ao plano por canal.
9. Margem vazia ou zero; margem aplicada sobre contrato em vez de recebido; margem e custo trocados (40% digitado como custo
   quando o padrão do squad manda 40% de lucro e 60% de custo).
10. Fórmulas quebradas, valor digitado sobre fórmula, anos trocados (defeitos da seção 2).
11. Roma vaga na aba PRODUTOS HT.
12. Ticket que não bate com `02-oferta` ou sem a marcação "provisório".
13. Clientes ativos acima de 20 sem mentor ou navegador previsto (padrão do squad).
14. Plano por canal que não fecha a meta de novos (diferença negativa sem plano de ação).
