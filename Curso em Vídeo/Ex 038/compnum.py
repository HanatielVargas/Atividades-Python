while True:
    try:
        num1 = int(input('Digite o primeiro número: '))
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar!')
        quit()
    else:
        break

while True:
    try:
        num2 = int(input('Digite o segundo número: '))
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar!')
        quit()
    else:
        break

if num1 > num2:
    print('O primeiro número é maior')
else:
    print('O segundo número é maior')
