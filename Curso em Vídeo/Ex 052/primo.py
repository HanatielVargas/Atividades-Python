'''
Número primo
'''

while True:
    try:
        num = int(input('Digite um número: '))
    except Exception:
        print('Ocorreu um erro')
    except KeyboardInterrupt:
        print('Programa interrompido')
        exit()
    else:
        break

soma = 0 

for c in range(1, num+1, 1):
    if num % c == 0:
        soma += 1

if soma == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')
