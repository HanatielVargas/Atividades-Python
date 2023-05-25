# Criando um validador de expressões aritméticas, analisando se a ordem e a quantidade dos parenteses está correta.

while True:
    try:
        exp = str(input('Digite sua expressão: ')).strip()
        if exp == '':
            raise TypeError
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...')
        quit()
    except:
        print('Você digitou algo errado. Por favor escreva certo')
    else:
        break

aberto = 0
certo = 'correta!'

for c in exp:
    if c == '(':
        aberto += 1
    if c == ')':
        aberto -= 1
    if aberto == -1:
        certo = 'errada!'
    
if certo == 'correta!' and aberto != 0:
    certo = 'errada!'

print(f'Sua expressão está {certo}\n')
