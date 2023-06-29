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


while True:
    try:
        aumento = float(input('Digite fator de mudança: % '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado! Por favor corrija.')
    else:
        break


print(f'\nA metade de {brl(preco)} é igual a {brl(metade(preco))}')
print(f'O dobro de {brl(preco)} é igual a {brl(dobro(preco))}')
print(f'Aumentando {aumento:.2f}%, temos {brl(aumentar(preco, aumento))}')
print(f'Diminuindo {aumento:.2f}%, temos {brl(diminuir(preco, aumento))}\n')
