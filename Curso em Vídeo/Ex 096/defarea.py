'''
Criando uma Função que calcula área
'''

def calcArea(larg, comp):
    print(f'A área do terreno {larg}mx{comp}m é de {larg*comp}m²\n')

print('-'*20 + '\nCONTROLE DE TERRENOS\n'+ '-'*20)

calcArea(larg=float(input('LARGURA (m): ')), comp=float(input('COMPRIMENTO (m): ')))
