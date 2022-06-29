pares = list()

for c in range(6):
    num = int(input(f'Digite o {c+1}º número: '))
    if num % 2 == 0:
        pares.append(num)

print(f'Você informou {len(pares)} número(s) par(es) e soma dele(s) é {sum(pares)}')
