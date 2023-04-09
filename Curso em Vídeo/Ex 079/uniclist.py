'''
Valores unicos numa lista
'''

lista = []

while True:
    while True:
        try:
            num = int(input('Digite um número: '))
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nSaindo...')
            exit()
        except:
            print('\033[1;31mOcorreu um erro! Escreva certo.\033[m')
        else:
            break

    lista.append(num)
    print('Número salvo com sucesso...')

    while True:
        try:
            cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if cont not in 'SN':
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nFinalizando...')
            cont = 'N'
            break
        except:
            print('\033[1;31mOcorreu um erro! Escreva certo.\033[m')
        else:
            break
    
    if cont == 'N':
        break

print('-='*20)
print(f'Você digitou os valores: {sorted(list(set(lista)))}\n')
