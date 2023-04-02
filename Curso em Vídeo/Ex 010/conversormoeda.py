while True:
    try:
        din = float(input('Digite um valor: R$'))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'Você tem US${din/5.13:.2f}')
        break
