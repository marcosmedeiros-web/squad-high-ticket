# Armadilhas medidas operando Mautic 7.1.2 em producao

Cada item custou um incidente ou uma tarde de diagnostico na operacao de origem. O pacote ja carrega a protecao de
quase todos; os que dependem de decisao ficam aqui para o agente nao tropecar.

## Envio
1. **Publicar nao envia; agendar por data tambem nao.** O cron padrao da imagem roda so `segments:update`,
   `campaigns:update` e `campaigns:trigger`. O unico gatilho de e-mail de segmento e `POST /api/emails/<id>/send`.
2. **Depois do POST nao ha freio.** O lote inteiro entra na fila dentro da requisicao e o worker drena em segundos.
   Despublicar nao tira da fila. Por isso: canario, lote piloto (`limit`), conferencia, e so entao o resto.
3. **Quem entra no segmento depois do envio nao recebe.** O segundo POST so pega quem ainda esta pendente.
   Antes de dizer "todos receberam", compare as estatisticas do e-mail com o segmento.
4. **Envio individual de e-mail de segmento a quem ja recebeu e pulado em silencio** (a API diz sucesso e nao cria
   estatistica). Canario repetido no mesmo contato nao prova nada; use outro contato ou outro e-mail.
5. **`email_stats` grava "enviado" no enfileiramento, nao na entrega.** A verdade da entrega esta no log do worker
   ou no painel do servico de envio. Falha que o worker descartou depois de 3 tentativas some da fila.

## Troca de servico de envio
6. **Trocou o `mailer_dsn`, reinicie os consumidores do worker** (`messenger:stop-workers`) e prove que eles subiram
   depois da troca. O botao "enviar teste" da tela usa o web, que rele a config na hora; ele fica verde enquanto o
   worker, que entrega campanha e segmento, segue no servico antigo. `cache:clear` sozinho nao resolve.
7. **`cache:clear` como root derruba o site em 500** (var/cache fica com dono root). Sempre como www-data.
8. **Campo de senha da tela de e-mail mantem a antiga se colar por cima sem limpar.** Por isso o pacote troca pelo
   arquivo, nunca pela tela. Porta 587 usa `smtp://`; 465 usa `smtps://`.
9. **SES em sandbox recusa com `554 Access denied` citando o DESTINATARIO.** Nao e senha errada: e o sandbox.
   Remetente de outro dominio tambem da 554 (a credencial SMTP so vale para a identidade verificada).
10. **Rastreio de clique e de abertura do servico de envio fica DESLIGADO.** O Mautic ja rastreia; o embrulho do
    servico atrapalha o diagnostico e conta clique duas vezes.
11. **Bounce muda de dono quando o servico muda.** Com SendGrid ou Resend, a caixa de bounce do Mautic para de receber;
    quem captura e o servico. Traga as supressoes de volta para o "nao contatar" do Mautic de tempos em tempos.

## Rastreio e descadastro
12. **Token de descadastro dentro de link:** `<a href="{unsubscribe_url}">`. `{unsubscribe_text}` sai no idioma do
    e-mail, nao do contato.
13. **O Mautic 7.1.2 ja manda `List-Unsubscribe` de um clique** em todo envio de marketing. Config vazia de
    cabecalhos extras nao quer dizer que o cabecalho falta: confira numa mensagem entregue.
14. **Clique com o painel do Mautic aberto no mesmo navegador nao conta** (o Mautic ignora visitante logado). Teste
    em aba anonima. `curl` de dentro do servidor chega pelo loopback e tambem nao conta.
15. **Conferir link de rastreio clicando suja a metrica.** O pacote confere o endereco do link sem visitar.
16. **Atras de proxy, o `site_url` tem que ser `https://<endereco publico>`.** Sem isso os links saem em http ou em
    localhost. Mexer em `trusted_proxies` e `site_url` sem conferir ja causou laco de redirecionamento: o
    `https conferir` pega isso (login tem que responder 200 sem redirecionar).

## Campanha
17. **Fuso padrao e UTC.** Janela de horario de evento e em UTC. Parada as 00:00 inverte a janela: use 23:59.
18. **PATCH de campanha pela API leva TODOS os eventos e o `canvasSettings`.** Parcial quebra a hierarquia, que vem
    so de `canvasSettings.connections`.
19. **`campaigns:trigger` sem `--campaign-id` processa todas as campanhas.**

## Operacao
20. **O container de cron trava se o `tail -f /tmp/stdout` morre** (FIFO sem leitor): o vigia do cron reinicia so ele.
21. **O laco do `campaigns:trigger` na 7.1.2 encheu o disco de binlog** (177 GB em ~2 h): `email-mkt binlog aplicar`.
    A 7.1.3 corrige o laco, mas quebrou o login na origem; suba de versao so com teste de login de fora.
22. **Nunca `docker exec ... env` nem `docker inspect` inteiro na tela:** o ambiente traz a senha do banco.
23. **O `local.php` guarda segredo.** O pacote grava com 640 e backup 600 numa pasta 700 do proprio volume.
