print(('\033[1;35m=-'*25)[:-1])
print(f'\033[1;36m{"Analisador de Triângulos":^49}\033[m')
print(('\033[1;35m=-'*25)[:-1])

while True:
    try:
        reta1 = float(input('\033[mDigite o valor da primeira reta: '))
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar!')
        quit()
    else:
        break

while True:
    try:
        reta2 = float(input('Digite o valor da segunda reta: '))
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar!')
        quit()
    else:
        break

while True:
    try:
        reta3 = float(input('Digite o valor da terceira reta: '))
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar!')
        quit()
    else:
        break


if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As retas acima podem formar um triângulo!')
else:
    print('Impossível formar o formar um triângulo!')
