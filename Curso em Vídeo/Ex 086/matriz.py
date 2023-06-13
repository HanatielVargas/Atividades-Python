'''
Criando uma Matriz 3x3
'''

matriz = ''

for l in range(3):
    for c in range(3):
        while True:
            try:
                num = f'{int(input(f"Digite um valor para a posição [{l}][{c}]: ")):^5}'
            except KeyboardInterrupt:
                print('\nUsuário não quer continuar! Encerrando...\n')
                exit()
            except:
                print('Você digitou algo errado!')
            else:
                break
        matriz += f'[{num}]'
    matriz += '\n'    

print('=-'*25)
print(f'{matriz}')
