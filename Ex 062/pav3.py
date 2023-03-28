'''
Criando um gerador de Progessão Aritmética ilimitado
'''

def gerarpa(limite=10, cont=0):
    while cont != limite:
        print(f'{pri+(raz*cont)} -> ', end='')
        cont += 1
    print('PAUSA\n')
    return cont

print('Gerador de PA\n' + '=-'*10)

pri = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))

cont = gerarpa()

while True:
    mais = int(input('Quantos você quer mostrar a mais? '))
    if mais == 0:
        print(f'Progressão finalizada com {cont} termos mostrados.')
        break
    cont = gerarpa(limite=(cont+mais), cont=cont)
