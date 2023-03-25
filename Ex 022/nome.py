while True:
    try:
        nome = input('Digite seu nome completo: ').strip()
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'Analisando seu nome...')
        print(f'Seu nome em maiúsculas é {nome.upper()}')
        print(f'Seu nome em minúsculas é {nome.lower()}')
        print(f' Seu nome tem ao todo {len(nome)-(len(nome.split())-1)} letras')
        print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras''')
        break
