'''
Criando um gerador de Progessão Aritmética usando While
'''

print('Gerador de PA\n' + '=-'*10)

while True:
    try:
        pri = int(input('Primeiro termo: '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar.\nEncerrando...')
        exit()
    except:
        print('\033[1;31mDigite algo válido.\033[m')
    else:
        break

while True:
    try:
        raz = int(input('Razão da PA: '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar.\nEncerrando...')
        exit()
    except:
        print('\033[1;31mDigite algo válido.\033[m')
    else:
        break

cont = 1

print(f'{pri} ->', end='')

while cont != 10:
    print(f' {pri+(raz*cont)} ->', end='')
    cont += 1

print(' FIM\n')
