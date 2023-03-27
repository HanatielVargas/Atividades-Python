'''
Criando um menu básico repetitível
'''

inv = '\033[1;31mValor digitado é inválido.\033[m'
num1 = int
num2 = int
menu = 4


def saindo(s=True):
    if s == True:
        print('\nUsuário não quer continuar!')
    print('Encerrando...')
    exit()


while True:
    if num1 != int:
        while True:
            try:
                menu = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
>>>> Qual é a sua opção? '''))
            except KeyboardInterrupt:
                saindo()
            except:
                print(inv)
            else:
                break
    if menu == 1:
        print(f'A soma de {num1} e {num2} é igual a {num1+num2}.') # type: ignore
    elif menu == 2:
        print(f'O resultado de {num1} x {num2} é de {num1*num2}.') # type: ignore
    elif menu == 3:
        if num1 > num2: # type: ignore
            print(f'Entre os números {num1} e {num2}, o maior é o {num1}.')
        elif num2 > num1: # type: ignore
            print(f'Entre os números {num1} e {num2}, o maior é o {num2}.')
        else:
            print(f'Os números {num1} e {num2} são iguais.')
    elif menu == 4:
            while True:
                try:
                    num1 = int(input('Primeiro Valor: '))
                except KeyboardInterrupt:
                    saindo()
                except:
                    print(inv)
                else:
                    break
            while True:
                try:
                    num2 = int(input('Segundo Valor: '))
                except KeyboardInterrupt:
                    saindo()
                except:
                    print(inv)
                else:
                    break
    elif menu == 5:
        saindo(s=False)
    else:
        print(inv)
    print('=-='*10)
