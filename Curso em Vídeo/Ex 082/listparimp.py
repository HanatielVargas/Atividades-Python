'''
Dividindo uma lista em valores pares e ìmpares
'''

lista = []
par = []
impar = []

parar = str

while parar != 'N':
    num = int(input('Digite um número: '))

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    
    lista.append(num)

    parar = str(input('Quer coninuar? [S/N] ')).strip().upper()[0]

print('-='*20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ìmpares é {impar}')
