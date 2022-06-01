ano = input('Digite um ano: ').strip()
intano = int(ano)

if intano % 4 == 0 and intano % 100 != 0 or intano % 400 == 0:
    print(True)
else:
    print(False)
