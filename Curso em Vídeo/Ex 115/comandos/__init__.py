LINHA = '-'*50


def menu():
    print(LINHA)
    print(f'{"MENU PRINCIPAL":^50}')
    print(LINHA)
    print('''1 - Ver pessoas cadastradas
2 - Cadastrar novas pessoas
3 - Sair do Programa''')
    print(LINHA)


def mensagem(msg):
    print(LINHA)
    print(f'{msg:^50}')
    print(LINHA)
