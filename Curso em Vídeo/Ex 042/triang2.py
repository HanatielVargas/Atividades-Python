while True:

    while True:
        try:
            reta1 = float(input('Primeira reta: '))
        except Exception:
            print('\033[1;31mOcorreu um erro!\033[m')
        except KeyboardInterrupt:
            print('Usuário não quer continuar')
            quit()
        else:
            break

    while True:
        try:
            reta2 = float(input('Segunda reta: '))
        except Exception:
            print('\033[1;31mOcorreu um erro!\033[m')
        except KeyboardInterrupt:
            print('Usuário não quer continuar')
            quit()
        else:
            break

    while True:
        try:
            reta3 = float(input('Terceira reta: '))
        except Exception:
            print('\033[1;31mOcorreu um erro!\033[m')
        except KeyboardInterrupt:
            print('Usuário não quer continuar')
            quit()
        else:
            break

    if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:

        if reta1 == reta2 == reta3:
            print('Equilátero')
        elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
            print('Isósceles')
        elif reta1 != reta2 != reta3:
            print('Escaleno')
        break
    
    else:
        print('Digite valores que formam um triângulo. \nPara sair aperte Ctrl+C a qualquer momento.')
    