while True:
    try:
        n1, n2 = int(input('Digite um número: ').strip()), int(input('Digite outro número: ').strip())
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'A soma de {n1} e {n2} é igual a {n1 + n2}.')
        break