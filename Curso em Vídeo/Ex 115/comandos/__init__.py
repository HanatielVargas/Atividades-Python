LINHA = '-'*50


def menu():
    print(LINHA)
    print(f'{"MENU PRINCIPAL":^50}')
    print(LINHA)
    print('''\033[33m1\033[m - \033[36mVer pessoas cadastradas\033[m
\033[33m2\033[m - \033[36mCadastrar novas pessoas\033[m
\033[33m3\033[m - \033[36mSair do Programa\033[m''')
    print(LINHA)


def mensagem(msg):
    print(LINHA)
    print(f'{msg:^50}')
    print(LINHA)


def cadastrados():
    dados = 0
    try:
        with open('./Curso em Vídeo/Ex 115/dados/dados.txt', 'r') as arq:
            data = arq.readlines()
            dados = data
        dados = dados[0].split(';')
        for c in dados[0:-1]:
            c = c.split(',')
            print(f'  {c[0]:<38} {c[1]} Anos')
    except IndexError:
        print('\033[1;31mERRO! Não existe pessoa cadastrada.\033[m')
    except FileNotFoundError:
        print('\033[1;31mERRO! O arquivo foi apagado.\033[m')


def cadastrar():
    while True:
        try:
            nome = str(input('Nome: '))
            if nome.isnumeric():
                raise TypeError
        except KeyboardInterrupt:
            print('Usuário não quer continuar!\nEncerrando...')
            quit()
        except:
            print('\033[1;31mERRO! Digite um valor válido.\033[m')
        else:
            break

    while True:
        try:
            idade = int(input('Idade: '))
        except KeyboardInterrupt:
            print('Usuário não quer continuar!\nEncerrando...')
            quit()
        except:
            print('\033[1;31mERRO! Digite um valor válido.\033[m')
        else:
            break

    try:
        with open('./Curso em Vídeo/Ex 115/dados/dados.txt', 'a') as arq:
            arq.write(f'{nome},{idade};')
    except FileNotFoundError:
        print('\033[1;31mERRO! Arquivo não encontrado.\033[m')
    except:
        print('\033[1;31mERRO! Ocorreu um erro inesperado.\033[m')
    else:
        print(f'Novo registro de {nome} adicionado.')
