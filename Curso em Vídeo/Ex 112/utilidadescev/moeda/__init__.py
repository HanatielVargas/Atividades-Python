'''
Parte das funções
'''


def metade(num, moeda=True):
    num = strtofloat(num)
    if moeda:
        return brl(num/2)
    else:
        return num/2


def dobro(num, moeda=True):
    num = strtofloat(num)
    if moeda:
        return brl(num*2)
    else:
        return (num*2)


def aumentar(num, percentagem, moeda=True):
    num = strtofloat(num)
    if moeda:
        return brl(num*(1+percentagem/100))
    else:
        return (num*(1+percentagem/100))


def diminuir(num, percentagem, moeda=True):
    num = strtofloat(num)
    if moeda:
        return brl(num*(1-percentagem/100))
    else:
        return (num*(1-percentagem/100))


def brl(float, moeda='R$'):
    return f'{moeda}{strtofloat(float):.2f}'.replace('.', ',')


def strtofloat(string):
    string = str(string)
    if ',' in string:
        return float(string.replace(',', '.'))
    else:
        return float(string)


def resumo(num, aum=0.0, dim=0.0):
    straum = f'{brl(aum, "")}% de Aumento:'
    strdim = f'{brl(dim, "")}% de Redução:'

    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço Analisado:":<20}{brl(num):<10}')
    print(f'{"Dobro do Preço: ":<20}{dobro(num):<10}')
    print(f'{"Metade do Preço:":<20}{metade(num):<10}')
    print(f'{straum:<20}{aumentar(num, aum):<10}')
    print(f'{strdim:<20}{diminuir(num, dim):<10}')
    print('-'*30)
    print()
