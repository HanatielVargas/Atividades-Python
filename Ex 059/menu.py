'''
Criando um menu básico repetitível
'''

num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo Valor: '))

while True:
    menu = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
>>>> Qual é a sua opção? '''))
    
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
        num1 = int(input('Primeiro Valor: '))
        num2 = int(input('Segundo Valor: '))
    elif menu == 5:
        print('Encerrando...')
        exit()
    else:
        print('\033[1;31mValor inválido.\033[m')

    print('=-='*10)
        