'''
Tratando vários valores v1
'''

soma = 0
qtde = 0

while True:
    while True:
        try:
            num = int(input('Digite um número [999 para parar]: '))
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...')
            exit()
        except:
            print('\033[1;31mDigite um valor válido!\033[m')
        else:
            break
    if num == 999:
        break
    soma += num
    qtde += 1

print(f'\nVocê digitou {qtde} números e o resultado da soma deles foi de {soma}.\n')
