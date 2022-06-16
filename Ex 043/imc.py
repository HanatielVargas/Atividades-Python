kg = float(input('Sua massa corporal: (KG) '))
tam = float(input('Sua Altura: (M) '))

imc = kg/tam**2

print(f'O IMC dessa pessoa é {imc:.2f}')
print('Essa pessoa está em estado de ', end='')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
