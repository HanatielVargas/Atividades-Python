'''
Unindo dicionários e listas v2
'''

gols = list()
jogador = dict()
time = list()

while True:
    while True:
        try:
            jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
            if jogador['Nome'] == '':
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('ERRO! Digite algum nome.')
        else:
            break

    while True:
        try:
            jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
            if jogador['Partidas'] < 0:
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('ERRO! Digite algum número válido.')
        else:
            break

    for c in range(jogador['Partidas']):
        while True:
            try:
                gol = int(input(f'\tQuantos gols na partida {c+1}? '))
                if gol < 0:
                    raise TypeError
            except KeyboardInterrupt:
                print('\nUsuário não quer continuar!\nEncerrando...\n')
                quit()
            except:
                print('ERRO! Digite algum número válido.')
            else:
                break
        gols.append(gol)

    jogador['Gols'] = gols.copy()

    time.append(jogador.copy())
    jogador.clear()
    gols.clear()

    while True:
        try:
            cont = str(input('Continuar? [S/N] ')).strip().upper()[0]
            if cont not in 'SN':
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('ERRO! Digite somente S ou N.')
        else:
            break
    if cont == 'N':
        break

print('=-'*20)
print(f'Nº {"Nome":<12} {"Gols":<18} Total')
print('-'*40)
for c, i in enumerate(time):
    print(f'{c:>2} {i["Nome"]:<12} {str(i["Gols"]):<18} {sum(i["Gols"])}')
print('-'*40)

while True:
    while True:
        try:
            cod = int(input('Ver dados de qual jogador? (999 para) '))
            if cod != 999 and (cod < 0 or cod > len(time)-1): 
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('ERRO! Digite algum nome.')
            print('-'*40)
        else:
            break

    if cod == 999:
        break

    print(f'Levantando dados do jogador {time[cod]["Nome"]}')
    for c, i in enumerate(time[cod]["Gols"]):
        print(f'\tNo jogo {c+1} fez {i} Gols')

    print('-'*40)

print('-'*40)
print('<<< VOLTE SEMPRE >>>\n')
