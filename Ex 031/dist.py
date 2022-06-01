dist = float(input('Qual a distância da viagem em km? '))

if dist <= 200:
    valorpkm = 0.5
else: 
    valorpkm = 0.45
print(f'Você está prestes a começar um viagem de {dist:.2f}km')
print(f'E o preço da passagem custará R${dist*valorpkm}')