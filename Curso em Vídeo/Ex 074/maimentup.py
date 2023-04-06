'''
Maior e Menor número com tuplas
'''

from random import randint 

tup = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: {" ".join(map(str, tup))}')
print(f'O maior número sorteado foi {max(tup)}')
print(f'O menor número sorteade foi {min(tup)}\n')
