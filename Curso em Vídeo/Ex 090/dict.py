'''
Usando dicionário para guardar nome, média e situação de um aluno
'''

aluno = dict()

nome = str(input('Nome: ')).strip()
aluno.update({'Nome': nome})
media = float(input(f'Média de {nome}: '))
aluno.update({'Média': media})
sit = str()
if media >= 7:
     sit = 'Aprovado'
elif media >= 5:
     sit = 'Recuperação'
else:
     sit = 'Reprovado'
    
aluno.update({'Situação': sit})

print('=-'*20)

print(f'\t- Nome é igual a {aluno["Nome"]}')
print(f'\t- Média é igual a {aluno["Média"]}')
print(f'\t- Situação é igual a {aluno["Situação"]}\n')
