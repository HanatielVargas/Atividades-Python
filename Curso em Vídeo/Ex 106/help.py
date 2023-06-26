'''
Criando um menu que mostra o help() das coisas
'''

def ajuda(msg):
    help(msg)


def msg(txt):
    txt = '~'*(len(txt)+4)+f'\n  {txt}\n'+'~'*(len(txt)+4)
    return txt


while True:
    print(msg('SISTEMA DE AJUDA PyHELP'))

    func = str(input('Função ou Bblioteca > '))

    if func.upper() == 'FIM':
        print(msg('Até Logo!'))
        break

    print(msg(f'Acessando o manual do comando \'{func}\''))

    ajuda(func)

