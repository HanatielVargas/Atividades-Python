'''
Maior e Menor valores na Lista
'''

lista = []

for c in range(5):
    num = int(input(f'Digite um valor para a posição {c}: '))
    lista.append(num)

print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')

for c in range(len(lista)):
    if lista[c] == max(lista):
        print(f'{c}... ', end='')
    
print('')

print(f'O menor valor digitado foi {min(lista)} nas posições ', end='')

for c in range(len(lista)):
    if lista[c] == min(lista):
        print(f'{c}... ', end='')
