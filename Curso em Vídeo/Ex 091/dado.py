'''
Usando python para simular um jogo de dados entre 4 jogadores
'''

from random import randint

jogadores = dict()

for c in range(4):
    dado = randint(1, 6)
    print(f'Jogador {c+1} tirou {dado} no dado')
    jogadores.update({f'jogador{c+1}': dado})

print('\n' + '=-'*20)
print(f'{" RANKING DOS JOGADORES ":=^40}')
print('=-'*20)

sorted_jogadores = sorted(jogadores.items(), key=lambda x:x[1], reverse=True)

for c, i in enumerate(sorted_jogadores):
    print(f"{f'{c+1}º Lugar: {i[0]} com {i[1]}':^40}")

print()
