'''
Verificar se o site pudim.com.br está funcionando
'''

from urllib.request import urlopen

while True:
    try:
        site = str(input('Digite a url completa de um site: ')).strip().lower()
    except KeyboardInterrupt:
        print('\nUsuário não quer continuar!\nEncerrando...\n')
        quit()
    except:
        print('ERRO: Por favor digite algo válido!')
    else:
        break

try:
    pudimon = urlopen(site)
except:
    print(f'\nO site "{site}" está inacessível!\n')
else:
    print(f'\nO site "{site}" está acessível!\n')
