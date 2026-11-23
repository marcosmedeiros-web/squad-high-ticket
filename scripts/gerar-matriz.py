#!/usr/bin/env python3
"""Gera docs/MATRIZ-AGENTES-SKILLS.md a partir dos cabeçalhos dos agentes e das skills do plugin squad-high-ticket.

Lê agents/*.md (frontmatter: name, skills, color, model) e skills/*/SKILL.md (frontmatter: name).
Por agente: skills pré-carregadas (campo skills) e skills citadas no corpo.
Por skill: quais agentes a pré-carregam e quais a citam.
Alertas: skill citada ou pré-carregada que não existe, skill ht- sem dono, mais de 8 pré-carregadas,
name diferente do nome do arquivo, cabeçalho YAML inválido.

Uso: python3 scripts/gerar-matriz.py [--raiz <pasta do plugin>] [--estrito]
  --estrito  sai com código 1 se houver alerta (para usar em verificação).
"""
import argparse
import datetime
import os
import re
import sys

try:
    import yaml
except ImportError:  # sem PyYAML, cai no leitor simples
    yaml = None

# Os 32 papéis do squad. Um "ht-..." citado que é agente não conta como skill.
AGENTES_DO_SQUAD = {
    "ht-diretor", "ht-controller", "ht-gestor-projetos",
    "ht-revisor-metodo-copy", "ht-revisor-visual",
    "ht-estrategista-produto", "ht-estrategista-demanda", "ht-estrategista-comercial",
    "ht-estrategista-eventos", "ht-estrategista-sucesso",
    "ht-pesquisador", "ht-arquiteto-oferta",
    "ht-estrategista-conteudo", "ht-sdr",
    "ht-closer", "ht-treinador-comercial",
    "ht-produtor-eventos", "ht-roteirista-palco", "ht-ingressos-e-patrocinio", "ht-diretor-desafio",
    "ht-cs", "ht-arquiteto-entrega", "ht-gestor-renovacao",
    "ht-diretor-copy", "ht-copy-paginas-e-emails", "ht-copy-anuncios-e-mensagens",
    "ht-diretor-arte", "ht-designer", "ht-web-designer",
    "ht-gestor-trafego", "ht-gestor-automacoes",
    "ht-consultor-casos",
}
MAX_PRECARREGADAS = 8
PREFIXO_PLUGIN = "squad-high-ticket:"

RE_HT = re.compile(r"(?<![A-Za-z0-9_/-])ht-[a-z0-9]+(?:-[a-z0-9]+)*")
RE_PLUGIN = re.compile(r"squad-high-ticket:([a-z0-9][a-z0-9-]*)")


def separar_frontmatter(texto):
    """Devolve (cabecalho, corpo). Sem cabeçalho, ('', texto)."""
    if not texto.startswith("---"):
        return "", texto
    linhas = texto.split("\n")
    for i in range(1, len(linhas)):
        if linhas[i].strip() == "---":
            return "\n".join(linhas[1:i]), "\n".join(linhas[i + 1:])
    return "", texto


def ler_cabecalho(cab):
    """Lê o YAML; se falhar, extrai name e a lista skills por expressão regular. Devolve (dict, erro)."""
    erro = None
    if yaml is not None:
        try:
            dado = yaml.safe_load(cab) or {}
            if isinstance(dado, dict):
                return dado, None
            erro = "cabeçalho não é um mapa"
        except Exception as e:  # noqa: BLE001
            erro = str(e).split("\n")[0]
    else:
        erro = "PyYAML ausente (leitor simples)"
    dado = {}
    m = re.search(r"^name:\s*(.+)$", cab, re.M)
    if m:
        dado["name"] = m.group(1).strip().strip("'\"")
    for campo in ("color", "model"):
        m = re.search(r"^%s:\s*(.+)$" % campo, cab, re.M)
        if m:
            dado[campo] = m.group(1).strip()
    m = re.search(r"^skills:\s*\n((?:[ \t]+-.*\n?)+)", cab, re.M)
    if m:
        dado["skills"] = [re.sub(r"^[ \t]+-\s*", "", l).split("#")[0].strip().strip("'\"")
                          for l in m.group(1).splitlines() if l.strip()]
    return dado, erro


def normalizar(nome):
    nome = str(nome).strip()
    if nome.startswith(PREFIXO_PLUGIN):
        nome = nome[len(PREFIXO_PLUGIN):]
    return nome


def citadas_no_corpo(corpo, nomes_agentes):
    """Skills citadas no corpo: tokens ht-... (que não são agentes) e squad-high-ticket:<nome>."""
    achados = set()
    for m in RE_HT.finditer(corpo):
        token = m.group(0)
        depois = corpo[m.end():m.end() + 2]
        if depois.startswith("-*") or depois.startswith("*"):
            continue  # padrão com curinga (ex.: ht-revisor-*), não é nome
        if token in nomes_agentes:
            continue
        achados.add(token)
    for m in RE_PLUGIN.finditer(corpo):
        achados.add(m.group(1).rstrip("-"))
    return achados


def numeros_das_skills(raiz):
    """Lê o nº de cada skill ht- no mapa do protocolo (| 12 | `ht-raio-x` |)."""
    caminho = os.path.join(raiz, "skills", "ht-protocolo", "references", "mapa-das-46-skills.md")
    nums = {}
    if os.path.isfile(caminho):
        for linha in open(caminho, encoding="utf-8"):
            m = re.match(r"\|\s*(\d+)\s*\|\s*`(ht-[a-z0-9-]+)`", linha)
            if m:
                nums[m.group(2)] = int(m.group(1))
    return nums


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--raiz", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--estrito", action="store_true")
    args = ap.parse_args()
    raiz = os.path.abspath(args.raiz)
    alertas = []

    # Skills: identificador = nome da pasta; o name do cabeçalho também vale como apelido.
    skills = {}
    apelidos = {}
    dir_skills = os.path.join(raiz, "skills")
    for pasta in sorted(os.listdir(dir_skills)) if os.path.isdir(dir_skills) else []:
        arq = os.path.join(dir_skills, pasta, "SKILL.md")
        if not os.path.isfile(arq):
            continue
        cab, _ = separar_frontmatter(open(arq, encoding="utf-8").read())
        dado, erro = ler_cabecalho(cab)
        nome = dado.get("name", pasta)
        skills[pasta] = {"name": nome, "erro_yaml": erro}
        apelidos[normalizar(nome)] = pasta
        if erro and pasta.startswith("ht-"):
            alertas.append("Skill `%s`: cabeçalho YAML inválido (%s)." % (pasta, erro))
        if pasta.startswith("ht-") and nome != pasta:
            alertas.append("Skill `%s`: name `%s` diferente do nome da pasta." % (pasta, nome))

    def resolver(nome):
        n = normalizar(nome)
        if n in skills:
            return n
        return apelidos.get(n)

    # Agentes
    agentes = {}
    dir_agentes = os.path.join(raiz, "agents")
    arquivos = sorted(f for f in os.listdir(dir_agentes) if f.endswith(".md")) if os.path.isdir(dir_agentes) else []
    nomes_agentes = set(AGENTES_DO_SQUAD) | {os.path.splitext(f)[0] for f in arquivos}
    for f in arquivos:
        arq = os.path.join(dir_agentes, f)
        texto = open(arq, encoding="utf-8").read()
        cab, corpo = separar_frontmatter(texto)
        dado, erro = ler_cabecalho(cab)
        base = os.path.splitext(f)[0]
        nome = str(dado.get("name", base))
        if erro:
            alertas.append("Agente `%s`: cabeçalho YAML inválido (%s)." % (base, erro))
        if nome != base:
            alertas.append("Agente `%s`: name `%s` diferente do nome do arquivo." % (base, nome))
        pre = [normalizar(s) for s in (dado.get("skills") or [])]
        if len(pre) > MAX_PRECARREGADAS:
            alertas.append("Agente `%s`: %d skills pré-carregadas (máximo %d)." % (base, len(pre), MAX_PRECARREGADAS))
        cit = citadas_no_corpo(corpo, nomes_agentes)
        pre_res, cit_res = [], []
        for s in pre:
            r = resolver(s)
            if r is None:
                alertas.append("Agente `%s`: skill pré-carregada `%s` não existe em skills/." % (base, s))
            else:
                pre_res.append(r)
        for s in sorted(cit):
            r = resolver(s)
            if r is None:
                alertas.append("Agente `%s`: skill citada no corpo `%s` não existe em skills/." % (base, s))
            elif r not in pre_res:
                cit_res.append(r)
        agentes[base] = {
            "color": dado.get("color", ""), "model": dado.get("model", ""),
            "pre": pre_res, "cit": sorted(set(cit_res)), "linhas": texto.count("\n") + 1,
        }
        if "ht-protocolo" not in pre_res:
            alertas.append("Agente `%s`: não pré-carrega `ht-protocolo`." % base)

    # Por skill
    uso = {s: {"pre": [], "cit": []} for s in skills}
    for a, d in agentes.items():
        for s in d["pre"]:
            uso[s]["pre"].append(a)
        for s in d["cit"]:
            uso[s]["cit"].append(a)
    for s in sorted(skills):
        if s.startswith("ht-") and not uso[s]["pre"] and not uso[s]["cit"]:
            alertas.append("Skill `%s` sem dono: nenhum agente a pré-carrega nem a cita." % s)
    faltam = sorted(AGENTES_DO_SQUAD - set(agentes))

    nums = numeros_das_skills(raiz)
    agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    out = []
    out.append("# Matriz agente × skill do Squad High Ticket")
    out.append("")
    out.append("Gerada por `scripts/gerar-matriz.py` em %s a partir dos cabeçalhos de `agents/*.md` e "
               "`skills/*/SKILL.md`. Não editar à mão: rodar o script de novo." % agora)
    out.append("")
    out.append("- Agentes com arquivo: %d de %d do squad." % (len(agentes), len(AGENTES_DO_SQUAD)))
    out.append("- Skills no plugin: %d (%d ht-, %d de execução do kit Turbo)." % (
        len(skills), sum(1 for s in skills if s.startswith("ht-")), sum(1 for s in skills if not s.startswith("ht-"))))
    out.append("- Alertas: %d (lista no fim)." % len(alertas))
    out.append("- P = pré-carregada (campo `skills` do cabeçalho); C = citada no corpo (invocada pela ferramenta Skill).")
    out.append("")
    out.append("## Por agente")
    out.append("")
    out.append("| Agente | Cor | Modelo | Linhas | Pré-carregadas (P) | Citadas no corpo (C) |")
    out.append("|---|---|---|---|---|---|")
    for a in sorted(agentes):
        d = agentes[a]
        out.append("| `%s` | %s | %s | %d | %s | %s |" % (
            a, d["color"], d["model"], d["linhas"],
            ", ".join("`%s`" % s for s in d["pre"]) or "nenhuma",
            ", ".join("`%s`" % s for s in d["cit"]) or "nenhuma"))
    if faltam:
        out.append("")
        out.append("Agentes do squad ainda sem arquivo: " + ", ".join("`%s`" % a for a in faltam) + ".")
    out.append("")
    out.append("## Por skill ht- (método FHT)")
    out.append("")
    out.append("| Nº | Skill | Pré-carregada por (P) | Citada por (C) |")
    out.append("|---|---|---|---|")
    for s in sorted((s for s in skills if s.startswith("ht-")), key=lambda x: (nums.get(x, 0), x)):
        out.append("| %s | `%s` | %s | %s |" % (
            nums.get(s, "") if nums.get(s) else "base" if s == "ht-protocolo" else "",
            s, ", ".join("`%s`" % a for a in uso[s]["pre"]) or "nenhum",
            ", ".join("`%s`" % a for a in uso[s]["cit"]) or "nenhum"))
    out.append("")
    out.append("## Por skill de execução (do kit Turbo, `squad-high-ticket:<nome>`)")
    out.append("")
    out.append("| Skill | name no cabeçalho | Pré-carregada por (P) | Citada por (C) |")
    out.append("|---|---|---|---|")
    for s in sorted(x for x in skills if not x.startswith("ht-")):
        out.append("| `%s` | `%s`%s | %s | %s |" % (
            s, skills[s]["name"], " (YAML inválido)" if skills[s]["erro_yaml"] else "",
            ", ".join("`%s`" % a for a in uso[s]["pre"]) or "nenhum",
            ", ".join("`%s`" % a for a in uso[s]["cit"]) or "nenhum"))
    out.append("")
    out.append("## Alertas")
    out.append("")
    if alertas:
        for i, al in enumerate(alertas, 1):
            out.append("%d. %s" % (i, al))
    else:
        out.append("Nenhum.")
    out.append("")
    destino = os.path.join(raiz, "docs", "MATRIZ-AGENTES-SKILLS.md")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print("Matriz gravada em %s" % destino)
    print("Agentes: %d | skills: %d | alertas: %d" % (len(agentes), len(skills), len(alertas)))
    for al in alertas:
        print("ALERTA: " + al)
    return 1 if (args.estrito and alertas) else 0


if __name__ == "__main__":
    sys.exit(main())
