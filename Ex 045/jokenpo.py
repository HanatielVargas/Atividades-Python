from random import choice
from time import sleep

opc = ('Pedra', 'Papel', 'Tesoura')

print('''Suas opções:
[1] Pedra
[2] Papel
[3] Tesoura''')
pes = int(input('Qual sua escolha? '))
com = choice(opc)

if pes == 1:
    pes = 'Pedra'
elif pes == 2:
    pes = 'Papel'
elif pes == 3:
    pes = 'Tesoura'

if pes == com:
    venc = 'Empate'
elif pes == 'Pedra' and com == 'Tesoura' or pes == 'Papel' and com == 'Pedra' or pes == 'Tesoura' and com == 'Papel':
    venc = 'Player'
else:
    venc = 'Computador'

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')

print(('-='*15)[:-1])
print(f'Computador Jogou {com}')
print(f'Jogador Jogou {pes}')
print(('-='*15)[:-1])

if venc == 'Empate':
    print('Empatou')
else:
    print(f'O vencedor é {venc}')
