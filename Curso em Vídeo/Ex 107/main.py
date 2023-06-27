'''
Fazendo umas funções básicas de matemática usando modulos
'''

import moeda

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

print(f'\nA metade de R${preco:.2f} é igual a R${moeda.metade(preco):.2f}')
print(f'O dorbo de R${preco:.2f} é igual a R${moeda.dobro(preco):.2f}')
print(f'Aumentando {aumento:.2f}%, temos R${moeda.percentagem(preco, aumento):.2f}\n')
