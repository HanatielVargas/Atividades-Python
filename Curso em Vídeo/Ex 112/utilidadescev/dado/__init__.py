'''
Parte das funções
'''

def leiaDinheiro(msg):
    valido = True
    while True:
        strpreco = str(input(msg)).strip()
        for c in strpreco:
            if c not in '0123456789,.':
                valido = False
        if valido:
            break
        else:
            print(f'(ERRO) "{strpreco}" é um preço inválido!')
    return strpreco
