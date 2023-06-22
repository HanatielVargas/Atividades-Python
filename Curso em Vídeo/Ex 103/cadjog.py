'''
Criando uma função para cadastrar jogadores 
'''

def jogador(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato!\n')


while True:
    try:
        nome = str(input('Nome do Jogador: ')).strip()
        if nome == '':
            raise TypeError
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        nome = '<Desconhecido>'
        break
    else:
        break

while True:
    try:
        gols = int(input('Número de gols: '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        gols = 0
        break
    else:
        break

jogador(nome, gols)
