'''
Criando um gerador de Progessão Aritmética usando While
'''

print('Gerador de PA\n' + '=-'*10)

pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
cont = 1

print(f'{pri} ->', end='')

while cont != 10:
    print(f' {pri+(raz*cont)} ->', end='')
    cont += 1

print(' FIM\n')
