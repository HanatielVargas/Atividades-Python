'''
Analisando e Gerando Resultados
'''


def notas(*nums, sit=False):
    """-> Função para analisar notas e situações de vários alunos.
:param n: uma ou mais notas dos alunos (aceita várias)
:param sit: valor opicional, indicando se deve ou não adicionar a situação
:return: dicionário com várias informações sobre a situação da turma.
"""
    lista = (nums)
    dicio = dict()
    dicio['Total'] = len(lista)
    dicio['Maior'] = max(lista)
    dicio['Menor'] = min(lista)
    dicio['Média'] = sum(lista)/len(lista) # type: ignore
    if sit:
        if dicio['Média'] >= 7:
            dicio['Situação'] = 'Aprovado'
        elif dicio['Média'] >= 6:
            dicio['Situação'] = 'Recuperação'
        else:
            dicio['Situação'] = 'Reprovado'
    
    return dicio


resp = notas(5.9, sit=True)
print(resp)
help(notas)
