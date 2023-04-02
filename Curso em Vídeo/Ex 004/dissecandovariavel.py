while True:
    try:
        teste = input('Digite algo: ')
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'O tipo primitivo desse valor é {type(teste)}')
        print('Só tem espaços?', True if teste.isspace() else False) 
        print('É um número?', True if teste.isnumeric() else False) 
        print('É alfabético?', True if teste.isalpha() else False)
        print('É alfanúmerico?', True if teste.isalnum() else False) 
        print('Está em maiúsculas?', True if teste.isupper() else False)
        print('Está em minúsculas?', True if teste.islower() else False) 
        print('Está capitalizada?', True if teste.istitle() else False)
        break
