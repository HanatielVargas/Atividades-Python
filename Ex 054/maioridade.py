from datetime import datetime

year = datetime.today().year

less18 = list()
more18 = list()

for c in range(7):
    birth = int(input(f'Digite o ano de nascimento da {c+1} pessoa: '))

    age = year-birth

    if age >= 18:
        more18.append(age)
    else:
        less18.append(age)
    
print(f'Ao todo tivemos {len(more18)} maiores de idade')
print(f'E também tivemos {len(less18)} menores de idade')
