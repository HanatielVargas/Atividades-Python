num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} convertido para binário é: {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para octal é: {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para hexadecimal é: {hex(num)[2:]}')
else:
    print(f'"{opcao}" não faz parte das opções disponíveis')
