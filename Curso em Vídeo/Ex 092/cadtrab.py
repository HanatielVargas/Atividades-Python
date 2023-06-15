'''
Criando um Cadastro de trabalhador
'''

from datetime import datetime

ano = datetime.now().year

trabalhador = dict()

trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Idade'] = ano - int(input('Ano de Nascimento: '))
trabalhador['Ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if trabalhador['Ctps'] != 0:
    trabalhador['Contratação'] = int(input('Ano de Contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$'))
    trabalhador['Aposentadoria'] = trabalhador['Contratação'] + trabalhador['Idade'] + 35 - ano

print('-='*20)
for c in trabalhador.items():
    print(f'\t- {c[0]} tem o valor {c[1]}')

