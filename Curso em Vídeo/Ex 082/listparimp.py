'''
Dividindo uma lista em valores pares e ìmpares
'''

lista = []
par = []
impar = []

parar = str

while parar != 'N':
    while True:
        try:
            num = int(input('Digite um número: '))
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            exit()
        except:
            print('\033[1;31mOcorreu um erro! Digite Novamente...\033[m')
        else:
            break

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    
    lista.append(num)

    while True:
        try:
            parar = str(input('Quer coninuar? [S/N] ')).strip().upper()[0]
            if parar not in 'SN':
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            exit()
        except:
            print('\033[1;31mOcorreu um erro! Digite Novamente...')
        else:
            break

print('-='*20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ìmpares é {impar}')
