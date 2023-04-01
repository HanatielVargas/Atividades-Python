'''
Criando um jogo de par ou ímpar
'''

from random import randint
cont = 0

print('=-'*15)
print('   VAMOS JOGAR PAR OU ÍMPAR')

while True:
    print('=-'*15)

    while True:
        try:
            val = int(input(' Diga um valor: '))
            if val < 0 or val > 10:
                raise TypeError
        except KeyboardInterrupt:
            print('\n Usuário não quer mais continuar')
            quit()
        except:
            print('\033[1;31m Ocorreu um Erro\033[m')
        else:
            break

    while True:
        try:
            tipo = str(input(' Par ou Ímpar? [P/I] ')).strip().upper()[0]
            if tipo not in 'PI':
                raise TypeError
        except KeyboardInterrupt:
            print('\n Usuário não quer mais continuar')
            quit()
        except:
            print('\033[1;31m Ocorreu um Erro\033[m')
        else:
            break

    comp = randint(0, 10)
    comp_win = False
    soma = comp+val

    if soma % 2 == 0:
        parimp = "Par"
        if tipo != 'P':
            comp_win = True
    else:
        parimp = 'Ímpar'
        if tipo != 'I':
            comp_win = True

    print('-'*30)
    print(f' Você jogou {val}, o computador {comp}\n Total de {soma}, deu {parimp}')
    print('-'*30)

    if comp_win == True:
        print('\033[1;31m Você Perdeu!\033[m')
        break
    
    print('\033[1;32m Você Venceu!\033[m') 
    print(' Vamos jogar novamente...')
    cont += 1

print('=-'*15)
print(f' \033[1;31mGAME OVER!\033[m\n Você venceu {cont} vez(es).\n')
