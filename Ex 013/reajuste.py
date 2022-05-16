while True:
    try:
        valor = float(input('Digite o salário do funcionário: R$'))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'Um funcionário que ganhava R${valor} com o reajuste de 15% ganhará R${valor*1.15:.2f}.')
        break
