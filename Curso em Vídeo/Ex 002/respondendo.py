while True:
    try:
        nome = input('Digite seu nome: ').strip()
        if nome.isnumeric():
            raise SyntaxError
    except SyntaxError:
        print('\033[1;31mOcorreu um erro\033[m')
    except:
        print('\n\033[1;31mOcorreu um erro\033[m')
    else:
        print(f'É um prazer te conhecer, {nome}!')
        break
