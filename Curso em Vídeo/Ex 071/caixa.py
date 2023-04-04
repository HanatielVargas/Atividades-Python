'''
Simulador de Caixa Eletrônico
'''

print('-'*40)
print(f'{"BANCO HS":^40}')
print('-'*40)

valor = int(input('Qual valor você quer sacar? R$'))
resto = valor

ced = 100
qtde = 0

while True:
    if resto >= ced:
        resto -= ced
        qtde += 1
    else:
        if qtde > 0 and ced != 1:
            print(f'Total de {qtde} cédulas de R$ {ced}.')
        elif ced == 1:
            print(f'Total de {qtde} moedas de R$ {ced}.')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        qtde = 0
        if resto == 0:
            break


print('-'*40)
print('Volte sempre ao BANCO HS. Tenha um bom dia!\n')
