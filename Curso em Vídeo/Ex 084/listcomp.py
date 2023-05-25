#Fazendo uma lista composta que guarda alguns dados e depois irá mostrá-los

lista = []
maior = 0
menor = 0

while True:
    nome = str(input('NOME: ')).strip().title()
    peso = float(input('PESO: '))
    lista.append([nome, peso])

    if peso > maior or maior == 0:
        maior = peso
    if peso < menor or menor == 0:
        menor = peso

    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if cont == 'N':
        break

print('-='*40)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for c in lista:
    if c[1] == maior:
        print(c[0], end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for c in lista:
    if c[1] == menor:
        print(c[0], end=' ')
print('\n')