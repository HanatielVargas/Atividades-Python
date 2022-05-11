while True:
    try:
        num = int(input('Digite um número: '))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print('-'*(len(f' {num} x 10 = {num*10} ')))
        for c in range(1, 11):
            print(f' {num} x {c:>2} = {num*c}')
        print('-'*(len(f' {num} x 10 = {num*10} ')))
        break
