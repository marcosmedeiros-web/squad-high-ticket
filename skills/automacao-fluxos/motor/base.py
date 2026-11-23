"""base.py: perfil do dono, segredos, caminhos e o vocabulário comum do motor. Só biblioteca padrão.

O perfil é um arquivo NOME=VALOR do dono, fora do pacote (modelo em perfil/perfil.exemplo.env). Toda recusa sai
como `Recusa(motivo)`, e o CLI imprime `MOTIVO=<motivo>` na primeira linha do stderr. Valor de segredo nunca entra
em mensagem de erro, repr nem log: só o CAMINHO do arquivo e o motivo.
"""
import hashlib
import hmac
import json
import os
import re
from pathlib import Path

PREENCHER = 'PREENCHER'
_RE_LINHA = re.compile(r'^([A-Z][A-Z0-9_]{1,60})=(.*)$')
_RE_NOME_FLUXO = re.compile(r'^[a-z][a-z0-9-]{2,40}$')


class Recusa(Exception):
    """Motivo curto e fechado (slug) mais um detalhe para gente; o rc do CLI vem junto."""
    def __init__(self, motivo, detalhe='', rc=11):
        super().__init__(f'{motivo}: {detalhe}' if detalhe else motivo)
        self.motivo = motivo
        self.detalhe = detalhe
        self.rc = rc


def sha(texto, n=None):
    h = hashlib.sha256(texto.encode('utf-8')).hexdigest()
    return h[:n] if n else h


def iguais(a, b):
    """Comparação em tempo constante para segredo (nunca `==`)."""
    return hmac.compare_digest(a.encode('utf-8'), b.encode('utf-8'))


def fisico(caminho):
    """Caminho físico, mesmo quando o destino ainda não existe: resolve o PAI QUE EXISTE e junta o resto.
    No macOS /var é /private/var e /tmp é /private/tmp: comparar o caminho cru deixa passar um destino dentro de
    uma pasta proibida. os.path.realpath sozinho não resolve o pai de um caminho que ainda não existe em todo
    sistema, então a caminhada é explícita."""
    p = Path(os.path.expanduser(str(caminho)))
    if not p.is_absolute():
        p = Path.cwd() / p
    resto = []
    atual = p
    while not atual.exists():
        if atual.parent == atual:
            break
        resto.append(atual.name)
        atual = atual.parent
    base = Path(os.path.realpath(atual))
    for nome in reversed(resto):
        base = base / nome
    return base


def dentro_de(filho, pai):
    f, p = fisico(filho), fisico(pai)
    return f == p or p in f.parents


# ------------------------------------------------------------------------------------------------- segredos
def ler_segredo(caminho, nomes):
    """Lê NOME=VALOR de um arquivo do dono: regular, não link, do mesmo usuário, sem permissão de grupo nem de
    outros (600 ou 400). Formato simples, sem crase nem $( (o arquivo nunca é executado, mas quem escreve com
    isso esperava expansão e o valor estaria errado)."""
    if not caminho:
        raise Recusa('segredo_nao_configurado', 'falta o caminho do arquivo no perfil', rc=10)
    p = Path(caminho)
    if p.is_symlink() or not p.is_file():
        raise Recusa('segredo_ausente', str(p), rc=10)
    st = p.stat()
    if st.st_mode & 0o077:
        raise Recusa('permissao_segredo', f'{p} (exigido 600: chmod 600 {p})', rc=10)
    if hasattr(os, 'geteuid') and st.st_uid != os.geteuid():
        raise Recusa('dono_segredo', str(p), rc=10)
    achados = {}
    for linha in p.read_text(encoding='utf-8', errors='replace').splitlines():
        s = linha.strip()
        if not s or s.startswith('#'):
            continue
        if '`' in s or '$(' in s or '=' not in s:
            raise Recusa('formato_segredo', f'{p} (uma linha NOME=VALOR por segredo)', rc=10)
        k, v = s.split('=', 1)
        if k.strip() in nomes:
            achados[k.strip()] = v.strip().strip('"').strip("'")
    faltam = [n for n in nomes if not achados.get(n)]
    if faltam:
        raise Recusa('segredo_vazio', f'{p} não tem {", ".join(faltam)}', rc=10)
    return achados


# ------------------------------------------------------------------------------------------------- perfil
PADROES = {
    'AF_DADOS_DIR': PREENCHER,
    'AF_FLUXOS_DIR': PREENCHER,
    'AF_URL_PUBLICA': PREENCHER,
    'AF_PORTA': '8790',
    'AF_FUSO_UTC': '-3',
    'AF_AVISO_CANAL': 'avisar-dono',
    'HEAD_TURBO_HOME': '~/.claude/head-turbo',
    'AF_MAUTIC_URL': '',
    'AF_MAUTIC_CRED_ARQUIVO': '',
    'AF_OPENWA_BASE': '',
    'AF_OPENWA_SESSAO_ID': '',
    'AF_OPENWA_CHAVE_ARQUIVO': '',
    'AF_HOTMART_HOTTOK_ARQUIVO': '',
    'AF_JANELA_INICIO': '8',
    'AF_JANELA_FIM': '21',
    'AF_TETO_WHATSAPP_DIA': '60',
    'AF_RETENCAO_DIAS': '30',
    'AF_CONFIRMAR_S': '60',
}


def _int(c, nome, lo, hi):
    v = c[nome]
    if not re.fullmatch(r'-?[0-9]{1,6}', v or '') or not lo <= int(v) <= hi:
        raise Recusa('perfil_valor_invalido', f'{nome}={v!r} (de {lo} a {hi})')
    return int(v)


def ler_perfil(caminho=None):
    caminho = caminho or os.environ.get('AF_PERFIL') or ''
    if not caminho:
        raise Recusa('sem_perfil', 'passe --perfil <perfil.env> ou AF_PERFIL')
    p = Path(os.path.expanduser(caminho))
    if not p.is_file():
        raise Recusa('sem_perfil', f'não achei {p}')
    c = dict(PADROES)
    for n, linha in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
        s = linha.strip()
        if not s or s.startswith('#'):
            continue
        s = re.sub(r'\s+#.*$', '', s)
        m = _RE_LINHA.match(s)
        if not m:
            raise Recusa('perfil_linha_torta', f'{p}:{n}')
        if m.group(1) not in PADROES:
            raise Recusa('perfil_chave_desconhecida', f'{p}:{n} {m.group(1)}')
        c[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    falta = [k for k, v in c.items() if v == PREENCHER]
    if falta:
        raise Recusa('perfil_incompleto', 'preencha ' + ', '.join(falta))
    out = {'arquivo': str(p)}
    for k in ('AF_DADOS_DIR', 'AF_FLUXOS_DIR', 'HEAD_TURBO_HOME'):
        v = os.path.expanduser(c[k])
        if not os.path.isabs(v):
            raise Recusa('perfil_caminho_relativo', f'{k} precisa ser caminho absoluto')
        out[k.lower()] = v
    url = c['AF_URL_PUBLICA'].rstrip('/')
    if not re.fullmatch(r'https://[a-z0-9.-]{3,200}(:[0-9]{2,5})?(/[A-Za-z0-9._/-]*)?', url):
        raise Recusa('perfil_url_publica', 'AF_URL_PUBLICA precisa ser https://<subdomínio do dono>')
    out['url_publica'] = url
    out['porta'] = _int(c, 'AF_PORTA', 1024, 65535)
    out['fuso_utc'] = _int(c, 'AF_FUSO_UTC', -12, 14)
    out['janela_inicio'] = _int(c, 'AF_JANELA_INICIO', 0, 23)
    out['janela_fim'] = _int(c, 'AF_JANELA_FIM', 1, 24)
    if out['janela_fim'] <= out['janela_inicio']:
        raise Recusa('perfil_valor_invalido', 'AF_JANELA_FIM tem que ser depois de AF_JANELA_INICIO')
    out['teto_whatsapp_dia'] = _int(c, 'AF_TETO_WHATSAPP_DIA', 1, 1000)
    out['retencao_dias'] = _int(c, 'AF_RETENCAO_DIAS', 1, 365)
    out['confirmar_s'] = _int(c, 'AF_CONFIRMAR_S', 5, 600)
    canal = c['AF_AVISO_CANAL']
    if not (canal in ('avisar-dono', 'arquivo') or re.fullmatch(r'comando:/[^\s]+', canal)):
        raise Recusa('perfil_canal_torto', 'AF_AVISO_CANAL aceita avisar-dono, arquivo ou comando:/caminho')
    out['aviso_canal'] = canal
    m = c['AF_MAUTIC_URL'].rstrip('/')
    if m and not re.fullmatch(r'(https://[a-z0-9.-]{3,200}(:[0-9]{2,5})?|http://(127\.0\.0\.1|localhost):[0-9]{2,5})(/[A-Za-z0-9._/-]*)?', m):
        raise Recusa('perfil_mautic_url', 'AF_MAUTIC_URL precisa ser https://... (ou http://127.0.0.1:<porta>)')
    out['mautic_url'] = m
    out['mautic_cred'] = os.path.expanduser(c['AF_MAUTIC_CRED_ARQUIVO'])
    w = c['AF_OPENWA_BASE'].rstrip('/')
    if w and not re.fullmatch(r'http://(127\.0\.0\.1|localhost):[0-9]{2,5}(/[A-Za-z0-9._/-]*)?', w):
        raise Recusa('perfil_openwa_base', 'AF_OPENWA_BASE só local: http://127.0.0.1:<porta>/api')
    out['openwa_base'] = w
    sid = c['AF_OPENWA_SESSAO_ID']
    if sid and not re.fullmatch(r'[0-9a-fA-F-]{36}', sid):
        raise Recusa('perfil_openwa_sessao', 'AF_OPENWA_SESSAO_ID é o uuid da sessão')
    out['openwa_sessao'] = sid
    out['openwa_chave'] = os.path.expanduser(c['AF_OPENWA_CHAVE_ARQUIVO'])
    out['hottok_arquivo'] = os.path.expanduser(c['AF_HOTMART_HOTTOK_ARQUIVO'])
    return out


def nome_rota(fluxo):
    return 'ROTA_' + fluxo.upper().replace('-', '_')


def nome_fluxo_valido(nome):
    return isinstance(nome, str) and bool(_RE_NOME_FLUXO.match(nome))


def json_canonico(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
