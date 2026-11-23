"""Modulo (a): endereco publico com HTTPS para o Mautic, e o SELO que libera o disparo para segmento.

Por que publico: o pixel de abertura, o clique rastreado, a pagina de descadastro e o formulario sao servidos pelo
MESMO host. Proteger o dominio inteiro com senha quebra os quatro; se um dia quiser camada extra, proteja so /s/*.

O selo so nasce quando TUDO foi medido de fora:
  1. DNS publico do endereco aponta para algum IP (resolvedor publico, nao o da VPS);
  2. certificado valido e /s/login responde 200 com o formulario, sem redirecionar (pega laco de redirect);
  3. a rota publica de descadastro responde sem pedir senha e sem redirecionar;
  4. uma mensagem REAL entregue (o .eml do canario) traz List-Unsubscribe e links de descadastro e de clique no
     endereco publico com HTTPS, assinada pelo dominio do dono.
Sem o item 4 o estado e "https ok, descadastro nao medido", e a guarda continua fechada.
"""
import json
import os
import re
import secrets
import time

from . import rede
from .cabecalho import conferir_eml
from .docker_cfg import Docker
from .saida import Recusa, info, motivo

AQUI = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAT_SITE = re.compile(r"^(\s*'site_url'\s*=>\s*)'([^']*)'(\s*,\s*)$", re.M)


def _dominio_valido(d):
    return bool(re.fullmatch(r'(?=.{4,253}$)([a-z0-9-]{1,63}\.)+[a-z]{2,63}', d.lower()))


def gerar_caddy(perfil, modo, upstream, saida=None):
    dom = perfil['EMK_DOMINIO_MAUTIC']
    if not _dominio_valido(dom):
        raise Recusa('dominio_invalido', rc=3, dominio=dom)
    if modo not in ('container', 'host'):
        raise Recusa('modo_caddy_invalido', rc=3, aceitos='container|host')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+:\d{1,5}', upstream):
        raise Recusa('upstream_invalido', rc=3, exemplo='nome-do-container:80_ou_localhost:8080')
    with open(os.path.join(AQUI, 'modelos', f'caddy-{modo}.caddy'), encoding='utf-8') as f:
        txt = f.read().replace('{{DOMINIO}}', dom).replace('{{UPSTREAM}}', upstream)
    if saida:
        with open(saida, 'w', encoding='utf-8') as f:
            f.write(txt)
        info(f'bloco do Caddy gravado em {saida}')
    else:
        info(txt)
    return motivo('caddy_gerado', 0, modo=modo, dominio=dom)


def checar_ao_vivo(dom):
    """Itens 1 a 3. -> lista de (nome, estado, detalhe), estado em ok|falhou|nao_medido."""
    itens = []
    a = rede.doh(dom, 'A')
    aaaa = rede.doh(dom, 'AAAA')
    if a is None and aaaa is None:
        itens.append(('dns_publico', 'nao_medido', 'resolvedor publico nao respondeu'))
    else:
        ips = (a or []) + (aaaa or [])
        itens.append(('dns_publico', 'ok' if ips else 'falhou', ','.join(ips) or 'sem registro A/AAAA'))
    h = rede.hop(f'https://{dom}/s/login')
    if h['classe'] != 'resposta':
        est = 'falhou' if str(h.get('erro', '')).startswith('tls:') else 'nao_medido'
        itens.append(('https_login', est, h.get('erro', '')))
    elif h['codigo'] != 200:
        itens.append(('https_login', 'falhou', f"http {h['codigo']} (redirect aqui = laco ou site_url errado)"))
    elif 'name="_username"' not in (h.get('corpo') or ''):
        itens.append(('https_login', 'falhou', '200 sem o formulario de login'))
    else:
        hsts = any(k.lower() == 'strict-transport-security' for k in h.get('headers', {}))
        itens.append(('https_login', 'ok', 'com HSTS' if hsts else 'sem HSTS (recomendado ligar)'))
    falso = secrets.token_hex(12)
    u = rede.hop(f'https://{dom}/email/unsubscribe/{falso}')
    if u['classe'] != 'resposta':
        est = 'falhou' if str(u.get('erro', '')).startswith('tls:') else 'nao_medido'
        itens.append(('rota_descadastro_publica', est, u.get('erro', '')))
    elif u['codigo'] in (200, 404):
        itens.append(('rota_descadastro_publica', 'ok', f"http {u['codigo']} com codigo falso (sem efeito em ninguem)"))
    else:
        itens.append(('rota_descadastro_publica', 'falhou',
                      f"http {u['codigo']} (401/403 = senha no dominio inteiro; 30x = redirect)"))
    return itens


def _arquivo_selo(perfil):
    return os.path.join(perfil.estado_dir(), 'selo-https.json')


def conferir(perfil, eml=None):
    perfil.exigir('https')
    dom = perfil['EMK_DOMINIO_MAUTIC']
    if not _dominio_valido(dom):
        raise Recusa('dominio_invalido', rc=3, dominio=dom)
    itens = checar_ao_vivo(dom)
    eml_ok = None
    if eml:
        with open(os.path.expanduser(eml), 'rb') as f:
            eml_ok, sub = conferir_eml(f.read(), dom, perfil['EMK_DOMINIO_REMETENTE'], perfil['EMK_ESP'])
        for nome, ok, det in sub:
            itens.append(('eml:' + nome, 'ok' if ok else 'falhou', det))
    for nome, est, det in itens:
        info(f'[{est}] {nome} {det}')
    if any(e == 'falhou' for _, e, _ in itens):
        return motivo('https_reprovado', 1, dominio=dom)
    if any(e == 'nao_medido' for _, e, _ in itens):
        return motivo('https_nao_medido', 2, dominio=dom)
    if not eml:
        return motivo('https_ok_descadastro_nao_medido', 1, dominio=dom,
                      fazer='mandar_o_canario_e_rodar_de_novo_com_--eml')
    selo = {'dominio': dom, 'quando': int(time.time()), 'itens': [n for n, _, _ in itens], 'eml': True}
    tmp = _arquivo_selo(perfil) + '.tmp'
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, 'w') as f:
        json.dump(selo, f)
    os.replace(tmp, _arquivo_selo(perfil))
    return motivo('https_e_descadastro_ok', 0, dominio=dom, selo=_arquivo_selo(perfil))


def guarda(perfil):
    """Trava do disparo para segmento. Recusa (rc 1) se o selo nao existe, venceu, e de outro dominio, ou se o
    endereco publico caiu AGORA. Medicao que falha conta como fechado, nunca como aberto."""
    dom = perfil['EMK_DOMINIO_MAUTIC']
    try:
        with open(_arquivo_selo(perfil), encoding='utf-8') as f:
            selo = json.load(f)
    except (OSError, ValueError):
        raise Recusa('lista_bloqueada_sem_https', rc=1, fazer='email-mkt https conferir --eml <canario.eml>')
    if selo.get('dominio') != dom or not selo.get('eml'):
        raise Recusa('lista_bloqueada_selo_de_outro_dominio', rc=1)
    validade = perfil.int('EMK_SELO_VALIDADE_H') * 3600
    if time.time() - int(selo.get('quando', 0)) > validade:
        raise Recusa('lista_bloqueada_selo_vencido', rc=1, fazer='email-mkt https conferir --eml <canario.eml>')
    agora = checar_ao_vivo(dom)
    ruins = [n for n, e, _ in agora if e != 'ok']
    if ruins:
        raise Recusa('lista_bloqueada_https_caiu_agora', rc=1, item=ruins[0])
    return True


def site_url(perfil, aplicar=False, dk=None):
    perfil.exigir('https', 'docker')
    dk = dk or Docker(perfil.docker_cmd())
    web = perfil['EMK_CT_WEB']
    alvo = f"https://{perfil['EMK_DOMINIO_MAUTIC']}"
    txt = dk.ler_local_php(web).decode()
    ms = list(PAT_SITE.finditer(txt))
    if len(ms) != 1:
        raise Recusa('site_url_nao_unico', rc=2, achadas=len(ms))
    atual = ms[0].group(2).rstrip('/')
    if atual == alvo:
        return motivo('site_url_ok', 0, site_url=atual)
    if not aplicar:
        info(f'site_url atual: {atual} ; esperado: {alvo}')
        return motivo('site_url_diferente', 1, fazer='email-mkt https site-url --aplicar')
    dk.backup_local_php(web, 'site-url')
    novo = txt[:ms[0].start(2)] + alvo + txt[ms[0].end(2):]
    dk.gravar_local_php(web, novo.encode())
    for ct in (perfil['EMK_CT_WEB'], perfil['EMK_CT_WORKER'], perfil['EMK_CT_CRON']):
        dk.console(ct, ['cache:clear'], motivo='cache_clear_falhou')
    return motivo('site_url_aplicado', 0, site_url=alvo, fazer='email-mkt https conferir')
