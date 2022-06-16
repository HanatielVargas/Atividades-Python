from datetime import date
ano = date.today().year

nasc = int(input('Ano de nascimento: '))
idade = ano - nasc

print(f'O atleta tem {idade} anos')
print('Classificação: ', end='')

if idade < 10:
    print('Mirim')
elif idade < 15:
    print('Infantil')
elif idade < 20:
    print('Junior')
elif idade < 26:
    print('Senior')
else:
    print('Master')
