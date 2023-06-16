'''
Unindo dicionários e listas
'''

pessoa = dict()
povo = list()
soma = 0

while True:
    while True:
        try:
            pessoa['Nome'] = str(input('Nome: '))
            if pessoa['Nome'] == '':
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('ERRO! Digite algum nome.')
        else:
            break
    
    while True:
        try:
            pessoa['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
            if pessoa['Sexo'] not in 'FM':
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('ERRO! Digite somente M ou F.')
        else:
            break

    while True:
        try:
            pessoa['Idade'] = int(input('Idade: '))
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('ERRO! Digite sua idade.')
        else:
            break

    soma += pessoa['Idade']

    povo.append(pessoa.copy())
    pessoa.clear()

    while True:
        try:
            cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if cont not in 'SN':
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('ERRO! Digite somente S ou N.')
        else:
            break

    if cont == 'N':
        break

print('=-'*25)
print(f'A) Ao todo temos {len(povo)} pessoas cadastradas')
print(f'B) A média de idade é de {soma/len(povo):.2f}')
print(f'C) As mulheres cadastradas foram ', end='')
for c in range(len(povo)):
    if povo[c]['Sexo'] == 'F':
        print(povo[c]['Nome'], end=' ')

print(f'\nD) Lista das pessoas que estão acima da média:')
for c in range(len(povo)):
    if povo[c]['Idade'] > soma/len(povo):
        print(f'\tNome = {povo[c]["Nome"]}; Sexo = {povo[c]["Sexo"]}; Idade = {povo[c]["Idade"]};')
