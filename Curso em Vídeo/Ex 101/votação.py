'''
Criando uma função para votação
'''

from datetime import datetime


def vota(nasc):
    idade = datetime.now().year - nasc
    print(f'Com {idade} anos: ', end='')
    if idade >= 65 or 16 <= idade < 18:
        print('Voto OPICIONAL\n')
    elif 18 <= idade < 65:
        print('Voto OBRIGATÓRIO\n')
    else:
        print('NÃO VOTA!\n')


vota(int(input('Em que ano você nasceu? ')))
