'''
Programa que simula uma compra
'''

LOJA = 'LOJA SUPER BARATÃO'
FIM = 'FIM DO PROGRAMA'

tot = qtdemil = 0
barato = list()

print('-'*30)
print(f'{LOJA:^30}')
print('-'*30)

while True:
    while True:
        try:
            nome = str(input('Nome do Produto: ')).strip()
            if nome == '' or nome.isnumeric():
                raise SyntaxError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar. \nEncerrando...')
            exit()
        except:
            print('\033[1;31mVocê digitou algo errado!\033[m')
        else:
            break
    while True:
        try:
            preco = float(input('Preço: R$'))
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar. \nEncerrando...')
            exit()
        except:
            print('\033[1;31mVocê digitou algo errado!\033[m')
        else:
            break

    tot += preco
    if barato == [] or preco < barato[1]:
        barato.clear()
        barato.append(nome)
        barato.append(preco)
    if preco > 1000:
        qtdemil += 1

    while True:
        try:
            cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if cont not in 'SN':
                raise SyntaxError
        except KeyboardInterrupt:
            print('Usuário não quer continuar. \nEncerrando...')
            exit()
        except:
            print('\033[1;31mVocê digitou algo errado!\033[m')
        else:
            break
    
    if cont == 'N':
        break

print(f'{FIM:-^30}')
print(f'O total da compra foi de R${tot}')
print(f'Temos {qtdemil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato[0]} que custa {barato[1]}\n')
