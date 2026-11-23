# email-marketing 1.0.2

Pacote para o e-mail marketing proprio do dono: o Mautic da VPS dele ganha endereco publico com HTTPS,
o disparo para segmento passa a ter guardas, o servico de envio troca com volta atras, e dois vigias impedem os dois
incidentes que mais custaram na operacao de origem (cron travado e disco cheio de binlog).

So Linux, Python 3.8 ou mais, biblioteca padrao. Nao instala pacote do sistema e nao pede root; o acesso ao Docker
e o do perfil (`EMK_DOCKER=docker` ou `sudo -n docker`).

## Pecas
| Comando | O que faz | Escreve? |
|---|---|---|
| `descobrir` | acha web, cron, worker e banco do Mautic e sugere o perfil | nao |
| `perfil conferir` | campos, valores de exemplo, cofre 600 | nao |
| `https caddy` | gera o bloco do Caddy (container ou sistema) | so com `--saida` |
| `https site-url [--aplicar]` | confere e corrige o `site_url` para `https://<endereco>` | com `--aplicar` |
| `https conferir [--eml X]` | mede de fora; com o .eml do canario grava o SELO que libera a lista | o selo |
| `dns conferir` | SPF unico, DKIM sem proxy, DMARC, retorno | nao |
| `envio mostrar / aplicar / reverter` | troca o servico de envio com backup e worker reiniciado | sim |
| `envio recuar` | Resend cortou ou recusou: aplica a primeira reserva com credencial (ses, sendgrid) | sim |
| `envio teste / conferir-eml` | manda ao contato do dono e le a mensagem entregue | envio individual |
| `segmentos listar / criar` | segmentos do Mautic | `criar` fora do seco |
| `email criar` | e-mail de segmento despublicado, ja conferido | fora do seco |
| `disparo plano / canario / lote / resto / estado` | o disparo com codigo de OK, guarda do HTTPS e lote piloto | POST so no modo certo |
| `binlog conferir / aplicar [--executar]` | desliga o binlog e corrige o laco da 7.1.2 por override | o override |
| `vigia cron / disco` | o que os timers rodam | log e avisos |

## Modos (EMK_MODO)
- `seco` (padrao): roda todas as conferencias e para antes de qualquer POST.
- `canario`: libera so o envio individual ao contato do dono.
- `lista`: libera o segmento, sempre atras da guarda do HTTPS e do lote piloto.

## Testes
```bash
python3 -B -m unittest discover -s tests -v      # da raiz do pacote
```
Tudo falso: Docker falso (`tests/fake_docker.py`), API do Mautic falsa no loopback, rede falsa. Nada sai.
`tests/mutantes.py` reintroduz os defeitos que o pacote previne e mostra a suite pegando cada um.

## Limites conhecidos
- O canario prova o caminho ate UMA caixa. Entrega por destinatario so no painel do servico de envio.
- `https conferir` mede de onde roda. Rodado na propria VPS, o DNS e publico (resolvedor externo), mas a conexao
  pode voltar pela propria maquina; para prova de fora de verdade, rode tambem do computador do dono.
- O envio individual de e-mail de segmento ao contato do dono deve trazer `List-Unsubscribe` (observado em producao
  na 7.1.2). Se a mensagem do canario vier sem, o selo nao nasce: confira se o e-mail e de segmento (`list`).
- A correcao do laco e por override de um arquivo da 7.1.2. Ao subir de versao, rode `binlog conferir`: se a linha
  defeituosa sumiu, apague o override do Executioner e mantenha o `--disable-log-bin`.
- A troca de servico de envio edita a linha `'mailer_dsn' => '...'` do `local.php`. Se a instalacao passa o DSN por
  variavel de ambiente do container, essa linha nao existe e o comando recusa (`mailer_dsn_nao_unico achadas=0`,
  rc 2) sem mexer em nada; nesse caso a troca e no arquivo de ambiente do compose, com o mesmo cuidado.
- O vigia de disco mede `/`. Volume do Docker em outro disco: aponte outro vigia para ele.
