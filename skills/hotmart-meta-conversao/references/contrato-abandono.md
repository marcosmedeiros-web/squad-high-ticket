# Contrato: o carrinho abandonado que a recuperação de carrinho lê

Este pacote só RECEBE e GUARDA. Quem decide escrever para o lead é a skill de recuperação, com o roteiro, os tetos e
o "pode" do dono. Ela lê daqui; nunca escreve no banco daqui.

## Como ler

Linha de comando (uma linha JSON por lead):
```bash
HM_PERFIL=<perfil.env> python3 -I <dir>/motor/eventos.py abandonos --estado aberto --desde-min 1440 --com-contato
```
Python:
```python
import sys; sys.path.insert(0, '<dir>/motor')
import banco, config
b = banco.Banco(config.carregar('<perfil.env>')['dados_dir'])
for lead in b.abandonos(estado='aberto', desde=<epoch>, com_contato=True): ...
```

## Campos

| Campo | O que é |
|---|---|
| `id_evento` | id do evento da Hotmart (chave estável; use para não escrever duas vezes) |
| `recebido_em` | quando o receptor recebeu (epoch, segundos) |
| `criado_em_ms` | quando a Hotmart criou o evento (epoch, milissegundos) |
| `produto_id`, `oferta` | o produto e o código da oferta da página de pagamento |
| `pais_iso` | país escolhido no checkout |
| `hmac_email`, `hmac_tel` | digitais locais (HMAC com a chave do receptor); servem para juntar com compra e exclusão |
| `estado` | `aberto`, `comprou` (a mesma pessoa comprou ESTE produto depois, ou pouco antes) ou `expirado` |
| `resolvido_em` | quando virou `comprou` |
| `nome`, `email`, `telefone` | só com `--com-contato`. Telefone já com o código do país. Apagados na retenção |

## Regras que a recuperação precisa respeitar

- **Releia o estado logo antes de escrever.** Um abandono vira `comprou` a qualquer momento.
- **Boleto impresso ou Pix gerado não resolve o abandono** (só aprovação resolve). Se a recuperação quiser tratar
  "gerou boleto e não pagou", os eventos `PURCHASE_BILLET_PRINTED` e `PURCHASE_DELAYED` estão na tabela `evento`.
- **Consentimento.** O lead só deixou o contato no checkout. Escrever para ele pede base legal (LGPD): a decisão e
  o texto são do dono, e precisam estar no roteiro antes de sair do seco.
- **Retenção.** `HM_RETENCAO_CONTATO_DIAS` (padrão 30). Depois disso o contato não existe mais aqui.
