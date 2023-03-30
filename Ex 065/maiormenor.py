'''
Verificar a média dos números digitados e também o maio e o menor número entre eles
'''

nums = list()
soma = 0

while True:
    while True:
        try:
            num = float(input('Digite um número: '))
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...')
            exit()
        except:
            print('\033[1;31mOcorreu um erro. Digite certo.\033[m')
        else:
            break

    soma += num
    nums.append(num)

    while True:
        try:
            cont = str(input('Quer continuar? [s/n] ')).strip()[0]
            if cont not in 'sn' or cont == '':
                raise TypeError
        except KeyboardInterrupt:
            print('\nUsuário não quer continuar!\nEncerrando...')
            exit()
        except:
            print('\033[1;31mOcorreu um erro. Digite certo.\033[m')
        else:
            break

    if cont == 'n':
        break

nums.sort()

print(f'Você digitou {len(nums)} números e a média deles foi {soma/len(nums)}')
print(f'O maior valor foi {nums[-1]} e o menor foi {nums[0]}')
