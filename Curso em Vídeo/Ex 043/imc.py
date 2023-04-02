while True:
    try:
        kg = float(input('Sua massa corporal: (KG) '))
        if kg <= 0:
            raise ZeroDivisionError
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        quit()
    else:
        break

while True:
    try:
        tam = float(input('Sua Altura: (M) '))
        imc = kg/tam**2
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        quit()
    else:
        break

print(f'O IMC dessa pessoa é {imc:.2f}')
print('Essa pessoa está ', end='')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('com o Peso ideal')
elif imc < 30:
    print('em Sobrepeso')
elif imc < 40:
    print('com Obesidade')
else:
    print('com Obesidade Mórbida')
