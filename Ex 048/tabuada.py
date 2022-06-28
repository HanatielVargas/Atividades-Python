num = int(input('Digite um número para ver sua tabuada: '))

for c in range(10):
    print(f'{num} X {c+1:>2} = {num*(c+1)}')
