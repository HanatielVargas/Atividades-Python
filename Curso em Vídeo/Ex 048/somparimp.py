qtd = 0
soma = 0

for c in range(3, 501, 3):
    if c % 2 != 0:
        qtd += 1
        soma += c

print(f'A soma de todos os {qtd} valores é {soma}')