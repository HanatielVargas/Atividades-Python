'''
Verificar se o site pudim.com.br está funcionando
'''

from urllib.request import urlopen

try:
    pudimon = urlopen('pudim.com.br')
except:
    print('\nO site "pudim.com.br" está inacessível!\n')
else:
    print('\nO site "pudim.com.br" está acessível!\n')
