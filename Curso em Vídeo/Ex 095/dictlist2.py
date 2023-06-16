'''
Unindo dicionários e listas v2
'''

gols = list()
jogador = dict()
time = list()


while True:
    jogador['Nome'] = str(input('Nome do jogador: '))
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    for c in range(jogador['Partidas']):
        gol = int(input(f'\tQuantos gols na partida {c+1}? '))
        gols.append(gol)

    jogador['Gols'] = gols.copy()

    time.append(jogador.copy())
    jogador.clear()
    gols.clear()

    cont = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break

print('=-'*20)
print(f'Nº {"Nome":<12} {"Gols":<18} Total')
print('-'*40)
for c, i in enumerate(time):
    print(f'{c:>2} {i["Nome"]:<12} {str(i["Gols"]):<18} {sum(i["Gols"])}')
print('-'*40)

while True:
    cod = int(input('Ver dados de qual jogador? (999 para) '))

    if cod == 999:
        break

    print(f'Levantando dados do jogador {time[cod]["Nome"]}')
    for c, i in enumerate(time[cod]["Gols"]):
        print(f'\tNo jogo {c+1} fez {i} Gols')

    print('-'*40)
    