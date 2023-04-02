'''
Tratando vários números com flag
'''

nums = list()

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
    nums.append(num)

print(f'\nVocê digitou {len(nums)} números e o resultado da soma deles foi de {sum(nums)}.\n')
