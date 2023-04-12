'''
Lista ordenada sem repetições
'''

lista = list()

while len(lista) != 5:
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

    if num in lista:
        print('Número já está na lista')
    elif len(lista) == 0 or lista[-1] <= num:
        lista.append(num)
        print('Valor adicionado ao final da lista...')
    elif lista[0] >= num:
        lista.insert(0, num)
        print('Valor adicionado ao inicio da lista...')
    else:
        for c in range(len(lista)):
            if lista[c] < num <= lista[c+1]:
                lista.insert(c+1, num)
                print(f'Valor adicionado na posição {c+1}...')
                break

print(f'Os valores digitados em ordem foram: {lista}\n')
