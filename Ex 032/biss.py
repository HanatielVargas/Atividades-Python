while True:
    try:
        ano = input('Digite um ano: ').strip()
        intano = int(ano)
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        break
    else:
        if intano % 4 == 0 and intano % 100 != 0 or intano % 400 == 0:
            print(True)
        else:
            print(False)
        break
