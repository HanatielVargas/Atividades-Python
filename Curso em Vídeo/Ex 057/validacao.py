'''
Fazer a validação de um input
'''

while True:
    try:
        sexo = str(input('Informe seu sexo [M/F]:')).strip().upper()[0]
        if sexo not in 'MF' or sexo == '':
            raise TypeError
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...')
        exit()
    except:
        print('\033[1;31mAlgo está errado.\033[m Digite certo')
    else:
        print(f'Sexo {sexo} registrado com sucesso.')
        break
