while True:
    try:
        cidade = input('Digite o nome da cidade: ').strip()
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(True if cidade.split()[0].lower() == 'santo' else False)
        break
