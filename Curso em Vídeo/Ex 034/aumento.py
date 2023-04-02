while True:
    try:
        sal = float(input('Digite o salário: R$'))
    except Exception:
        print('\033[1;31mOcorreu um Erro!\033[m')
    except KeyboardInterrupt:
        print('\022[1;31mUsuário não quis continuar!\033[m')
        quit()
    else:

        if sal > 1250:
            novo_sal = sal * 1.1
        else:
            novo_sal = sal * 1.15

        print(f'Quem ganhava R${sal:.2f} passa a ganhar R${novo_sal:.2f} agora.')
        break
