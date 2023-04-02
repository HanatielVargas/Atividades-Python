while True:
    try:
        num = int(input('Digite um número: '))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'Analisando o número {num}, seu antecessor é {num-1} e seu sucessor é {num+1}')
        break
