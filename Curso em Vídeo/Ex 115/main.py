'''
Criando um menu em python
'''

from comandos import *
from time import sleep


sair = False

while not sair:
    menu()
    while True:
        try:
            opcao = int(input('Sua opção: '))
            if opcao < 1 or opcao > 3:
                raise IndexError
        except KeyboardInterrupt:
            print('Usuário não quer continuar!\nEncerrando...')
            quit()
        except:
            print('ERRO! Digite um valor válido.')
        else:
            break
    
    match opcao:
        case 1:
            mensagem('Opção 1')
        case 2:
            mensagem('Opção 2')
        case 3:
            sair = True
        case _:
            pass
    
    sleep(1)

mensagem('Saindo do sistema... Até logo!')
