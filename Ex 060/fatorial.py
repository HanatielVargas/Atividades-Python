'''
calculando fatorial
'''

while True:
    try:
        num = int(input('Digite um número para calcular seu fatorial: '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...')
        exit()
    except:
        print('\033[1;31mValor digitado é inválido.\033[m')
    else:
        break

fat = 1
cam = '= '

for c in range(num, 0, -1):
    fat *= c
    cam += f'{c} X '

print(f'Calculando {num}! {cam[0:-2]}= {fat}\n')
