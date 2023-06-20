'''
Criando uma função que recebe vários valores e mostra o maior entre eles
'''

from time import sleep


def maior(* num):
    print('=-'*25)
    print('Analisando os valores passados...')
    for c in num:
        print(c, end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(num)} números ao todo')
    if len(num) != 0:
        print(f'O maior número informado foi {max(num)}.')
    else:
        print(f'Não foi informado número para definir o maior.')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
