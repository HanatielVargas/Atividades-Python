from datetime import date
ano = date.today().year

idade_alistar = 18
nasc = int(input('Ano de Nascimento: '))
print(f'Quem nasceu em {nasc} tem {ano-nasc} anos em {ano}')

if nasc + idade_alistar < ano:
    print(f'Você já deveria ter se alistado há {ano-(nasc+idade_alistar)} anos')
    print(f'Você se alistou em {nasc+18}')
elif nasc + idade_alistar == ano:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print(f'Ainda faltam {nasc+idade_alistar-ano} anos para o seu alistamento')
    print(f'Seu alistamento será em {nasc+idade_alistar}')
