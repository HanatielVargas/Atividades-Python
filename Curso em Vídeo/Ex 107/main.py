'''
Fazendo umas funções básicas de matemática usando modulos
'''

import moeda

preco = float(input('Digite o preço: R$'))

print(f'A metade de R${preco:.2f} é igual a {moeda.metade(preco):.2f}')
print(f'O dorbo de R${preco:.2f} é igual a {moeda.dobro(preco):.2f}')
print(f'O preço R${preco:.2f} aumentando 10% é igual a {moeda.percentagem(preco):.2f}')
