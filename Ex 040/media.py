nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1+nota2)/2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')
print('O aluno está ', end='')

if media >= 7:
    print('Aprovado!')
elif media >= 5:
    print('em Recuperação')
else:
    print('Reprovado')
