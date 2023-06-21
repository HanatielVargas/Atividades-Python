'''
Criando uma função para calcular fatorial
'''

def fat(n, show=False):
    '''fat(n, show=False)
-> Calcula o fatorial de um número.
:param n: O número que será fatorado.
:param show: (opicional) Mostrar ou não a conta.
:return: O valor do fatorial do número n.'''

    result = 1

    for c in range(n, 0, -1):
        if c != 1:
            if show:
                print(c, end=' X ')
            result *= c
        elif c == 1 and show:
            print(c, end=' = ')
        
    print(result)
    return result

help(fat)
fat(5)
fat(6, True)