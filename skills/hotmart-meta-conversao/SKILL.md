---
name: hotmart-meta-conversao
description: Liga a Hotmart à Meta no servidor do dono. Instala e opera um receptor do webhook 2.0.0 da Hotmart (valida o hottok, deduplica e grava cada evento num banco local), manda Purchase e o clique de checkout para a API de Conversões com event_id igual ao do pixel, guarda o carrinho abandonado (PURCHASE_OUT_OF_SHOPPING_CART) para a recuperação de carrinho e vigia se o webhook parou de entregar. Use quando o dono disser "configurar webhook da Hotmart", "API de Conversões", "CAPI", "conversão do site para a Meta", "pixel no servidor", "deduplicar pixel e servidor", "evento de compra no Gerenciador de Eventos", "carrinho abandonado da Hotmart", "postback da Hotmart", "minhas vendas não aparecem na Meta" ou "o webhook parou". NÃO cria campanha, NÃO mexe em orçamento, NÃO escreve para lead (a recuperação é outra skill, que só LÊ o abandono daqui), NÃO instala o pixel na página (isso é do pacote de página; aqui só o snippet do clique) e NÃO decide consentimento/LGPD pelo dono.
---

# Conversão Hotmart → Meta, com webhook

O dono entrega a conta e as credenciais. O agente instala, configura, testa de ponta a ponta e opera, seguindo o
procedimento abaixo. Tudo nasce **desligado e seco**: nada sai para a Meta até o dono aprovar o teste.

Antes de começar, leia `references/gotchas.md` (as pegadinhas medidas) e, se for mexer no código,
`references/fontes.md` (de onde veio cada regra).

## O que fica com o dono (e não conta contra o "pronto")

1. Criar o webhook no painel da Hotmart, ou dar acesso para o agente guiar na tela. Versão **2.0.0**.
2. Copiar o **hottok** (aba Autenticação do Webhook) para um arquivo no servidor, pelo terminal, nunca pelo chat:
   `umask 077; cat > ~/hotmart-meta-perfil/hottok.env` e uma linha `HOTMART_HOTTOK=<valor>`, Ctrl+D.
3. O **id do pixel** (conjunto de dados) e o **token da API de Conversões** (Gerenciador de Eventos > o conjunto de
   dados > Configurações > API de Conversões > Gerar token), no mesmo formato: `META_CAPI_TOKEN=<valor>`.
4. Um subdomínio apontando para a VPS (ex.: `conversao.dominio-do-dono`) e o domínio verificado no Business Manager.
5. Dizer o que o **pixel nativo da Hotmart** já faz (Ferramentas > Pixel de Rastreamento > produto). O agente pode
   olhar junto. Isso decide quem manda o Purchase (ver passo 2).
6. O **banner de consentimento** do site. É decisão jurídica do dono; o snippet já espera o aceite por padrão.
7. A decisão de sair do teste para o real.

## Procedimento do agente

**1. Perfil.** Copie `perfil/perfil.exemplo.env` para uma pasta do dono FORA do pacote e preencha. Confira:
`python3 -I motor/config.py --conferir <perfil.env>`. Recusa vem com `MOTIVO=` na primeira linha.

**2. Quem manda o Purchase.** A Hotmart tem pixel e API de Conversões próprios e não publica o event_id que usa;
então o kit não consegue deduplicar contra ela. Regra: se "Vendas realizadas" está ligado no pixel da Hotmart,
`CAPI_PURCHASE=desligado` (o perfil recusa o contrário com `purchase_em_dobro`). Se o dono quer o Purchase com o
clique do anúncio junto (fbp/fbc/navegador via xcod), ele desliga "Vendas realizadas" lá e o kit assume.
O mesmo para o checkout: com "Visitas na página de pagamento" ligado lá, o clique do site vai como `CliqueCheckout`.

**3. Instalar.**
```bash
bash instalar.sh --perfil <perfil.env> --destino <dir> --so-conferir      # não escreve nada
bash instalar.sh --perfil <perfil.env> --destino <dir> --com-vigia        # instala parado, roda a suíte
```
Ponha o bloco de `unidades/Caddyfile.exemplo` no Caddy da VPS (ele tira o hottok do log de acesso) e ligue:
`systemctl --user enable --now hotmart-meta-receptor.service hotmart-meta-capi.timer hotmart-meta-vigia.timer`.
Se a VPS não tem `loginctl enable-linger` para o usuário, o serviço para quando a sessão fecha: confira.

**4. Testar a Hotmart.** No painel: Webhook > Minhas configurações > ícone de lista > teste de envio. Depois
`HM_PERFIL=<perfil.env> python3 -I <dir>/motor/eventos.py status`. O evento aparece em `eventos` ou, se a Hotmart
mandou algo fora do esperado, em `quarentena` com o motivo. Recusa `hottok_errado` em `recusas_24h` = o arquivo do
hottok não bate com o painel.

**5. Testar a Meta.** No perfil: `CAPI_MODO=teste`, `CAPI_PIXEL_ID`, `CAPI_TOKEN_ARQUIVO` e o
`CAPI_TEST_EVENT_CODE` da aba "Testar eventos". Rode `instalar.sh ... --com-capi`, reinicie o receptor e rode
`HM_PERFIL=<perfil.env> python3 -I <dir>/motor/capi_worker.py --evento-sintetico`. Em até 1 min o Purchase de teste
aparece na aba "Testar eventos". Para o checkout: abra o site do dono, clique no botão de compra e confira na mesma
aba o evento do navegador e o do servidor com o mesmo ID de evento, marcado como deduplicado.

**6. Real.** Com o "pode" do dono: tire o `CAPI_TEST_EVENT_CODE`, `CAPI_MODO=real`, reinicie o receptor.

**7. Operar.**
- `eventos.py status` mostra fila da Meta (`enviado`, `rejeitado`, `velho_demais`), quarentena e recusas.
- O vigia avisa venda aprovada que o webhook não trouxe. "webhook_desativado_provavel" = abrir o painel da Hotmart,
  conferir se a configuração foi desativada, corrigir a causa e reativar; as vendas do buraco podem ser reenviadas
  em Minhas Vendas > Ações > Reenviar Post.
- Parar a Meta na hora: `touch <HM_DADOS_DIR>/PARAR-CAPI`. Voltar: apagar o arquivo.
- Trocar o hottok: a Hotmart só troca pelo suporte dela. Atualize o arquivo; o receptor relê sozinho.

## O que a recuperação de carrinho recebe daqui

`references/contrato-abandono.md`. Em resumo: `eventos.py abandonos --estado aberto [--com-contato]`, um JSON
por lead, com estado `aberto`, `comprou` (a mesma pessoa comprou o produto) ou `expirado` (passou da retenção e o
contato foi apagado).
