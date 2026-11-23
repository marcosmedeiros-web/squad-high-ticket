---
name: email-marketing-mautic
description: Monta e opera o e-mail marketing proprio do dono no Mautic da VPS. Poe o Mautic num endereco publico com HTTPS (descadastro, clique e abertura funcionando), confere SPF, DKIM e DMARC de fora, envia pelo Resend (padrao) com a regua de copy como guarda, recua para Amazon SES ou SendGrid (reservas) quando o Resend recusar ou cortar a conta, com volta atras, cria segmentos e e-mails e dispara para segmento com canario, lote piloto e OK do dono por disparo, e liga os vigias do cron e do disco (binlog). Use quando o dono disser "e-mail marketing", "Mautic", "disparar e-mail para a lista", "mandar e-mail para o segmento", "descadastro nao funciona", "HTTPS do Mautic", "trocar Resend por SES", "usar SendGrid", "o Resend cortou a conta", "o Resend recusou", "e-mail caiu no spam", "SPF", "DKIM", "DMARC", "disco cheio do Mautic", "cron do Mautic parou". NAO escreve a copy (isso e do agente copywriter do kit, revisada pelo agente revisor de copy), NAO compra lista, NAO manda para quem nao deu opt-in, NAO dispara sem o OK do dono para aquele e-mail, e NAO instala o Mautic (isso e do instalador do kit).
---

# E-mail marketing proprio (Mautic + HTTPS + disparo seguro + troca de servico de envio)

O dono entrega a conta e a credencial do servico de envio, o acesso ao DNS e o subdominio. O resto e seu: instalar
este pacote, publicar o Mautic com HTTPS, provar o descadastro de fora, conferir o DNS, operar o disparo e vigiar.
Tudo aqui vem de procedimento medido em producao; os porques estao em `references/gotchas-mautic.md`.

Comando: `email-mkt` (atalho do instalador). A ULTIMA linha de todo comando e `MOTIVO=<codigo> ... rc=<n>`:
0 ok, 1 reprovado ou recusado por trava, 2 nao consegui medir (trate como "nao", nunca como ok), 3 perfil.

## Regras que nao se negociam
1. **Nenhum disparo para segmento sem o OK do dono para AQUELE e-mail.** O OK e o codigo que `disparo plano` imprime.
   Mudou uma letra depois do OK, o codigo muda e nada sai: refaca o plano e peca de novo.
2. **A lista fica bloqueada ate o HTTPS e o descadastro funcionarem**, medidos de fora e provados numa mensagem real.
   Essa trava e codigo (`https_mod.guarda`), nao combinado. Nao contorne.
3. **Nunca imprima chave, senha, DSN ou o `local.php`.** Credencial so em arquivo 600, apontado pelo perfil. Nunca
   peca credencial pelo chat: o dono grava o arquivo direto no servidor.
4. **Depois do POST de segmento nao ha freio.** Por isso a ordem e sempre: plano, canario, lote piloto, conferencia,
   resto. Nunca pule o lote piloto.
5. **Opt-in de verdade.** Lista comprada, raspada ou "de um parceiro" nao entra. Se o dono pedir, explique que derruba
   a conta em qualquer servico de envio e recuse.
6. **"Nao consegui medir" (rc 2) nunca vira verde** no relatorio para o dono.

## Ordem de montagem (primeira vez)
1. `email-mkt descobrir` e copie as linhas para o perfil (modelo em `perfil/email.exemplo.env`, fora do pacote).
2. Servico de envio: o padrao e o **Resend**. Diga ao dono, em uma frase, que a politica do Resend proibe "get rich
   quick" e que por isso o pacote barra, sem excecao, texto com promessa de ganho. Peca tambem uma **reserva** pronta
   (SES ou SendGrid, com o dominio verificado e a chave no cofre): e o que segura a operacao se o Resend cortar.
   No SES, redija com ele o pedido de acesso de producao (como a lista foi formada, opt-in, descadastro).
3. `bash instalar-email-marketing.sh --perfil <perfil> --destino <kit> --so-conferir`, depois sem `--so-conferir`
   e com `--com-vigias`.
4. `email-mkt binlog conferir`. Exposto? `email-mkt binlog aplicar`, mostre o arquivo gerado, e com OK
   `email-mkt binlog aplicar --executar` (recria os containers; o Mautic fica fora uns segundos).
5. **HTTPS:** o dono cria o registro A do subdominio apontando para a VPS (ou voce cria, com a credencial do DNS
   dele). `email-mkt https caddy --modo container|host --upstream <alvo>` gera o bloco do Caddy; aplique no proxy da
   VPS. Depois `email-mkt https site-url --aplicar`.
6. **DNS do remetente:** o dono verifica o dominio no servico de envio; voce publica os registros que o servico
   pedir. SPF: EDITE o registro que existe, nunca crie um segundo. DKIM sem proxy. `email-mkt dns conferir` ate rc 0.
7. **Servico de envio:** `email-mkt envio aplicar` (le a chave do cofre, troca, reinicia o worker e prova).
8. **Prova de fora:** um e-mail de segmento de teste, `EMK_MODO=canario`, `disparo plano` e `disparo canario`. O dono
   salva a mensagem recebida como `.eml` e voce roda `email-mkt https conferir --eml <arquivo>`. rc 0 = selo gravado,
   lista liberavel. Mostre ao dono o que passou.

## Gestor de disparo (cada e-mail)
1. Copy pelo agente copywriter do kit, revisao pelo agente revisor de copy. O rodape tem que ter `{unsubscribe_url}` em link,
   o nome da empresa e o endereco exatamente como no perfil.
2. Segmento: `email-mkt segmentos listar`; segmento novo a partir de um JSON de filtros com `segmentos criar`.
   Para quem nao abre ha meses, proponha frequencia menor, nunca "apagar sem perguntar".
3. `email-mkt email criar --nome --assunto --html <arquivo> --segmento <id>` (nasce despublicado).
4. `email-mkt disparo plano --email-id <id>`: mostre ao dono assunto, segmento, quantos pendentes e o codigo.
   Achou copy de risco? Mostre os trechos. No Resend o plano, o canario, o lote e o resto RECUSAM ate a copy ser
   reescrita sem promessa de ganho; nao existe opcao para passar por cima.
5. Com o OK (o dono responde com o codigo): `disparo canario`, confira a caixa do dono; `disparo lote`; confira a
   primeira abertura e as falhas; `disparo resto`. O e-mail fica despublicado no fim.
6. Relatorio ao dono: enviados, falhas, pendentes que sobraram (quem entrou depois), e o que ainda nao foi medido
   (entrega por destinatario so no painel do servico de envio).

## Quando o Resend recusar ou cortar a conta (as reservas)
Sinais: e-mail do Resend avisando revisao ou suspensao, `535`/`550` de autenticacao ou de conta no log do worker,
canario que nao chega com o worker vivo, painel do Resend com a conta pausada. Nao tente "contornar" reescrevendo
para o mesmo envio: conte ao dono e, com o OK dele, `email-mkt envio recuar`. Ele aplica a primeira reserva de
`EMK_ESP_RESERVA` (padrao `ses,sendgrid`) que tem credencial no cofre. Depois: `EMK_ESP=<reserva>` no perfil,
`email-mkt dns conferir`, `envio teste` e `envio conferir-eml`. Deu errado: `email-mkt envio reverter`.
Troca planejada (sem corte): `email-mkt envio aplicar --esp <ses|sendgrid|resend>`.
Com SES ou SendGrid a regua de copy so avisa; a copy continua sendo do copywriter e do revisor.

## Vigias
`email-vigia-cron.timer` (10 min) reinicia so o container de cron nas tres assinaturas medidas; nunca reinicia por
diagnostico que falhou. `email-vigia-disco.timer` (2 min) avisa disco em alerta, crescimento rapido e binlog religado.
Os avisos vao para `<estado>/avisos.jsonl` ou para o script do dono (`EMK_AVISO_CANAL=comando:...`). Leia o arquivo
de avisos no inicio de cada conversa sobre e-mail.

## Fica com o dono
Conta, plano e chave do servico de envio; verificacao do dominio nele; o pedido de acesso de producao no SES (voce
redige, ele envia); o DNS (ou a credencial dele); o subdominio; o remetente; o consentimento da base; o OK de cada
disparo; a decisao do servico de envio diante das politicas.
