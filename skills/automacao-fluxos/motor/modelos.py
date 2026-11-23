"""modelos.py: os FLUXOS-MODELO. Cada tipo sabe (1) conferir o desenho que o dono preencheu, (2) decidir o RAMO de
um evento que entrou e (3) listar os PASSOS que esse evento manda fazer. Nada aqui fala com rede nem com banco.

Tipos
  lead-formulario   formulário do site -> contato no Mautic (segmento, tags, e-mail opcional) e WhatsApp de boas-vindas
  venda-hotmart     webhook 2.0.0 da Hotmart, PURCHASE_APPROVED -> Mautic (segmento, e-mail) e WhatsApp de boas-vindas
  lembrete-aula     agenda de aulas ao vivo -> lembretes no(s) grupo(s) de WhatsApp na hora marcada
  batida            o fluxo roda FORA daqui (ManyChat, n8n, código do dono) e só manda uma batida a cada evento,
                    para o vigia saber se ele continua passando gente (comentário vira DM, fluxo sob medida)

TODO ROTEADOR TEM TRÊS SAÍDAS: entendi A, entendi B, NÃO ENTENDI. O "não entendi" tem ramo próprio (`sem_regra`,
`invalido`, `palavra_fora_da_lista`) e é contado e vigiado; ele nunca cai no mesmo destino de um ramo real.
Casamento de aceite e de palavra é pelo valor INTEIRO normalizado, nunca por pedaço: "não aceito" não é "aceito".
"""
import re
import string
import unicodedata
from datetime import datetime, timedelta, timezone

from base import Recusa, json_canonico, nome_fluxo_valido, sha

TIPOS = ('lead-formulario', 'venda-hotmart', 'lembrete-aula', 'batida')
ACEITE_PADRAO = ('sim', 'on', 'true', '1', 'yes', 'aceito', 'aceite', 'concordo', 'checked')
DIAS = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo')
_RE_EMAIL = re.compile(r'^[A-Za-z0-9._%+-]{1,64}@[A-Za-z0-9.-]{1,200}\.[A-Za-z]{2,24}$')
CAMPOS_TEXTO = {
    'lead-formulario': {'primeiro_nome', 'nome', 'link'},
    'venda-hotmart': {'primeiro_nome', 'nome', 'produto', 'link'},
    'lembrete-aula': {'titulo', 'data', 'hora', 'dia_semana', 'link'},
}
FORA_DO_DESENHO = ('descricao', 'vigia', 'teste', 'aulas')


def norm(t):
    """minúscula, sem acento, espaços colapsados: a forma em que palavra e aceite são comparados."""
    t = unicodedata.normalize('NFKD', str(t or '')).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'\s+', ' ', t).strip()


def desenho(cfg):
    """Digital do que o fluxo FAZ. Mudou o texto, o segmento ou o produto = desenho novo, que pede teste e OK de novo.
    Fica de fora o que não muda o que sai: descrição, limites do vigia, contatos de teste e a lista de aulas."""
    return sha(json_canonico({k: v for k, v in cfg.items() if k not in FORA_DO_DESENHO}), 16)


# ------------------------------------------------------------------------------------------------ textos
def _campos(texto):
    try:
        return {f for _, f, _, _ in string.Formatter().parse(texto) if f is not None}
    except ValueError:
        raise Recusa('texto_chave_torta', 'chave { } aberta sem fechar no texto') from None


def conferir_texto(texto, tipo, onde):
    if not isinstance(texto, str) or not texto.strip() or len(texto) > 1500:
        raise Recusa('texto_invalido', f'{onde}: texto vazio ou maior que 1500 caracteres')
    if '{{' in texto or '}}' in texto or 'cuf_' in texto:
        raise Recusa('texto_com_marcador_cru', f'{onde}: use {{campo}}, nunca marcador de outra ferramenta')
    desconhecidos = _campos(texto) - CAMPOS_TEXTO[tipo]
    if desconhecidos:
        raise Recusa('texto_campo_desconhecido', f'{onde}: {", ".join(sorted(desconhecidos))} '
                     f'(aceitos: {", ".join(sorted(CAMPOS_TEXTO[tipo]))})')


def conferir_whatsapp(w, tipo, onde):
    if not isinstance(w, dict):
        raise Recusa('fluxo_whatsapp_torto', onde)
    conferir_texto(w.get('texto'), tipo, f'{onde}.texto')
    if _campos(w['texto']) & {'primeiro_nome', 'nome'}:
        if not w.get('texto_sem_nome'):
            raise Recusa('fluxo_falta_texto_sem_nome', f'{onde}: o texto usa o nome; ponha texto_sem_nome para quem '
                         'não informou (senão sai "Oi ," para a pessoa)')
        conferir_texto(w['texto_sem_nome'], tipo, f'{onde}.texto_sem_nome')
        if _campos(w['texto_sem_nome']) & {'primeiro_nome', 'nome'}:
            raise Recusa('fluxo_texto_sem_nome_usa_nome', onde)
    if not isinstance(w.get('consentimento_base'), str) or len(w['consentimento_base'].strip()) < 10:
        raise Recusa('fluxo_sem_consentimento', f'{onde}.consentimento_base: diga como a pessoa aceitou receber '
                     'WhatsApp (a política do WhatsApp exige permissão antes de escrever)')


def render(texto, valores):
    return texto.format_map({k: (valores.get(k) or '') for k in _campos(texto)})


def conferir_mautic(m, onde):
    if not isinstance(m, dict):
        raise Recusa('fluxo_mautic_torto', onde)
    if not isinstance(m.get('segmento_id'), int) or m['segmento_id'] <= 0:
        raise Recusa('fluxo_mautic_segmento', f'{onde}.segmento_id: o número do segmento no Mautic')
    if 'email_id' in m and (not isinstance(m['email_id'], int) or m['email_id'] <= 0):
        raise Recusa('fluxo_mautic_email', f'{onde}.email_id')
    tags = m.get('tags', [])
    if not isinstance(tags, list) or not all(isinstance(t, str) and re.fullmatch(r'[A-Za-z0-9 ._-]{1,60}', t) for t in tags):
        raise Recusa('fluxo_mautic_tags', f'{onde}.tags: lista de nomes simples')


# ------------------------------------------------------------------------------------------------ conferência
def conferir(cfg, nome_arquivo=None):
    """Recusa (com motivo) qualquer desenho torto. Devolve o cfg."""
    if not isinstance(cfg, dict):
        raise Recusa('fluxo_nao_e_objeto')
    nome, tipo = cfg.get('nome'), cfg.get('tipo')
    if 'PREENCHER' in json_canonico(cfg):
        raise Recusa('fluxo_incompleto', f'{nome_arquivo or nome}: ainda tem PREENCHER no desenho')
    if not nome_fluxo_valido(nome):
        raise Recusa('fluxo_nome_invalido', 'nome: minúsculas, dígitos e hífen, de 3 a 41 caracteres')
    if nome_arquivo and nome != nome_arquivo:
        raise Recusa('fluxo_nome_diferente_do_arquivo', f'{nome_arquivo}.json declara nome {nome}')
    if tipo not in TIPOS:
        raise Recusa('fluxo_tipo_desconhecido', f'{nome}: tipo {tipo!r} (aceitos: {", ".join(TIPOS)})')
    v = cfg.get('vigia', {})
    if not isinstance(v, dict) or not all(isinstance(x, int) and x >= 0 for x in v.values()):
        raise Recusa('fluxo_vigia_torto', f'{nome}.vigia: números inteiros')
    t = cfg.get('teste', {})
    if not isinstance(t, dict):
        raise Recusa('fluxo_teste_torto', nome)
    if tipo == 'lead-formulario':
        c = cfg.get('campos')
        if not isinstance(c, dict) or not isinstance(c.get('email'), str):
            raise Recusa('fluxo_campos', f'{nome}.campos.email: o nome do campo de e-mail no formulário')
        if not (cfg.get('mautic') or cfg.get('whatsapp')):
            raise Recusa('fluxo_sem_saida', f'{nome}: precisa de mautic, whatsapp ou os dois')
        if cfg.get('mautic'):
            conferir_mautic(cfg['mautic'], f'{nome}.mautic')
        if cfg.get('whatsapp'):
            conferir_whatsapp(cfg['whatsapp'], tipo, f'{nome}.whatsapp')
            if not (isinstance(c.get('telefone'), str) and isinstance(c.get('consentimento_whatsapp'), str)):
                raise Recusa('fluxo_campos', f'{nome}.campos: com whatsapp, diga os campos telefone e '
                             'consentimento_whatsapp (a caixa de aceite do formulário)')
    elif tipo == 'venda-hotmart':
        prods = cfg.get('produtos')
        if not isinstance(prods, dict) or not prods:
            raise Recusa('fluxo_sem_produtos', f'{nome}.produtos: {{"<id do produto na Hotmart>": {{...}}}}')
        for pid, regra in prods.items():
            if not re.fullmatch(r'[0-9]{1,15}', pid) or not isinstance(regra, dict):
                raise Recusa('fluxo_produto_torto', f'{nome}.produtos.{pid}')
            if not (regra.get('mautic') or regra.get('whatsapp')):
                raise Recusa('fluxo_sem_saida', f'{nome}.produtos.{pid}: precisa de mautic, whatsapp ou os dois')
            if regra.get('mautic'):
                conferir_mautic(regra['mautic'], f'{nome}.produtos.{pid}.mautic')
            if regra.get('whatsapp'):
                conferir_whatsapp(regra['whatsapp'], tipo, f'{nome}.produtos.{pid}.whatsapp')
        ign = cfg.get('produtos_ignorados', [])
        if not isinstance(ign, list) or not all(isinstance(x, str) and x.isdigit() for x in ign):
            raise Recusa('fluxo_produtos_ignorados', f'{nome}.produtos_ignorados: lista de ids em texto')
        if set(ign) & set(prods):
            raise Recusa('fluxo_produto_duplo', f'{nome}: o mesmo produto em produtos e produtos_ignorados')
    elif tipo == 'lembrete-aula':
        gs = cfg.get('grupos')
        if not isinstance(gs, list) or not gs or not all(isinstance(g, str) and re.fullmatch(r'[0-9-]{10,40}@g\.us', g) for g in gs):
            raise Recusa('fluxo_grupos', f'{nome}.grupos: ids de grupo terminando em @g.us')
        ls = cfg.get('lembretes')
        if not isinstance(ls, list) or not ls:
            raise Recusa('fluxo_lembretes', f'{nome}.lembretes: lista de {{"antes_min": N, "texto": "..."}}')
        vistos = set()
        for i, lb in enumerate(ls):
            if not isinstance(lb, dict) or not isinstance(lb.get('antes_min'), int) or not 0 <= lb['antes_min'] <= 20160:
                raise Recusa('fluxo_lembretes', f'{nome}.lembretes[{i}].antes_min: minutos antes da aula (0 a 20160)')
            if lb['antes_min'] in vistos:
                raise Recusa('fluxo_lembretes', f'{nome}: dois lembretes com o mesmo antes_min')
            vistos.add(lb['antes_min'])
            conferir_texto(lb.get('texto'), tipo, f'{nome}.lembretes[{i}].texto')
        aulas_de(cfg)
        tg = t.get('grupos', [])
        if not isinstance(tg, list) or not all(isinstance(g, str) and re.fullmatch(r'[0-9-]{10,40}@g\.us', g) for g in tg):
            raise Recusa('fluxo_teste_torto', f'{nome}.teste.grupos: ids @g.us do grupo de teste')
    elif tipo == 'batida':
        ps = cfg.get('palavras', [])
        if not isinstance(ps, list) or not all(isinstance(p, str) and norm(p) for p in ps):
            raise Recusa('fluxo_palavras', f'{nome}.palavras: lista de palavras-chave')
    return cfg


def aulas_de(cfg):
    out = []
    ids = set()
    for i, a in enumerate(cfg.get('aulas', [])):
        if not isinstance(a, dict) or not re.fullmatch(r'[A-Za-z0-9_-]{1,40}', str(a.get('id', ''))):
            raise Recusa('fluxo_aula', f'{cfg["nome"]}.aulas[{i}].id')
        if a['id'] in ids:
            raise Recusa('fluxo_aula', f'{cfg["nome"]}: id de aula repetido ({a["id"]})')
        ids.add(a['id'])
        try:
            ini = datetime.fromisoformat(str(a.get('inicio', '')))
        except ValueError:
            ini = None
        if ini is None or ini.tzinfo is None:
            raise Recusa('fluxo_aula', f'{cfg["nome"]}.aulas[{i}].inicio: data e hora com fuso, '
                         'ex. 2026-10-20T20:00:00-03:00')
        if not isinstance(a.get('titulo'), str) or not a['titulo'].strip():
            raise Recusa('fluxo_aula', f'{cfg["nome"]}.aulas[{i}].titulo')
        link = a.get('link', '')
        if link and not re.fullmatch(r'https://\S{4,400}', link):
            raise Recusa('fluxo_aula', f'{cfg["nome"]}.aulas[{i}].link: https://...')
        out.append(dict(a, _inicio=ini))
    return out


# ------------------------------------------------------------------------------------------------ contato
def telefone_br(bruto, pais='BR'):
    """Telefone em dígitos com DDI. Fora do Brasil só passa se já vier com DDI (o fuso e o formato não são
    conhecidos aqui). None = ilegível."""
    d = re.sub(r'[^0-9]', '', str(bruto or ''))
    if pais == 'BR':
        if len(d) in (10, 11):
            d = '55' + d
        if d.startswith('55') and len(d) in (12, 13):
            return d
        return None
    return d if 11 <= len(d) <= 15 else None


def variantes_br(fone):
    """Com e sem o nono dígito: o WhatsApp de contas antigas pode estar registrado sem ele."""
    v = [fone]
    if fone.startswith('55') and len(fone) == 13 and fone[4] == '9':
        v.append(fone[:4] + fone[5:])
    elif fone.startswith('55') and len(fone) == 12 and fone[4] in '6789':
        v.append(fone[:4] + '9' + fone[4:])
    return v


def email_ok(e):
    e = (e or '').strip()
    return e.lower() if _RE_EMAIL.match(e) else None


def contato_h(email, fone):
    return sha('c:' + (email or fone or ''), 12) if (email or fone) else None


def no_teste(cfg, email, fone):
    t = cfg.get('teste', {})
    emails = {norm(x) for x in t.get('emails', [])}
    fones = set()
    for f in t.get('telefones', []):
        tf = telefone_br(f)
        if tf:
            fones.update(variantes_br(tf))
    return bool((email and norm(email) in emails) or (fone and fone in fones))


def _caminho(dados, chave):
    if chave in dados:
        return dados[chave]
    x = dados
    for parte in chave.split('.'):
        if isinstance(x, dict) and parte in x:
            x = x[parte]
        elif isinstance(x, list) and parte.isdigit() and int(parte) < len(x):
            x = x[int(parte)]
        else:
            return None
    return x


def _primeiro_nome(nome):
    p = (nome or '').strip().split()
    return p[0].capitalize() if p and re.fullmatch(r"[^\W\d_][^\W\d_'-]{0,40}", p[0]) else ''


# ------------------------------------------------------------------------------------------------ passos
def passos_saida(cfg_saida, email, fone, nome, consentiu, valores, tipo):
    """Mautic e WhatsApp de um evento. Cada saída que NÃO vai acontecer vira passo `pulado` com motivo, para o
    trânsito mostrar a pessoa que passou pelo fluxo e não recebeu, em vez de sumir."""
    passos = []
    m = cfg_saida.get('mautic')
    if m:
        if email:
            passos.append({'ordem': 1, 'tipo': 'mautic_contato', 'estado': 'pendente',
                           'dados': {'email': email, 'nome': nome, 'telefone': fone, 'tags': m.get('tags', []),
                                     'segmento_id': m['segmento_id']}})
            if m.get('email_id'):
                passos.append({'ordem': 2, 'tipo': 'mautic_email', 'depende': 1, 'estado': 'pendente',
                               'dados': {'email_id': m['email_id']}})
        else:
            passos.append({'ordem': 1, 'tipo': 'mautic_contato', 'estado': 'pulado', 'motivo': 'sem_email', 'dados': {}})
    w = cfg_saida.get('whatsapp')
    if w:
        if not fone:
            passos.append({'ordem': 3, 'tipo': 'whatsapp_individual', 'estado': 'pulado', 'motivo': 'sem_telefone',
                           'dados': {}})
        elif not consentiu:
            passos.append({'ordem': 3, 'tipo': 'whatsapp_individual', 'estado': 'pulado',
                           'motivo': 'sem_consentimento', 'dados': {}})
        else:
            base = w['texto'] if valores.get('primeiro_nome') else w.get('texto_sem_nome', w['texto'])
            texto = render(base, valores)
            passos.append({'ordem': 3, 'tipo': 'whatsapp_individual', 'estado': 'pendente',
                           'dados': {'telefone': fone, 'texto': texto, 'sha': sha(texto, 12)}})
    return passos


def entrada(cfg, corpo, cabecalhos=None):
    """Um evento que chegou pela rota. -> dict(ramo, chave, contato_h, passos, nota). Nunca levanta por causa do
    conteúdo: o que não entende vira ramo próprio."""
    tipo = cfg['tipo']
    if tipo == 'lead-formulario':
        return _entrada_lead(cfg, corpo)
    if tipo == 'venda-hotmart':
        return _entrada_venda(cfg, corpo)
    if tipo == 'batida':
        return _entrada_batida(cfg, corpo)
    raise Recusa('fluxo_sem_entrada', f'{cfg["nome"]}: o tipo {tipo} não recebe evento de fora')


def _entrada_lead(cfg, corpo):
    c = cfg['campos']
    if not isinstance(corpo, dict):
        return {'ramo': 'invalido', 'chave': None, 'contato_h': None, 'passos': [], 'nota': 'corpo_nao_objeto'}
    email = email_ok(_caminho(corpo, c['email']) if isinstance(_caminho(corpo, c['email']), str) else '')
    nome_b = _caminho(corpo, c['nome']) if c.get('nome') else ''
    nome = nome_b.strip()[:120] if isinstance(nome_b, str) else ''
    fone = telefone_br(_caminho(corpo, c['telefone'])) if c.get('telefone') else None
    aceites = {norm(x) for x in cfg.get('valores_aceite', ACEITE_PADRAO)}
    ac = _caminho(corpo, c['consentimento_whatsapp']) if c.get('consentimento_whatsapp') else None
    if isinstance(ac, list):
        ac = ac[0] if len(ac) == 1 else None
    consentiu = isinstance(ac, (str, bool, int)) and norm(str(ac)) in aceites
    ch = contato_h(email, fone)
    if not email and not fone:
        return {'ramo': 'invalido', 'chave': None, 'contato_h': None, 'passos': [], 'nota': 'sem_email_nem_telefone'}
    janela = int(cfg.get('dedupe_h', 24)) or 24
    valores = {'primeiro_nome': _primeiro_nome(nome), 'nome': nome, 'link': (cfg.get('whatsapp') or {}).get('link', '')}
    return {'ramo': 'ok', 'chave_base': f'lead:{ch}', 'janela_h': janela, 'contato_h': ch,
            'email': email, 'fone': fone,
            'passos': passos_saida(cfg, email, fone, nome, consentiu, valores, 'lead-formulario'), 'nota': None}


def _d(x, *ks):
    for k in ks:
        if not isinstance(x, dict):
            return None
        x = x.get(k)
    return x


def _entrada_venda(cfg, corpo):
    if not isinstance(corpo, dict):
        return {'ramo': 'sem_regra', 'chave': None, 'contato_h': None, 'passos': [], 'nota': 'corpo_nao_objeto'}
    ev, versao, eid = corpo.get('event'), corpo.get('version'), corpo.get('id')
    eid = eid if isinstance(eid, str) and re.fullmatch(r'[A-Za-z0-9-]{1,80}', eid) else None
    ev = ev if isinstance(ev, str) and re.fullmatch(r'[A-Z][A-Z0-9_]{2,60}', ev) else None
    if versao != '2.0.0':
        return {'ramo': 'sem_regra', 'chave': f'ev:{eid}' if eid else None, 'contato_h': None, 'passos': [],
                'nota': 'versao_do_webhook_nao_e_2.0.0'}
    if ev != 'PURCHASE_APPROVED':
        return {'ramo': f'ignorado:{ev or "sem_nome"}', 'chave': f'ev:{eid}' if eid else None, 'contato_h': None,
                'passos': [], 'nota': None}
    trans = _d(corpo, 'data', 'purchase', 'transaction')
    if not (isinstance(trans, str) and re.fullmatch(r'[A-Z]{1,4}[0-9A-Z]{4,40}', trans)):
        return {'ramo': 'sem_regra', 'chave': f'ev:{eid}' if eid else None, 'contato_h': None, 'passos': [],
                'nota': 'compra_sem_transacao'}
    pid = _d(corpo, 'data', 'product', 'id')
    pid = str(pid) if isinstance(pid, int) or (isinstance(pid, str) and pid.isdigit()) else None
    buyer = _d(corpo, 'data', 'buyer') or {}
    email = email_ok(buyer.get('email') if isinstance(buyer.get('email'), str) else '')
    nome = buyer.get('name').strip()[:120] if isinstance(buyer.get('name'), str) else ''
    pais = (_d(corpo, 'data', 'purchase', 'checkout_country', 'iso') or _d(buyer, 'address', 'country_iso') or 'BR')
    cod, num = buyer.get('checkout_phone_code'), buyer.get('checkout_phone')
    fone = None
    if isinstance(num, str) and num.strip():
        n = re.sub(r'[^0-9]', '', num)
        cd = re.sub(r'[^0-9]', '', cod) if isinstance(cod, str) else ''
        fone = telefone_br((cd + n) if (cd and len(n) in (8, 9)) else n, 'BR' if pais == 'BR' else pais)
    ch = contato_h(email, fone)
    base = {'chave': f'hm:{trans}', 'contato_h': ch, 'email': email, 'fone': fone}
    if pid in cfg.get('produtos_ignorados', []):
        return dict(base, ramo='ignorado_produto', passos=[], nota=None)
    regra = cfg['produtos'].get(pid or '')
    if not regra:
        return dict(base, ramo='sem_regra', passos=[], nota='produto_sem_regra')
    prod = _d(corpo, 'data', 'product', 'name')
    valores = {'primeiro_nome': _primeiro_nome(nome), 'nome': nome,
               'produto': prod.strip()[:120] if isinstance(prod, str) else '',
               'link': (regra.get('whatsapp') or {}).get('link', '')}
    return dict(base, ramo=f'produto:{pid}', nota=None,
                passos=passos_saida(regra, email, fone, nome, True, valores, 'venda-hotmart'))


def _entrada_batida(cfg, corpo):
    corpo = corpo if isinstance(corpo, dict) else {}
    palavra = norm(corpo.get('palavra')) if isinstance(corpo.get('palavra'), str) else ''
    esperadas = {norm(p) for p in cfg.get('palavras', [])}
    if esperadas:
        ramo = f'palavra:{palavra}' if palavra in esperadas else 'palavra_fora_da_lista'
    else:
        ramo = f'palavra:{palavra}' if palavra else 'batida'
    contato = corpo.get('contato')
    ch = sha('b:' + str(contato), 12) if isinstance(contato, (str, int)) and str(contato) else None
    eid = corpo.get('id')
    chave = f'id:{sha(str(eid), 16)}' if isinstance(eid, (str, int)) and str(eid) else None
    return {'ramo': ramo, 'chave': chave, 'contato_h': ch, 'passos': [], 'nota': None}


# ------------------------------------------------------------------------------------------------ lembretes
def lembretes_devidos(cfg, agora, desde, tolerancia_s, destinos):
    """Lembretes cuja hora chegou e que ainda valem (até `tolerancia_s` de atraso), mais os PERDIDOS (passaram da
    tolerância sem sair). Só conta o que ficou devido depois de `desde` (quando o fluxo foi ligado), para não
    disparar o passado de uma vez. -> (devidos, perdidos), cada item com chave, texto e grupo."""
    devidos, perdidos = [], []
    for a in aulas_de(cfg):
        ini = a['_inicio']
        for lb in cfg['lembretes']:
            momento = int((ini - timedelta(minutes=lb['antes_min'])).timestamp())
            if momento < desde or momento > agora:
                continue
            valores = {'titulo': a['titulo'], 'link': a.get('link', ''), 'hora': ini.strftime('%H:%M'),
                       'data': ini.strftime('%d/%m'), 'dia_semana': DIAS[ini.weekday()]}
            texto = render(lb['texto'], valores)
            for g in destinos:
                item = {'chave': f'aula:{a["id"]}:{lb["antes_min"]}:{sha(g, 8)}', 'grupo': g, 'texto': texto,
                        'momento': momento}
                (perdidos if agora - momento > tolerancia_s else devidos).append(item)
    return devidos, perdidos


def proxima_aula(cfg, agora):
    futuras = [a['_inicio'] for a in aulas_de(cfg) if a['_inicio'].timestamp() > agora]
    return min(futuras).timestamp() if futuras else None


def agora_utc():
    return datetime.now(timezone.utc)
