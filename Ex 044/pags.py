valor = float(input('Valor das compras: R$'))
pagam = int(input('''FORMAS DE PAGAMENTOS
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Qual é a opção? '''))

match pagam:
    case 1: #10% de desconto
        print(f'Sua compra de R${valor:.2f} no final vai custar R${valor*0.9:.2f}')
    case 2: #5% de desconto
        print(f'Sua compra de R${valor:.2f} no final vai custar R${valor*0.95:.2f}')
    case 3: #Preço normal
        print(f'Sua compra de R${valor:.2f} no final vai custar R${valor:.2f}')
    case 4: #20% de juros
        parce = int(input('Quantas parcelas? '))
        print(f'Sua compra será parcelada em {parce}x de R${valor/12*1.2:.2f} cada')
        print(f'Sua compra de R${valor:.2f} no final vai custar R${valor*1.2:.2f}')
    case _: #default
        print('Você digitou algo errado!')
