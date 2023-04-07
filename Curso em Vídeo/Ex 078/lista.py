'''
Maior e Menor valores na Lista
'''

lista = []

for c in range(5):
    while True:
        try:
            num = int(input(f'Digite um valor para a posição {c}: '))
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...')
            exit()
        except:
            print('\033[1;31mOcorreu um erro! Digite Novamente.\033[m')
        else:
            lista.append(num)
            break

print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')

for c in range(len(lista)):
    if lista[c] == max(lista):
        print(f'{c}... ', end='')

print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')

for c in range(len(lista)):
    if lista[c] == min(lista):
        print(f'{c}... ', end='')
