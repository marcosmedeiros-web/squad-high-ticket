"""Acesso ao Mautic em container, sem root e sem caminho de volume do host.

Toda leitura e escrita do `local.php` passa por `docker exec -u www-data` no container web. O conteudo novo entra
por STDIN (`dd of=`), nunca por argv: segredo em argv aparece no `ps` de qualquer usuario e no log de auditoria.

Licoes da operacao de origem que este modulo carrega:
- `cache:clear` como root deixa var/cache com dono root e o site cai em 500: aqui tudo roda como www-data.
- O arquivo novo passa por `php -l` ANTES de substituir o antigo; reprovado, o antigo fica intocado.
- O backup fica DENTRO do volume de config, numa pasta 700, arquivo 600 (o local.php guarda segredo).
- O `local.php` novo sai com 640: o de origem estava 755 (legivel por qualquer usuario do host) com a chave dentro.
"""
import subprocess
import time

from .saida import Recusa

CFG = '/var/www/html/config/local.php'
CFG_TMP = '/var/www/html/config/.local.php.emk-tmp'
ARQUIVO = '/var/www/html/config/archive'
CONSOLE = ['php', '/var/www/html/bin/console']
EXECUTIONER = '/var/www/html/docroot/app/bundles/CampaignBundle/Executioner/ScheduledExecutioner.php'


class Docker:
    def __init__(self, cmd, timeout=60):
        self.cmd = list(cmd)
        self.timeout = timeout

    def run(self, args, stdin=None, timeout=None):
        """-> (rc, stdout, stderr). rc 125 = nao rodou (timeout ou binario ausente)."""
        try:
            r = subprocess.run(self.cmd + list(args), input=stdin, capture_output=True,
                               timeout=timeout or self.timeout)
        except (OSError, subprocess.TimeoutExpired) as e:
            return 125, b'', type(e).__name__.encode()
        return r.returncode, r.stdout, r.stderr

    def exec(self, ct, args, user='www-data', stdin=None, timeout=None):
        base = ['exec']
        if stdin is not None:
            base.append('-i')
        if user:
            base += ['-u', user]
        return self.run(base + [ct] + list(args), stdin=stdin, timeout=timeout)

    def exigir(self, ct, args, motivo, user='www-data', stdin=None, timeout=None):
        rc, out, err = self.exec(ct, args, user=user, stdin=stdin, timeout=timeout)
        if rc != 0:
            raise Recusa(motivo, rc=2, container=ct, rc_docker=rc)
        return out

    # ------------------------------------------------------------------ local.php
    def ler_local_php(self, web):
        out = self.exigir(web, ['cat', CFG], 'local_php_ilegivel')
        if b'<?php' not in out[:64]:
            raise Recusa('local_php_formato_inesperado', rc=2)
        return out

    def backup_local_php(self, web, rotulo):
        ts = time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())
        destino = f'{ARQUIVO}/local.php.bak-emk-{rotulo}-{ts}'
        self.exigir(web, ['mkdir', '-p', ARQUIVO], 'backup_falhou')
        self.exigir(web, ['chmod', '700', ARQUIVO], 'backup_falhou')
        self.exigir(web, ['cp', '-p', CFG, destino], 'backup_falhou')
        self.exigir(web, ['chmod', '600', destino], 'backup_falhou')
        return destino

    def listar_backups(self, web, rotulo):
        rc, out, _ = self.exec(web, ['ls', '-1', ARQUIVO])
        if rc != 0:
            return []
        nomes = [n for n in out.decode().split() if n.startswith(f'local.php.bak-emk-{rotulo}-')]
        return [f'{ARQUIVO}/{n}' for n in sorted(nomes)]

    def ler_arquivo(self, web, caminho):
        return self.exigir(web, ['cat', caminho], 'arquivo_ilegivel')

    def gravar_local_php(self, web, conteudo):
        """Grava por stdin num temporario, confere com php -l, e so entao troca. Devolve o epoch da troca."""
        self.exigir(web, ['dd', f'of={CFG_TMP}', 'status=none'], 'gravacao_falhou', stdin=conteudo)
        self.exigir(web, ['chmod', '640', CFG_TMP], 'gravacao_falhou')
        rc, _, _ = self.exec(web, ['php', '-l', CFG_TMP])
        if rc != 0:
            self.exec(web, ['rm', '-f', CFG_TMP])
            raise Recusa('php_l_reprovou', rc=1, original='intocado')
        lido = self.exigir(web, ['cat', CFG_TMP], 'gravacao_falhou')
        if lido != conteudo:
            self.exec(web, ['rm', '-f', CFG_TMP])
            raise Recusa('releitura_difere', rc=1, original='intocado')
        quando = time.time()
        self.exigir(web, ['mv', '-f', CFG_TMP, CFG], 'gravacao_falhou')
        return quando

    # ------------------------------------------------------------------ console
    def console(self, ct, args, motivo='console_falhou', timeout=300):
        return self.exigir(ct, CONSOLE + list(args) + ['--env=prod'], motivo, timeout=timeout)

    def ps(self, ct):
        """-> lista de (etimes, args) ou None se nao mediu."""
        rc, out, err = self.exec(ct, ['ps', '-eo', 'etimes=,args='], user=None)
        if rc != 0:
            return None
        linhas = []
        for linha in out.decode(errors='replace').splitlines():
            partes = linha.strip().split(None, 1)
            if len(partes) == 2 and partes[0].isdigit():
                linhas.append((int(partes[0]), partes[1]))
        return linhas
