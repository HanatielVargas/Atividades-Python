'''
Analisador de tuplas
'''

while True:
    try:
        a = int(input('Digite um número: '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        exit()
    except:
        print('\033[1;31mOcorreu um erro. Digite certo!\033[m')
    else:
        break

while True:
    try:
        b = int(input('Digite outro número: '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        exit()
    except:
        print('\033[1;31mOcorreu um erro. Digite certo!\033[m')
    else:
        break

while True:
    try:
        c = int(input('Digite outro número: '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        exit()
    except:
        print('\033[1;31mOcorreu um erro. Digite certo!\033[m')
    else:
        break

while True:
    try:
        d = int(input('Digite outro número: '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        exit()
    except:
        print('\033[1;31mOcorreu um erro. Digite certo!\033[m')
    else:
        break

tup = (a, b, c, d)

par = 0 

for c in range(len(tup)):
    if c % 2 == 0:
        par += 1

print(f'Você digitou os valores: {tup}')
print(f'O número 9 apareceu {tup.count(9)} vezes')

try:
    print(f'O número 3 apareceu na {tup.index(3)}ª posição')
except:
    print('O número 3 apareceu não apareceu')

print(f'Os valores pares digitados foram {par}\n')
