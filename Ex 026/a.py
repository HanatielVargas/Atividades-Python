frase = ' '.join(input('Digite uma frase: ').strip().lower().split())

print(f'''{frase.title()}
A letra A aparece {frase.count('a')} vezes na frase
A primeira letra A aparece na posição {frase.find('a')+1}
A últims letra A aparece na posição {frase.rfind('a')+1}
''')