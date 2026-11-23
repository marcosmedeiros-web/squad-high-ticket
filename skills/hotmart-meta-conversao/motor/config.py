"""config.py: lê e confere o perfil do dono (perfil.env).

Regras que este arquivo cobra, e por quê:
  * Tudo que decide ENVIO não tem valor padrão escondido. CAPI_MODO, CAPI_PURCHASE, CAPI_CHECKOUT e as duas
    declarações sobre o pixel nativo da Hotmart são obrigatórias. Perfil sem elas é recusado.
  * Purchase em dobro é recusado na instalação. A Hotmart tem pixel e API de Conversões próprios ("Pixel de
    Rastreamento", envio Web, API ou ambos). O event_id que ela usa não é publicado, então o kit não consegue
    deduplicar contra ela. Se o pixel nativo manda "Vendas realizadas", o kit não manda Purchase.
  * O mesmo vale para o clique de checkout: com "Visitas na página de pagamento" ligado na Hotmart, o site não
    pode mandar InitiateCheckout, só o evento personalizado.
  * Chave com nome errado recusa (erro de digitação vira configuração silenciosa).
  * O receptor só escuta em endereço local. HTTPS é papel do proxy (Caddy) na frente.

Uso de linha de comando: config.py --conferir <perfil.env>   (rc 0 ok, rc 78 recusado, MOTIVO= na 1a linha)
"""
import os
import re
import sys
from pathlib import Path


class PerfilRecusado(Exception):
    def __init__(self, motivo, detalhe=''):
        super().__init__(f'{motivo}: {detalhe}' if detalhe else motivo)
        self.motivo = motivo
        self.detalhe = detalhe


OBRIGATORIOS = ('HM_DADOS_DIR', 'HM_HOTTOK_ARQUIVO', 'HM_PORTA', 'CAPI_MODO', 'CAPI_PURCHASE', 'CAPI_CHECKOUT',
                'HOTMART_PIXEL_NATIVO_COMPRA', 'HOTMART_PIXEL_NATIVO_CHECKOUT')
OPCIONAIS = {
    'HM_ESCUTA': '127.0.0.1',
    'HM_PRODUTOS': '',
    'HM_RETENCAO_CONTATO_DIAS': '30',
    'HM_SITE_ORIGENS': '',
    'HM_CONFIA_PROXY': '1',
    'HM_AVISO_CANAL': '',
    'HM_HOTMART_CRED_ARQUIVO': '',
    'CAPI_PIXEL_ID': '',
    'CAPI_TOKEN_ARQUIVO': '',
    'CAPI_TEST_EVENT_CODE': '',
    'CAPI_VERSAO_GRAPH': 'v25.0',
    'CAPI_VALOR': 'preco',
    'CAPI_RECORRENCIA': 'primeira',
    'CAPI_ABANDONO': 'desligado',
    'CAPI_URL_PADRAO': '',
    'CAPI_ORIGEM_SEM_NAVEGADOR': 'other',
    'SITE_EVENTO_CLIQUE': '',
    'VIGIA_JANELA_HORAS': '48',
    'VIGIA_TOLERANCIA_MIN': '30',
    'VIGIA_SILENCIO_HORAS': '0',
}
MARCADOR_VAZIO = 'PREENCHER'
_RE_ORIGEM = re.compile(r'^https://[a-z0-9.-]+(:[0-9]{2,5})?$')
_RE_URL = re.compile(r'^https://[^\s]{4,500}$')


def ler_env(caminho):
    """NOME=VALOR por linha. Linha com crase, $( ou sem '=' recusa (o arquivo nunca é executado por shell)."""
    p = Path(caminho)
    if not p.is_file():
        raise PerfilRecusado('perfil_ausente', str(caminho))
    valores, ruins = {}, 0
    for linha in p.read_text(encoding='utf-8', errors='replace').splitlines():
        s = linha.strip()
        if not s or s.startswith('#'):
            continue
        if s.startswith('export '):
            s = s[len('export '):].strip()
        if '`' in s or '$(' in s or '=' not in s:
            ruins += 1
            continue
        k, v = s.split('=', 1)
        v = re.sub(r'\s+#.*$', '', v)          # comentário no fim da linha (espaço antes do #)
        valores[k.strip()] = v.strip().strip('"').strip("'")
    if ruins:
        raise PerfilRecusado('linha_fora_do_formato', f'{ruins} linha(s) fora de NOME=VALOR em {caminho}')
    return valores


def _escolha(v, nome, opcoes):
    if v not in opcoes:
        raise PerfilRecusado('valor_invalido', f'{nome} tem que ser um de {"|".join(opcoes)}')
    return v


def _abs(v, nome):
    if not v.startswith('/'):
        raise PerfilRecusado('caminho_relativo', f'{nome} precisa de caminho absoluto')
    return v


def _int(v, nome, minimo, maximo):
    if not re.fullmatch(r'[0-9]{1,6}', v or '') or not (minimo <= int(v) <= maximo):
        raise PerfilRecusado('valor_invalido', f'{nome} tem que ser inteiro entre {minimo} e {maximo}')
    return int(v)


def conferir(valores):
    """-> dict normalizado. Levanta PerfilRecusado com o primeiro problema achado."""
    desconhecidas = sorted(k for k in valores if k not in OBRIGATORIOS and k not in OPCIONAIS)
    if desconhecidas:
        raise PerfilRecusado('chave_desconhecida', ', '.join(desconhecidas))
    for k, v in valores.items():
        if MARCADOR_VAZIO in v:
            raise PerfilRecusado('campo_nao_preenchido', k)
    for k in OBRIGATORIOS:
        if not valores.get(k):
            raise PerfilRecusado('campo_obrigatorio', k)
    c = dict(OPCIONAIS)
    c.update(valores)
    p = {}
    p['dados_dir'] = _abs(c['HM_DADOS_DIR'], 'HM_DADOS_DIR')
    p['hottok_arquivo'] = _abs(c['HM_HOTTOK_ARQUIVO'], 'HM_HOTTOK_ARQUIVO')
    p['porta'] = _int(c['HM_PORTA'], 'HM_PORTA', 1024, 65535)
    p['escuta'] = c['HM_ESCUTA']
    if p['escuta'] not in ('127.0.0.1', '::1'):
        raise PerfilRecusado('escuta_nao_local', 'HM_ESCUTA tem que ser 127.0.0.1 ou ::1 (o HTTPS fica no proxy)')
    p['produtos'] = [x.strip() for x in c['HM_PRODUTOS'].split(',') if x.strip()]
    for x in p['produtos']:
        if not re.fullmatch(r'[0-9]{1,15}', x):
            raise PerfilRecusado('valor_invalido', 'HM_PRODUTOS aceita só ids numéricos separados por vírgula')
    p['retencao_contato_dias'] = _int(c['HM_RETENCAO_CONTATO_DIAS'], 'HM_RETENCAO_CONTATO_DIAS', 1, 90)
    p['site_origens'] = [x.strip().lower() for x in c['HM_SITE_ORIGENS'].split(',') if x.strip()]
    for o in p['site_origens']:
        if not _RE_ORIGEM.match(o):
            raise PerfilRecusado('valor_invalido', 'HM_SITE_ORIGENS: só https://dominio, sem caminho')
    p['confia_proxy'] = _escolha(c['HM_CONFIA_PROXY'], 'HM_CONFIA_PROXY', ('0', '1')) == '1'
    p['aviso_canal'] = c['HM_AVISO_CANAL']
    if p['aviso_canal'] and not re.match(r'^(arquivo|comando):/', p['aviso_canal']):
        raise PerfilRecusado('valor_invalido', 'HM_AVISO_CANAL: arquivo:/caminho.jsonl ou comando:/script')
    p['hotmart_cred_arquivo'] = c['HM_HOTMART_CRED_ARQUIVO']
    if p['hotmart_cred_arquivo']:
        _abs(p['hotmart_cred_arquivo'], 'HM_HOTMART_CRED_ARQUIVO')

    p['modo'] = _escolha(c['CAPI_MODO'], 'CAPI_MODO', ('seco', 'teste', 'real'))
    p['nativo_compra'] = _escolha(c['HOTMART_PIXEL_NATIVO_COMPRA'], 'HOTMART_PIXEL_NATIVO_COMPRA',
                                  ('ligado', 'desligado'))
    p['nativo_checkout'] = _escolha(c['HOTMART_PIXEL_NATIVO_CHECKOUT'], 'HOTMART_PIXEL_NATIVO_CHECKOUT',
                                    ('ligado', 'desligado'))
    p['capi_purchase'] = _escolha(c['CAPI_PURCHASE'], 'CAPI_PURCHASE', ('kit', 'desligado'))
    p['capi_checkout'] = _escolha(c['CAPI_CHECKOUT'], 'CAPI_CHECKOUT', ('kit', 'desligado'))
    if p['capi_purchase'] == 'kit' and p['nativo_compra'] == 'ligado':
        raise PerfilRecusado('purchase_em_dobro', 'o pixel da Hotmart já manda Purchase; desligue "Vendas realizadas" '
                             'lá ou use CAPI_PURCHASE=desligado')
    evento_clique = c['SITE_EVENTO_CLIQUE'] or ('CliqueCheckout' if p['nativo_checkout'] == 'ligado'
                                                 else 'InitiateCheckout')
    p['evento_clique'] = _escolha(evento_clique, 'SITE_EVENTO_CLIQUE', ('InitiateCheckout', 'CliqueCheckout'))
    if p['evento_clique'] == 'InitiateCheckout' and p['nativo_checkout'] == 'ligado':
        raise PerfilRecusado('checkout_em_dobro', 'a Hotmart já manda InitiateCheckout na página de pagamento; '
                             'use SITE_EVENTO_CLIQUE=CliqueCheckout')
    if p['capi_checkout'] == 'kit' and not p['site_origens']:
        raise PerfilRecusado('campo_obrigatorio', 'HM_SITE_ORIGENS (CAPI_CHECKOUT=kit recebe o aviso do site)')

    p['pixel_id'] = c['CAPI_PIXEL_ID']
    p['token_arquivo'] = c['CAPI_TOKEN_ARQUIVO']
    p['test_event_code'] = c['CAPI_TEST_EVENT_CODE']
    p['versao_graph'] = c['CAPI_VERSAO_GRAPH']
    if not re.fullmatch(r'v[0-9]{2}\.[0-9]', p['versao_graph']):
        raise PerfilRecusado('valor_invalido', 'CAPI_VERSAO_GRAPH no formato v25.0')
    if p['modo'] != 'seco':
        if not re.fullmatch(r'[0-9]{8,20}', p['pixel_id']):
            raise PerfilRecusado('campo_obrigatorio', 'CAPI_PIXEL_ID (só dígitos) fora do modo seco')
        _abs(p['token_arquivo'] or 'x', 'CAPI_TOKEN_ARQUIVO')
    if p['modo'] == 'teste' and not re.fullmatch(r'[A-Z0-9]{4,20}', p['test_event_code']):
        raise PerfilRecusado('campo_obrigatorio', 'CAPI_TEST_EVENT_CODE (do Gerenciador de Eventos) no modo teste')
    if p['modo'] == 'real' and p['test_event_code']:
        raise PerfilRecusado('valor_invalido', 'CAPI_TEST_EVENT_CODE tem que sair do perfil no modo real')
    p['valor'] = _escolha(c['CAPI_VALOR'], 'CAPI_VALOR', ('preco', 'cheio'))
    p['recorrencia'] = _escolha(c['CAPI_RECORRENCIA'], 'CAPI_RECORRENCIA', ('primeira', 'todas'))
    p['capi_abandono'] = _escolha(c['CAPI_ABANDONO'], 'CAPI_ABANDONO', ('desligado', 'personalizado'))
    p['url_padrao'] = c['CAPI_URL_PADRAO']
    if p['url_padrao'] and not _RE_URL.match(p['url_padrao']):
        raise PerfilRecusado('valor_invalido', 'CAPI_URL_PADRAO tem que ser https://')
    p['origem_sem_navegador'] = _escolha(c['CAPI_ORIGEM_SEM_NAVEGADOR'], 'CAPI_ORIGEM_SEM_NAVEGADOR',
                                         ('other', 'system_generated', 'website'))
    p['vigia_janela_h'] = _int(c['VIGIA_JANELA_HORAS'], 'VIGIA_JANELA_HORAS', 1, 720)
    p['vigia_tolerancia_min'] = _int(c['VIGIA_TOLERANCIA_MIN'], 'VIGIA_TOLERANCIA_MIN', 5, 1440)
    p['vigia_silencio_h'] = _int(c['VIGIA_SILENCIO_HORAS'], 'VIGIA_SILENCIO_HORAS', 0, 720)
    return p


def carregar(caminho=None):
    caminho = caminho or os.environ.get('HM_PERFIL', '')
    if not caminho:
        raise PerfilRecusado('perfil_ausente', 'defina HM_PERFIL=/caminho/perfil.env')
    return conferir(ler_env(caminho))


def main(argv):
    if len(argv) != 3 or argv[1] != '--conferir':
        print('uso: config.py --conferir <perfil.env>', file=sys.stderr)
        return 2
    try:
        p = carregar(argv[2])
    except PerfilRecusado as e:
        print(f'MOTIVO={e.motivo}', file=sys.stderr)
        print(f'perfil: {e.detalhe}', file=sys.stderr)
        return 78
    print(f'perfil ok: modo={p["modo"]} purchase={p["capi_purchase"]} checkout={p["capi_checkout"]} '
          f'evento_clique={p["evento_clique"]} abandono_capi={p["capi_abandono"]}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
