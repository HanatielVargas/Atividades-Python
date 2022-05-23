cidade = input('Digite o nome da cidade: ').strip()

print(True if cidade.split()[0].lower() == 'santo' else False)