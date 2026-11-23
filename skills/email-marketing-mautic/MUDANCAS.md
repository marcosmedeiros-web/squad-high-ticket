# email-marketing: mudancas

## 1.0.2 (ajuste da integração)

- A suíte (`tests/`) não vai no pacote: as chaves falsas dela têm a forma de chave real e travas de credencial recusariam o pacote inteiro.
- `instalar-email-marketing.sh`: `fisico()` resolve o caminho físico mesmo quando o `--destino` ainda não existe (sobe até o ancestral que existe). Antes, um destino novo voltava cru e não casava com a árvore de skills resolvida quando havia link no caminho (macOS: `/var` → `/private/var`): `test_destino_dentro_da_arvore_de_skills_ou_de_agentes_e_recusado` e `test_config_dir_do_claude_fora_do_home_tambem_vale` reprovavam no Mac (o destino dentro de skills passava sem recusa).

## email-marketing-1.0.2

Mesma classe de defeito achada em outro pacote, provada aqui por varredura numa HOME
temporaria: o instalador cria `<destino>/email-marketing` e, numa atualizacao, move o que havia para
`<destino>/.email-marketing-anterior-*`. Com `--destino ~/.claude/skills` isso e uma segunda skill (com `SKILL.md`), e se
a pasta da skill tiver o nome `email-marketing` o instalador move a si mesmo. O destino documentado,
uma pasta de instalacao fora de `~/.claude/skills`, nunca teve o problema; o defeito era aceitar o outro sem avisar.

- **O instalador recusa, antes de escrever qualquer coisa (tambem com `--so-conferir`)**, um `--destino` que e a pasta que
  contem esta skill (`destino_e_a_pasta_das_skills`), que fica dentro de `~/.claude/skills`, `~/.claude/agents` ou do
  `CLAUDE_CONFIG_DIR` (`destino_dentro_de_skills`), ou que fica dentro da propria skill (`destino_dentro_do_pacote`).
  Comparacao pelo caminho fisico (`pwd -P`).
- Sem `__pycache__`: ja nao havia (`python3 -I -B`); o teste novo passa a medir.
- Teste novo (`tests/test_instalador_no_kit.py`, 7 casos): o instalador rodado de dentro da pasta instalada, com o
  destino documentado, duas vezes e numa atualizacao (backup na pasta de instalacao, nunca em skills); e os cinco destinos
  recusados. 5 dos 7 reprovam a 1.0.1; os 2 do destino documentado passam nas duas (controle de que o conserto nao
  quebra o uso normal). 3 mutantes novos (17).

Resto do pacote igual a 1.0.1 (so `VERSAO` mudou).

## email-marketing-1.0.1

Decisao do pacote: o Resend e o servico de envio padrao; Amazon SES e SendGrid ficam de reserva para quando o
Resend recusar ou cortar a conta.

- Perfil de exemplo: `EMK_ESP=resend` e `EMK_ESP_RESERVA=ses,sendgrid`.
- Regua de copy vira GUARDA DO ENVIO no Resend: reprova no plano, no canario, no lote, no resto, no `envio teste` e
  no `email criar`. Saiu a opcao `--aceito-copy` da 1.0.0: no Resend o texto que reprova nao sai. Com SES e SendGrid
  ela continua so avisando.
- Comando novo `envio recuar`: aplica a primeira reserva da ordem que tem credencial no cofre (pula a que nao tem;
  sem nenhuma, recusa sem mexer no Mautic).
- SKILL.md, references/esp-politicas.md e LEIA.md reescritos para a nova ordem; testes novos da guarda no envio e do
  recuo (81 casos) e 3 mutantes novos (14).

## email-marketing-1.0.0

Primeira versao. Junta tres itens numa instalacao so: endereco publico com HTTPS para descadastro e rastreio,
gestor de disparo para segmento, e troca de servico de envio (Amazon SES, SendGrid, Resend).

- Guarda da lista em codigo: nenhum POST de segmento sem o selo do HTTPS (medido de fora e provado num .eml real) e
  sem a medicao ao vivo do login e da rota de descadastro no momento do envio.
- Disparo em passos com codigo de OK derivado do conteudo do e-mail: plano, canario, lote piloto, conferencia, resto.
  Despublica depois de cada POST.
- Troca do servico de envio sem a chave em argv nem na saida; backup 600; `php -l`; `local.php` regravado com 640;
  worker reiniciado e provado pela idade dos consumidores.
- Prevencao do binlog: `--disable-log-bin` e a correcao da linha 322 do ScheduledExecutioner da 7.1.2, gerada a
  partir do proprio container, por `docker-compose.override.yml`.
- Vigias do cron (tres assinaturas, tres estados, assinatura do tail que se desliga se nao volta) e do disco.
- Padrao recomendado de servico de envio para infoproduto e educacao em marketing digital: SES, com as fontes em
  `references/esp-politicas.md`. Regua de copy de risco que bloqueia promessa de ganho quando o servico e o Resend.
