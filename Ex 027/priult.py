while True:
    try:
        nome = ' '.join(input('Digite seu nome completo: ').strip().title().split())
        if nome == '' or not nome.isalpha():
            raise KeyError
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'''Prazer em te conhecer!
Seu primeiro nome é {nome.split()[0]}
Seu último nome é {nome.split()[-1]}
''')
        break
