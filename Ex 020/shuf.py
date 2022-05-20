from random import shuffle

nomes = list((input('Primeiro aluno: ').title(), input('Segundo aluno: ').title(), input('Terceiro aluno: ').title(), input('Quarto aluno: ').title()))
shuffle(nomes)
print(f'A ordem de apresentação será: \n{nomes}')
