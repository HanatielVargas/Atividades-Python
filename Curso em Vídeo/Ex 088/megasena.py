'''
Criando um programa que sorteia números que poderão ser usados para jogar na Mega Sena, quantos jogos forem necessários
'''

from random import shuffle

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 
               32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

palpites = list()

print('-'*50)
print(f'{"JOGA NA MEGA SENA":^50}')
print('-'*50)

while True:
    try:
        jogos = int(input('Quantos jogos você quer que eu sorteie? '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar! Encerrando...\n')
        exit()
    except:
        print('Você digitou algo errado.')
    else:
        break
frase = ('  SORTEANDO ' + str(jogos) + ' JOGOS  ')
print(f'{frase:-^50}')

for c in range(jogos):
    shuffle(numeros)
    while sorted(numeros[0:6]) in palpites:
        shuffle(numeros)
    palpites.append(sorted(numeros[0:6]))
    print(f'JOGO {c+1}: {palpites[c]}')

print(f'{" < BOA SORTE > ":-^50}\n')
    
