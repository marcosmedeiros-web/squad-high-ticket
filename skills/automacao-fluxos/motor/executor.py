"""executor.py: o motor. Recebe evento, decide modo e passos, executa os passos com as travas e grava a prova.

MODOS DE UM FLUXO (no banco, nunca no desenho do dono)
  desligado   a rota responde 404 e nada é gravado (a tentativa conta como recusa)
  seco        o evento entra, o ramo é decidido e os passos ficam `seco`: nada sai para serviço nenhum
  teste       só os contatos de `teste` (e-mail ou telefone do dono) passam de verdade; o resto fica `retido_teste`.
              No lembrete, a mensagem vai para os grupos de teste no lugar dos grupos reais
  real        tudo passa, MAS só se o desenho é o mesmo que passou no teste e o dono ligou (`ligar --ok`).
              Desenho mudou depois do OK = os passos novos ficam `esperando_ok` (não somem) e o vigia avisa

LIGAR exige PROVA DE TRÂNSITO: um evento de teste que atravessou o fluxo INTEIRO (cada passo `feito`, conferido na
ponta pela releitura) com o mesmo desenho, nos últimos 7 dias. Fiação certa sem trânsito não liga nada.
"""
import json
import os
import re
import time
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

import banco as bco
import canais
import modelos
from base import Recusa, ler_segredo, nome_rota, sha

PROVA_VALIDA_S = 7 * 86400
MAX_TENTATIVAS = 6
_PARAR = re.compile(r'(^|\b)(parar|pare|para de|sair|stop|descadastr\w*|cancelar|nao quero (mais )?receber|'
                    r'me tira|tira meu|remover|remova)(\b|$)')


def pediu_parar(texto):
    return bool(_PARAR.search(modelos.norm(texto)))


class Motor:
    def __init__(self, perfil, relogio=None, dormir=None, clientes=None, monotonic=None):
        self.perfil = perfil
        self.monotonic = monotonic or time.monotonic
        self.dados = Path(perfil['af_dados_dir'])
        self._banco = None
        self.relogio = relogio or (lambda: int(time.time()))
        self.dormir = dormir or time.sleep
        self._clientes = clientes or {}
        self._cache = {}

    @property
    def banco(self):
        """Aberto só quando precisa: o `conferir` (e o `--so-conferir` do instalador) nunca cria nada."""
        if self._banco is None:
            self._banco = bco.Banco(self.dados)
        return self._banco

    def modo_sem_escrever(self, nome):
        """O modo, lido sem criar nem tocar em arquivo (SQLite imutável, só leitura)."""
        import sqlite3
        p = self.dados / 'fluxos.sqlite3'
        if not p.exists():
            return 'desligado (banco ainda não existe)'
        c = sqlite3.connect(f'file:{p}?mode=ro&immutable=1', uri=True)
        try:
            r = c.execute('SELECT valor FROM estado WHERE chave=?', (f'modo:{nome}',)).fetchone()
            return r[0] if r else 'desligado'
        finally:
            c.close()

    # ------------------------------------------------------------------------------------------ desenhos
    def fluxos(self):
        """Os desenhos do dono (AF_FLUXOS_DIR/*.json), conferidos. Arquivo torto = Recusa com o nome dele."""
        d = Path(self.perfil['af_fluxos_dir'])
        if not d.is_dir():
            return {}
        out = {}
        for p in sorted(d.glob('*.json')):
            m = p.stat().st_mtime_ns
            if self._cache.get(p.name, (None,))[0] != m:
                try:
                    cfg = json.loads(p.read_text(encoding='utf-8'))
                except ValueError:
                    raise Recusa('fluxo_json_invalido', p.name) from None
                modelos.conferir(cfg, p.stem)
                self._cache[p.name] = (m, cfg)
            cfg = self._cache[p.name][1]
            out[cfg['nome']] = cfg
        return out

    def fluxo(self, nome):
        f = self.fluxos().get(nome)
        if not f:
            raise Recusa('fluxo_inexistente', nome, rc=2)
        return f

    def cliente(self, qual):
        if qual not in self._clientes:
            self._clientes[qual] = (canais.Mautic if qual == 'mautic' else canais.OpenWA).do_perfil(self.perfil)
        return self._clientes[qual]

    def parado(self):
        return (self.dados / 'PARAR').exists()

    # ------------------------------------------------------------------------------------------ modos
    def modo(self, nome):
        return self.banco.modo(nome)

    def mudar_modo(self, nome, modo):
        if modo not in ('desligado', 'seco', 'teste'):
            raise Recusa('modo_invalido', 'use desligado, seco ou teste; real só com `ligar --ok`')
        self.fluxo(nome)
        agora = self.relogio()
        self.banco.set(f'modo:{nome}', modo)
        self.banco.set(f'armado:{nome}', None)
        self.banco.set(f'ativo_desde:{nome}', agora)
        return modo

    def ligar(self, nome):
        cfg = self.fluxo(nome)
        agora = self.relogio()
        if self.modo(nome) != 'teste':
            raise Recusa('ligar_sem_teste', f'{nome} está em {self.modo(nome)}: passe por `modo {nome} teste` e '
                         'pela prova de trânsito antes', rc=3)
        des = modelos.desenho(cfg)
        pv = self.banco.prova(nome, des, agora - PROVA_VALIDA_S)
        if not pv:
            raise Recusa('sem_prova_de_transito', f'{nome}: nenhum evento de teste atravessou o desenho atual '
                         f'({des[:8]}) inteiro nos últimos 7 dias. Faça o teste (SKILL.md, passo 5)', rc=3)
        if cfg['tipo'] == 'venda-hotmart':
            r = self.banco.c.execute("SELECT count(*) n FROM eventos WHERE fluxo=? AND recebido>=? "
                                     "AND coalesce(nota, '') != 'simulado'", (nome, agora - PROVA_VALIDA_S)).fetchone()
            if not r['n']:
                raise Recusa('sem_evento_da_hotmart', f'{nome}: a simulação passou, mas nenhum evento veio da '
                             'Hotmart. Use o "teste de envio" do painel do webhook', rc=3)
        self.banco.set(f'modo:{nome}', 'real')
        self.banco.set(f'armado:{nome}', des)
        self.banco.set(f'ativo_desde:{nome}', agora)
        return des

    def armado_ok(self, cfg):
        return self.banco.get(f'armado:{cfg["nome"]}') == modelos.desenho(cfg)

    # ------------------------------------------------------------------------------------------ rotas
    def token_rota(self, nome):
        p = self.dados / 'rotas.env'
        try:
            return ler_segredo(p, [nome_rota(nome)])[nome_rota(nome)]
        except Recusa:
            return None

    def gerar_rota(self, nome):
        """Cria (uma vez) o caminho secreto da rota e grava a URL completa num arquivo 600 para o DONO abrir no
        terminal dele. Nada é impresso com o segredo."""
        import secrets
        cfg = self.fluxo(nome)
        self.banco                      # cria a pasta de dados (700) se ainda não existe
        p = self.dados / 'rotas.env'
        if cfg['tipo'] == 'venda-hotmart':
            url = f'{self.perfil["url_publica"]}/f/{nome}'
        elif cfg['tipo'] == 'lembrete-aula':
            raise Recusa('fluxo_sem_rota', f'{nome}: o lembrete não recebe evento de fora')
        else:
            tok = self.token_rota(nome)
            if not tok:
                tok = secrets.token_urlsafe(24)
                fd = os.open(p, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o600)
                with os.fdopen(fd, 'a') as f:
                    f.write(f'{nome_rota(nome)}={tok}\n')
                os.chmod(p, 0o600)
            url = f'{self.perfil["url_publica"]}/f/{nome}/{tok}'
        saida = self.dados / f'url-{nome}.txt'
        fd = os.open(saida, os.O_WRONLY | os.O_TRUNC | os.O_CREAT, 0o600)
        with os.fdopen(fd, 'w') as f:
            f.write(url + '\n')
        return saida

    # ------------------------------------------------------------------------------------------ entrada
    def receber(self, nome, corpo, simulado=False):
        """O evento passou na autenticação da rota. -> (evento_id, novo, ramo). Grava antes de responder."""
        cfg = self.fluxo(nome)
        agora = self.relogio()
        modo = self.modo(nome)
        if modo == 'desligado':
            raise Recusa('fluxo_desligado', f'{nome}: use `modo {nome} seco` ou `teste` primeiro', rc=3)
        res = modelos.entrada(cfg, corpo)
        ramo, passos = res['ramo'], res['passos']
        chave = res.get('chave')
        if res.get('chave_base'):
            # o modo entra na chave: o envio de teste do dono depois do seco não pode ser engolido como repetido
            chave = f'{res["chave_base"]}:{modo}:{agora // (res["janela_h"] * 3600)}'
        if not chave:
            chave = 'r:' + uuid.uuid4().hex
        if simulado:
            chave = 'sim:' + chave
        if modo == 'teste' and passos and not modelos.no_teste(cfg, res.get('email'), res.get('fone')):
            ramo, passos = 'retido_teste', []
        passos = self._aplicar_modo(cfg, modo, passos)
        eid, novo = self.banco.gravar_evento(nome, agora, ramo, chave, res.get('contato_h'), modo,
                                            modelos.desenho(cfg), passos, 'simulado' if simulado else res.get('nota'))
        if novo and modo == 'teste' and cfg['tipo'] == 'batida' and not simulado:
            self.banco.gravar_prova(nome, modelos.desenho(cfg), eid, agora)
        return eid, novo, ramo

    def _aplicar_modo(self, cfg, modo, passos):
        for p in passos:
            if p['estado'] != 'pendente':
                continue
            if modo == 'seco':
                p['estado'], p['motivo'] = 'seco', 'modo_seco'
            elif modo == 'real' and not self.armado_ok(cfg):
                p['estado'], p['motivo'] = 'esperando_ok', 'desenho_mudou_depois_do_ok'
        return passos

    # ------------------------------------------------------------------------------------------ ciclo
    def ciclo(self):
        """O que o timer roda a cada minuto: lembretes devidos, passos devidos, provas, retenção.
        Um ciclo por vez (trava em arquivo): o timer e um `esperar --rodar-ciclo` nunca executam o mesmo passo juntos."""
        import fcntl
        self.banco
        fd = os.open(self.dados / 'ciclo.trava', os.O_WRONLY | os.O_CREAT, 0o600)
        try:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError:
                return {'ocupado': True, 'lembretes': 0, 'perdidos': 0, 'passos': 0, 'parado': self.parado()}
            return self._ciclo()
        finally:
            os.close(fd)

    def _ciclo(self):
        agora = self.relogio()
        resumo = {'lembretes': 0, 'perdidos': 0, 'passos': 0, 'parado': self.parado()}
        fluxos = self.fluxos()
        for nome, cfg in fluxos.items():
            if cfg['tipo'] == 'lembrete-aula' and self.modo(nome) in ('seco', 'teste', 'real'):
                n, p = self._agendar_lembretes(cfg, agora)
                resumo['lembretes'] += n
                resumo['perdidos'] += p
        if not resumo['parado']:
            for row in self.banco.devidos(agora):
                cfg = fluxos.get(row['fluxo'])
                if not cfg:
                    continue
                self._executar(cfg, row)
                resumo['passos'] += 1
        self._provas(agora)
        self.banco.purgar(agora, self.perfil['retencao_dias'])
        return resumo

    def _agendar_lembretes(self, cfg, agora):
        nome, modo = cfg['nome'], self.modo(cfg['nome'])
        desde = int(self.banco.get(f'ativo_desde:{nome}', agora))
        destinos = cfg.get('teste', {}).get('grupos', []) if modo == 'teste' else cfg['grupos']
        tol = int(cfg.get('vigia', {}).get('tolerancia_min', 20)) * 60
        devidos, perdidos = modelos.lembretes_devidos(cfg, agora, desde, tol, destinos)
        n = 0
        for it in devidos:
            passos = self._aplicar_modo(cfg, modo, [{'ordem': 1, 'tipo': 'whatsapp_grupo', 'estado': 'pendente',
                                                    'dados': {'grupo': it['grupo'], 'texto': it['texto'],
                                                              'sha': sha(it['texto'], 12), 'momento': it['momento'],
                                                              'tolerancia_s': tol}}])
            _, novo = self.banco.gravar_evento(nome, agora, 'lembrete', it['chave'], None, modo, modelos.desenho(cfg),
                                               passos)
            n += novo
        p = 0
        for it in perdidos:
            _, novo = self.banco.gravar_evento(nome, agora, 'perdido', it['chave'], None, modo, modelos.desenho(cfg), [])
            p += novo
        return n, p

    def lembrete_teste(self, nome):
        """Manda AGORA, para os grupos de teste, o primeiro lembrete da próxima aula. Só em modo teste."""
        cfg = self.fluxo(nome)
        if cfg['tipo'] != 'lembrete-aula' or self.modo(nome) != 'teste':
            raise Recusa('lembrete_teste_fora_do_teste', f'{nome}: precisa ser lembrete-aula em modo teste', rc=3)
        agora = self.relogio()
        aulas = [a for a in modelos.aulas_de(cfg) if a['_inicio'].timestamp() > agora]
        grupos = cfg.get('teste', {}).get('grupos', [])
        if not aulas or not grupos:
            raise Recusa('lembrete_teste_sem_aula_ou_grupo', 'cadastre uma aula futura e teste.grupos', rc=3)
        a = min(aulas, key=lambda x: x['_inicio'])
        lb = cfg['lembretes'][0]
        ini = a['_inicio']
        texto = modelos.render(lb['texto'], {'titulo': a['titulo'], 'link': a.get('link', ''),
                                             'hora': ini.strftime('%H:%M'), 'data': ini.strftime('%d/%m'),
                                             'dia_semana': modelos.DIAS[ini.weekday()]})
        eids = []
        for g in grupos:
            eid, _ = self.banco.gravar_evento(nome, agora, 'lembrete', f'teste:{agora}:{sha(g, 8)}', None, 'teste',
                                              modelos.desenho(cfg), [{'ordem': 1, 'tipo': 'whatsapp_grupo',
                                                                      'estado': 'pendente',
                                                                      'dados': {'grupo': g, 'texto': texto,
                                                                                'sha': sha(texto, 12), 'momento': agora,
                                                                                'tolerancia_s': 3600}}])
            eids.append(eid)
        return eids

    def _provas(self, agora):
        """Evento de teste cujos passos terminaram TODOS `feito` (pelo menos um) vira prova do desenho dele."""
        rows = self.banco.c.execute(
            "SELECT e.id, e.fluxo, e.desenho, e.nota FROM eventos e WHERE e.modo='teste' AND e.recebido>=? "
            "AND NOT EXISTS (SELECT 1 FROM provas p WHERE p.evento_id=e.id) "
            "AND EXISTS (SELECT 1 FROM passos x WHERE x.evento_id=e.id) "
            "AND NOT EXISTS (SELECT 1 FROM passos x WHERE x.evento_id=e.id AND x.estado!='feito')",
            (agora - PROVA_VALIDA_S,)).fetchall()
        fl = self.fluxos()
        for r in rows:
            cfg = fl.get(r['fluxo'])
            if not cfg or r['desenho'] != modelos.desenho(cfg):
                continue
            if cfg['tipo'] == 'lead-formulario' and r['nota'] == 'simulado':
                continue   # a prova do formulário tem que vir do formulário de verdade
            self.banco.gravar_prova(r['fluxo'], r['desenho'], r['id'], agora)

    # ------------------------------------------------------------------------------------------ passos
    def _executar(self, cfg, row):
        agora = self.relogio()
        pid = row['id']
        dados = json.loads(row['dados'] or '{}')
        if row['estado'] == 'esperando_ok':
            if self.modo(cfg['nome']) == 'real' and self.armado_ok(cfg):
                self.banco.atualizar_passo(pid, agora, estado='pendente', motivo=None)
                row = self.banco.passo(pid)
            else:
                if agora - row['criado'] > int(cfg.get('vigia', {}).get('validade_h', 48)) * 3600:
                    self.banco.atualizar_passo(pid, agora, estado='expirado', motivo='esperou_ok_demais')
                return
        if row['tipo'] == 'whatsapp_grupo' and not row['post_feito'] and \
                agora - dados.get('momento', agora) > dados.get('tolerancia_s', 1200):
            self.banco.atualizar_passo(pid, agora, estado='expirado', motivo='lembrete_passou_da_hora')
            return
        if not row['post_feito'] and agora - row['criado'] > int(cfg.get('vigia', {}).get('validade_h', 48)) * 3600:
            self.banco.atualizar_passo(pid, agora, estado='expirado', motivo='velho_demais')
            return
        if row['depende']:
            dep = [p for p in self.banco.passos_do_evento(row['evento_id']) if p['ordem'] == row['depende']]
            if not dep or dep[0]['estado'] in bco.TERMINAIS and dep[0]['estado'] != 'feito':
                self.banco.atualizar_passo(pid, agora, estado='pulado',
                                           motivo=f'dependencia_{dep[0]["estado"] if dep else "ausente"}')
                return
            if dep[0]['estado'] != 'feito':
                return
            dados['_dep'] = json.loads(dep[0]['saida'] or '{}')
        fn = {'mautic_contato': self._mautic_contato, 'mautic_email': self._mautic_email,
              'whatsapp_individual': self._wa_individual, 'whatsapp_grupo': self._wa_grupo}[row['tipo']]
        try:
            estado, motivo, saida = fn(cfg, row, dados, agora)
        except canais.ServicoErro as e:
            atual = self.banco.passo(pid)          # o POST pode ter acontecido DURANTE esta execução
            t = atual['tentativas'] + 1
            if atual['post_feito']:
                # pode ter saído: nunca reenviar; a próxima rodada só RELÊ a ponta para confirmar
                if t >= MAX_TENTATIVAS:
                    estado, motivo, saida = 'incerto', f'{e.motivo}_sem_confirmar', None
                else:
                    self.banco.atualizar_passo(pid, agora, tentativas=t, motivo=f'confirmar:{e.motivo}',
                                               proxima_em=agora + 60)
                    return
            elif not e.transitorio:
                estado, motivo, saida = 'falhou', e.motivo, None
            elif t >= MAX_TENTATIVAS:
                estado, motivo, saida = 'falhou', f'{e.motivo}_depois_de_{t}', None
            else:
                self.banco.atualizar_passo(pid, agora, tentativas=t, motivo=e.motivo,
                                           proxima_em=agora + min(60 * 2 ** t, 3600))
                return
        except Recusa as e:
            estado, motivo, saida = 'falhou', e.motivo, None
        campos = {'estado': estado, 'motivo': motivo}
        if estado == 'esperando':
            campos['proxima_em'] = (saida or {}).get('_proxima_em') or agora + 600
        elif saida is not None:
            campos['saida'] = saida
        self.banco.atualizar_passo(pid, agora, **campos)

    def _mautic_contato(self, cfg, row, d, agora):
        m = self.cliente('mautic')
        cid = m.contato(d['email'], d.get('nome'), d.get('telefone'), d.get('tags', []))
        m.por_no_segmento(d['segmento_id'], cid)
        if int(d['segmento_id']) not in m.segmentos_do_contato(cid):
            return 'falhou', 'segmento_nao_confirmado_na_releitura', {'contato_id': cid}
        return 'feito', None, {'contato_id': cid}

    def _mautic_email(self, cfg, row, d, agora):
        m = self.cliente('mautic')
        cid = d['_dep'].get('contato_id')
        if not isinstance(cid, int):
            return 'falhou', 'sem_contato_id', {}
        if row['post_feito']:
            ok = m.email_registrado(d['email_id'], cid)
            return ('feito', None, {}) if ok else ('incerto', 'envio_sem_registro', {})
        self.banco.marcar_post(row['id'], agora)
        m.enviar_email(d['email_id'], cid)
        if m.email_registrado(d['email_id'], cid):
            return 'feito', None, {'contato_id': cid}
        return 'incerto', 'envio_sem_registro_na_releitura', {'contato_id': cid}

    def _janela(self, agora):
        """(dentro, próximo início) no fuso do perfil."""
        tz = timezone(timedelta(hours=self.perfil['fuso_utc']))
        dt = datetime.fromtimestamp(agora, tz)
        ini, fim = self.perfil['janela_inicio'], self.perfil['janela_fim']
        if ini <= dt.hour < fim:
            return True, None
        prox = dt.replace(hour=ini, minute=0, second=0, microsecond=0)
        if dt.hour >= fim:
            prox += timedelta(days=1)
        return False, int(prox.timestamp())

    def _inicio_do_dia(self, agora):
        tz = timezone(timedelta(hours=self.perfil['fuso_utc']))
        dt = datetime.fromtimestamp(agora, tz)
        return int(dt.replace(hour=0, minute=0, second=0, microsecond=0).timestamp()), dt.strftime('%Y-%m-%d')

    def _wa_individual(self, cfg, row, d, agora):
        wa = self.cliente('openwa')
        saida = json.loads(row['saida'] or '{}')
        if row['post_feito']:
            return self._confirmar(wa, saida.get('lid'), set(saida.get('antes', [])), d['sha'], saida)
        dentro, prox = self._janela(agora)
        if not dentro:
            return 'esperando', 'janela_fora_do_horario', {'_proxima_em': prox}
        dia0, dia = self._inicio_do_dia(agora)
        if self.banco.contar_wa(dia0) >= self.perfil['teto_whatsapp_dia']:
            self.banco.set(f'teto:{dia}', agora)
            return 'esperando', 'janela_teto_do_dia', {'_proxima_em': dia0 + 86400 + 60}
        wa.sessao_pronta()
        lids = set()
        for n in modelos.variantes_br(d['telefone']):
            lid = wa.lid(n)
            if lid:
                lids.add(lid)
        if not lids:
            return 'pulado', 'numero_sem_whatsapp', {}
        if len(lids) > 1:
            return 'falhou', 'duas_contas_para_o_mesmo_numero', {}
        lid = lids.pop()
        if not canais.RE_LID.match(lid):
            return 'falhou', 'whatsapp_nao_devolveu_lid', {}
        ck = sha('wa:' + lid, 12)
        teste = self.banco.evento(row['evento_id'])['modo'] == 'teste'
        # o dono testa vários fluxos com o próprio número no mesmo dia: no modo teste a regra de 24 h não vale
        if not teste and self.banco.envio_wa_recente(ck, agora - 86400):
            return 'pulado', 'ja_recebeu_nas_ultimas_24h', {'chat_key': ck}
        conversa = wa.conversa(lid)
        if any(str(m.get('direction', '')).lower() == 'incoming' and pediu_parar(m.get('body') or '')
               for m in conversa):
            return 'pulado', 'pediu_para_parar', {'chat_key': ck}
        antes = sorted(str(m.get('id') or m.get('waMessageId') or '') for m in conversa)
        saida = {'lid': lid, 'chat_key': ck, 'antes': antes}
        self.banco.atualizar_passo(row['id'], agora, saida=saida)
        self.banco.marcar_post(row['id'], agora)
        self.banco.registrar_wa(ck, agora, cfg['nome'])
        st, _ = wa.enviar(lid, d['texto'])
        saida['post_http'] = st
        return self._confirmar(wa, lid, set(antes), d['sha'], saida)

    def _wa_grupo(self, cfg, row, d, agora):
        wa = self.cliente('openwa')
        saida = json.loads(row['saida'] or '{}')
        g = d['grupo']
        if row['post_feito']:
            return self._confirmar(wa, g, set(saida.get('antes', [])), d['sha'], saida)
        wa.sessao_pronta()
        if g not in wa.grupos():
            return 'falhou', 'grupo_fora_da_sessao', {}
        conversa = wa.conversa(g)
        antes = sorted(str(m.get('id') or m.get('waMessageId') or '') for m in conversa)
        saida = {'grupo_h': sha(g, 8), 'antes': antes}
        self.banco.atualizar_passo(row['id'], agora, saida=saida)
        self.banco.marcar_post(row['id'], agora)
        st, _ = wa.enviar(g, d['texto'])
        saida['post_http'] = st
        return self._confirmar(wa, g, set(antes), d['sha'], saida)

    def _confirmar(self, wa, chat, antes, sha12, saida):
        """RELÊ a conversa até achar EXATAMENTE uma saída nova com o mesmo texto. HTTP 201 não conta."""
        saida = {k: v for k, v in saida.items() if k not in ('lid', 'antes')}
        fim = self.monotonic() + self.perfil['confirmar_s']
        passo = 2.0
        while True:
            try:
                conv = wa.conversa(chat)
            except canais.ServicoErro:
                conv = None
            if conv is not None:
                novas = [m for m in conv if str(m.get('direction', '')).lower() == 'outgoing'
                         and str(m.get('id') or m.get('waMessageId') or '') not in antes
                         and sha(m.get('body') or '', 12) == sha12]
                boas = [m for m in novas if m.get('waMessageId') and str(m.get('status', '')).lower() != 'failed']
                falhas = [m for m in novas if str(m.get('status', '')).lower() == 'failed']
                if len(boas) > 1:
                    return 'incerto', 'saiu_duplicada', saida
                if len(boas) == 1:
                    return 'feito', None, saida
                if falhas and not boas and len(falhas) == len(novas):
                    return 'falhou', 'o_whatsapp_recusou', saida
            if self.monotonic() >= fim:
                return 'incerto', 'nao_confirmado_na_releitura', saida
            self.dormir(passo)
            passo = min(passo * 1.6, 15.0)

    # ------------------------------------------------------------------------------------------ manutenção
    def refazer(self, pid):
        """Um passo `falhou` que NUNCA fez POST volta para a fila. `incerto` nunca: pode ter saído."""
        r = self.banco.passo(pid)
        if not r:
            raise Recusa('passo_inexistente', str(pid), rc=2)
        if r['estado'] != 'falhou' or r['post_feito']:
            raise Recusa('passo_nao_refazivel', f'{pid}: só `falhou` sem POST feito (estado {r["estado"]}, '
                         f'post {r["post_feito"]}). Incerto: confira na ponta e marque `visto`', rc=3)
        self.banco.atualizar_passo(pid, self.relogio(), estado='pendente', tentativas=0, proxima_em=0, motivo='refeito')

    def visto(self, nome):
        n = self.banco.c.execute("UPDATE passos SET visto=1 WHERE fluxo=? AND estado IN ('falhou', 'incerto', 'expirado') "
                                 'AND visto=0', (nome,)).rowcount
        self.banco.c.execute("UPDATE eventos SET nota='visto' WHERE fluxo=? AND ramo='perdido' "
                             "AND coalesce(nota, '')!='visto'", (nome,))
        return n
