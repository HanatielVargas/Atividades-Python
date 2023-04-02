while True:
    try:
        word = ''.join(str(input('Digite uma frase: ')).strip().lower().split())
        if word == '':
            raise Exception
    except Exception:
        print('Ocorreu um erro!')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        exit()
    else:
        break

print(f'O inverso de {word} é {word[-1::-1]}')

if word == word[-1::-1]:
    print('É um Palíndromo')
else:
    print('Não é um Palíndromo')