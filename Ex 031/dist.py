while True:
    try:
        dist = float(input('Qual a distância da viagem em km? '))
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        break
    else:
        if dist <= 200:
            valorpkm = 0.5
        else: 
            valorpkm = 0.45
        print(f'Você está prestes a começar um viagem de {dist:.2f}km')
        print(f'E o preço da passagem custará R${dist*valorpkm}')
        break
