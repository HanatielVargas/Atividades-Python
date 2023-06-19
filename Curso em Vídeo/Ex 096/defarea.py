'''
Criando uma Função que calcula área
'''

def calcArea(larg, comp):
    print(f'\nA área do terreno {larg}m x {comp}m é de {larg*comp:.2f}m²\n')

print('-'*20 + '\nCONTROLE DE TERRENOS\n'+ '-'*20)

while True:
    try:
        largura = float(input('LARGURA (m): '))
        if largura < 0:
            raise ZeroDivisionError
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado!')
    else:
        break

while True:
    try:
        comprimento = float(input('COMPRIMENTO (m): '))
        if comprimento < 0:
            raise ZeroDivisionError
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado!')
    else:
        break

calcArea(larg=largura, comp=comprimento)
