'''
Parte das funções
'''


def metade(num, moeda=True):
    if moeda:
        return brl(num/2)
    else:
        return num/2


def dobro(num, moeda=True):
    if moeda:
        return brl(num*2)
    else:
        return (num*2)


def aumentar(num, percentagem, moeda=True):
    if moeda:
        return brl(num*(1+percentagem/100))
    else:
        return (num*(1+percentagem/100))


def diminuir(num, percentagem, moeda=True):
    if moeda:
        return brl(num*(1-percentagem/100))
    else:
        return (num*(1-percentagem/100))


def brl(float, moeda='R$'):
    return f'{moeda}{float:.2f}'.replace('.', ',')


def resumo(num, aum=0.0, dim=0.0):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço Analisado:":<20}{brl(num):<10}')
    print(f'{"Dobro do Preço: ":<20}{dobro(num):<10}')
    print(f'{"Metade do Preço:":<20}{metade(num):<10}')
    print(f'{f"{aum}% de Aumento:":<20}{aumentar(num, aum):<10}')
    print(f'{f"{dim}% de Redução:":<20}{diminuir(num, dim):<10}')
    print('-'*30)
    print()
