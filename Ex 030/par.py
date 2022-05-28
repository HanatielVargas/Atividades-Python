while True:
    try:
        num = int(input('Digite um número: '))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'O número {num} é', 'ÍMPAR' if num%2 != 0 else 'PAR')
        break
