word = str(input('Digite uma palavra: ')).strip().lower()

if word == word[-1::-1]:
    print('É um Palíndromo')
else:
    print('Não é um Palíndromo')