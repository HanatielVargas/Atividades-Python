'''
Criando um identificador de par e ímpar usando listas
'''

listapar = list()
listaimpar = list()

for c in range(7):
    num = int(input(f'Digite o {c+1}º número: '))
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)

print(f'Os valores pares digitados foram: {listapar}')
print(f'Os valores pares digitados foram: {listaimpar}')
