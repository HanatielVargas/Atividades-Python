'''
Fazendo umas funções básicas de matemática usando modulos
'''
from utilidadescev.moeda import *


while True:
    try:
        preco = float(input('Digite o preço: R$'))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado! Por favor corrija.')
    else:
        break


while True:
    try:
        aum = float(input('Digite fator de aumento: % '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado! Por favor corrija.')
    else:
        break


while True:
    try:
        dim = float(input('Digite fator de redução: % '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado! Por favor corrija.')
    else:
        break

resumo(preco, aum, dim)
