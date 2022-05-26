from time import sleep
from random import randint

linha = '\033[1;33m-='*26 + '-\033[m'

print(linha)
print('\033[1;36m Vou pensar em um número de 0 a 5. Tente advinhar...\033[m')
print(linha)
num = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(1)

adv_num = randint(0, 5)

if num == adv_num:
    print('\033[1;32mParabéns, você conseguiu me vencer!\033[m')
else:
    print(f'\033[1;31mGANHEI! Pensei no número {adv_num} e não no {num}\033[m\n')
