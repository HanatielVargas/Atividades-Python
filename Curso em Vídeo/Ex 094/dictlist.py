'''
Unindo dicionários e listas
'''

pessoa = dict()
povo = list()
soma = 0

while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['Idade'] = int(input('Idade: '))

    soma += pessoa['Idade']

    povo.append(pessoa.copy())
    pessoa.clear()

    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break


print('=-'*25)
print(f'A) Ao todo temos {len(povo)} pessoas cadastradas')
print(f'B) A média de idade é de {soma/len(povo):.2f}')
print(f'C) As mulheres cadastradas foram ', end='')
for c in range(len(povo)):
    if povo[c]['Sexo'] == 'F':
        print(povo[c]['Nome'], end='')

print(f'\nD) Lista das pessoas que estão acima da média:')
for c in range(len(povo)):
    if povo[c]['Idade'] > soma/len(povo):
        print(f'\tNome = {povo[c]["Nome"]}; Sexo = {povo[c]["Sexo"]}; Idade = {povo[c]["Idade"]};')
