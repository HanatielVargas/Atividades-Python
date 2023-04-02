while True:
    try:
        d = float(input('Uma distância em metros: '))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'A medida de {d} metros corresponde à: \n{d/1000}km \n{d/100}hm \n{d/10}dam \n{d*10}dm \n{d*100}cm \n{d*1000}mm')
        break
