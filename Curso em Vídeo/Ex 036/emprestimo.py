while True:
    try:
        valor = float(input('Qual o valor da casa? R$'))
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        exit()
    else:
        break

while True:
    try:
        sal = float(input('Qual o salário do comprador? R$'))
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        exit()
    else:
        break

while True:
    try:
        anos = int(input('Anos de financiamento: '))
        if anos == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print('Impossivel ser 0 anos')
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        exit()
    else:
        break


parcela = valor/(anos*12)
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${parcela:.2f}')
if parcela > sal*0.3:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo CONCEDIDO')
