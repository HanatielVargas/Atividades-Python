'''
Criando uma função para ler números inteiros
'''

def leiaInt():
    while True:
        num = str(input('Digite um número: ')).strip()
        if num.isnumeric():
            return num
        else:
            print('Você digitou errado. Digite um número inteiro válido!')


num = leiaInt()
print(f'Você acabou de digitar o número {num}\n')
