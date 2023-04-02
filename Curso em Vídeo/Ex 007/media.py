while True:
    try:
        n1 = float(input('Digite a primeira nota: '))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        while True:
            try:
                n2 = float(input('Digite a segunda nota: '))
            except:
                print('\033[1;31mOcorreu um erro!\033[m')
            else:
                print(f'A média de {n1} e {n2} é {(n1+n2)/2}')
                break
        break
