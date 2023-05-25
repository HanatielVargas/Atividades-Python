# Criando um validador de expressões aritméticas, analisando se a ordem e a quantidade dos parenteses está correta.

exp = str(input('Digite sua expressão: ')).strip()

aberto = 0
certo = True

for c in exp:
    if c == '(':
        aberto += 1
    if c == ')':
        aberto -= 1
    if aberto == -1:
        certo = False
    
if certo and aberto != 0:
    certo = False

print(exp, certo, aberto)