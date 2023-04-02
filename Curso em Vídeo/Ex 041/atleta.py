try:
    from datetime import date
    ano = date.today().year
except: 
    print('Erro ao importar biblioteca')
    while True:
        try:
            ano = int(input('Ano atual: '))
        except Exception:
            print('\033[1;31mOcorreu um erro!\033[m')
        except KeyboardInterrupt:
            print('Usuário não quer continuar')
            quit()
        else:
            break

while True:
    try:
        nasc = int(input('Ano de nascimento: '))
        idade = ano - nasc
        if idade < 0:
            raise ZeroDivisionError
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        quit()
    else:
        break

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
