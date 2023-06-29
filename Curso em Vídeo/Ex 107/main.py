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
        aumento = float(input('Digite fator de aumento: '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado! Por favor corrija.')
    else:
        break

print(f'\nA metade de R${preco:.2f} é igual a R${metade(preco):.2f}')
print(f'O dobro de R${preco:.2f} é igual a R${dobro(preco):.2f}')
print(f'Aumentando {aumento:.2f}%, temos R${aumentar(preco, aumento):.2f}')
print(f'Diminuindo {aumento:.2f}%, temos R${diminuir(preco, aumento):.2f}\n')
