'''
Analisador de tuplas
'''

tup = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')))

par = 0 

for c in range(len(tup)):
    if c % 2 == 0:
        par += 1

print(f'Você digitou os valores: {tup}')
print(f'O número 9 apareceu {tup.count(9)} vezes')
print(f'O número 3 apareceu na {tup.index(3)}ª posição')
print(f'Os valores pares digitados foram {par}')
