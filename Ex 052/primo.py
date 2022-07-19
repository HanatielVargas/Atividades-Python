'''
Número primo
'''

num = int(input('Digite um número: '))

soma = 0 

for c in range(1, num+1, 1):
    if num % c == 0:
        print(c)
        soma += 1

if soma == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')
    print(soma)
