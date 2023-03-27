'''
calculando fatorial
'''

num = int(input('Digite um número para calcular seu fatorial: '))

fat = 1
cam = ''

for c in range(num, 0, -1):
    fat *= c
    cam += f'{c} X '

print(f'Calculando {num}! = {cam[0:-3]} = {fat}\n')
