'''
Analisador de um grupo de pessoas
'''

dados = {}
maisvelho = 0
numvelho = 0
mul20 = 0

for c in range(4):
    pessoa = f'{c+1}ª Pessoa'
    print(f'{pessoa:-^20}')
    while True:
        try:
            nome = str(input('Nome: ')).capitalize().strip()
            if nome.isalnum() and not nome.isalpha() or nome == '':
                raise TypeError
        except TypeError:
            print('\033[1;31mAlgo deu errado.\033[m Escreva certo!')
        except KeyboardInterrupt:
            print('Usuário não quer continuar!\nEncerrando...')
            quit()
        except:
            print('\033[1;31mAlgo deu errado.\033[m Escreva certo!')
        else:
            break
    
    while True:
        try:
            idade = int(input('Idade: '))
        except KeyboardInterrupt:
            print('Usuário não quer continuar!\nEncerrando...')
            quit()
        except:
            print('\033[1;31mAlgo deu errado.\033[m Escreva certo!')
        else:
            break
    
    while True:
        try:
            sexo = str(input('Sexo [M/F]: '))[0].upper()
            if sexo.isalnum() and not sexo.isalpha() or sexo == '' or not sexo in 'mfFM':
                raise TypeError
        except KeyboardInterrupt:
            print('Usuário não quer continuar!\nEncerrando...')
            quit()
        except TypeError:
            print('\033[1;31mAlgo deu errado.\033[m Escreva certo!')
        except:
            print('\033[1;31mAlgo deu errado.\033[m Escreva certo!')
        else:
            break
    
    dadopess = {'Nome': nome, 'Idade': idade, 'Sexo': sexo}

    dados.update({c:dadopess})

    if sexo == 'F' and idade < 20:
        mul20 += 1

    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        numvelho = c


print("-"*20)
print(f'A média de Idade do grupo é de {(dados[0]["Idade"]+dados[1]["Idade"]+dados[2]["Idade"]+dados[3]["Idade"])/4}.')
print(f'O homem mais velho tem {dados[numvelho]["Idade"]} anos e se chama {dados[numvelho]["Nome"]}.')
print(f'Ao todo são {mul20} mulheres com menos de 20 anos.')
