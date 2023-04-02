while True:
    try:
        preco = float(input('Qual o valor do produto? R$'))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'O produto que custava R${preco} com o desconto de 5% vai custar {preco*0.95:.2f}')
        break
