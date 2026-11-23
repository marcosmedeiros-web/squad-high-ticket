"""Regua de copy de risco para o servico de envio.

Por que existe: a politica de uso aceitavel do Resend (versao de 13/10/2026) proibe por nome "get rich quick
opportunities" e deixa a criterio dele qualquer negocio "high risk", com desligamento possivel sem aviso. Curso de
marketing digital nao e isso por si; o que aproxima e a COPY que promete renda. SendGrid e SES nao nomeiam a
categoria, mas reclamacao de spam derruba conta nos tres. Ver references/esp-politicas.md.

A regua procura promessa de dinheiro facil e de ganho garantido. Ela nao julga o produto: aponta o trecho para o
copywriter reescrever. Com o Resend (o padrao do kit) ela e GUARDA DO ENVIO: o texto que reprova nao sai, nem no
plano, nem no canario, nem no lote, nem no resto, e nao ha opcao para passar por cima. Com SES e SendGrid (reservas)
ela AVISA.
"""
import re
import unicodedata

from .saida import Recusa, info

PADROES = [
    (r'fique ric[oa]|enriquec', 'promessa de enriquecer'),
    (r'dinheiro f[aá]cil|grana f[aá]cil', 'dinheiro facil'),
    (r'renda (extra|passiva)', 'renda extra ou passiva'),
    (r'(lucro|ganho|retorno|resultado|faturamento) garantid', 'ganho garantido'),
    (r'(ganhe|fature|faturar|lucre|lucrar|ganhar)\s+(at[eé]\s+)?(r\$\s?)?\d', 'valor de ganho prometido'),
    (r'\d+\s?(mil|k)\s*(reais\s*)?(por|/|ao)\s?(m[eê]s|dia|semana)', 'valor por periodo'),
    (r'sem (esfor[cç]o|trabalhar|experi[eê]ncia)', 'ganho sem esforco'),
    (r'trabalh[ea] (de|em) casa', 'trabalhe de casa'),
    (r'liberdade financeira|independ[eê]ncia financeira', 'liberdade financeira'),
    (r'(milion[aá]ri|primeiro milh[aã]o)', 'milionario'),
    (r'(roas|retorno)\s+\d+\s?x\s+garantid', 'retorno garantido'),
]
_RE = [(re.compile(p, re.I), rotulo) for p, rotulo in PADROES]


def _texto(html):
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', html or '', flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = re.sub(r'&nbsp;', ' ', t)
    return unicodedata.normalize('NFC', re.sub(r'\s+', ' ', t))


def achados(assunto, html):
    """-> lista de (rotulo, trecho de ate 60 caracteres)."""
    out = []
    for origem in (assunto or '', _texto(html)):
        for r, rotulo in _RE:
            for m in r.finditer(origem):
                a, b = max(0, m.start() - 20), min(len(origem), m.end() + 20)
                out.append((rotulo, origem[a:b].strip()[:60]))
    return out


def politica(esp):
    return 'bloquear' if esp == 'resend' else 'avisar'


def guarda_envio(esp, assunto, html, passo):
    """Chamada antes de TODO envio. Com o Resend, achado = Recusa (nada sai). Com os outros, so mostra."""
    ach = achados(assunto, html)
    for rotulo, trecho in ach:
        info(f'[copy de risco] {rotulo}: "{trecho}"')
    if ach and politica(esp) == 'bloquear':
        raise Recusa('copy_reprovada_para_o_resend', rc=1, passo=passo, achados=len(ach),
                     fazer='reescrever_sem_promessa_de_ganho_e_refazer_o_plano')
    return len(ach)
