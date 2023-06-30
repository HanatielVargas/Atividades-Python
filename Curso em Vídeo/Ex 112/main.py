'''
Fazendo umas funções básicas de matemática usando modulos
'''
from utilidadescev.moeda import *
from utilidadescev.dado import *


preco = leiaDinheiro('Digite o preço: R$')
aum = leiaDinheiro('Digite fator de aumento: % ')
dim = leiaDinheiro('Digite fator de redução: % ')

resumo(preco, aum, dim)
