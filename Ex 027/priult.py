nome = ' '.join(input('Digite seu nome completo: ').strip().title().split())

print(f'''Prazer em te conhecer!
Seu primeiro nome é {nome.split()[0]}
Seu último nome é {nome.split()[-1]}
''')
