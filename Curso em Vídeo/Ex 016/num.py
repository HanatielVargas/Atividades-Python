while True:
    try:
        valor = float(input('Digite um valor: '))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'O valor digitado foi {valor} e sua parte inteira é de {int(valor)}')
        break
