# Execução pela ferramenta de tráfego do perfil

A ferramenta que sobe e lê campanha é a do perfil (`trafego.ferramenta` em `~/.config/squad-ht/perfil.md`): Meta Ads CLI
oficial ou outra CLI. **Sem ferramenta definida (ou sem perfil), o padrão é o Gerenciador de Anúncios à mão**: o agente entrega a
campanha especificada campo a campo, com o passo a passo curto e o checklist do que conferir na tela, e nunca exige CLI, token
nem login. Os comandos abaixo são **exemplos com a Meta Ads CLI oficial**
(`meta --output json ads ...`); a sintaxe muda entre versões, então conferir sempre com `meta ads <recurso> <ação> --help`.
Sintaxe e armadilhas: o `--help` da CLI e a skill `meta-ads-cli`. Com o Gerenciador manual, o roteiro é o mesmo: mesmos campos, mesma ordem, mesma conferência.

**Token:** nunca no chat, nunca em argv, nunca em arquivo do projeto. O agente não abre, não lê e não imprime arquivo `.env`
ou de configuração que guarde token; quem cola token é o estrategista, no editor ou no gerenciador de segredos dele. O
processo que chama a API recebe o token pelo ambiente ou pela entrada padrão.

## 1. Leitura (roda livre)

Exemplo com a Meta Ads CLI oficial (conta do expert já configurada na CLI):
```bash
meta --output json ads campaign list                       # campanhas
meta --output json ads insights get --date-preset last_7d  # números dos últimos 7 dias
meta --output json ads adset get <ADSET_ID> --fields name,status,daily_budget,end_time,targeting,promoted_object
meta --output json ads dataset list                        # pixels/datasets visíveis na conta
```
Antes de qualquer trabalho, conferir: token válido e a data de validade, os escopos (lista abaixo), a conta de anúncios
certa do expert, o `account_status` e o Instagram vinculado. Para escolher o Reels a turbinar, ler os posts e insights do
Instagram do expert (pela ferramenta do perfil ou pelo próprio app).

**Escopos que o token precisa ter (7):** `ads_management`, `ads_read`, `business_management` (anúncios);
`pages_show_list`, `pages_read_engagement` (Página); `instagram_basic`, `instagram_manage_insights` (Instagram). Token só
com os 4 primeiros mais `pages_read_engagement` não enxerga o Instagram. Escopo faltando = registrar no plano e pedir ao
estrategista um token novo; não seguir como se estivesse completo. Um "token ok" que não lista escopos **não confere escopos**.

## 2. Escrita (sempre com OK; tudo nasce PAUSED)

### 2.0 Público personalizado (criar antes da campanha)
A Meta Ads CLI oficial, na versão conferida, **não tem subcomando de público personalizado**. Por isso:
1. **Criar** pelo Gerenciador de Públicos (interface); quem cria é o estrategista ou o gestor com o OK dele, com a lista e o
   nome de `setup-ativos-e-pixel.md` §4 (fonte + recorte + janela). Alternativa, só com OK para aquela ação: POST na Graph API
   (`act_<id>/customaudiences`) por um script que lê o token do ambiente, como no runbook da `meta-ads-cli`; token nunca em argv, no chat ou em
   arquivo do projeto.
2. **Ler o ID e o tamanho** (leitura, roda livre): GET em `act_<id>/customaudiences` com
   `fields=id,name,subtype,approximate_count_lower_bound,approximate_count_upper_bound,time_updated` e `limit=200`, por um
   script que lê o token do ambiente, ou pelo próprio Gerenciador de Públicos. Público abaixo de ~1.000 pessoas: avisar que a
   entrega pode não rodar.
3. Registrar no plano a tabela público → ID → tamanho → data, e usar os IDs em `custom_audiences` e `excluded_custom_audiences`
   do JSON de targeting. Público ainda não criado: o conjunto fica `[A CONFIRMAR COM o estrategista: criar público X]` e não sobe.

### 2.1 Campanha, conjunto e anúncio

- Criar campanha, conjunto e anúncio com `status=PAUSED` nos três níveis. `create|update|delete|pause|resume` só com o OK do
  estrategista para aquela ação (o OK de criar não vale para ativar).
- Ordem: campanha → conjuntos → criativos → anúncios. Guardar os IDs devolvidos no registro de subida.
- Sintaxe de exemplo (Meta Ads CLI oficial; conferir sempre com `--help`, a CLI muda):

| Passo | Comando e flags que importam (exemplo) |
|---|---|
| Campanha | `meta ads campaign create --name "<nome no padrão, com o prefixo do perfil se houver>" --objective OUTCOME_LEADS` (ou `OUTCOME_SALES` para ingresso e minicurso; `OUTCOME_AWARENESS` só para lembrete de quem já é lead, receita em `campanhas-por-canal.md` §D) `--status PAUSED`. Orçamento no conjunto (ABO no teste, regra do squad) = **não** passar orçamento aqui. |
| Conjunto | `meta ads adset create <CAMPAIGN_ID> --name "00 \| ..." --optimization-goal OFFSITE_CONVERSIONS --billing-event IMPRESSIONS --pixel-id <PIXEL> --custom-event-type LEAD` (ou `PURCHASE`) `--daily-budget <centavos> --status PAUSED --targeting @targeting.json` e `--end-time` (ISO 8601) quando a campanha tem fim. |
| Público no JSON | `geo_locations`, `age_min`/`age_max`, `genders`, `custom_audiences`, `excluded_custom_audiences`, `flexible_spec` (interesses) e, em público fechado, `targeting_relaxation_types` `{"lookalike": 0, "custom_audience": 0}`; passar `--no-advantage-audience` quando restringir o público. |
| Criativo e anúncio | `meta ads creative create ...` e depois `meta ads ad create --creative-id <ID> --conversion-domain <dominio> --status PAUSED`. |

- **Orçamento é em centavos**: R$ 10/dia = `--daily-budget 1000`; R$ 42/dia = `4200`. Errar a unidade multiplica a verba por 100.
- Orçamento na campanha e no conjunto ao mesmo tempo dá erro ("more than one budget"); escolher um modo (ABO no teste).
- Público fechado: passar `targeting_relaxation_types` com `{"lookalike": 0, "custom_audience": 0}` na criação. Pela API, a
  expansão do público personalizado pode nascer ligada; desligar só o `advantage_audience` **não** desliga essa expansão
  (caso observado: remarketing de ~1.200 pessoas alcançou ~47,8 mil). Sempre zerar e reler o alcance estimado.
- Nome da campanha no padrão de `nomenclatura-e-planilha-d1.md`, com o prefixo do perfil (`trafego.prefixo_campanha`), se houver.
- Ativar: ação separada, só depois do OK escrito do estrategista em `00-plano/aprovacoes.md`.

## 3. Conferência por leitura (obrigatória depois de criar)

Reler cada objeto (pela ferramenta, não pela saída do comando de criação) e registrar:
- [ ] `status` = PAUSED em campanha, conjuntos e anúncios.
- [ ] objetivo, otimização e `promoted_object` (pixel + evento Lead/Purchase) no **conjunto** (a leitura da conta não traz
      `promoted_object`; ler o conjunto pelo ADSET_ID, exemplo: `meta ads adset get <ADSET_ID> --fields
      name,status,daily_budget,end_time,targeting,promoted_object`).
- [ ] públicos incluídos e excluídos, idade, localização, `targeting_relaxation_types`, alcance estimado coerente.
- [ ] orçamento (nível certo), data de início e de término.
- [ ] anúncio: Página e IG corretos, URL com UTM, CTA, criativo com o CPF certo.
Comparar com o plano; divergência = corrigir antes de pedir o OK de ativação.

## 4. Armadilhas conhecidas

- **Status da conta** (`account_status`, com `disable_reason`):
  1 ativa (segue); 2 desativada (não sobe nada; `disable_reason` diz o motivo, contestação é do estrategista); 3 não quitada (bloqueia
  toda escrita, inclusive exclusão; pagamento é do estrategista); 7 em análise de risco e 8 com acerto pendente (não sobe; esperar e
  avisar); 9 em período de carência (sobe só com OK do estrategista sabendo do risco de bloqueio); 100 e 101 fechando ou fechada
  (outra conta, só com OK do estrategista). Qualquer status diferente de 1 vai para o plano como bloqueio e para o Diretor como decisão.
- Pixel ou dataset de outro BM aparecendo na conta (exemplo: `meta ads dataset list`): não usar, registrar e avisar o estrategista
  (regra: nada de pixel de terceiro).
- App em modo de desenvolvimento cria campanha e conjunto mas não cria criativo/anúncio: precisa estar ao vivo.
- Turbinar Reels e publicar no Instagram ou na Página não fazem parte dos 7 escopos exigidos: Turbinar é feito no celular ou
  no gerenciador, pelo expert ou pelo estrategista.
- Token de usuário expira (o de longa duração dura cerca de 60 dias): conferir a validade antes de cada ciclo; renovar é do
  estrategista.
- Token `EAA...` apareceu no chat: está queimado; avisar o estrategista para revogar e gerar outro.
- Conta sem acesso visível (BM não compartilhado com o usuário do token): a listagem de contas não mostra; pedir o acesso ao expert.
