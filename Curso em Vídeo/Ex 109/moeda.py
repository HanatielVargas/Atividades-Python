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

