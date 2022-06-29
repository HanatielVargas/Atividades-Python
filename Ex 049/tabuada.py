while True:
    try:
        num = int(input('Digite um número para ver sua tabuada: '))
    except Exception:
        print('Ocorreu um Erro')
    except KeyboardInterrupt:
        print('Usuário não quer mais continuar')
        quit()
    else:
        for c in range(10):
            print(f'{num} X {c+1:>2} = {num*(c+1)}')
        break
