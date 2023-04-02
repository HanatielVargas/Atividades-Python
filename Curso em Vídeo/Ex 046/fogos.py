try:
    from time import sleep
except ImportError:
    print('Erro ao importar módulo necessário para funcionamento do programa.')
    quit()

for c in range(10, -1, -1):
    sleep(1)
    print(c)

print('\n\nBUM! BUM! POOOW!')
