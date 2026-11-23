# Formulário, tag e segmentação pós-clique

Referência da `ht-pagina-inscricao-sessao`.

## 1. Formulário da sessão (padrão do método)

| Campo | Obrigatório? | Motivo |
|---|---|---|
| E-mail | Sim | Identifica o lead no e-mail marketing |
| Telefone (WhatsApp) | Sim | A equipe liga e agenda; "muito importante" |
| Nome | Opcional | Abordar pelo primeiro nome; tirar se o formulário ficar grande |
| Melhor período (manhã, tarde, noite) | Opcional, recomendado | O agendamento oferece 2 horários dentro do período (padrão do squad) |
| Pergunta de corte | Só com segmentação | Seção 3 |

Configuração:
- Tag do tipo `solicitou-diagnostico` (ou `solicitou-[nome-da-sessao]`); toda inscrição recebe a tag.
- Confirmação simples, sem dupla confirmação.
- Destino de confirmação: a página de obrigado própria.
- Texto de LGPD no rodapé da página (a aula tirou o bloco de LGPD do formulário para encurtá-lo).
- Nome do formulário claro ("Solicitação de [nome da sessão]") e anotado com a URL, a tag e o destino num documento do projeto.
- Aviso à equipe: cada inscrição gera alerta para quem agenda (o contato em minutos é do `ht-agendamento-e-follow-up`); a
  automação de aviso interno é do `ht-gestor-automacoes`; qualquer mensagem automática ao lead só liga com OK do estrategista.

**Não perguntar:** quanto a pessoa quer investir; se prefere grupo ou individual. Cada campo a mais reduz a
conversão; perguntas de diagnóstico ficam para o Raio-X na sessão.

## 2. Formulário de aplicação (quando o projeto usa aplicação)

Se a sessão é precedida de aplicação (gratuita ou paga), o desenho da ficha, do pagamento e da seleção é do
`ht-agendamento-e-follow-up` (aplicação e seleção). Esta skill só garante que a página leve à aplicação e que a tag e o
obrigado estejam certos.

## 3. Segmentação pós-clique

**Quando usar:** o expert tem mais de um destino para o mesmo público (HT e produto de entrada; HT e repasse a parceiro) e o
criativo atrai gente de níveis diferentes. Regra: o criativo atrai qualquer persona; a segmentação vem
depois, no formulário.

**Desenho:** mesmo criativo, mesmo formulário, destino diferente conforme uma resposta.
```
Pergunta de corte: [Qual é hoje o seu [faturamento mensal / gasto médio / tempo de atuação / situação]?]
Opções: [abaixo de X] · [entre X e Y] · [acima de Y]
Regra:  acima do corte   → obrigado da sessão + tag solicitou-[sessao] + contato da equipe para agendar
        abaixo do corte  → [página do produto de entrada do expert / cadastro da aula semanal / repasse] + tag [destino]
```
Exemplo (estrutura): formulário com nome, e-mail e média de gasto; acima de um valor, sessão do HT; abaixo, página do
produto de entrada. O corte citado no exemplo era específico daquele expert; aqui o valor é assumido e conversa com a
parcela de `02-oferta`.

**Variações citadas:**
- Três linhas no funil: direto para o produto de entrada, direto para a aplicação, e o formulário que faz a divisão.
- Encaminhamento condicional no agendamento: quem não pretende decidir agora ou não tem o perfil não recebe o calendário, mas
  os dados ficam para contato posterior.
- Copy diferente para iniciante e experiente mesmo com o mesmo criativo.

**Cuidados:** a segmentação não substitui a qualificação do SLG nem o Raio-X; perguntas mínimas; o destino de quem fica abaixo
tem de existir e estar pronto antes de ligar (senão o lead cai no vazio).

## 4. Para onde vai o contato

Especificar no arquivo do formulário: ferramenta de e-mail/CRM, lista ou tag, quem recebe o aviso, em quanto tempo o lead é
chamado, e como o lead entra na Central 1x1 (origem "Tráfego" ou "Orgânico", conforme a fonte; ver `ht-slg`, agente e
registro).
