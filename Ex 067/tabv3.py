'''
tabuada versâo 3
'''


while True:
    print('-'*40)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*40)

    if num < 0:
        break

    for c in range(10):
        print(f'{num} X {c+1:>2} = {num*(c+1)}')

print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre...')
