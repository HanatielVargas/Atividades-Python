nums = list()

while True:
    try:
        num1 = int(input('Primeiro valor: '))
        nums.append(num1)
    except Exception:
        print('\033[1;31mOcorreu um erro!\033[m')
    except KeyboardInterrupt:
        print('\033[1;31mUsuário não quis continuar!\033[m')
        quit()
    else:
        while True:
            try:
                num2 = int(input('Segundo valor: '))
                nums.append(num2)
            except Exception:
                print('\033[1;31mOcorreu um erro!\033[m')
            except KeyboardInterrupt:
                print('\033[1;31mUsuário não quis continuar!\033[m')
                quit()
            else:
                while True:
                    try:
                        num3 = int(input('Terceiro valor: '))
                        nums.append(num3)
                    except Exception:
                        print('\033[1;31mOcorreu um erro!\033[m')
                    except KeyboardInterrupt:
                        print('\033[1;31mUsuário não quis continuar!\033[m')
                        quit()
                    else:
                        break
                break
        break

print(f'O menor valor digitado foi {min(nums)}')
print(f'O maior número digitado foi {max(nums)}')
