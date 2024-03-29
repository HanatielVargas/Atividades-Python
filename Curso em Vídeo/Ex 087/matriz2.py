'''
Criando uma Matriz 3x3
'''

matriz = ''
pares = coluna3 = 0
maiorl2 = int

for l in range(3):
    for c in range(3):
        while True:
            try:
                num = int(input(f"Digite um valor para a posição [{l}][{c}]: "))
            except KeyboardInterrupt:
                print('\nUsuário não quer continuar! Encerrando...\n')
                exit()
            except:
                print('Você digitou algo errado!')
            else:
                break
        matriz += f'[{num:^5}]'
        if num % 2 == 0:
            pares += num
        if c == 2:
            coluna3 += num
        if l == 1 and maiorl2 == int or l == 1 and maiorl2 < num: # type: ignore
            maiorl2 = num
    if l != 2:
        matriz += '\n'

print('=-'*25)
print(f'{matriz}')
print('=-'*25)
print(f'A soma dos valores pares é: {pares}.')
print(f'A soma dos valores da terceira coluna é: {coluna3}.')
print(f'O maior valor da segunda linha é: {maiorl2}.\n')
