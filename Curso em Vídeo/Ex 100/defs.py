'''
Criando duas funções, uma irá sortear 5 valores e outra irá somar os números pares sorteados pela primeira função
'''

from random import randint
from time import sleep


lista = list()


def sortear():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        num = randint(0, 10)
        print(num, end=' ', flush=True)
        sleep(0.5)
        lista.append(num)
    print('PRONTO!')
    

def somapar(list):
    print(f'Somando os valores pares de {list}, temos:', end=' ')
    soma = 0
    for c in list:
        if c % 2 == 0:
            soma += c
    print(soma, '\n')


sortear()
somapar(lista)
