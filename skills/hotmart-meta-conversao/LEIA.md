# hotmart-meta-conversao 1.0.0

Receptor do webhook da Hotmart, envio para a API de Conversões da Meta com deduplicação contra o pixel, guarda do
carrinho abandonado e vigia do webhook. Só biblioteca padrão do Python (3.10 ou mais novo) e systemd de usuário.

## Peças

| Peça | O que faz |
|---|---|
| `motor/receptor.py` | HTTP local: `/v1/hotmart` (webhook, hottok no cabeçalho), `/v1/visita` (clique do site), `/saude` |
| `motor/capi_worker.py` | timer de 1 min: esvazia a fila da Meta (seco, teste ou real), retenta, aplica a retenção |
| `motor/vigia.py` | timer de 30 min: venda aprovada na API da Hotmart que o webhook não trouxe |
| `motor/eventos.py` | leitura: `status`, `abandonos`, `purgar` |
| `site/conversao-site.js` | snippet do clique de checkout: fbq + aviso ao receptor + xcod no link |
| `instalar.sh` | `--so-conferir`, instala parado, `--com-capi`, `--com-vigia` |
| `testes/` | suíte (unittest, sem rede; Meta e Hotmart falsas; node opcional para o snippet) |

## Estados e códigos

- Receptor: 401 hottok errado ou ausente · 200 aceito, duplicado ou quarentena · 500 banco não gravou.
- Fila da Meta: `pendente` · `enviado` · `rejeitado` · `velho_demais` · `seco`.
- Vigia: 0 COBERTO · 1 BURACO · 2 NAO_CONSEGUI_MEDIR.
- Instalador: 0 ok · 2 uso · 3 pré-voo · 4 instalação · 78 perfil, sempre com `MOTIVO=` na primeira linha.

## Rodar a suíte

```bash
python3 -I -B -m unittest discover -s testes -t .
```

Procedimento completo de instalação e operação: `SKILL.md`. Pegadinhas: `references/gotchas.md`.
