'''
Usando dicionário para guardar nome, média e situação de um aluno
'''

aluno = dict()

while True:
    try:
        nome = str(input('Nome: ')).strip()
        if nome == '' or nome.isalnum() and not nome.isalpha():
            raise TypeError
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar! Encerrando...\n')
        exit()
    except:
        print('Você digitou algo errado.')
    else:
        aluno.update({'Nome': nome})
        break

while True:
    try:
        media = float(input(f'Média de {nome}: '))
        if 0 > media or media > 10:
            raise TypeError
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar! Encerrando...\n')
        exit()
    except:
        print('Você digitou algo errado.')
    else:
        aluno.update({'Média': media})
        break

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
