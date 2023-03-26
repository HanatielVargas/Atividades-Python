'''
Selecionar o maio e o menor número de uma sequência
'''

pessoas = list()

for c in range(5):
    peso = float(input(f'Peso da {c+1}ª Pessoa: '))
    pessoas.append(peso)

pessoas.sort()

print(f'O maior peso lido foi de {pessoas[-1]}Kg')
print(f'O menor peso lido foi de {pessoas[0]}Kg ')
