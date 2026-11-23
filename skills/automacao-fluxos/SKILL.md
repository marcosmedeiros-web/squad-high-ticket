---
name: automacao-fluxos
description: 'Monta automação de marketing (formulário para Mautic e WhatsApp, venda Hotmart, lembrete de aula, comentário vira DM, fluxo n8n sob medida) com teste de trânsito antes de ligar e alarme quando para. Use para "monta uma automação", "comentário vira DM", "lembrete da aula ao vivo", "minha automação parou". NÃO usar para e-mail em massa nem CAPI.'
---

# Automação montada com o dono, e vigiada

O dono entrega a conta e as credenciais. O agente instala, desenha, monta, testa o trânsito e liga com o OK dele.
Daí em diante o vigia avisa quando o fluxo para de passar evento, porque o defeito mais comum em automação de
marketing não dá erro: é o fluxo cabeado certinho que ninguém atravessa.

Antes de mexer em qualquer fluxo, leia `references/licoes.md` (as lições medidas que viraram trava no código).

## O que vai pronto e o que fica com o dono

**Pronto:** o motor (receptor HTTP local, ciclo de um minuto, banco local, vigia), os quatro fluxos-modelo, o teste
de trânsito, a prova exigida para ligar e o alarme pelo canal de avisos que você escolher (`AF_AVISO_CANAL`: arquivo
local por padrão, ou `comando:/caminho/script` para o seu notificador de Telegram, e-mail ou Slack).

**Fica com o dono** (não conta contra o "pronto"):
1. As credenciais, cada uma num arquivo 600 escrito por ele no terminal, nunca pelo chat:
   `umask 077; cat > ~/automacao-perfil/<nome>.env`, uma linha `NOME=valor`, Ctrl+D. Nomes: `MAUTIC_API_USUARIO` e
   `MAUTIC_API_SENHA`; `OPENWA_CHAVE` (papel operator, escopada à sessão do número); `HOTMART_HOTTOK`.
2. Um subdomínio apontando para a VPS (registro A) e o bloco do Caddy (`unidades/Caddyfile.exemplo`).
3. O que só existe na tela de cada ferramenta: o webhook no painel da Hotmart, o envio do formulário para a URL, o
   gatilho de comentário e a "Solicitação externa" na ManyChat, o login de cada uma.
4. O texto que fala com cliente e a base do consentimento para WhatsApp (decisão dele, inclusive jurídica).
5. O teste com o contato dele (e-mail e WhatsApp próprios, conta de teste no Instagram, grupo de teste).
6. O OK para ligar.

## Procedimento

### 1. Entender o pedido (antes de desenhar)
Pergunte uma coisa por vez, até ter as sete respostas: (a) o que dispara (formulário, venda, horário, comentário,
outra ferramenta); (b) quem recebe; (c) o que sai, com o texto exato; (d) em quanto tempo; (e) como a pessoa aceitou
receber; (f) o que conta como "deu certo", e onde se confere isso NA PONTA (o contato no segmento, a mensagem na
conversa); (g) quantos eventos por dia se espera, que vira o limite de silêncio do vigia.

### 2. Existe modelo?
| Pedido | Modelo (`modelos/`) | Tipo |
|---|---|---|
| Formulário vai para o Mautic e para o WhatsApp | `lead-formulario.exemplo.json` | lead-formulario |
| Venda aprovada na Hotmart dispara boas-vindas | `venda-boas-vindas.exemplo.json` | venda-hotmart |
| Lembrete de aula ao vivo no grupo | `lembrete-aula.exemplo.json` | lembrete-aula |
| Comentário com palavra-chave vira DM com link | `comentario-dm.exemplo.json` + `references/manychat-comentario-dm.md` | batida |
| Qualquer outra coisa | passo 8 (sob medida) | batida |

### 3. Instalar
O receptor roda na VPS do dono (Linux com `systemctl --user` e `loginctl enable-linger`). No Mac, só a linha de
comando e o roteiro.
```bash
cp perfil/perfil.exemplo.env ~/automacao-perfil/perfil.env          # e preencher
bash instalar-automacao.sh --perfil ~/automacao-perfil/perfil.env --so-conferir   # não escreve nada
bash instalar-automacao.sh --perfil ~/automacao-perfil/perfil.env --com-servico --ligar
```
O `--ligar` liga o receptor e o timer; os fluxos continuam `desligado`. Ponha o bloco do Caddyfile e confira de
fora: `curl -s -o /dev/null -w '%{http_code}' https://<subdomínio>/f/x` tem que dar 404 (o receptor respondeu).
Comandos daqui em diante: `F="python3 -B ~/.claude/skills/automacao-fluxos/motor/fluxos.py --perfil ~/.config/automacao-fluxos/perfil.env"`.

### 4. Desenhar
Copie o modelo para `AF_FLUXOS_DIR/<nome>.json` e preencha com o dono (o `nome` dentro do arquivo é o nome do
arquivo). `$F conferir` recusa, com `MOTIVO=`, desenho com PREENCHER, campo de texto desconhecido, marcador cru de
outra ferramenta (`{{...}}`), texto que usa o nome sem `texto_sem_nome`, WhatsApp sem `consentimento_base`.
Mostre ao dono o texto exato que vai sair.

### 5. Ligar a fiação em seco
`$F modo <fluxo> seco` e `$F rota <fluxo>`. A URL vai para um arquivo 600 que o DONO abre no terminal dele e cola
na ferramenta de origem (formulário, ManyChat). Na Hotmart a URL é `https://<subdomínio>/f/<fluxo>` e a
autenticação é o hottok. Peça ao dono um envio real (o formulário preenchido, o "teste de envio" do painel da
Hotmart) e confira `$F transito <fluxo>`: o evento entrou no ramo esperado? Em seco nada sai para ninguém.

### 6. Teste de TRÂNSITO (não só fiação)
`$F modo <fluxo> teste`. Em teste, só o contato de `teste` (e-mail e WhatsApp do dono, grupo de teste) recebe; o
resto fica `retido_teste` e é contado.
- **Formulário:** o dono preenche o formulário de verdade com os dados dele; `$F esperar <fluxo> --minutos 10`.
  Simulação (`$F simular`) não vale como prova aqui: a prova tem que passar pelo formulário real.
- **Venda:** o "teste de envio" do painel prova que a Hotmart chega; `$F simular venda-boas-vindas --json <compra>`
  com o e-mail, o telefone e o id de produto reais do dono prova o resto (passa pelo HTTPS público).
- **Lembrete:** cadastre a próxima aula e rode `$F lembrete-teste <fluxo>`: o lembrete sai agora no grupo de teste.
- **Comentário vira DM:** o dono comenta a palavra com a conta de teste; a DM tem que chegar nela e a batida aqui.
O passo só vira `feito` quando a RELEITURA confirma na ponta: o contato aparece no segmento do Mautic, a linha do
e-mail existe nas estatísticas, a mensagem aparece na conversa do WhatsApp. "200" e "201" não contam.
Faça também a contraprova: um contato fora do teste fica retido; "não aceito" na caixa de aceite não recebe
WhatsApp; uma palavra fora da lista cai em `palavra_fora_da_lista`.

### 7. Ligar com o OK do dono
Mostre: o desenho (os 8 primeiros caracteres que o `conferir` imprime), o texto exato, quem recebe, a prova
(`$F status <fluxo>`). Com o "pode" dele: `$F ligar <fluxo> --ok`. O `ligar` recusa sem prova de trânsito do
desenho atual nos últimos 7 dias; na venda, recusa também se nenhum evento veio da Hotmart de verdade.
**Mudou o desenho depois do OK** (texto, segmento, produto): o que entrar fica `esperando_ok` (não se perde por
até `validade_h`), o vigia avisa, e o caminho é voltar ao passo 6 e ligar de novo.
Agende a reconferência para o dia seguinte: `$F transito <fluxo> --horas 24`, ramo por ramo. Sem tráfego
observado, "funcionando" é só inferência.

### 8. Fluxo sob medida
1. Desenhe com o dono no papel: gatilho, ramos e **o ramo "não entendi"** (todo roteador de texto tem três saídas:
   entendi A, entendi B, não entendi; o "não entendi" nunca aponta para o destino de um ramo real), saídas, e onde
   cada saída é conferida na ponta.
2. Onde montar: se o modelo existente resolve com outro desenho, use o motor. Se precisa de ferramenta que o motor
   não fala, monte no n8n do dono (`references/n8n-sob-medida.md`) ou na ManyChat, pela tela, com ele.
3. Regras de montagem: casar palavra e aceite pelo valor inteiro normalizado, nunca por pedaço ("não consegui"
   contém "consegui"); `case_sensitive: false` explícito na ManyChat; uma mensagem por gatilho; nunca envio às cegas
   depois de erro (pode ter saído).
4. Alarme: o último passo do fluxo manda a **batida** (`references/contrato-batida.md`) para um fluxo do tipo
   `batida` daqui (copie `modelos/sob-medida.exemplo.json`). O vigia avisa quando a batida para.
5. Teste com serviço falso primeiro (n8n: dados fixados no nó; código: um servidor local de mentira), depois o
   teste de trânsito real do passo 6, depois o OK.

## Operar
- `$F status` (modo, último evento, trânsito de 24 h, alarmes abertos) e `$F transito <fluxo>` (o contador por ramo
  e por passo).
- O alarme chega pelo canal de avisos do perfil (`AF_AVISO_CANAL`), um por episódio e um na volta. O que cada um quer dizer e o que fazer
  está no cabeçalho de `motor/vigia.py`. Os mais comuns: `silencio` (a origem parou de bater: formulário trocado,
  webhook desativado pela Hotmart, gatilho da ManyChat despublicado, receptor fora); `sem_regra` (entrou o que o
  fluxo não sabe tratar: produto novo sem regra, formulário com campo renomeado); `falhas` (passo que falhou ou
  ficou incerto).
- `incerto` = pode ter saído. Nunca reenvie: confira na ponta (a conversa, o Mautic) e depois `$F visto <fluxo>`.
  `falhou` sem POST feito pode voltar com `$F refazer <passo>`.
- Parar tudo na hora: `bash instalar-automacao.sh --parar` (nenhum passo sai; a entrada continua gravando).
  Voltar: `--retomar`. Desligar um fluxo: `$F modo <fluxo> desligado` (a rota passa a dar 404).

## Nunca
- Ligar fluxo, mudar texto que fala com cliente ou mandar mensagem real sem o OK do dono.
- Escrever credencial no chat, em desenho, em log ou em prompt; o agente cita o CAMINHO do arquivo, nunca o valor.
- DM proativa pela API da ManyChat (`sendContent` recusa fora e às vezes dentro da janela; ver `references/licoes.md`).
- Dar por funcionando o que só foi conferido na configuração.
