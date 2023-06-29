'''
Parte das funções
'''


def metade(num):
    return (num/2)


def dobro(num):
    return (num*2)


def aumentar(num, percentagem):
    return (num*(1+percentagem/100))


def diminuir(num, percentagem):
    return (num*(1-percentagem/100))


def brl(float):
    string = str(float)
    new = 'R$'
    for c in string:
        if c in '012345679':
            new += c
        elif c == '.':
            new += ','
            break
    vir = string[string.index('.')+1:string.index('.')+3]
    if len(vir) == 1:
        new += vir + '0'
    else:
        new += vir
    return new

