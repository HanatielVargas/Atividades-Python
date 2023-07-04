'''
Funções aprofundadas em python
'''

def leiaInteiro(msg):
    while True:
        try:
            num = input(msg).strip()
            if str(int(num)) != num:
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('\033[;31mERRO: Por favor digite um número inteiro válido!\033[m')
        else:
            break
    return num


def leiaReal(msg):
    while True:
        try:
            num = input(msg).strip()
            if str(float(num)) != num:
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...\n')
            quit()
        except:
            print('\033[;31mERRO: Por favor digite um número real válido!\033[m')
        else:
            break
    return num


inteiro = leiaInteiro('Digite um número inteiro: ')
real = leiaReal('Digite um número real: ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.\n')
