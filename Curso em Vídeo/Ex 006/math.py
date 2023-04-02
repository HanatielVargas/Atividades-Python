while True:
    try:
        num = int(input('Digite um número: '))
    except:
        print('\033[1;31mOcooreu um erro!\033[m')
    else:
        print(f'O dobro de {num} é: {num*2} \nO triplo de {num} é: {num*3} \nA raiz quadrada de {num} é: {num**(1/2)}')
        break
