'''
Progreção Aritimétca
'''

ini = float(input('Início da PA: '))
raz = float(input('Razão da PA: '))
atu = ini

for c in range(10):
    print(f'{c+1} - {atu:.2f}')
    atu += raz