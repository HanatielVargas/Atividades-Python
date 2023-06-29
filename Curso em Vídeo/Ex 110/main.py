'''
Fazendo umas funções básicas de matemática usando modulos
'''
from moeda import *


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


resumo(preco, 20, 12)
