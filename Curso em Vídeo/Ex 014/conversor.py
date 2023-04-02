while True:
    try:
        temp = float(input('Informe a temperatura em °C: '))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'A temperatura de °C {temp} corresponde a °F {(temp*9/5)+32}.')
        break
