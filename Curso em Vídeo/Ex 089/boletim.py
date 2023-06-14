'''
Criando um  boletim usando listas compostas
'''

boletim = list()

while True:
    while True:
        try:
            nome = str(input('Nome: ')).strip().capitalize()
            if nome == '' or nome.isalnum() and not nome.isalpha():
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar! Encerrando...\n')
            exit()
        except:
            print('Você digitou algo errado.')
        else:
            break
    while True:
        try:
            n1 = float(input('Nota 1: '))
            if n1 > 10 or n1 < 0:
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar! Encerrando...\n')
            exit()
        except:
            print('Você digitou algo errado.')
        else:
            break
    while True:
        try:
            n2 = float(input('Nota 2: '))
            if n2 > 10 or n2 < 0:
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar! Encerrando...\n')
            exit()
        except:
            print('Você digitou algo errado.')
        else:
            break

    boletim.append([nome, n1, n2])
    
    while True:
        try:
            cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if cont not in 'SN':
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar! Encerrando...\n')
            exit()
        except:
            print('Você digitou algo errado.')
        else:
            break

    if cont == 'N':
        break

print('=-'*20)
print(f'Nº.\t{"NOME":<25}MÉDIA')
print('-'*40)

for c in range(len(boletim)):
    print(f'{c}\t{boletim[c][0]:<25}{(boletim[c][1]+boletim[c][2])/2}')

while True:
    print('-'*40)

    while True:
        try:
            aluno = int(input('Ver notas de qual aluno? [999 para] '))
            if aluno > len(boletim)-1 and aluno != 999:
                raise IndexError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar! Encerrando...\n')
            exit()
        except:
            print('Você digitou algo errado.')
            print('-'*40)
        else:
            break

    if aluno == 999:
        break
    print(f'Notas de {boletim[aluno][0]} são {boletim[aluno][1:]}')

print('Finalizando...\n')
