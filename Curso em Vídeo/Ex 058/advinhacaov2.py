'''
Criar um jogo de advinhação melhor que o já criado (Ex 028)
'''

from random import randint

num = randint(0, 10)
qtde = 0
tent = int
numeros = list()

print('Acabei de pensar num número de 0 a 10.')
print('Será que você consegue advinhar qual foi?')

while tent != num:
    qtde += 1
    while True:
        try:
            tent = int(input('Qual é o seu palpite? '))
            if tent in numeros or tent < 0 or tent > 10:
                raise SyntaxError
        except KeyboardInterrupt:
            print('O usuário não quer continuar!\nEncerrando.')
            exit()
        except SyntaxError:
            print('Digite um número válido não digitado antes.')
        except:
            print('\033[1;31mOcorreu um problema.\033[m Escreva certo!')
        else:
            break
        finally:
            if tent not in numeros:
                numeros.append(tent)

    if tent < num:
        print('Mais... Tente mais uma vez.')
    elif tent > num:
        print('Menos... Tente mais uma vez.')

print(f'Acertou com {qtde} tentativa(s). Parabéns!')
