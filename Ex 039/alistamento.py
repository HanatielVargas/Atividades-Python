try:
    from datetime import date
    ano = date.today().year
except:
    print('\033[1;31mOcorreu um erro!\033[m')
    ano = int(input('Digite o ano atual: '))

idade_alistar = 18

while True:
    try:
        nasc = int(input('Ano de Nascimento: '))
    except Exception:
        print('\033[1;31mOcorreu um erro\033[m')
    except KeyboardInterrupt:
        print('Usuário não quer continuar')
        quit()
    else:
        break

print(f'Quem nasceu em {nasc} tem {ano-nasc} anos em {ano}')

if nasc + idade_alistar < ano:
    print(f'Você já deveria ter se alistado há {ano-(nasc+idade_alistar)} anos')
    print(f'Você se alistou em {nasc+18}')
elif nasc + idade_alistar == ano:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print(f'Ainda faltam {nasc+idade_alistar-ano} anos para o seu alistamento')
    print(f'Seu alistamento será em {nasc+idade_alistar}')
