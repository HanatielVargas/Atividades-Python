pares = list()

for c in range(6):
    while True:
        try:
            num = int(input(f'Digite o {c+1}º número: '))
        except Exception:
            print('\033[1;31mOcorreu um erro!\033[m')
        except KeyboardInterrupt:
            print('Usuário não quer continuar')
            quit()
        else:
            break
    if num % 2 == 0:
        pares.append(num)

print(f'Você informou {len(pares)} número(s) par(es) e soma dele(s) é {sum(pares)}')
