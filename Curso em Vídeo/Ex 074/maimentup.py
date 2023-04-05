'''
Maior e Menor número com tuplas
'''

from random import randint 

tup = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: ', end='')
for c in range(len(tup)):
    print(tup[c], end=' ')

print(f'\nO maior número sorteado foi {max(tup)}')
print(f'O menor número sorteade foi {min(tup)}\n')
