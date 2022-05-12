while True:
    try:
        larg = float(input('Largura: '))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        while True:
            try:
                altu = float(input('Altura: '))
            except:
                print('\033[1;31mOcorreu um erro!\033[m')
            else:
                print(f'Sua parede tem dimensões {larg}x{altu} e sua área é de {larg*altu}.')
                print(f'Para pintar essa parede será necessário {(larg*altu)/2}l de tinta.')
                break
        break
