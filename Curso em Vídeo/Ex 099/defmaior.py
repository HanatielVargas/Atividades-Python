'''
Criando uma função que recebe vários valores e mostra o maior entre eles
'''

def maior(* num):
    print('=-'*25)
    print('Analisando os valores passados...')
    for c in num:
        print(c, end=' ')
    print(f'Foram informados {len(num)} números ao todo')
    print('O maior número informado foi', end=' ')
    print(f'{max(num)}.') if len(num) != 0 else print('0.')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
