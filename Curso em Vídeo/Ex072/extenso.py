'''
Trnasformar um número digitado para escrito por extenso usando tuplas
'''

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
       'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    try:
        val = int(input('Digite um número de 0 a 20: '))
        if val < 0 or val > 20:
            raise TypeError
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...')
        exit()
    except:
        print('\033[1;31mEscreva Certo!\033[m')
    else:
        break

print(f'Você digitou o número {num[val]}\n')
