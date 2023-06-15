'''
Criando um Cadastro de jogador
'''

gols = list()
jogador = dict()

jogador['Nome'] = str(input('Nome do Jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for c in range(partidas):
    gol = int(input(f'\tQuantos gols na partida {c}? '))
    gols.append(gol)

jogador['Gols'] = gols
jogador['Total'] = sum(gols)

print('-='*20)
print(jogador)
print('-='*20)

for c in jogador.items():
    print(f'O campo {c[0]} tem valor {c[1]}')

print('-='*20)

print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for c, i in enumerate(jogador['Gols']):
    print(f'\t=> Na partida {c}, fez {i} gols')

print(f'Foi um total de {len(jogador["Gols"])}')
