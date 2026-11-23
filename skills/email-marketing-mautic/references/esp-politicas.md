# Servico de envio para infoproduto e educacao em marketing digital: padrao e reservas

Pesquisa feita em 18/10/2026 nas politicas publicas de cada servico. As citacoes sao curtas e literais; o resto e
parafrase. Releia as fontes antes de decidir por um cliente: politica muda, e a data de cada uma esta ao lado.

## Decisao do pacote: Resend como padrao, SES e SendGrid de reserva

**Padrao: Resend**, com uma guarda. Das tres politicas, a do Resend e a unica que proibe pelo nome "get rich quick" e
que guarda o direito de recusar qualquer negocio que ele considere de alto risco, com desligamento possivel sem
aviso, alem do teto de reclamacao mais baixo. Curso e educacao em marketing digital nao sao "get rich quick" por si;
o que aproxima e a copy que promete renda. Por isso, com `EMK_ESP=resend`, a regua de copy do pacote e GUARDA DO
ENVIO: o texto com promessa de ganho reprova no plano, no canario, no lote e no resto, e nao sai. Nao existe opcao
para passar por cima.

**Reservas, nesta ordem: Amazon SES, depois SendGrid** (`EMK_ESP_RESERVA=ses,sendgrid`). Sao para quando o Resend
recusar o dominio ou cortar a conta: `email-mkt envio recuar` aplica a primeira reserva que ja tem credencial no
cofre. Nenhuma das duas politicas nomeia o nicho.
- SES: o mais barato por mil envios e com limites publicados em numero. Conta nova nasce em "sandbox" (so manda para
  endereco verificado) ate a AWS aprovar o acesso de producao; a aprovacao nao e garantida nem tem prazo, entao o
  pedido deve ser feito ANTES de precisar da reserva.
- SendGrid: sem plano gratuito permanente e com revisao de conformidade na conta nova.

Reserva so serve se estiver pronta antes do corte: dominio verificado no servico, DNS publicado
(`email-mkt dns conferir` com `EMK_ESP` da reserva) e credencial no cofre.

## O que cada politica diz

### Resend: Acceptable Use Policy
Fonte: https://resend.com/legal/acceptable-use (pagina atualizada em 13/10/2026).

- Conteudo proibido inclui, entre outros, "Get rich quick opportunities" e marketing multinivel ou piramide.
- Proposito proibido: negocio que, a criterio dele, seja enganoso, antietico ou de alto risco.
- Exige opt-in explicito de todo destinatario; proibe lista comprada, raspada e prospeccao fria.
- Envio em volume: descadastro sem atrito e atendido em ate 7 dias, endereco valido e nome da empresa.
- Limites: reclamacao abaixo de 0,08% e bounce abaixo de 4%; acima disso a conta pode ser desligada sem aviso.

### SendGrid (Twilio): Email Policy
Fonte: https://www.twilio.com/en-us/legal/service-country-specific-terms/email (atualizada em 09/04/2026), junto
com a AUP da Twilio (https://www.twilio.com/en-us/legal/aup, atualizada em 12/05/2025).

- Conteudo proibido: pornografia, acompanhantes, alegacao de saude sem aprovacao, remedio controlado e conteudo
  fraudulento (cita corrente e piramide). Nao fala em "get rich quick", afiliado nem renda.
- Exige consentimento afirmativo, prova do consentimento guardada, e novo consentimento depois de longo tempo sem
  interacao; proibe lista comprada e endereco tirado da internet ou de rede social.
- E-mail que nao e transacional precisa de endereco fisico, link de descadastro funcionando e link da politica de
  privacidade; pedido de descadastro atendido em ate 10 dias.
- Nao publica limite numerico; fala em numero "irrazoavel" de reclamacoes, decidido caso a caso.

### Amazon SES: AWS AUP e Service Terms
Fontes: https://aws.amazon.com/aup/ (atualizada em 01/07/2021), https://aws.amazon.com/service-terms/ (secao 15,
pagina atualizada em 13/10/2026) e https://docs.aws.amazon.com/ses/latest/dg/faqs-enforcement.html.

- A AUP proibe spam (e-mail em massa nao solicitado). Nao nomeia categoria de conteudo do nicho.
- A secao 15 permite suspender a conta que descumpre a AUP e cita e-mail abusivo ou de baixa qualidade.
- Limites publicados: bounce de 5% poe a conta em revisao e 10% pode pausar; reclamacao de 0,1% poe em revisao e
  0,5% pode pausar.
- Revisao manual pode acontecer por e-mail que parece nao solicitado ou por uso que o SES nao suporta.

## O que vale para os tres (e o pacote cobra)

- Lista so com opt-in de verdade. Comprar, alugar ou raspar lista derruba a conta em qualquer um.
- Descadastro funcionando e de um clique: por isso a lista fica bloqueada ate o HTTPS publico e a prova do canario.
- Nome da empresa e endereco fisico no rodape: o plano do disparo recusa sem os dois.
- Reclamacao e bounce baixos: lote piloto antes do resto, e limpeza de quem nao abre ha meses.
- A copy importa: promessa de renda e o que transforma "educacao" em "get rich quick" aos olhos de quem modera.

## Troca entre servicos

`email-mkt envio recuar` (corte do Resend) ou `email-mkt envio aplicar --esp ses|sendgrid|resend` (troca
planejada) troca o `mailer_dsn` do Mautic com backup e volta atras (`email-mkt envio reverter`). Antes de trocar, o dominio tem que estar verificado no servico novo e o DNS conferido
(`email-mkt dns conferir`). Depois, a prova e uma mensagem real: `email-mkt envio teste` e `envio conferir-eml`.
