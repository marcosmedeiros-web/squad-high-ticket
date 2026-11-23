# Mudanças: automacao-fluxos

## 1.0.0 no kit 5.3.8 (ajuste da integração)

- Dono: o agente `automacao-turbo` do kit.
- O alarme "automacao-fluxos: …" passa no `vigias/avisar-dono.sh` do kit sem o opt-in dos vigias (o dono desliga com
  `vigias/automacao-desligado`): no kit 5.3.x o vigia comum ficou calado no Telegram, o rc 1 virava "não entregue" e este
  vigia tentava de novo a cada hora. A suíte mora em `testes/automacao-fluxos/testes` do repositório.
- Nomes de exemplo nos testes e uma palavra de comentário em `motor/banco.py` trocados (batiam na lista de nomes de pessoas do kit).
- 🔸 Não testado: Mac real, `caddy validate` do `unidades/Caddyfile.exemplo`, as rotas do Mautic 7 (`contacts/new`, segmentos,
  `emails/<id>/contact/<id>/send`) e o `GET /sessions/<id>/groups` do OpenWA contra serviço real.

## 1.0.0 (18/10/2026)

Primeira versão.

- Quatro fluxos-modelo: `lead-formulario` (formulário para Mautic, com segmento, etiqueta e e-mail opcional, e
  WhatsApp de boas-vindas só para quem marcou o aceite), `venda-hotmart` (webhook 2.0.0, PURCHASE_APPROVED, por
  produto, com dedupe pela transação), `lembrete-aula` (lembretes nos grupos na hora marcada, com tolerância de
  atraso) e `batida` (o fluxo roda na ManyChat, no n8n ou em código e manda uma batida a cada evento).
- Modos `desligado`, `seco`, `teste` e `real`. Ligar exige prova de trânsito do desenho atual (evento de teste que
  passou inteiro, conferido na ponta) e o OK do dono; desenho mudado depois do OK segura os passos novos.
- Releitura na ponta de cada passo: segmento do contato no Mautic, estatística do e-mail, mensagem nova na conversa
  do WhatsApp. Sem confirmação o passo vira `incerto` e nunca é reenviado.
- Vigia de falha silenciosa: silêncio, palavra muda, evento sem regra, recusas em série, passo travado, falhas,
  desenho mudado, teto, lembrete perdido, agenda vazia e receptor fora. Um aviso por episódio e um na volta, pelo
  canal de avisos do kit.
- Instalador portátil (Linux e macOS): soma e permissão conferidas em Python, sem `sha256sum` nem `stat -c`;
  caminho físico resolvendo o pai que existe; a skill instalada leva o instalador, o `SHA256SUMS.interno` e este
  arquivo; rodado de dentro dela não move nem duplica; a versão anterior vai para fora de `~/.claude/skills`.
