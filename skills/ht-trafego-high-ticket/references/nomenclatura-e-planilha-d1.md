# Nomenclatura e planilha D-1

Fontes: padrão de nomenclatura do squad (com o prefixo de campanha do perfil, `trafego.prefixo_campanha`, se houver), trilha 13 `RESUMO-trafego.md` §3.10 e §5.3, trilha 17 `RESUMO-parte-A` §5.1 (via `parte-D`), FEV26 §5.7 (via
`parte-G`), trilha 14 Central 1x1.

## 1. Campanha (padrão do squad, obrigatório)

```
[<DESTINO>][<OBJETIVO>][PREFIXO] [<PRODUTO/CANAL>] [<estratégia>] - DD.MM.AA
```
- `[PREFIXO]` = o prefixo de campanha do perfil (`trafego.prefixo_campanha`), se houver; sem prefixo, o bloco sai.
- Os primeiros colchetes **colados**; espaço antes de `[PRODUTO]`.
- `<DESTINO>`: versão da página de destino (o sufixo da URL: `v1`, `v7`; várias: `[v1, v8]` ou `[v1-v3]`), `CKT` quando vai
  direto ao checkout, `YT` quando vai ao YouTube (live ou playlist da aula semanal), `IG` quando vai ao perfil.
- `<OBJETIVO>`: `LEADS`, `VENDAS`, `ENGAJAMENTO` (só Turbinar/visita ao perfil quando feito pelo gerenciador), `RECONHECIMENTO`
  (só lembrete para quem já é lead: remarketing de aula ou de live; nunca captação).
- `<PRODUTO/CANAL>` no vocabulário do HT: `SESSAO1A1`, `IMI-ONLINE-MAR26`, `IMA-PRESENCIAL-BH`, `AULASEMANAL`,
  `AULASEMANAL-RMKT`, `LDP-<nome>`, `LDP-<nome>-RMKT`, `MINICURSO-<nome>`, `WEBINARIO-<nome>`, `INGRESSO-<evento>`.
- `<estratégia>`: `00-01-02`, `LOW`, `SEGMENTADA`, `REGIOES`, `TESTE-CRIATIVO`, `CAMPEAO`, `ESCALA-H2` (segunda duplicação),
  `4-ESTAGIOS` (remarketing de aula).
- Exemplos: `[v1][LEADS][PREFIXO] [SESSAO1A1] [00-01-02] - 22.11.26` ·
  `[YT][RECONHECIMENTO][PREFIXO] [AULASEMANAL-RMKT] [4-ESTAGIOS] - 22.11.26` ·
  `[v2][LEADS] [IMI-ONLINE-MAR26] [LOW] - 22.11.26` (sem prefixo) · `[CKT][VENDAS][PREFIXO] [MINICURSO-PRECIFICA] [FRIO] - 22.11.26`.
- **Conta com padrão próprio** (o expert ou o gestor anterior já usa outro padrão): seguir o padrão da conta e marcar só o
  prefixo do perfil (se houver), a data e a versão: `[VENDAS][WIHG][PREFIXO 26.10.26] - V7`.

## 2. Conjunto

Número da hierarquia + público + janela, batendo com o público dentro:
`00 | Visitantes | Inscrição sessão | 180d` · `01 | IG engajamento | 365d` · `02 | Semelhante IG eng 365 | 1%` ·
`02 | Interesses | <termos>` · `R-SP | Interesses | <termos>` (região, presencial). Se a conta tiver padrão próprio de
conjunto (ex.: `ADV+-<estratégia>`), manter o da conta e anexar o número de hierarquia. Remarketing de aula:
`01 | RMKT | Genérico` · `02 | RMKT | É amanhã` · `03 | RMKT | É hoje` · `04 | RMKT | Replay`.

## 3. Anúncio = CPF do criativo

Código único do criativo, **igual em todas as campanhas**, sem descrição extra (poluir o nome quebra o mapeamento nome →
arquivo nos relatórios). Sugestão de formato: `<CANAL>-<FORMATO>-<ANGULO>-<NN>` (ex.: `SES-VID-AUDITORIA-03`,
`IMI-EST-DOR-02`, `AS-RMKT-EHOJE-01`). O CPF nasce na ficha do criativo (`ht-criativos-high-ticket`) e vem de `09-visual/`.

## 4. Públicos

`Visitantes | Site | <canal> | Inscrição | 180d` · `Leads | <canal> | Obrigado | 180d` · `IG | Engajamento | 365d` ·
`Vídeo 75% | <campanha> | 365d` · `Lista | Alunos | <data>` · `LAL 1% | <origem>`.

## 5. Planilha D-1 (todo dia, dados de ontem)

Aba **Campanhas**: data · campanha · verba do dia · gasto · leads (ou compras) · CPL (ou CPA) · meta de CPL · desvio % ·
leads acumulados · meta acumulada · ritmo (leads/dia necessário para fechar) · ação do dia.
Aba **Criativos**: data · CPF do criativo · campanha · conjunto · gasto · impressões · alcance · cliques no link · CTR do link ·
leads · CPL · hook rate · hold rate · status (ativo, pausado, campeão) · observação.
Aba **Funil**: CPM · CTR · taxa de carregamento · conversão da página · CPL, por campanha e por página (teste A/B).
Aba **Até a venda** (puxa da Central 1x1): leads por origem · agendamentos · comparecimentos · vendas · custo por agendamento ·
custo por venda · faturamento.
Rotina: lançar D-1 → calcular desvio → otimizar (desativar o que não funciona, criar mais do que funciona) → registrar a ação.

## 6. Registro de Reels turbinados (aba da Central 1x1)

nome · link · status · estilo (CTA) · data · seguidores · investimento · visitas ao perfil · alcance · custo por seguidor.
Totais: seguidores, investido e custo global (investimento total ÷ seguidores totais; pode divergir da média simples).
O Instagram guarda dados por 2 anos; a planilha forma o histórico.
