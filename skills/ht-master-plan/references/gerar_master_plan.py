#!/usr/bin/env python3
"""Gera a planilha do Master Plan (método FHT) com as fórmulas corrigidas.

Uso:
    python3 gerar_master_plan.py entrada.json saida.xlsx
    python3 gerar_master_plan.py --exemplo > entrada.json   # imprime um JSON de exemplo

Estrutura da planilha gerada (células amarelas = entrada; o resto é fórmula):
  PREMISSAS            ano inicial, % de recebimento, MARGEM (lucro) sobre o recebido e o custo que ela implica (1 - margem),
                       capacidade (padrão do squad)
  PRODUTOS HT          o que é, pra quem é, Roma, ticket, canais de venda (até 3 HTs)
  PLANEJAMENTO 7 ANOS  por HT: novos, ticket, renovação, total de clientes, contrato, recebido, custos, líquido, acumulados
  NUMERO MAGICO        vendas por mês e por semana, plano por canal (frequência x volume x conversão), funil reverso 1a1
  CAPACIDADE           alunos ativos x expert sozinho, mentores e navegadores (só HTs com "conta_capacidade": true;
                       use false para EHT e outros produtos sem acompanhamento)

Correções em relação ao modelo da FHT (07-descricao / master-plan.xlsx):
  - renovação sempre sobre o TOTAL de clientes do ano anterior (no modelo, o 1º ano do HT 1 usava só os novos);
  - faturamento de renovação = renovados x ticket de renovação (no modelo, C19 tinha 70000 fixo);
  - novos + renovação soma faturamentos (no modelo, D38 do HT 2 somava o ticket);
  - padrão do squad: MARGEM (lucro) de 40% sobre o RECEBIDO, ou seja, custo de 60% do recebido.
    Atenção: no modelo da FHT a linha se chama "margem de custo" e o número digitado é o % de CUSTO (40% de custo na aula).
    O squad decidiu ser mais conservador: o que se digita aqui é a margem de lucro; custos = recebido x (1 - margem)
    e líquido = recebido x margem. A chave antiga "margem_custo_sobre_recebido" é recusada para não inverter a conta;
  - linha de alunos já ativos antes do ano 1 (permite renovação no ano 1 de quem já tem base);
  - anos calculados a partir do ano inicial (no modelo havia 2034 no lugar de 2033).
Números padrão são referência do método/decisões do squad, não dado do expert.
"""
import json
import sys

try:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
except ImportError:  # pragma: no cover
    sys.exit("Instale openpyxl: python3 -m pip install openpyxl")

AMARELO = PatternFill("solid", fgColor="FFF2CC")
VERDE = PatternFill("solid", fgColor="E2EFDA")
CINZA = PatternFill("solid", fgColor="EDEDED")
NEGRITO = Font(bold=True)
MOEDA = 'R$ #,##0;[Red]-R$ #,##0'
PCT = '0%'

EXEMPLO = {
    "expert": "exemplo",
    "ano_inicial": 2027,
    "anos": 7,
    "pct_recebimento": 0.80,
    "margem_sobre_recebido": 0.40,
    "capacidade": {"expert_sozinho": 20, "alunos_por_mentor": 70, "alunos_por_navegador": 100},
    "produtos": [
        {
            "nome": "AR <nome>",
            "o_que_e": "Programa de acompanhamento personalizado para ... (definição de 02-oferta)",
            "pra_quem": "...",
            "roma": "Ajudo ... a ...",
            "ticket_texto": "R$ 10.000 (PROVISÓRIO: referência do método até 02-oferta)",
            "canais": "Sessão 1a1; depois SHT e imersão online",
            "alunos_ativos_antes": 0,
            "novos": [24, 36, 52, 70, 80, 90, 100],
            "ticket": [10000, 10000, 10000, 10000, 10000, 10000, 10000],
            "pct_renovacao": [0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
            "ticket_renovacao": [0, 10000, 10000, 10000, 10000, 10000, 10000],
            "conta_capacidade": True,
        }
    ],
    "canais_ano1": [
        {"canal": "Sessão 1a1", "frequencia_ano": 48, "volume_por_vez": 2, "unidade": "sessões por semana", "conversao": 0.15},
        {"canal": "Imersão online 1 dia", "frequencia_ano": 0, "volume_por_vez": 100, "unidade": "presentes", "conversao": 0.05},
        {"canal": "SHT (live direto ao ponto)", "frequencia_ano": 0, "volume_por_vez": 0, "unidade": "vendas por live", "conversao": 1},
    ],
    "funil_1a1": {"vendas_mes_1a1": 2, "conversao_sessao": 0.15, "comparecimento": 0.75},
}


def _cel(ws, ref, valor, fill=None, fmt=None, bold=False):
    c = ws[ref]
    c.value = valor
    if fill:
        c.fill = fill
    if fmt:
        c.number_format = fmt
    if bold:
        c.font = NEGRITO
    return c


def validar(cfg):
    if "margem_custo_sobre_recebido" in cfg:
        sys.exit("ERRO: a chave 'margem_custo_sobre_recebido' (custo) foi trocada por 'margem_sobre_recebido' (MARGEM de lucro, "
                 "padrão do squad: 0.40 = 40% de lucro e 60% de custo). Renomeie e confira o valor antes de gerar.")
    m = cfg.get("margem_sobre_recebido", 0.4)
    if not (0 < m <= 1):
        sys.exit(f"ERRO: margem_sobre_recebido deve estar entre 0 e 1 (ex.: 0.40); veio {m}.")
    for p in cfg.get("produtos", []):
        if "margem_custo_sobre_recebido" in p:
            sys.exit("ERRO: produto com 'margem_custo_sobre_recebido'; use 'margem_sobre_recebido' (margem de lucro).")
        mp = p.get("margem_sobre_recebido")
        if mp is not None and not (0 < mp <= 1):
            sys.exit(f"ERRO: margem_sobre_recebido do produto {p.get('nome', '')} fora de 0 a 1: {mp}.")
    r = cfg.get("pct_recebimento", 0.8)
    if not (0 < r <= 1):
        sys.exit(f"ERRO: pct_recebimento deve estar entre 0 e 1 (ex.: 0.80); veio {r}.")


def gerar(cfg, saida):
    validar(cfg)
    anos = int(cfg.get("anos", 7))
    ano0 = int(cfg["ano_inicial"])
    produtos = cfg["produtos"][:3]
    wb = Workbook()

    # PREMISSAS
    pr = wb.active
    pr.title = "PREMISSAS"
    pr.column_dimensions["A"].width = 52
    pr.column_dimensions["B"].width = 16
    pr.column_dimensions["C"].width = 70
    _cel(pr, "A1", f"MASTER PLAN: {cfg.get('expert', '')}", bold=True)
    linhas = [
        ("Ano inicial", ano0, None, "Ano 1 do plano"),
        ("% de recebimento sobre o contrato", cfg.get("pct_recebimento", 0.8), PCT,
         "Referência: live 054 (1 mi de contrato, ~800 mil recebidos); cancelamento 20% a 30% (lives 040/052). Trocar pelo dado próprio."),
        ("MARGEM (lucro) sobre o recebido", cfg.get("margem_sobre_recebido", 0.4), PCT,
         "Padrão do squad: margem de 40% sobre o recebido até haver dado próprio. Custo = 1 - margem (60%): imposto, equipe, comissão, tráfego."),
        ("Custo sobre o recebido (fórmula: 1 - margem)", "=1-B5", PCT,
         "Não editar: sai da margem acima. No modelo FHT esta é a linha 'margem de custo' (a aula usa 40% de custo; o squad usa 60%)."),
        ("Expert sozinho atende até (alunos ativos)", cfg["capacidade"]["expert_sozinho"], None, "Padrão do squad"),
        ("Alunos por mentor", cfg["capacidade"]["alunos_por_mentor"], None, "Padrão do squad"),
        ("Alunos por navegador", cfg["capacidade"]["alunos_por_navegador"], None, "Padrão do squad"),
    ]
    for i, (rot, val, fmt, nota) in enumerate(linhas, start=3):
        _cel(pr, f"A{i}", rot)
        _cel(pr, f"B{i}", val, CINZA if isinstance(val, str) and val.startswith("=") else AMARELO, fmt)
        _cel(pr, f"C{i}", nota)
    P_ANO, P_REC, P_MARG, P_SOLO, P_MENT, P_NAV = ("PREMISSAS!$B$3", "PREMISSAS!$B$4", "PREMISSAS!$B$5",
                                                    "PREMISSAS!$B$7", "PREMISSAS!$B$8", "PREMISSAS!$B$9")

    # PRODUTOS HT
    ph = wb.create_sheet("PRODUTOS HT")
    ph.column_dimensions["A"].width = 18
    ph.column_dimensions["B"].width = 110
    _cel(ph, "A1", "VISÃO GERAL DOS PRODUTOS HT", bold=True)
    r = 3
    for i, p in enumerate(produtos, start=1):
        _cel(ph, f"A{r}", f"HT {i}", bold=True)
        _cel(ph, f"B{r}", p.get("nome", ""), AMARELO, bold=True)
        for rot, chave in (("O que é", "o_que_e"), ("Pra quem é", "pra_quem"), ("Roma", "roma"),
                           ("Ticket", "ticket_texto"), ("Canais de venda", "canais")):
            r += 1
            _cel(ph, f"A{r}", rot)
            c = _cel(ph, f"B{r}", p.get(chave, ""), AMARELO)
            c.alignment = Alignment(wrap_text=True)
        r += 2

    # PLANEJAMENTO
    pl = wb.create_sheet("PLANEJAMENTO 7 ANOS")
    pl.column_dimensions["A"].width = 46
    for j in range(anos):
        pl.column_dimensions[get_column_letter(2 + j)].width = 15
    cols = [get_column_letter(2 + j) for j in range(anos)]
    _cel(pl, "A1", "MASTER PLAN (amarelo = entrada; verde = consolidado)", bold=True)

    def cab(linha):
        for j, col in enumerate(cols):
            _cel(pl, f"{col}{linha}", f"={P_ANO}+{j}", CINZA, bold=True)

    # consolidado nas linhas 3 a 9; blocos a partir da 12
    cab(3)
    consol = {"contrato": 4, "recebido": 5, "liquido": 6, "contrato_acum": 7, "liquido_acum": 8, "ativos": 9}
    rot_consol = {"contrato": "FATURAMENTO EM CONTRATO (todos os HTs)", "recebido": "RECEBIDO (todos os HTs)",
                  "liquido": "LÍQUIDO (todos os HTs)", "contrato_acum": "CONTRATO ACUMULADO",
                  "liquido_acum": "LÍQUIDO ACUMULADO", "ativos": "CLIENTES ATIVOS NO ANO (HTs com acompanhamento)"}
    for k, ln in consol.items():
        _cel(pl, f"A{ln}", rot_consol[k], VERDE, bold=True)

    blocos = []
    base = 12
    for i, p in enumerate(produtos, start=1):
        L = {n: base + k for k, n in enumerate([
            "titulo", "ativos_antes", "novos", "ticket", "fat_novos", "pct_renov", "renovados", "ticket_renov",
            "fat_renov", "total", "contrato", "pct_rec", "recebido", "margem", "custos", "liquido", "contrato_acum"])}
        _cel(pl, f"A{L['titulo']}", f"PRODUTO HT {i}: {p.get('nome', '')}", CINZA, bold=True)
        cab(L["titulo"])
        rot = {"ativos_antes": "Alunos já ativos antes do ano 1 (só coluna do ano 1)",
               "novos": "Meta de novos alunos/clientes", "ticket": "Ticket (de 02-oferta)",
               "fat_novos": "Faturamento com NOVOS (contrato)", "pct_renov": "Meta de % de renovação",
               "renovados": "Número de renovados (total do ano anterior x %)", "ticket_renov": "Ticket de renovação (definido por projeto: o estrategista decide)",
               "fat_renov": "Faturamento APENAS renovação (contrato)", "total": "Total de clientes no ano (novos + renovados)",
               "contrato": "Faturamento bruto NOVOS + RENOVAÇÃO (contrato)", "pct_rec": "% de recebimento",
               "recebido": "Recebido", "margem": "MARGEM (lucro) sobre o recebido (%), padrão do squad", "custos": "Custos previstos (recebido x (1 - margem))",
               "liquido": "Faturamento líquido", "contrato_acum": f"CONTRATO ACUMULADO HT {i}"}
        for k, txt in rot.items():
            _cel(pl, f"A{L[k]}", txt)
        for j, col in enumerate(cols):
            prev = cols[j - 1] if j else None
            def v(lista, padrao=0):
                return (lista[j] if j < len(lista) else padrao)
            if j == 0:
                _cel(pl, f"{col}{L['ativos_antes']}", p.get("alunos_ativos_antes", 0), AMARELO)
            else:
                _cel(pl, f"{col}{L['ativos_antes']}", None, CINZA)
            _cel(pl, f"{col}{L['novos']}", v(p.get("novos", [])), AMARELO)
            _cel(pl, f"{col}{L['ticket']}", v(p.get("ticket", [])), AMARELO, MOEDA)
            _cel(pl, f"{col}{L['fat_novos']}", f"={col}{L['novos']}*{col}{L['ticket']}", fmt=MOEDA)
            _cel(pl, f"{col}{L['pct_renov']}", v(p.get("pct_renovacao", [])), AMARELO, PCT)
            if j == 0:
                ren = f"=ROUND({col}{L['ativos_antes']}*{col}{L['pct_renov']},0)"
            else:
                ren = f"=ROUND({prev}{L['total']}*{col}{L['pct_renov']},0)"
            _cel(pl, f"{col}{L['renovados']}", ren)
            _cel(pl, f"{col}{L['ticket_renov']}", v(p.get("ticket_renovacao", [])), AMARELO, MOEDA)
            _cel(pl, f"{col}{L['fat_renov']}", f"={col}{L['renovados']}*{col}{L['ticket_renov']}", fmt=MOEDA)
            _cel(pl, f"{col}{L['total']}", f"={col}{L['novos']}+{col}{L['renovados']}")
            _cel(pl, f"{col}{L['contrato']}", f"={col}{L['fat_novos']}+{col}{L['fat_renov']}", fmt=MOEDA)
            _cel(pl, f"{col}{L['pct_rec']}", f"={P_REC}", AMARELO, PCT)
            _cel(pl, f"{col}{L['recebido']}", f"={col}{L['contrato']}*{col}{L['pct_rec']}", fmt=MOEDA)
            m_prod = p.get("margem_sobre_recebido")  # opcional: margem própria do HT (ex.: EHT), sempre MARGEM, nunca custo
            _cel(pl, f"{col}{L['margem']}", m_prod if m_prod is not None else f"={P_MARG}", AMARELO, PCT)
            _cel(pl, f"{col}{L['custos']}", f"={col}{L['recebido']}*(1-{col}{L['margem']})", fmt=MOEDA)
            _cel(pl, f"{col}{L['liquido']}", f"={col}{L['recebido']}-{col}{L['custos']}", fmt=MOEDA)
            acum = f"={col}{L['contrato']}" if j == 0 else f"={prev}{L['contrato_acum']}+{col}{L['contrato']}"
            _cel(pl, f"{col}{L['contrato_acum']}", acum, fmt=MOEDA)
        L["conta_capacidade"] = bool(p.get("conta_capacidade", True))
        blocos.append(L)
        base = L["contrato_acum"] + 3

    for j, col in enumerate(cols):
        prev = cols[j - 1] if j else None
        def soma(chave):
            return "=" + "+".join(f"{col}{b[chave]}" for b in blocos)
        _cel(pl, f"{col}{consol['contrato']}", soma("contrato"), VERDE, MOEDA)
        _cel(pl, f"{col}{consol['recebido']}", soma("recebido"), VERDE, MOEDA)
        _cel(pl, f"{col}{consol['liquido']}", soma("liquido"), VERDE, MOEDA)
        acomp = [b for b in blocos if b["conta_capacidade"]] or blocos
        _cel(pl, f"{col}{consol['ativos']}", "=" + "+".join(f"{col}{b['total']}" for b in acomp), VERDE)
        if j == 0:
            _cel(pl, f"{col}{consol['contrato_acum']}", f"={col}{consol['contrato']}", VERDE, MOEDA)
            _cel(pl, f"{col}{consol['liquido_acum']}", f"={col}{consol['liquido']}", VERDE, MOEDA)
        else:
            _cel(pl, f"{col}{consol['contrato_acum']}", f"={prev}{consol['contrato_acum']}+{col}{consol['contrato']}", VERDE, MOEDA)
            _cel(pl, f"{col}{consol['liquido_acum']}", f"={prev}{consol['liquido_acum']}+{col}{consol['liquido']}", VERDE, MOEDA)

    # NUMERO MAGICO
    nm = wb.create_sheet("NUMERO MAGICO")
    nm.column_dimensions["A"].width = 44
    for c in "BCDEFGH":
        nm.column_dimensions[c].width = 17
    _cel(nm, "A1", "NÚMERO MÁGICO E PLANO POR CANAL", bold=True)
    _cel(nm, "A3", "Novos alunos no ano (todos os HTs)", bold=True)
    for j, col in enumerate(cols):
        _cel(nm, f"{col}2", f"={P_ANO}+{j}", CINZA, bold=True)
        _cel(nm, f"{col}3", "=" + "+".join(f"'PLANEJAMENTO 7 ANOS'!{col}{b['novos']}" for b in blocos))
        _cel(nm, f"{col}4", f"={col}3/12", fmt='0.0')
        _cel(nm, f"{col}5", f"={col}3/52", fmt='0.00')
    _cel(nm, "A4", "Número mágico: vendas por mês")
    _cel(nm, "A5", "Vendas por semana")

    _cel(nm, "A7", "PLANO POR CANAL NO ANO 1 (frequência x volume x conversão)", bold=True)
    for k, t in enumerate(["Canal", "Frequência no ano", "Volume por vez", "Unidade do volume", "Conversão", "Vendas previstas"]):
        _cel(nm, f"{get_column_letter(1 + k)}8", t, CINZA, bold=True)
    canais = cfg.get("canais_ano1", [])
    ln = 9
    for cn in canais:
        _cel(nm, f"A{ln}", cn["canal"], AMARELO)
        _cel(nm, f"B{ln}", cn["frequencia_ano"], AMARELO)
        _cel(nm, f"C{ln}", cn["volume_por_vez"], AMARELO)
        _cel(nm, f"D{ln}", cn.get("unidade", ""), AMARELO)
        _cel(nm, f"E{ln}", cn["conversao"], AMARELO, PCT)
        _cel(nm, f"F{ln}", f"=ROUND(B{ln}*C{ln}*E{ln},0)")
        ln += 1
    _cel(nm, f"A{ln}", "Total previsto pelos canais", bold=True)
    _cel(nm, f"F{ln}", f"=SUM(F9:F{ln - 1})" if canais else 0, VERDE)
    _cel(nm, f"A{ln + 1}", "Meta de novos do ano 1", bold=True)
    _cel(nm, f"F{ln + 1}", f"={cols[0]}3", VERDE)
    _cel(nm, f"A{ln + 2}", "Diferença (canais - meta): negativo = plano não fecha", bold=True)
    _cel(nm, f"F{ln + 2}", f"=F{ln}-F{ln + 1}", VERDE)

    f0 = ln + 4
    fun = cfg.get("funil_1a1", {})
    _cel(nm, f"A{f0}", "FUNIL REVERSO DA SESSÃO 1A1 (por mês)", bold=True)
    _cel(nm, f"A{f0 + 1}", "Vendas por mês que virão do 1a1")
    _cel(nm, f"B{f0 + 1}", fun.get("vendas_mes_1a1", 2), AMARELO)
    _cel(nm, f"A{f0 + 2}", "Conversão da sessão (padrão do squad: 10% a 20%)")
    _cel(nm, f"B{f0 + 2}", fun.get("conversao_sessao", 0.15), AMARELO, PCT)
    _cel(nm, f"A{f0 + 3}", "Comparecimento à sessão (referência 75% a 80%, live 051)")
    _cel(nm, f"B{f0 + 3}", fun.get("comparecimento", 0.75), AMARELO, PCT)
    _cel(nm, f"A{f0 + 4}", "Sessões realizadas necessárias")
    _cel(nm, f"B{f0 + 4}", f"=ROUNDUP(B{f0 + 1}/B{f0 + 2},0)")
    _cel(nm, f"A{f0 + 5}", "Agendamentos necessários")
    _cel(nm, f"B{f0 + 5}", f"=ROUNDUP(B{f0 + 4}/B{f0 + 3},0)")
    _cel(nm, f"A{f0 + 6}", "Sessões por semana (4,3 semanas/mês)")
    _cel(nm, f"B{f0 + 6}", f"=ROUNDUP(B{f0 + 4}/4.3,1)")

    # CAPACIDADE
    cp = wb.create_sheet("CAPACIDADE")
    cp.column_dimensions["A"].width = 48
    for col in cols:
        cp.column_dimensions[col].width = 14
    _cel(cp, "A1", "CAPACIDADE DE ENTREGA (padrão do squad)", bold=True)
    for j, col in enumerate(cols):
        _cel(cp, f"{col}2", f"={P_ANO}+{j}", CINZA, bold=True)
        _cel(cp, f"{col}3", f"='PLANEJAMENTO 7 ANOS'!{col}{consol['ativos']}")
        _cel(cp, f"{col}4", f'=IF({col}3>{P_SOLO},"precisa de time","expert sozinho")')
        _cel(cp, f"{col}5", f"=IF({col}3>{P_SOLO},ROUNDUP({col}3/{P_MENT},0),0)")
        _cel(cp, f"{col}6", f"=IF({col}3>{P_SOLO},ROUNDUP({col}3/{P_NAV},0),0)")
    _cel(cp, "A3", "Clientes ativos no ano (HTs com acompanhamento)")
    _cel(cp, "A4", "Situação")
    _cel(cp, "A5", "Mentores necessários")
    _cel(cp, "A6", "Navegadores necessários")

    wb.save(saida)


def main(argv):
    if len(argv) == 2 and argv[1] == "--exemplo":
        print(json.dumps(EXEMPLO, ensure_ascii=False, indent=2))
        return 0
    if len(argv) != 3:
        print(__doc__)
        return 2
    with open(argv[1], encoding="utf-8") as f:
        cfg = json.load(f)
    gerar(cfg, argv[2])
    print(f"ok: {argv[2]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
