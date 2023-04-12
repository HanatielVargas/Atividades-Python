'''
Lista  sem repetições em ordem decrescente
'''

lista = list()
cont = str

while cont != 'N':
    while True:
        try:
            num = int(input('Digite um valor: '))
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            exit()
        except:
            print('\033[1;31mOcorreu um erro! Escreva certo.\033[m')
        else:
            break

    if len(lista) == 0 or lista[-1] >= num:
        lista.append(num)
    elif lista[0] <= num:
        lista.insert(0, num)
    else:
        for c in range(len(lista)):
            if lista[c] > num >= lista[c+1]:
                lista.insert(c+1, num)
                break

    while True:
        try:
            cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if cont not in 'SN':
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            cont ='N'
            break
        except:
            print('\033[1;31mOcorreu um erro! Escreva certo.\033[m')
        else:
            break

print(f'Os valores digitados em ordem foram: {lista}')

if 5 in lista:
    print('O número 5 faz parte da lista\n')
else:
    print('O número 5 não faz parte da lista\n')
