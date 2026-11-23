# Agente de IA de SLG, registro e delegação à equipe

Referência da `ht-slg`.

## 1. Como usar o agente de IA

Um agente de IA de SLG recebe a definição do AR e o nome da sessão, depois o
print do perfil do lead, e devolve a desarmadora; com a resposta do lead (texto ou print), devolve condução e arremate. Uso
ensinado: print do perfil (Instagram funciona melhor; link do LinkedIn deu erro), revisão humana de coerência, linguagem e
ponto de conexão real. "A IA é o meio, não o fim": o que denuncia a mensagem é o uso genérico. O prompt a seguir é do squad.
Alerta: a desarmadora que o agente gera costuma já puxar para o negócio do expert. Toda
desarmadora vinda de IA passa pelo critério 4 da auditoria (zero cara de venda) antes de ir ao lote.

## 2. Prompt de trabalho do squad

Usado pelo `ht-sdr` para rascunhar.

```
Você rascunha mensagens de Social Lead Generation (método do Squad HT) para o expert [nome], que vende [definição do AR, de 02-oferta].
O convite é para a sessão "[nome da sessão, de 03-sessao]", gratuita.
Avatar e corte: [resumo do avatar e características mínimas].
Voz do expert: [3 traços de voz e 2 exemplos curtos de como ele escreve].

Regras: objetivo é vender o agendamento, nunca o programa; sem preço, link ou nome do programa; uma pergunta por mensagem;
mensagens curtas, a desarmadora em 2 partes (cumprimento com o nome; contexto + ponto de conexão + pergunta);
sem travessão, sem aspas, sem três adjetivos seguidos, sem "dei uma olhada rápida", sem abertura ou fecho de robô;
ponto de conexão tem de ser algo que aparece no material abaixo, nunca inventado.

Lead: [nome] · fonte/contexto: [como chegou] · material do perfil: [print ou texto: bio, últimos posts, destaques].
Etapa pedida: [desarmadora | condução | arremate]. Resposta do lead até aqui: [texto].

Devolva: a mensagem (ou as 2 partes), o ponto de conexão usado e onde ele está no perfil, e por que a pergunta não tem cara
de venda. Se o perfil não dá ponto de conexão verdadeiro ou o lead não passa na qualificação, diga isso em vez de escrever.
```

Depois: passar por `avoid-ai-writing` e `humanizer`, conferir com a seção 5 de `mensagens.md`, entregar como rascunho.

## 3. Registro na Central 1x1 (formato padrão)

Uma linha por lead a partir de quando é qualificado e abordado:

| Coluna | Preenchimento |
|---|---|
| Nº, Nome | |
| Origem do lead | Social (SLG), Orgânico, Tráfego, Bônus, Outbound |
| Desarmadora / Condução / Arremate | Sim / Não em cada |
| Sessão agendada? / Sessão realizada? | Sim / Não (agendar não é fazer) |
| Data da sessão | |
| Oferta à vista / Oferta parcelada | Valores de 02-oferta apresentados |
| Fazer follow-up (data) | Data combinada na sessão |
| Status conversão | Converteu / Não converteu |
| Valor do contrato | |
| Anotações da negociação / Objeções identificadas | |
| Link do Raio-X | |

A planilha de referência tem fórmulas de comparecimento e conversão por origem; um defeito de fórmula fazia a conversão geral passar
de 100% (conferir ao copiar). No squad, o SDR grava `04-demanda/slg/central-1x1-slg.csv`; o consolidado é do
`ht-central-e-kpis` em `07-numeros/`.

## 4. Delegar o SLG à equipe

- A desarmadora sai do perfil do expert (perfil de membro do time quase nunca funciona). A equipe opera o perfil pelo Meta
  Business Suite e assume depois da 2ª mensagem ou quando a conversa vai ao WhatsApp.
- Mesma linguagem do expert. Se o lead perguntar "é você?", nunca mentir: "aqui é [nome], da equipe do [expert]" ou o expert
  assume a conversa.
- Processo para validar quem entra: no começo, a pessoa usa só as mensagens do modelo e chama o expert se a conversa não
  desenrolar nas três etapas.
- SLG funciona como SDR: qualifica antes do closer; lead qualificado chega mais quente à sessão (casos de 80% a 90% de
  conversão citados, amostra pequena, conferir).
- Custo de referência dito em aula para uma pessoa de SLG: R$ 1.000 a 1.500 por mês, que se paga com uma venda (conferir;
  contratação é decisão do expert).
- Regra do kit: equipe nenhuma envia em massa, e o squad não envia nada; o rascunho segue para o OK do estrategista.
