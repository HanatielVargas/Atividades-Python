'''
Criando uma Função que faz uma contagem
'''


from time import sleep


def conta(ini=1, fim=10, pas=1):
    print('=-'*20)
    print(f'Contagem de {ini} até {fim} de {pas} em {pas}.')
    if pas < 0:
        pas *= -1
    atual = ini
    while True:
        print(atual, end=' ', flush=True)
        sleep(0.5)
        if ini > fim:
            atual -= pas
            if atual < fim:
                break
        if fim > ini:
            atual += pas
            if atual > fim:
                break
        if ini == fim:
            break
    print('Fim!')


conta()
conta(10, 0, 2)

print('=-'*20)
print('Agora é sua vez de personalizar a contagem!')

while True:
    try:
        inicio = int(input('Início: '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...')
        quit()
    except:
        print('Você digitou algo errado!')
    else:
        break
while True:
    try:
        final =  int(input('Final: '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...')
        quit()
    except:
        print('Você digitou algo errado!')
    else:
        break

while True:
    try:
        passo = int(input('Passo: '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...')
        quit()
    except:
        print('Você digitou algo errado!')
    else:
        break

conta(inicio , final, passo)
