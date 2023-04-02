dormir = True
linha = '\033[1;33m-='*26 + '-\033[m'

try:
    from time import sleep
except:
    dormir = False

try:
    from random import randint
except:
    print('\033[1;31mOcorreu um erro na importção da bibliteca random, impossível continuar\033[m')
    quit()

print(linha)
print('\033[1;36m Vou pensar em um número de 0 a 5. Tente advinhar...\033[m')
print(linha)

while True:
    try:
        num = int(input('Em que número eu pensei? '))
        if not 0 <= num <= 5:
            raise ZeroDivisionError
    except:
        print('\033[1;31mOcorreu um erro, digite um valor válido!\033[m')
    else:
        break

print('PROCESSANDO...')
if dormir:
    sleep(1)

adv_num = randint(0, 5)

if num == adv_num:
    print('\033[1;32mParabéns, você conseguiu me vencer!\033[m\n')
else:
    print(f'\033[1;31mGANHEI! Pensei no número {adv_num} e não no {num}\033[m\n')
