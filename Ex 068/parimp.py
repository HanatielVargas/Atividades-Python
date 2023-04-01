'''
Criando um jogo de par ou ímpar
'''

from random import randint
cont = 0

print('=-'*15)
print('   VAMOS JOGAR PAR OU ÍMPAR')

while True:
    print('=-'*15)

    val = int(input(' Diga um valor: '))
    pi = str(input(' Par ou Ímpar? [P/I] ')).upper()[0]

    comp = randint(0, 10)
    comp_win = False

    soma = comp+val

    if soma % 2 == 0:
        parimp = "Par"
        if pi != 'P':
            comp_win = True
    else:
        parimp = 'Ímpar'
        if pi != 'I':
            comp_win = True

    print('-'*30)
    print(f' Você jogou {val}, o computador {comp}\n Total de {soma}, deu {parimp}')
    print('-'*30)

    if comp_win == True:
        print(' Você Perdeu!')
        break
    else:
        print(' Você Venceu!') 
        cont += 1

    print(' Vamos jogar novamente...')

print('=-'*15)
print(f' GAME OVER!\n Você venceu {cont} vez(es).\n')
