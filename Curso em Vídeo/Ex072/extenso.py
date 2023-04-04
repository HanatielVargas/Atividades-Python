'''
Trnasformar um número digitado para escrito por extenso usando tuplas
'''

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
       'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

val = int(input('Digite um número de 0 a 20: '))

while 0 > val or val > 20:
    print('\033[1;31mEscreva Certo!\033[m')
    val = int(input('Digite um número de 0 a 20: '))

print(f'Você digitou o número {num[val]}\n')
