"""segredo.py: lê UM segredo de um arquivo do dono, com a disciplina de sempre.

  * arquivo regular, não link, do mesmo usuário, permissão sem grupo nem outros (600 ou 400);
  * formato NOME=VALOR, sem crase nem $(;
  * mensagem de erro leva só o CAMINHO e o motivo, nunca o nome de outra chave, nunca o valor.

Os segredos deste pacote:
  HOTMART_HOTTOK      o hottok da aba de autenticação do Webhook da Hotmart  (HM_HOTTOK_ARQUIVO)
  META_CAPI_TOKEN     o token de acesso da API de Conversões, gerado no Gerenciador de Eventos (CAPI_TOKEN_ARQUIVO)
  HOTMART_CLIENT_ID, HOTMART_CLIENT_SECRET, HOTMART_BASIC   credencial da API da Hotmart, só para o vigia
                                                            (HM_HOTMART_CRED_ARQUIVO, opcional)

Uso: segredo.py --conferir <arquivo> <NOME> [<NOME>...]   (rc 0 ok, rc 3 recusa; nunca imprime valor)
"""
import os
import sys
from pathlib import Path


class SegredoErro(RuntimeError):
    def __init__(self, motivo, caminho):
        super().__init__(f'{motivo}: {caminho}')
        self.motivo = motivo


def ler(caminho, nomes):
    p = Path(caminho)
    if p.is_symlink() or not p.is_file():
        raise SegredoErro('segredo_ausente', caminho)
    st = p.stat()
    if st.st_mode & 0o077:
        raise SegredoErro('permissao_segredo', f'{caminho} (exigido 600)')
    if hasattr(os, 'geteuid') and st.st_uid != os.geteuid():
        raise SegredoErro('dono_segredo', caminho)
    achados = {}
    for linha in p.read_text(encoding='utf-8', errors='replace').splitlines():
        s = linha.strip()
        if not s or s.startswith('#'):
            continue
        if '`' in s or '$(' in s or '=' not in s:
            raise SegredoErro('formato_segredo', caminho)
        k, v = s.split('=', 1)
        k = k.strip()
        if k in nomes:
            achados[k] = v.strip().strip('"').strip("'")
    if any(not achados.get(n) for n in nomes):
        raise SegredoErro('segredo_vazio', caminho)
    return achados


def main(argv):
    if len(argv) < 4 or argv[1] != '--conferir':
        print('uso: segredo.py --conferir <arquivo> <NOME>...', file=sys.stderr)
        return 2
    try:
        v = ler(argv[2], argv[3:])
    except SegredoErro as e:
        print(f'MOTIVO={e.motivo}', file=sys.stderr)
        print(f'segredo: {e}', file=sys.stderr)
        return 3
    print(f'segredo ok: {len(v)} valor(es) lido(s) de {argv[2]} (valores não exibidos)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
