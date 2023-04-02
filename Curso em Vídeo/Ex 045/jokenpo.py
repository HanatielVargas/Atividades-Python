try:
    from random import choice
except ImportError:
    print('Erro ao importar módulo necessário.')
    quit()

dormir = True

try:
    from time import sleep
except:
    dormir = False

opc = ('Pedra', 'Papel', 'Tesoura')

while True:
    try:
        pes = int(input('''Suas opções:
[1] Pedra
[2] Papel
[3] Tesoura
Qual sua escolha? '''))
        if pes < 1 or pes > 3:
            raise IndexError
    except IndexError:
        print('Digite um número válido')
    except Exception:
        print('Ocorreu um erro')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        quit()
    else:
        break

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

sleep(0.5) if dormir == True else print(end='')
print('JO')
sleep(0.5) if dormir == True else print(end='')
print('KEN')
sleep(0.5) if dormir == True else print(end='')
print('PO!')

print(('-='*15)[:-1])
print(f'Computador Jogou {com}')
print(f'Jogador Jogou {pes}')
print(('-='*15)[:-1])

if venc == 'Empate':
    print('Empatou')
else:
    print(f'O vencedor é {venc}')
