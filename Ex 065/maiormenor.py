'''
Verificar a média dos números digitados e também o maio e o menor número entre eles
'''

nums = list()
soma = 0

while True:
    num = float(input('Digite um número: '))

    soma += num
    nums.append(num)

    cont = str(input('Quer continuar? [s/n] '))
    if cont == 'n':
        break

nums.sort()

print(f'Você digitou {len(nums)} números e a média deles foi {soma/len(nums)}')
print(f'O maior valor foi {nums[-1]} e o menor foi {nums[0]}')
