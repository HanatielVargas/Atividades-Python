'''
Criando uma função para ler números inteiros
'''

def leiaInt():
    while True:
        try:
            num = int(input('Digite um número: '))
        except KeyboardInterrupt:
            print('Usuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('Você digitou errado. Digite um número inteiro válido!')
        else:
            return num


num = leiaInt()
print(f'Você acabou de digitar o número {num}\n')
