'''
Criando uma Função que faz um print especial aprimorado
'''

def mostra(msg, line):
    tam = len(msg)+4
    print(line*tam)
    print(f'  {msg}')
    print(line*tam)

mostra('Hanatiel Vargas', '~')
mostra('Curso em Vídeo', '=')
mostra('CeV', '#')
