'''
Criando uma função para cadastrar jogadores 
'''

def jogador(nome='<Desconhecido>', gols='0'):
    if gols not in '0123456789' or gols == '':
        gols = '0'
    if nome == '':
        nome = '<Desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato!\n')


jogador(nome=str(input('Nome do Jogador: ')).strip(), gols=str(input('Número de gols: ')).strip())
