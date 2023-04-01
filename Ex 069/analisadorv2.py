'''
Analisador de dados de pessoas até que o usuário não queira continuar
'''

CAD = 'CADASTRE UMA PESSOA'

hom = mul = m18 = 0

while True:
    print('-'*30)
    print(f'{CAD:^30}')
    print('-'*30)

    while True:
        try:
            idade = int(input('Idade: '))
        except KeyboardInterrupt:
            print('Usuário não quer mais continuar')
            quit()
        except:
            print('\033[1;31mOcorreu um Erro\033[m')
        else:
            break

    while True:
        try:
            sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
            if sexo not in 'FM':
                raise TypeError
        except KeyboardInterrupt:
            print('Usuário não quer mais continuar')
            quit()
        except:
            print('\033[1;31mOcorreu um Erro\033[m')
        else:
            break

    if sexo == 'M':
        hom += 1

    if sexo == 'F' and idade < 20:
        mul += 1
    
    if idade >= 18:
        m18 += 1

    print('-'*30)

    while True:
        try:
            cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if cont not in 'SN':
                raise TypeError
        except KeyboardInterrupt:
            print('Usuário não quer mais continuar')
            quit()
        except:
            print('\033[1;31mOcorreu um Erro\033[m')
        else:
            break

    if cont == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {m18}')
print(f'Ao todo temos {hom} homens cadastrados')
print(f'E temos {mul} mulheres com menos de 20 anos\n')
