'''
Progreção Aritimétca
'''

while True:
    try:
        ini = float(input('Início da PA: '))
    except Exception:
        print('Ocorreu um erro')
    except KeyboardInterrupt:
        print('Programa Interrompido')
        exit()
    else:
        break

while True:
    try:
        raz = float(input('Razão da PA: '))
    except Exception:
        print('Ocorreu um erro')
    except KeyboardInterrupt:
        print('Programa Interrompido')
        exit()
    else:
        break

atu = ini

for c in range(10):
    print(f'{c+1} - {atu:.2f}')
    atu += raz