try:
    from math import cos, radians, sin, tan
except:
    print('\033[1;31Não foi possível importar a biblioteca "MATH"!\033[m')
    quit()

while True:
    try:
        ang = float(input('Digite o ângulo que você deseja: '))
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'O ângulo de {ang} tem o SENO de:\t\t{sin(radians(ang)):.2f}')
        print(f'O ângulo de {ang} tem o COSSENO de:\t{cos(radians(ang)):.2f}')
        print(f'O ângulo de {ang} tem a TANGENTE de:\t{tan(radians(ang)):.2f}')
        break