LINHA = '-'*50


def menu():
    print(LINHA)
    print(f'{"MENU PRINCIPAL":^50}')
    print(LINHA)
    print('''\033[33m1\033[m - \033[36mVer pessoas cadastradas\033[m
\033[33m2\033[m - \033[36mCadastrar novas pessoas\033[m
\033[33m3\033[m - \033[36mSair do Programa\033[m''')
    print(LINHA)
    print('\033[33mSua opção: \033[m', end='')


def mensagem(msg):
    print(LINHA)
    print(f'{msg:^50}')
    print(LINHA)
