"""Perfil do dono (perfil.env) e cofre de credenciais.

O perfil e um arquivo KEY=VALOR lido como TEXTO (nunca executado por shell). O cofre e outro arquivo KEY=VALOR,
com permissao 600, fora do pacote; o valor fica so em memoria e nunca e impresso, nem em pedaco, nem em hash.
"""
import os
import re
import stat

from .saida import Recusa

ESPS = ('ses', 'sendgrid', 'resend')
MODOS = ('seco', 'canario', 'lista')

# Valor que ainda e o exemplo do pacote: recusa em vez de usar.
_PLACEHOLDER = re.compile(r'(<[^>]*>|PREENCHER|seudominio|exemplo\.com)', re.I)

PADROES = {
    'EMK_DOCKER': 'docker',
    'EMK_MODO': 'seco',
    'EMK_LOTE_PILOTO': '5',
    'EMK_AVISO_CANAL': 'arquivo',
    'EMK_DISCO_ALERTA_PCT': '85',
    'EMK_DISCO_URGENTE_PCT': '92',
    'EMK_DISCO_CRESCIMENTO_GB_30MIN': '5',
    'EMK_SELO_VALIDADE_H': '168',
    'EMK_SES_REGIAO': 'sa-east-1',
    'EMK_COMPOSE_CMD': 'docker compose',
    'EMK_ESP_RESERVA': 'ses,sendgrid',
}

# Chaves que cada grupo de comandos exige.
EXIGE = {
    'base': ('EMK_ESP', 'EMK_ESTADO_DIR'),
    'https': ('EMK_DOMINIO_MAUTIC',),
    'api': ('EMK_API_URL', 'EMK_API_ARQUIVO'),
    'docker': ('EMK_CT_WEB', 'EMK_CT_WORKER', 'EMK_CT_CRON', 'EMK_CT_DB'),
    'envio': ('EMK_CHAVE_ARQUIVO', 'EMK_DOMINIO_REMETENTE', 'EMK_REMETENTE'),
    'disparo': ('EMK_CANARIO_CONTATO_ID', 'EMK_EMPRESA_NOME', 'EMK_EMPRESA_ENDERECO', 'EMK_DOMINIO_MAUTIC'),
    'compose': ('EMK_COMPOSE_DIR', 'EMK_SERVICO_DB', 'EMK_SERVICOS_MAUTIC'),
}


def ler_kv(caminho):
    out = {}
    with open(caminho, encoding='utf-8') as f:
        for n, linha in enumerate(f, 1):
            s = linha.strip()
            if not s or s.startswith('#'):
                continue
            if s.startswith('export '):
                s = s[7:].strip()
            if '=' not in s:
                raise Recusa('perfil_linha_invalida', rc=3, linha=n)
            k, v = s.split('=', 1)
            k = k.strip()
            if not re.fullmatch(r'[A-Z][A-Z0-9_]*', k):
                raise Recusa('perfil_chave_invalida', rc=3, linha=n)
            v = v.strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
                v = v[1:-1]
            out[k] = v
    return out


class Perfil:
    def __init__(self, dados, caminho='(memoria)'):
        self.caminho = caminho
        self.d = dict(PADROES)
        self.d.update({k: v for k, v in dados.items() if v != ''})

    @classmethod
    def carregar(cls, caminho=None):
        caminho = caminho or os.environ.get('EMK_PERFIL')
        if not caminho:
            raise Recusa('perfil_ausente', rc=3, dica='EMK_PERFIL=<arquivo> ou --perfil')
        caminho = os.path.expanduser(caminho)
        if not os.path.isfile(caminho):
            raise Recusa('perfil_ausente', rc=3, caminho=caminho)
        dados = ler_kv(caminho)
        desconhecidas = [k for k in dados if not k.startswith('EMK_')]
        if desconhecidas:
            raise Recusa('perfil_chave_desconhecida', rc=3, chave=desconhecidas[0])
        return cls(dados, caminho)

    def get(self, k, padrao=None):
        return self.d.get(k, padrao)

    def __getitem__(self, k):
        v = self.d.get(k)
        if v is None or v == '':
            raise Recusa('perfil_campo_vazio', rc=3, campo=k)
        if _PLACEHOLDER.search(v):
            raise Recusa('perfil_campo_de_exemplo', rc=3, campo=k)
        return v

    def int(self, k):
        try:
            return int(self[k])
        except ValueError:
            raise Recusa('perfil_campo_nao_numerico', rc=3, campo=k)

    def caminho_de(self, k):
        return os.path.expanduser(self[k])

    def exigir(self, *grupos):
        for g in ('base',) + grupos:
            for k in EXIGE[g]:
                self[k]
        if self['EMK_ESP'] not in ESPS:
            raise Recusa('esp_desconhecido', rc=3, esp=self['EMK_ESP'], aceitos='|'.join(ESPS))
        if self.modo() not in MODOS:
            raise Recusa('modo_desconhecido', rc=3, modo=self.get('EMK_MODO'))

    def modo(self):
        return self.get('EMK_MODO', 'seco')

    def docker_cmd(self):
        return self['EMK_DOCKER'].split()

    def estado_dir(self):
        d = self.caminho_de('EMK_ESTADO_DIR')
        os.makedirs(d, mode=0o700, exist_ok=True)
        return d


def ler_cofre(caminho, nomes):
    """Le as variaveis `nomes` de um arquivo de segredo 600. Devolve dict em memoria. Recusa sem nunca citar valor."""
    caminho = os.path.expanduser(caminho)
    try:
        st = os.stat(caminho)
    except OSError:
        raise Recusa('cofre_ausente', rc=3, arquivo=caminho)
    if not stat.S_ISREG(st.st_mode):
        raise Recusa('cofre_nao_e_arquivo', rc=3, arquivo=caminho)
    if st.st_mode & 0o077:
        raise Recusa('cofre_permissao_aberta', rc=3, arquivo=caminho, modo=oct(st.st_mode & 0o777), exigido='600')
    if hasattr(os, 'getuid') and st.st_uid != os.getuid():
        raise Recusa('cofre_de_outro_dono', rc=3, arquivo=caminho)
    dados = ler_kv(caminho)
    falta = [n for n in nomes if not dados.get(n)]
    if falta:
        raise Recusa('cofre_sem_variavel', rc=3, arquivo=caminho, variavel=falta[0])
    return {n: dados[n] for n in nomes}
