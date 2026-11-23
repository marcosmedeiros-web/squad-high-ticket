# LDP: calculadora de metas, orçamento e cronograma reverso

Números de referência são indicativos, nunca garantia; o plano
do expert usa os números próprios assim que existirem (`07-numeros/`, debriefs anteriores em `13-aprendizados/`).

## 1. Calculadora (de trás para frente)

```
ENTRADAS
  V  = vagas reais (capacidade de absorver alunos novos agora)      -> meta de vendas = V
  c  = conversão sobre presentes (planejar 0,02 a 0,03; faixa de referência 0,02 a 0,05; ~0,03 no caso de referência)
  a  = comparecimento sobre inscritos (0,20 a 0,30; protocolo: 0,25)
  CPL = custo por cadastro pago (do histórico do expert; sem histórico: perguntar ao ht-gestor-trafego)
  O  = cadastros orgânicos esperados (soma das listas x taxa de resposta estimada; marcar como estimativa)

CONTAS
  presentes necessários  P = V / c
  inscritos necessários  I = P / a
  cadastros pagos        Ipago = max(0, I - O)
  verba de tráfego       = Ipago x CPL   (+ até R$ 2 mil de API oficial, se usar)
  receita em contrato    = vendas x preço vigente (02-oferta, citar versão)

CENÁRIOS (sempre os três no plano)
  conservador: c = 0,02 ; a = 0,20
  base:        c = 0,03 ; a = 0,25
  otimista:    c = 0,05 ; a = 0,30
```

Exemplo de referência: V = 1, c = 0,03, a = 0,25 → P ≈ 37 presentes → I ≈ 150 inscritos.
Exemplo de conta para 5 vagas no cenário base: P = 5 ÷ 0,03 ≈ 167; I = 167 ÷ 0,25 ≈ 667 inscritos.

Leitura: se I fica muito acima do que as listas alcançam, há três saídas (a skill assume a primeira e lista em "Assumi"): reduzir V, pôr verba, ou trocar
de ação. Não aumentar a conversão no papel para fechar a conta.

**Recuperação conta como parte da meta.** O método diz que a conversão da sessão 1a1 vinda do pós-LDP tende a ser igual ou um
pouco maior que a da sessão comum. Projetar as vendas da recuperação com a conversão de sessão do expert (`03-sessao/`), à parte
das vendas da live.

## 2. Orçamento de referência (casos anonimizados, conferir antes de citar)

| Caso | Investimento | Cadastros | Resultado citado |
|---|---|---|---|
| acelerador de carreira (pilotos de simulador) | ~R$ 6.860 (API + pouco tráfego) | 2.933 | ~R$ 506 mil em contrato, live de 1h55 |
| acelerador de conquista pessoal (finanças) | ~R$ 20 mil | ~1.000 | ~R$ 600 mil, repetido a cada 45 dias após lançamento clássico |
| acelerador de carreira (terapeutas) | ~R$ 2.400 | 500 | ~R$ 183 mil |
| acelerador de carreira (saúde e educação), LDP para vender ingresso de evento de R$ 3 mil | ~R$ 20 mil | n/d | ~R$ 232 mil (conferir: unidade a confirmar) |

Mínimo possível: zero (grupos, e-mail, convite orgânico). API oficial: dificilmente passa de R$ 2 mil. Um criativo basta.

## 3. Cronograma reverso (modelo; D0 = quinta da live)

O cronograma do método só fixa: captação de ~10 a 11 dias, live quinta 19h/20h, lembretes da véspera ao pós-abertura e contato no
dia seguinte. As datas de preparação abaixo são montagem do squad a partir dessas regras (marcar "inferido" no plano).

| Quando | O quê | Dono | Revisão |
|---|---|---|---|
| D-18 a D-15 | Ativos, metas, narrativa, CTA, orçamento; **portão de prontidão decidido em D-15** (go, go condicional com OK escrito, no-go; `ht-protocolo` §3.6); data conferida contra feriado e recesso; decisões assumidas e listadas em "Assumi" | ht-produtor-eventos, ht-controller | Diretor |
| D-15 a D-12 | Promessa, convites, criativo, página, pesquisa, formulário de aplicação, lembretes | ht-diretor-copy | ht-revisor-metodo-copy |
| D-14 a D-12 | Página no ar em prévia, grupo de avisos criado, pixel com evento Lead no envio da pesquisa, link de pagamento ou agenda no fim da aplicação | ht-web-designer, ht-gestor-automacoes | ht-revisor-visual |
| D-12 | Criativo gravado e editado; campanha montada PAUSADA | ht-gestor-trafego | ht-revisor-metodo-copy (compliance Meta) |
| D-11 (segunda) | Abre captação: convites às listas, OK simples da pessoa para ativar campanha e disparos | OK da pessoa, automações | n/a |
| D-11 a D-1 | Relatório diário: cadastros, entrada no grupo, respostas da pesquisa (nível de consciência e intenção) | ht-controller | n/a |
| D-7 | Roteiro da live pronto; 4 objeções eleitas; ensaio com o expert | ht-roteirista-palco | ht-revisor-metodo-copy |
| D-3 | Leitura da pesquisa: se a maioria "te conheceu agora", alertar a pessoa (sinal de formato errado) | ht-produtor-eventos | n/a |
| D-1 | Lembrete de véspera (grupo + e-mail 1); teste da sala e dos links | automações, produtor | n/a |
| D0 manhã / 1h antes / na hora / +10 min | Lembretes do grupo; e-mail 2 no dia | automações | n/a |
| D0 | Live | expert | n/a |
| D+1 | Equipe liga para todos os cadastrados (ordem: intenção alta primeiro); aprova aplicações | ht-closer (rascunhos), equipe do expert | n/a |
| D+1 a D+7 | Recuperação e sessões 1a1 dos que não viram a live | ht-closer | n/a |
| D+7 | Debrief em 13-aprendizados | ht-produtor-eventos | Diretor |

## 4. Painel do dia seguinte (campos mínimos)

inscritos · entraram no grupo · responderam a pesquisa · presentes no pico · presentes no momento do CTA · aplicações ·
aprovados · vendas na live · ligações feitas · sessões 1a1 agendadas · vendas da recuperação · objeções anotadas (contagem por tipo).
