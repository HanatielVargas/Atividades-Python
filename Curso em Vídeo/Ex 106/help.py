'''
Criando um menu que mostra o help() das coisas
'''

cores = ['\033[m',      #Normal
         '\033[0;39;41m',   #Vermelho
         '\033[0;39;42m',   #Verde
         '\033[0;39;43m',   #Amarelo
         '\033[0;39;44m',   #Roxo
         '\033[0;39;45m',   #Rosa
         '\033[0;39;46m',   #Azul
         '\033[0;39;47m',   #Bege
         '\033[7;30m']      #Branco

def ajuda(msg):
    titulo(f"Acessando o manual do comando '{func}'", 6)
    help(msg)


def titulo(txt, cor):
    print(cores[cor], end='')
    print('~'*(len(txt)+4))
    print(f'  {txt}')
    print('~'*(len(txt)+4))
    print(cores[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)

    func = str(input('Função ou Bblioteca > '))

    if func.upper() == 'FIM':
        titulo('Até Logo!', 7)
        break

    ajuda(func)

