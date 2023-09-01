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
            opcao = int(input('\033[33mSua opção: \033[m'))
            if opcao < 1 or opcao > 3:
                raise IndexError
        except KeyboardInterrupt:
            print('Usuário não quer continuar!\nEncerrando...')
            quit()
        except:
            print('\033[1;31mERRO! Digite um valor válido.\033[m')
        else:
            break
    
    match opcao:
        case 1:
            mensagem('PESSOAS CADASTRADAS')
            cadastrados()
        case 2:
            mensagem('FAZER CADASTRO')
        case 3:
            mensagem('Saindo do sistema... Até logo!')
            sair = True
        case _:
            pass
    
    sleep(1)
