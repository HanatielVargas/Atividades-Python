from random import shuffle

nomes = list()

for c in range(4):
    while True:
        try:
            nome = str(input(f'{c+1}° Aluno: ')).title().strip()
            if nome == '' or not nome.isalpha():
                raise KeyboardInterrupt
        except:
            print('\033[1;31mOcorreu um erro!\033[m')
        else:
            nomes.append(nome)
            break

shuffle(nomes)
print('\nA ordem das apresentações será:')

for i, c in enumerate(nomes):
    print(f'{i+1}°  {c}')
