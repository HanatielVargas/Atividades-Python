'''
Sequência fibonacci
'''

linha = '-'*40
onda = '~'*40

print(linha + '\n\t Sequência de Fibonacci\n' + linha)

ter = int(input(' Quantos termos você quer mostrar? '))

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
