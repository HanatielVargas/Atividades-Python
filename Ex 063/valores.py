'''
Tratando vários valores v1
'''

soma = 0
qtde = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    qtde += 1

print(f'\nVocê digitou {qtde} números e o resultado da soma deles foi de {soma}.\n')
