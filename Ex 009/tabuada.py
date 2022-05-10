num = int(input('Digite um número: '))

print('-'*(len(f' {num} x 10 = {num*10} ')))

for c in range(1, 11):
    print(f' {num} x {c:>2} = {num*c}')

print('-'*(len(f' {num} x 10 = {num*10} ')))