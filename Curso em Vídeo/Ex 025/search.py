while True:
    try:
        nome = ' '.join(input('Digite seu nome completo: ').title().split())
        if len(nome) == 0 or not nome.isalpha():
            raise KeyError
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print('Seu nome tem Silva?', True if 'Silva' in  nome else False)
        break
