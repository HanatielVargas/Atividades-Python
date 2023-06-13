'''
Criando uma Matriz 3x3
'''

matriz = ''

for l in range(3):
    for c in range(3):
        num = f'{str(input(f"Digite um valor para a posição [{l}][{c}]: ")):^5}'
        matriz += f'[{num}]'
    matriz += '\n'    

print('=-'*25)
print(f'{matriz}')
