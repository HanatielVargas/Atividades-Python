sal = float(input('Digite o salário: R$'))

if sal > 1250:
    novo_sal = sal * 1.1
else:
    novo_sal = sal * 1.15

print(f'Quem ganhava R${sal:.2f} passa a ganhar R${novo_sal:.2f} agora.')
