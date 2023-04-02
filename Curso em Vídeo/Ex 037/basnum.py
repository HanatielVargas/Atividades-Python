while True:
    try:
        num = int(input('Digite um número inteiro: '))
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        exit()
    else:
        break

while True:
    try:
        opcao = int(input('''Escolha uma das bases para conversão:
[0] Sair
[1] Binário
[2] Octal
[3] Hexadecimal
Sua opção: '''))
        if opcao not in [1, 2, 3, 0]:
            raise IndexError
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        exit()
    else:
        break

if opcao == 1:
    print(f'{num} convertido para binário é: {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para octal é: {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para hexadecimal é: {hex(num).upper()[2:]}')
