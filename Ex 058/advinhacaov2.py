'''
Criar um jogo de advinhação melhor que o já criado (Ex 028)
'''

from random import randint

num = randint(0, 10)
qtde = 0
tent = int
print(num)

print('Acabei de pensar num número de 0 a 10.')
print('Será que você consegue advinhar qual foi?')

while tent != num:
    qtde += 1
    tent = int(input('Qual é o seu palpite? '))

    if tent < num:
        print('Mais... Tente mais uma vez.')
    elif tent > num:
        print('Menos... Tente mais uma vez.')

print(f'Acertou com {qtde} tentativas. Parabéns!')
