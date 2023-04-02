while True:
    try:
        dias = int(input('Quantos dias foi utilizado? '))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        while True:
            try:
                km = float(input('Quantos kms foram rodados? '))
            except:
                print('\033[1;31mOcorreu um erro!\033[m')
            else:
                print(f'O total a pagar é de R${dias*60+km*0.15:.2f}')
                break
        break
