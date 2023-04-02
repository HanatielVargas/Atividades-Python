'''
Criando um gerador de Progessão Aritmética ilimitado
'''

def gerarpa(limite=10, cont=0):
    while cont != limite:
        print(f'{pri+(raz*cont)} -> ', end='')
        cont += 1
    print('PAUSA\n')
    return cont

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

cont = gerarpa()

while True:
    while True:
        try:
            mais = int(input('Quantos você quer mostrar a mais? '))
            if mais < 0:
                raise ValueError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar.\nEncerrando...')
            exit()
        except:
            print('\033[1;31mDigite algo válido.\033[m')
        else:
            break

    if mais == 0:
        print(f'Progressão finalizada com {cont} termos mostrados.')
        break

    cont = gerarpa(limite=(cont+mais), cont=cont)
