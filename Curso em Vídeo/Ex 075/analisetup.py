'''
Analisador de tuplas
'''

def input_number():
    while True:
        try:
            return int(input('Digite um número: '))
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            exit()
        except:
            print('\033[1;31mOcorreu um erro. Digite um número inteiro!\033[m')
        break

tup = (input_number(), input_number(), input_number(), input_number())

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
