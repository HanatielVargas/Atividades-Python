'''
Criando uma função para votação
'''

def vota(nasc):
    from datetime import datetime

    idade = datetime.now().year - nasc
    if idade < 0:
        print('Idade menor que 0.')
        return 0
    print(f'Com {idade} anos: ', end='')
    if idade >= 65 or 16 <= idade < 18:
        print('Voto OPICIONAL')
    elif 18 <= idade < 65:
        print('Voto OBRIGATÓRIO')
    else:
        print('NÃO VOTA!')
    
    return 1


while True:
    try:
        print('=-'*20)
        nascimento = int(input('Em que ano você nasceu? '))
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('Você digitou algo errado.')
    else:
        vot = vota(nascimento)
        if vot == 1:
            print()
            break
