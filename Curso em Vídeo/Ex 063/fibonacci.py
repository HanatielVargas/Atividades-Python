'''
Sequência fibonacci
'''

linha = '-'*40
onda = '~'*40

print(linha + '\n\t Sequência de Fibonacci\n' + linha)

while True:
    try:
        ter = int(input(' Quantos termos você quer mostrar? '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar.\nEncerrando...')
        exit()
    except:
        print('\033[1;31m Ocorreu um erro. Tente algo válido.\033[m')
    else:
        break

print(onda)

antigo = 0
atual = 0
novo = 0

for c in range(ter):
    print(f' {atual} ->', end='')
    if atual == 0:
        atual += 1
    else:
        novo = atual
        atual = atual + antigo    
    antigo = novo

print(' FIM\n' + onda + '\n')
