'''
Lista ordenada sem repetições
'''

lista = list()

for c in range(5):
    num = int(input('Digite um valor: '))

    if len(lista) == 0 or lista[-1] <= num:
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

print(f'Os valores digitados em ordem foram: {lista}')
