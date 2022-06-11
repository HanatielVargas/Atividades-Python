valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o salário do comprador? R$'))
anos = int(input('Anos de financiamento: '))
parcela = valor/(anos*12)
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${parcela:.2f}')
if parcela > sal*0.3:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo CONCEDIDO')
