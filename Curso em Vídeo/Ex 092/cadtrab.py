'''
Criando um Cadastro de trabalhador
'''

from datetime import datetime

ano = datetime.now().year

trabalhador = dict()

while True:
    try:
        trabalhador['Nome'] = str(input('Nome: ')).strip().title()
        if trabalhador['Nome'] == '' or trabalhador['Nome'].isnumeric():
            raise TypeError
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado!')
    else:
        break

while True:
    try:
        nasc = int(input('Ano de Nascimento: '))
        trabalhador['Idade'] = ano - nasc
        if trabalhador['Idade'] < 0:
            raise TypeError
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado!')
    else:
        break
while True:
    try:
        trabalhador['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado!')
    else:
        break

if trabalhador['Ctps'] != 0:
    while True:
        try:
            trabalhador['Contratação'] = int(input('Ano de Contratação: '))
            if trabalhador['Contratação'] < nasc:
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('Você digitou algo errado!')
        else:
            break
    
    while True:
        try:
            trabalhador['Salário'] = float(input('Salário: R$'))
            if trabalhador['Salário'] < 0:
                raise ZeroDivisionError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('Você digitou algo errado!')
        else:
            break

    trabalhador['Aposentadoria'] = trabalhador['Contratação'] + trabalhador['Idade'] + 35 - ano

print('-='*20)
for c in trabalhador.items():
    print(f'\t- {c[0]} tem o valor {c[1]}')
