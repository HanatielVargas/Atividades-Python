'''
Criando um Cadastro de jogador
'''

gols = list()
jogador = dict()

while True:
    try:
        jogador['Nome'] = str(input('Nome do Jogador: ')).strip().title()
        if jogador['Nome'] == '':
            raise TypeError
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado!')
    else:
        break

while True:
    try:
        partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado!')
    else:
        break

for c in range(partidas):
    while True:
        try:
            gol = int(input(f'\tQuantos gols na partida {c}? '))
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('Você digitou algo errado!')
        else:
            gols.append(gol)
            break

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

print(f'Foi um total de {sum(jogador["Gols"])} gols')
