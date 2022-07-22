try:
    from datetime import datetime
except ImportError:
    print('Erro ao capturar informações do ano atual')
    while True:
        try:
            year = int(input('Digite o ano atual: '))
        except Exception:
            print('Ocorreu um erro')
        except KeyboardInterrupt:
            print('Usuário não quer continuar')
            exit()
        else:
            break
else:
    year = datetime.today().year

less18 = list()
more18 = list()

for c in range(7):
    while True:
        try:
            birth = int(input(f'Digite o ano de nascimento da {c+1} pessoa: '))
            if year < birth:
                raise Exception
        except Exception:
            print('Ocorreu um erro')
        except KeyboardInterrupt:
            print('Usuário não quer continuar')
            exit()
        else:
            break

    age = year-birth

    if age >= 18:
        more18.append(age)
    else:
        less18.append(age)
    
print(f'Ao todo tivemos {len(more18)} maiores de idade')
print(f'E também tivemos {len(less18)} menores de idade')
