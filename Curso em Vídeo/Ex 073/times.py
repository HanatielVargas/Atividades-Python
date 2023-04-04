'''
Aprendendo tuplas com o brasileirão
'''

times22 = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')

LINHA = '-='*30

print(f'{LINHA} \nLista dos times do Brasileirão: {times22}')
print(f'{LINHA} \nOs 5 primeiros são {times22[0:5]}')
print(f'{LINHA} \nOs 4 últimos são {times22[-4:]}')
print(f'{LINHA} \nTimes em ordem alfabética: {sorted(times22)}')
print(f'{LINHA} \nO São Paulo está na posção: {times22.index("São Paulo")+1}\n')
