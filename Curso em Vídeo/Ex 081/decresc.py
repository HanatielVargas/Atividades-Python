'''
Lista  sem repetições em ordem decrescente
'''

lista = list()

while True:
    num = int(input('Digite um valor: '))

    if len(lista) == 0 or lista[-1] >= num:
        lista.append(num)
    elif lista[0] <= num:
        lista.insert(0, num)
    else:
        for c in range(len(lista)):
            if lista[c] > num >= lista[c+1]:
                lista.insert(c+1, num)
                break

    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break

print(f'Os valores digitados em ordem foram: {lista}\n')

if lista.index(5):
    print('O número 5 faz parte da lista')
else:
    print('O número 5 não faz parte da lista')
