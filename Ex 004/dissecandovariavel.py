while True:
    try:
        teste = input('Digite algo: ')
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'O tipo primitivo desse valor é {type(teste)}', '\nSó tem espaços?', True if teste.isspace() else False, '\nÉ um número?', True if teste.isnumeric() else False, '\nÉ alfabético?', True if teste.isalpha() else False, '\nÉ alfanúmerico?', True if teste.isalnum() else False, '\nEstá em maiúsculas?', True if teste.isupper() else False, '\nEstá em minúsculas?', True if teste.islower() else False, '\nEstá capitalizada?', True if teste.istitle() else False)
        break
