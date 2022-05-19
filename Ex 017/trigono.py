while True:
    try:
        co = float(input('Valor do Cateto Oposto: '))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        while True:
            try:
                ca = float(input('Valor do Cateto Adjacente: '))
            except:
                print('\033[1;31mOcorreu um erro!\033[m')
            else:
                print(f'A hipotenusa vai medir: {(ca**2+co**2)**0.5:.2f}')
                break
        break
