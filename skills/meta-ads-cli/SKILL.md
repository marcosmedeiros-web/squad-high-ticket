---
name: meta-ads-cli
description: 'Automatiza Meta Ads pela CLI oficial ou Graph API: batelada de criativos, testes de página, stop-loss, relatório diário, escalar vencedor, Cost Cap e ROAS floor, tudo nascendo PAUSED. Use para "subir batelada de criativos", "stop-loss automático", "relatório diário Meta Ads", "carrossel via API". NÃO usar para o primeiro setup (meta-ads-cli-setup).'
---

# Meta Ads CLI · camada de automação

## Identidade

Você integra a **Meta Ads CLI oficial** (anunciada em 29/04/2026 · `pip install meta-ads-cli`) ao fluxo de tráfego do expert. Sua função é gerar scripts shell parametrizados que substituem operação manual no Meta Business Manager por execução programática auditável.

Meta Ads CLI ≠ Marketing API SDK. CLI tem comandos previsíveis · output JSON nativo · exit codes padrão (0/3/4) · default `PAUSED` em todo create. Foi explicitamente desenhada pra **AI agents** (não só humanos).

**Esta skill NÃO substitui** `ht-trafego-high-ticket` (estratégia de campanha) nem `ht-criativos-high-ticket` (criativo) — ela é a **camada de execução** que o `ht-gestor-trafego` usa quando precisa materializar campanhas e criativos na Meta.

---

## Quando ativar

- Subir batelada de 15 criativos via terminal (~30s vs ~30min manual)
- Criar 5 campanhas de teste de página (V1-V5) em paralelo
- Configurar stop-loss horário (pausar ad se ROAS<X)
- Gerar relatório diário automatizado de tráfego
- Escalar vencedores (duplicar ad set vencedor com budget 2x)
- Substituir uploads manuais Hotmart/Meta por loops shell
- Reduzir scripts Python custom da Marketing API por shell + jq

---

## Quando NÃO usar

- Inteligência competitiva (Meta Ad Library) → use Apify scraper · CLI é só pra conta própria
- Workflows simples low-code → n8n com nó Meta Ads é mais ergonômico
- Quando MCP nativo Meta sair (provável próximos meses) → migrar gradualmente
- Operações críticas de produção sem revisão humana → CLI é poderosa demais pra rodar 100% autônomo

---

## Pré-requisitos

A skill confere o que falta e instala na hora, com o OK da pessoa, dizendo o que vai instalar (Python 3.12+ e a CLI).
Sem a CLI, os scripts Graph API (`06-upload-criativos-graphapi.py` e os runbooks 05/06) cobrem o essencial só com `curl`/Python.

```yaml
PYTHON:                   "3.12+ (CLI exige)"
INSTALL:                  "pip install meta-ads-cli"
AUTH:                     "System User Token Meta Business · NUNCA OAuth pessoal"
ENV_VARS:
  - META_ACCESS_TOKEN     # System User Token
  - META_AD_ACCOUNT_ID    # act_XXXXXXXXX
  - META_BUSINESS_ID      # opcional · multi-account

ARMAZENAMENTO_TOKEN:
  - "gerenciador de credenciais, ou export META_ACCESS_TOKEN=... no seu shell"
  - "OU arquivo .env fora do projeto com chmod 600"
  - "JAMAIS commitar · JAMAIS colar no chat"

PERMISSOES_TOKEN:
  - ads_management
  - ads_read
  - business_management
```

### Validação inicial

```bash
# 1. Confirmar install
meta ads --version
# → Meta Ads CLI v1.x.x

# 2. Confirmar auth
meta ads account info
# → retorna nome da conta + ID

# 3. Listar campanhas existentes (smoke test)
meta ads campaign list --limit 5 --output table
```

---

## Stack scripts prontos (5 templates)

Cada script em `scripts/` é parametrizado por variáveis · roda standalone · loga em `_private/logs/meta-cli/`.

| Script | Substitui | Tempo manual | Tempo CLI |
|---|---|---|---|
| `01-batelada-15-criativos.sh` | Upload 15 criativos no Business Manager | ~30min | ~30s |
| `02-criar-5-testes-paginas.sh` | Criar 5 ad sets para V1-V5 das páginas | ~15min | ~10s |
| `03-stop-loss-horario.sh` | Verificar ROAS e pausar perdedores (cron 1h) | manual diário | autônomo |
| `04-relatorio-diario.sh` | Pegar métricas + enviar pra Slack/Email | manual 30min | autônomo |
| `05-escalar-vencedores.sh` | Duplicar ad set vencedor com budget 2x | manual 10min | ~5s |

> Cada script usa `--status PAUSED` por default. ATIVAR é decisão humana.

---

## Nomenclatura padrão

Os scripts usam este padrão sem você precisar pensar (o nome da campanha segue a regra de nomenclatura do projeto, se houver):

```
{SIGLA}_{DDMMYY}_{TIPO}_{NUMERO}

SIGLA      3 letras MAIÚSCULAS da ação (MEN · MPR · SES...)
DDMMYY     data da batelada
TIPO       EST · CAR · VID · TES-PAG (teste de página)
NUMERO     001 a 999 (zero-padded · 3 dígitos)

Exemplos automáticos:
  MPR_120526_EST_001 ← estático 1 do ciclo 12/05/26
  MPR_120526_TES-PAG_003 ← teste da página V3
  MPR_120526_CAR_005 ← carrossel 5
```

Conecta direto com `ht-criativos-high-ticket`, `ht-trafego-high-ticket` e `ht-central-e-kpis`.

---

## Exemplo de uso · batelada de 15 criativos

### 1. Preparar arquivos da batelada (criativos aprovados, vindos do `ht-designer`)

```
batelada-120526/
├── README-batelada.md
├── estaticos/
│   ├── EST_001/{copy.md, final.png}
│   ├── EST_002/...
├── carrosseis/
│   ├── CAR_001/{copy.md, cards-1-10/, video-card-10.mp4}
├── videos/
│   └── VID_001/{roteiro.md, final.mp4}
└── manifest.yaml  ← lista dos criativos (nome, arquivo, copy)
```

### 2. Rodar script

```bash
cd batelada-120526
~/.claude/skills/meta-ads-cli/scripts/01-batelada-15-criativos.sh \
  --sigla MPR \
  --data 120526 \
  --campaign-id $MPR_CAMPAIGN_ID \
  --batelada-dir .
```

### 3. Output esperado

```
[12:34:56] Iniciando batelada MPR_120526
[12:34:57] ✓ Criativo MPR_120526_EST_001 criado (id: 23854xxx)
[12:34:58] ✓ Criativo MPR_120526_EST_002 criado (id: 23854xxy)
... (15 criativos)
[12:35:25] ✓ 15 criativos criados em PAUSED
[12:35:25] Manifest salvo: _private/logs/meta-cli/MPR_120526_manifest.json
[12:35:25] Próximo passo HUMANO: revisar e ATIVAR no Business Manager
```

---

## Guard rails OBRIGATÓRIOS

```yaml
1_DEFAULT_PAUSED:        "TODO create usa --status PAUSED · ativação é HUMANA"
2_LOG_AUDITAVEL:         "TODA execução em _private/logs/meta-cli/{cmd}_{date}.log"
3_DRY_RUN_PRIMEIRO:      "Antes de batelada real · sempre rodar com --dry-run"
4_RATE_LIMIT_BACKOFF:    "Scripts respeitam exit code 4 (API error) com sleep exponencial"
5_VALIDACAO_NOMENCLATURA: "Nomes seguem regex {3-LETRAS}_{6-DIGITOS}_{TIPO}_{3-DIGITOS}"
6_NUNCA_DELETAR:         "Scripts NÃO usam meta ads campaign delete · só pause/archive"
7_BUDGET_CAP:            "Daily budget máximo no script: R$ 200/dia/ad set (cap de segurança)"
8_TOKEN_NUNCA_LOGADO:    "ENV vars sensíveis NUNCA aparecem em logs (mask via sed)"
```

---

## Integração com outras skills

```
ht-criativos-high-ticket      → define os criativos · ht-designer produz arquivos + manifest → meta-ads-cli sobe
ht-trafego-high-ticket        → define estrutura + targeting → CLI cria
ht-gestor-trafego             → opera: sobe PAUSED, lê insights, dispara stop-loss, pede OK para ativar
ht-central-e-kpis             → ingere via CLI insights + jq → planilha / painel
```

---

## ⚠️ Limites da CLI — quando cair pra Graph API (validado em produção 2026-06-11)

A CLI `meta` cobre o básico (list, insights, campanha/adset/ad simples). Mas **falha** e exige Graph API direto pra:

- **ROAS floor** (`bid_strategy=LOWEST_COST_WITH_MIN_ROAS` + `roas_average_floor`) — CLI não expõe
- **Atribuição Incremental** — não tem API nenhuma; workaround duplicando ad set no UI
- **Identidade Instagram** — CLI usa `instagram_actor_id` (depreciado); API quer `instagram_user_id` (`17841...`)
- **Carrosséis** (`child_attachments`) — CLI não suporta
- **Vídeo > ~100MB** — exige upload resumável (start/transfer/finish)

- **Cost Cap** (`bid_strategy=COST_CAP` + `bid_amount` por resultado) — runbook dedicado
- **ROAS floor** (min-ROAS) — runbook dedicado

Nesses casos → **`scripts/06-upload-criativos-graphapi.py`** + os runbooks: **`references/05-...roas-incremental...`** (ROAS + Incremental) e **`references/06-...cost-cap...`** (Cost Cap). Ambos: configs, processo passo a passo, gotchas, checklist.

> Os dois runbooks são as duas campanhas do **protocolo de subida** (framework_9): Campanha 1 = Cost Cap (ref 06) · Campanha 2 = ROAS incremental (ref 05).

Pré-requisitos que sempre esquecem: **app Meta em modo Live** (developers.facebook.com → Publicar) e **`source ~/.zshrc`** antes de qualquer curl.

---

## Referências internas

- `references/01-instalacao-e-auth.md` — install, System User Token, ENV vars
- `references/02-comandos-essenciais.md` — campaign · adset · ad · creative · insights · catalog
- `references/03-troubleshooting.md` — rate limit, auth errors, exit codes, quirks
- `references/04-vs-alternativas.md` — Apify, n8n, Marketing API SDK, MCP futuro
- `references/05-runbook-campanha-roas-incremental-graphapi.md` — **runbook Graph API** (ROAS + Incremental + batelada 15) ⭐ · Campanha 2 do framework_9
- `references/06-runbook-campanha-cost-cap-graphapi.md` — **runbook Graph API** (Cost Cap · CAC ideal como teto · 1 adset adv+ com 15 criativos) ⭐ · Campanha 1 do framework_9
- `references/07-exemplo-resolvido-framework9.md` — **exemplo resolvido** do protocolo de subida (gate → CAC → 2 campanhas), caso genérico
- `scripts/01-batelada-15-criativos.sh`
- `scripts/02-criar-5-testes-paginas.sh`
- `scripts/03-stop-loss-horario.sh`
- `scripts/04-relatorio-diario.sh`
- `scripts/05-escalar-vencedores.sh`
- `scripts/06-upload-criativos-graphapi.py` — **upload via Graph API** (estáticos/vídeos/carrosséis, resumável, instagram_user_id) ⭐

---

## Princípios não-negociáveis

1. **Default PAUSED · ativação humana.** CLI nunca ativa nada autonomamente.
2. **Token em ENV var · jamais commitado nem colado no chat.** Gerenciador de credenciais, `export` no shell ou `.env` fora do projeto com `chmod 600`.
3. **Logs auditáveis sempre.** Toda execução em `_private/logs/meta-cli/`.
4. **Dry-run antes de produção.** Toda batelada nova testada com `--dry-run` primeiro.
5. **Nomenclatura padrão enforced.** Regex validation antes de criar.
6. **Budget cap de segurança.** Daily budget máximo por ad set: R$ 200.
7. **Output JSON parseável.** Pra integrar com jq · Sheets · Notion · Slack webhooks.
8. **Substitui scripts Python custom.** Reduz superfície de manutenção da Marketing API SDK.

---

**Fonte oficial:** [Meta Ads CLI announcement](https://developers.facebook.com/blog/post/2026/04/29/introducing-ads-cli/) · 29/04/2026.
**Stack:** `pip install meta-ads-cli` · Python 3.12+ · Marketing API v22+
