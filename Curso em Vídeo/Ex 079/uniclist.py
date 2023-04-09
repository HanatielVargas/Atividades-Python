'''
Valores unicos numa lista
'''

lista = []

while True:
    num = int(input('Digite um número: '))

    lista.append(num)
    print('Número salvo com sucesso...')

    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break

print('-='*20)
print(f'Você digitou os valores: {sorted(list(set(lista)))}')
