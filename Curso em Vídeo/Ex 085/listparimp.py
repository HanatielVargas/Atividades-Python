'''
Criando um identificador de par e ímpar usando listas
'''

listapar = list()
listaimpar = list()

for c in range(7):
    while True:
        try:
            num = int(input(f'Digite o {c+1}º número: '))
        except KeyboardInterrupt:
            print('Usuário não quer continuar! Encerrando...')
            exit()
        except:
            print('Você digitou algo errado!')
        else:
            break
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)

print('=-'*30)
print(f'Os valores pares digitados foram: {listapar}')
print(f'Os valores ímpares digitados foram: {listaimpar}\n')
