#Fazendo uma lista composta que guarda alguns dados e depois irá mostrá-los

lista = []
maior = 0
menor = 0

while True:
    while True:
        try:
            nome = str(input('NOME: ')).strip().title()
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar! Encerrando...')
            quit()
        except:
            print('Você digitou algo errado, por favor corrija!')
        else:
            break

    while True:
        try:
            peso = float(input('PESO: '))
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar! Encerrando...')
            quit()
        except:
            print('Você digitou algo errado, por favor corrija!')
        else:
            break
    
    lista.append([nome, peso])

    if peso > maior or maior == 0:
        maior = peso
    if peso < menor or menor == 0:
        menor = peso

    while True:
        try:
            cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if cont not in 'SN':
                raise TypeError
        except KeyboardInterrupt:
            break
        except:
            print('Você digitou algo errado, por favor corrija!')
        else:
            break

    if cont == 'N': # diz que ta errado mas não dá erro
        break

print('-='*30)
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