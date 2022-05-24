while True:
    try:
        frase = ' '.join(input('Digite uma frase: ').strip().lower().split())
        if len(frase) == 0:
            raise KeyError
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'''{frase.title()}
A letra A aparece {frase.count('a')} vezes na frase
A primeira letra A aparece na posição {frase.find('a')+1 if frase.find('a') != -1 else 'xx'}
A última letra A aparece na posição {frase.rfind('a')+1 if frase.rfind('a') != -1 else 'xx'}
''')
        break
