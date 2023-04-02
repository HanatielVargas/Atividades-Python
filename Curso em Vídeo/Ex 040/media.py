while True:
    try:
        nota1 = float(input('Primeira nota: '))
        if nota1 > 10 or nota1 < 0:
            raise Exception
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        quit()
    else:
        break

while True:
    try:
        nota2 = float(input('Segunda nota: '))
        if nota2 > 10 or nota2 < 0:
            raise Exception
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        quit()
    else:
        break

media = (nota1+nota2)/2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')
print('O aluno está ', end='')

if media >= 7:
    print('Aprovado!')
elif media >= 5:
    print('em Recuperação')
else:
    print('Reprovado')
