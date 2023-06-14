'''
Criando um  boletim usando listas compostas
'''

boletim = list()

while True:
    nome = str(input('Nome: ')).strip().capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    boletim.append([nome, n1, n2])
    
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break

print('=-'*20)
print(f'Nº.\t{"NOME":<25}MÉDIA')
print('-'*40)

for c in range(len(boletim)):
    print(f'{c}\t{boletim[c][0]:<25}{(boletim[c][1]+boletim[c][2])/2}')

while True:
    print('-'*40)
    aluno = int(input('Ver notas de qual aluno? [999 para] '))
    if aluno == 999:
        break
    print(f'Notas de {boletim[aluno][0]} são {boletim[aluno][1:]}')

print('Finalizando...\n')
