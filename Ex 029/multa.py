vel = float(input('Digite sua velocidade: '))

print('Tenha um bom dia! Dirija com segurança' if vel <= 80 else f'\033[1;31mMULTADO! Você excedeu o limite permitido que é de 80km/h \nVocê deve pagar uma multa de R${(vel-80)*7:.2f}!\033[m\nTenha um bom dia! Dirija com segurança')
