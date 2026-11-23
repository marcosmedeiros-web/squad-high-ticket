"""Troca do servico de envio do Mautic (Resend, SendGrid, Amazon SES), com volta atras.

Porte generico do procedimento que a operacao de origem usou para trocar SendGrid por Resend:
- a chave sai do cofre 600 e vai para o `mailer_dsn` sem passar por argv, log ou terminal;
- backup do local.php antes, `php -l` no arquivo novo, releitura conferida por igualdade;
- `cache:clear` nos tres containers como www-data;
- `messenger:stop-workers` no worker e prova de que os consumidores subiram DEPOIS da troca. Sem isso o botao de
  teste da tela fica verde (ele envia pelo web, que rele a config) enquanto o worker, que entrega campanha e
  segmento, segue preso na configuracao velha e descarta mensagem em silencio (incidente medido na origem).
"""
import re
import time
import urllib.parse

from .docker_cfg import Docker
from .perfil import ler_cofre
from .saida import Recusa, info, motivo

PAT = re.compile(r"^(\s*'mailer_dsn'\s*=>\s*)'((?:[^'\\]|\\.)*)'(\s*,\s*)$", re.M)
PAT_FROM = re.compile(r"^\s*'mailer_from_email'\s*=>\s*'([^']*)'", re.M)

HOST_RESEND = 'smtp.resend.com'
HOST_SENDGRID = 'smtp.sendgrid.net'

ESP_INFO = {
    'resend': {'vars': ('RESEND_API_KEY',), 'host': 'smtp.resend.com'},
    'sendgrid': {'vars': ('SENDGRID_API_KEY',), 'host': 'smtp.sendgrid.net'},
    'ses': {'vars': ('SES_SMTP_USUARIO', 'SES_SMTP_SENHA'), 'host': None},
}


def php_unq(s):
    return re.sub(r"\\(['\\])", r'\1', s)


def php_q(s):
    return s.replace('\\', '\\\\').replace("'", "\\'")


def host_ses(regiao):
    if not re.fullmatch(r'[a-z]{2}-[a-z]+-\d', regiao or ''):
        raise Recusa('ses_regiao_invalida', rc=3, regiao=regiao)
    return f'email-smtp.{regiao}.amazonaws.com'


def montar_dsn(esp, cred, regiao=None):
    """Monta o DSN em memoria. Recusa formato de chave errado sem citar o valor."""
    q = lambda v: urllib.parse.quote(v, safe='')  # noqa: E731
    if esp == 'resend':
        k = cred['RESEND_API_KEY']
        if not k.startswith('re_') or len(k) < 20:
            raise Recusa('chave_fora_do_formato', rc=3, esp=esp, esperado='re_...')
        return f'smtp://resend:{q(k)}@{HOST_RESEND}:587'
    if esp == 'sendgrid':
        k = cred['SENDGRID_API_KEY']
        if not k.startswith('SG.') or len(k) < 30:
            raise Recusa('chave_fora_do_formato', rc=3, esp=esp, esperado='SG....')
        return f'smtp://apikey:{q(k)}@{HOST_SENDGRID}:587'
    if esp == 'ses':
        u, s = cred['SES_SMTP_USUARIO'], cred['SES_SMTP_SENHA']
        if not re.fullmatch(r'AKIA[A-Z0-9]{16}', u) or len(s) < 40:
            raise Recusa('chave_fora_do_formato', rc=3, esp=esp,
                         esperado='credencial_SMTP_do_SES_(nao_a_chave_IAM)')
        return f'smtp://{q(u)}:{q(s)}@{host_ses(regiao)}:587'
    raise Recusa('esp_desconhecido', rc=3, esp=esp)


def host_do_dsn(dsn):
    try:
        return urllib.parse.urlsplit(dsn).hostname or '-'
    except ValueError:
        return '-'


def esp_do_host(host):
    if host == 'smtp.resend.com':
        return 'resend'
    if host == 'smtp.sendgrid.net':
        return 'sendgrid'
    if re.fullmatch(r'email-smtp\.[a-z0-9-]+\.amazonaws\.com', host or ''):
        return 'ses'
    return 'outro'


def _achar_dsn(txt):
    ms = list(PAT.finditer(txt))
    if len(ms) != 1:
        raise Recusa('mailer_dsn_nao_unico', rc=2, achadas=len(ms))
    return ms[0]


def mostrar(perfil, dk=None):
    perfil.exigir('docker')
    dk = dk or Docker(perfil.docker_cmd())
    txt = dk.ler_local_php(perfil['EMK_CT_WEB']).decode()
    m = _achar_dsn(txt)
    host = host_do_dsn(php_unq(m.group(2)))
    f = PAT_FROM.search(txt)
    remetente_dom = (f.group(1).rsplit('@', 1)[-1] if f else '-')
    info(f'servico de envio atual: {esp_do_host(host)} (host {host})')
    info(f'dominio do remetente no Mautic: {remetente_dom}')
    return motivo('ok', 0, esp=esp_do_host(host), host=host)


def _reiniciar_consumidores(perfil, dk, quando, espera_max=90):
    web, worker, cron = perfil['EMK_CT_WEB'], perfil['EMK_CT_WORKER'], perfil['EMK_CT_CRON']
    for ct in (web, worker, cron):
        dk.console(ct, ['cache:clear'], motivo='cache_clear_falhou')
    dk.console(worker, ['messenger:stop-workers'], motivo='stop_workers_falhou')
    limite = time.time() + espera_max
    while True:
        linhas = dk.ps(worker)
        if linhas is not None:
            idade_troca = time.time() - quando
            consumidores = [e for e, a in linhas if 'messenger:consume' in a]
            novos = [e for e in consumidores if e < idade_troca]
            if consumidores and len(novos) == len(consumidores):
                return len(novos)
        if time.time() >= limite:
            raise Recusa('worker_nao_voltou_com_config_nova', rc=2, container=worker,
                         fazer='conferir_supervisord_do_worker')
        time.sleep(3)


def aplicar(perfil, esp=None, dk=None, espera_max=90):
    perfil.exigir('docker', 'envio')
    esp = esp or perfil['EMK_ESP']
    dk = dk or Docker(perfil.docker_cmd())
    web = perfil['EMK_CT_WEB']
    cred = ler_cofre(perfil['EMK_CHAVE_ARQUIVO'], ESP_INFO[esp]['vars'])
    dsn = montar_dsn(esp, cred, perfil.get('EMK_SES_REGIAO'))
    orig = dk.ler_local_php(web)
    txt = orig.decode()
    m = _achar_dsn(txt)
    antigo = php_unq(m.group(2))
    if antigo == dsn:
        return motivo('ja_aplicado', 0, esp=esp, host=host_do_dsn(dsn))
    f = PAT_FROM.search(txt)
    if f and f.group(1).rsplit('@', 1)[-1].lower() != perfil['EMK_DOMINIO_REMETENTE'].lower():
        info('AVISO: o remetente configurado no Mautic nao e do dominio verificado no perfil; o servico de envio '
             'pode recusar (no SES isso aparece como 554 Access denied).')
    bak = dk.backup_local_php(web, 'envio')
    novo = (txt[:m.start(2)] + php_q(dsn) + txt[m.end(2):]).encode()
    quando = dk.gravar_local_php(web, novo)
    relido = dk.ler_local_php(web).decode()
    m2 = _achar_dsn(relido)
    if php_unq(m2.group(2)) != dsn or relido[:m2.start(2)] != txt[:m.start(2)] or relido[m2.end(2):] != txt[m.end(2):]:
        raise Recusa('releitura_difere_do_montado', rc=1, backup=bak, fazer='email-mkt envio reverter')
    info(f'backup: {bak} (600, dentro do volume de config)')
    info(f'host antigo: {host_do_dsn(antigo)} -> host novo: {host_do_dsn(dsn)}; resto do arquivo identico')
    n = _reiniciar_consumidores(perfil, dk, quando, espera_max)
    info(f'consumidores do worker que subiram depois da troca: {n}')
    info('falta a prova de fora: email-mkt envio teste --email-id <id> e depois --eml <mensagem salva>')
    return motivo('aplicado', 0, esp=esp, host=host_do_dsn(dsn), consumidores_novos=n)


def recuar(perfil, dk=None, espera_max=90):
    """Resend recusou ou cortou a conta: troca para a PRIMEIRA reserva (EMK_ESP_RESERVA, padrao ses,sendgrid) que
    tem credencial no cofre. Nao decide sozinho: e comando que o agente roda com o OK do dono. Depois de recuar,
    atualize EMK_ESP no perfil (a regua de copy passa de guarda a aviso) e rode dns conferir e envio teste."""
    perfil.exigir('docker', 'envio')
    atual = perfil['EMK_ESP']
    ordem = [x.strip() for x in perfil['EMK_ESP_RESERVA'].split(',') if x.strip()]
    ruins = [x for x in ordem if x not in ESP_INFO]
    if ruins:
        raise Recusa('reserva_desconhecida', rc=3, esp=ruins[0])
    for esp in ordem:
        if esp == atual:
            continue
        try:
            ler_cofre(perfil['EMK_CHAVE_ARQUIVO'], ESP_INFO[esp]['vars'])
        except Recusa as r:
            info(f'reserva {esp}: sem credencial no cofre ({r.codigo}); pulando')
            continue
        info(f'recuando de {atual} para a reserva {esp}')
        rc = aplicar(perfil, esp, dk, espera_max)
        if rc == 0:
            info(f'agora: troque EMK_ESP={esp} no perfil, rode email-mkt dns conferir e email-mkt envio teste')
        return rc
    raise Recusa('sem_reserva_com_credencial', rc=1, ordem=','.join(ordem),
                 fazer='o_dono_cria_a_conta_e_grava_a_chave_no_cofre')


def reverter(perfil, dk=None, espera_max=90):
    perfil.exigir('docker')
    dk = dk or Docker(perfil.docker_cmd())
    web = perfil['EMK_CT_WEB']
    baks = dk.listar_backups(web, 'envio')
    if not baks:
        raise Recusa('sem_backup_de_envio', rc=1)
    dados = dk.ler_arquivo(web, baks[-1])
    if b'<?php' not in dados[:64]:
        raise Recusa('backup_formato_inesperado', rc=2, backup=baks[-1])
    dk.backup_local_php(web, 'antes-de-reverter')
    quando = dk.gravar_local_php(web, dados)
    if dk.ler_local_php(web) != dados:
        raise Recusa('releitura_difere_do_backup', rc=1)
    host = host_do_dsn(php_unq(_achar_dsn(dados.decode()).group(2)))
    n = _reiniciar_consumidores(perfil, dk, quando, espera_max)
    return motivo('revertido', 0, de=baks[-1], host=host, consumidores_novos=n)
