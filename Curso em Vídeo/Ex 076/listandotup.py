'''
Usando tuplas para listar coisas
'''

tupla = ('Lápis',       1.75,
         'Borracha',    2.00,
         'Caderno',    15.90,
         'Estojo',     25.00,
         'Tranferidor', 4.20,
         'Compasso',    9.99,
         'Mochila',   120.32,
         'Canetas',    22.30,
         'Livro',      34.90)

print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)

precos_formatados = [f' {tupla[c]:.<39}R$ {tupla[c+1]:>6.2f}' for c in range(len(tupla)) if c % 2 == 0]
print('\n'.join(precos_formatados))
print('-'*50)
