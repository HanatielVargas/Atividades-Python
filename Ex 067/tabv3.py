'''
tabuada versâo 3
'''


while True:
    print('-'*40)
    while True:
        try:
            num = int(input('Quer ver a tabuada de qual valor? '))
        except KeyboardInterrupt:
            print('Usuário não quer mais continuar')
            quit()
        except:
            print('\033[1;31mOcorreu um Erro\033[m')
        else:
            break

    print('-'*40)

    if num < 0:
        break

    for c in range(10):
        print(f'{num} X {c+1:>2} = {num*(c+1)}')

print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre...')
