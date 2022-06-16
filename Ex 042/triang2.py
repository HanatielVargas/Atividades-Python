reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:

    if reta1 == reta2 == reta3:
        print('Equilátero')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Isósceles')
    elif reta1 != reta2 != reta3:
        print('Escaleno')
 