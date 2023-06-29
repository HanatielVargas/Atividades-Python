'''
Fazendo umas funções básicas de matemática usando modulos
'''
from moeda import *


preco = float(input('Digite o preço: R$'))

print(f'\nA metade de {brl(preco)} é igual a {brl(metade(preco))}')
print(f'O dobro de {brl(preco)} é igual a {brl(dobro(preco))}')
print(f'Aumentando 10%, temos {brl(aumentar(preco, 10))}')
