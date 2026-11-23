"""Vigias: o cron do Mautic e o disco. Porte do watchdog e do vigia de disco da operacao de origem.

VIGIA DO CRON. O entrypoint do container de cron da imagem oficial roda `cron -f | tail -f /tmp/stdout`. Quando o
`tail` morre, cada job (`segments:update`, `campaigns:update`, `campaigns:trigger`) trava escrevendo num FIFO sem
leitor e empilha; campanha para em silencio, web e worker seguem saudaveis (incidente de ~27 h na origem).
Assinaturas que reiniciam SO o container de cron:
  1. `tail -f /tmp/stdout` AUSENTE confirmado (pgrep rodou limpo, rc 1, sem saida e sem erro);
  2. 12 ou mais `bin/console` vivos e o mais antigo com mais de 900 s;
  3. UM `bin/console` (fora `messenger:consume`, que e daemon do worker) com mais de 1800 s: o laco que encheu o
     disco de binlog era um processo unico; a regua 2 nunca bateu naquela noite.
Cada medida tem TRES estados. Diagnostico que nao rodou (sudo recusou, docker fora, timeout) vira
DIAGNOSTICO_INDISPONIVEL: avisa e NUNCA reinicia (na origem, uma sonda recusada lida como "tail ausente" reiniciou o
cron sem ele estar doente).
Se depois de um reinicio o `tail` continua ausente, a imagem pode nao ter esse `tail`: a assinatura 1 se desliga
sozinha (avisa) para nao virar laco de reinicio a cada rodada.

VIGIA DE DISCO. Uso de / acima do alerta ou do urgente, crescimento acima do limite em 30 min, e binlog do MySQL
religado. Estado em memoria compartilhada quando existe (/dev/shm), porque com disco cheio nada grava.

Nenhum dos dois manda mensagem para ninguem: escreve no canal de aviso do perfil (arquivo local, ou um script do
dono via `comando:`). "Nao configurado" significa "nao manda".
"""
import fcntl
import hashlib
import json
import os
import subprocess
import time

from . import binlog
from .docker_cfg import Docker
from .saida import info, motivo

CONSOLE_LIMIT = 12
AGE_LIMIT_S = 900
LONGO_LIMIT_S = 1800
ESPERA_POS_RESTART = 15


def aviso(perfil, origem, texto):
    canal = perfil.get('EMK_AVISO_CANAL') or 'arquivo'
    linha = {'quando': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'origem': origem, 'texto': texto}
    if canal.startswith('comando:'):
        try:
            r = subprocess.run([canal.split(':', 1)[1]], input=json.dumps(linha).encode(), timeout=30,
                               capture_output=True)
            if r.returncode == 0:
                return True
        except (OSError, subprocess.TimeoutExpired):
            pass
    p = os.path.join(perfil.estado_dir(), 'avisos.jsonl')
    try:
        with open(p, 'a', encoding='utf-8') as f:
            f.write(json.dumps(linha, ensure_ascii=False) + '\n')
        os.chmod(p, 0o600)
        return canal == 'arquivo'
    except OSError:
        return False


def _log(perfil, nome, texto):
    p = os.path.join(perfil.estado_dir(), f'{nome}.log')
    try:
        with open(p, 'a', encoding='utf-8') as f:
            f.write(time.strftime('%Y-%m-%dT%H:%M:%SZ ', time.gmtime()) + texto + '\n')
        with open(p, encoding='utf-8') as f:
            linhas = f.readlines()
        if len(linhas) > 2000:
            with open(p + '.tmp', 'w', encoding='utf-8') as f:
                f.writelines(linhas[-2000:])
            os.replace(p + '.tmp', p)
    except OSError:
        pass


def _estado(perfil, nome):
    p = os.path.join(perfil.estado_dir(), f'{nome}.json')
    try:
        with open(p, encoding='utf-8') as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _gravar_estado(perfil, nome, d):
    p = os.path.join(perfil.estado_dir(), f'{nome}.json')
    with open(p + '.tmp', 'w', encoding='utf-8') as f:
        json.dump(d, f)
    os.replace(p + '.tmp', p)


def coletar_cron(dk, ct):
    m = {}
    rc, out, err = dk.exec(ct, ['pgrep', '-f', 'tail -f /tmp/stdout'], user=None, timeout=20)
    if rc == 0 and out.strip() and not err.strip():
        m['tail'] = 'presente'
    elif rc == 1 and not out.strip() and not err.strip():
        m['tail'] = 'ausente'
    else:
        m['tail'] = 'indisponivel'
    linhas = dk.ps(ct)
    if linhas is None:
        m['ps'] = 'indisponivel'
        m['console'] = m['mais_velho'] = m['mais_longo'] = -1
    else:
        cons = [(e, a) for e, a in linhas if 'bin/console' in a]
        m['ps'] = 'ok'
        m['console'] = len(cons)
        m['mais_velho'] = max([e for e, _ in cons], default=0)
        m['mais_longo'] = max([e for e, a in cons if 'messenger:consume' not in a], default=0)
    return m


def vigia_cron(perfil, dk=None, espera=ESPERA_POS_RESTART):
    perfil.exigir('docker')
    dk = dk or Docker(perfil.docker_cmd(), timeout=30)
    ct = perfil['EMK_CT_CRON']
    with open(os.path.join(perfil.estado_dir(), 'vigia-cron.lock'), 'w') as trava:
        try:
            fcntl.flock(trava, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            return motivo('outra_rodada_em_curso', 0)
        return _vigia_cron_rodada(perfil, dk, ct, espera)


def _vigia_cron_rodada(perfil, dk, ct, espera):
    est = _estado(perfil, 'vigia-cron')
    m = coletar_cron(dk, ct)
    antes = f"tail={m['tail']} console={m['console']} mais_velho={m['mais_velho']}s mais_longo={m['mais_longo']}s"
    motivos, indisp = [], []
    if m['tail'] == 'ausente' and not est.get('tail_desligado'):
        motivos.append('tail ausente')
    elif m['tail'] == 'indisponivel':
        indisp.append('tail')
    if m['ps'] == 'indisponivel':
        indisp.append('ps')
    else:
        if m['console'] >= CONSOLE_LIMIT and m['mais_velho'] > AGE_LIMIT_S:
            motivos.append(f"{m['console']} bin/console empilhados, mais velho {m['mais_velho']}s")
        if m['mais_longo'] > LONGO_LIMIT_S:
            motivos.append(f"bin/console unico ha {m['mais_longo']}s (laco tipo campaigns:trigger)")
    if motivos:
        rc, _, _ = dk.run(['restart', ct], timeout=60)
        time.sleep(espera)
        d = coletar_cron(dk, ct)
        if rc == 0 and d['tail'] == 'presente':
            res = 'RECUPERADO'
        elif rc != 0:
            res = f'RESTART_FALHOU rc={rc}'
        else:
            res = 'RESTART_OK_TAIL_AUSENTE'
            if motivos == ['tail ausente']:
                est['tail_desligado'] = True
                _gravar_estado(perfil, 'vigia-cron', est)
                aviso(perfil, 'vigia-cron', 'assinatura do tail desligada: o tail nao voltou depois do reinicio '
                      '(imagem diferente?). As outras duas assinaturas seguem valendo.')
        texto = f"INCIDENTE motivo=\"{'; '.join(motivos)}\" antes[{antes}] restart_rc={rc} resultado={res}"
        _log(perfil, 'vigia-cron', texto)
        aviso(perfil, 'vigia-cron', f'cron do Mautic reiniciado: {"; ".join(motivos)}. Resultado: {res}.')
        return motivo('incidente_tratado', 0 if res == 'RECUPERADO' else 1, resultado=res)
    if indisp:
        _log(perfil, 'vigia-cron', f"DIAGNOSTICO_INDISPONIVEL falhas={','.join(indisp)} estado[{antes}]")
        aviso(perfil, 'vigia-cron', f"nao consegui medir o cron do Mautic ({', '.join(indisp)}); nada reiniciado.")
        return motivo('diagnostico_indisponivel', 2, falhas=','.join(indisp))
    _log(perfil, 'vigia-cron', f'ok {antes}')
    return motivo('ok', 0)


def _dir_disco_estado(perfil):
    if os.path.isdir('/dev/shm') and os.access('/dev/shm', os.W_OK):
        marca = hashlib.sha256(perfil.estado_dir().encode()).hexdigest()[:8]
        d = f'/dev/shm/email-marketing-{os.getuid()}-{marca}'
        os.makedirs(d, mode=0o700, exist_ok=True)
        return d
    return perfil.estado_dir()


def vigia_disco(perfil, dk=None, statvfs=os.statvfs, agora=None):
    perfil.exigir()
    agora = agora or time.time()
    alerta, urgente = perfil.int('EMK_DISCO_ALERTA_PCT'), perfil.int('EMK_DISCO_URGENTE_PCT')
    cresc_gb = float(perfil['EMK_DISCO_CRESCIMENTO_GB_30MIN'])
    try:
        s = statvfs('/')
    except OSError:
        return motivo('disco_nao_medido', 2)
    total = s.f_blocks * s.f_frsize
    livre = s.f_bavail * s.f_frsize
    usado = total - livre
    pct = 100.0 * usado / total if total else 0.0
    sdir = _dir_disco_estado(perfil)
    p = os.path.join(sdir, 'vigia-disco.json')
    try:
        with open(p, encoding='utf-8') as f:
            hist = json.load(f)
    except (OSError, ValueError):
        hist = {'pontos': [], 'episodio': None}
    hist['pontos'] = [x for x in hist.get('pontos', []) if agora - x[0] <= 1800] + [[agora, usado]]
    cresc = (usado - hist['pontos'][0][1]) / (1 << 30)
    problemas = []
    if pct >= urgente:
        problemas.append(f'URGENTE disco em {pct:.1f}%')
    elif pct >= alerta:
        problemas.append(f'disco em {pct:.1f}%')
    if cresc > cresc_gb:
        problemas.append(f'disco cresceu {cresc:.1f} GB em ate 30 min (binlog? laco do cron?)')
    lb = None
    if perfil.get('EMK_CT_DB'):
        lb = binlog.medir_logbin(dk or Docker(perfil.docker_cmd(), timeout=30), perfil['EMK_CT_DB'])
        if lb:
            problemas.append('binlog do MySQL LIGADO de novo (rode email-mkt binlog conferir)')
    episodio = '; '.join(problemas) or None
    if episodio and episodio != hist.get('episodio'):
        aviso(perfil, 'vigia-disco', episodio)
    elif not episodio and hist.get('episodio'):
        aviso(perfil, 'vigia-disco', f'disco normalizado: {pct:.1f}%')
    hist['episodio'] = episodio
    try:
        with open(p + '.tmp', 'w', encoding='utf-8') as f:
            json.dump(hist, f)
        os.replace(p + '.tmp', p)
    except OSError:
        pass
    info(f'disco / {pct:.1f}% usado, crescimento 30 min {cresc:.2f} GB, binlog '
         f"{'ligado' if lb else 'desligado' if lb is False else 'nao medido'}")
    if problemas:
        return motivo('disco_alerta', 1, itens=len(problemas))
    return motivo('ok', 0, pct=f'{pct:.1f}')
