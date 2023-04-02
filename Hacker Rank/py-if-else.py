
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0 or (6 <= n <= 20 and n % 2 == 0):
        print('Weird')
    else:
        print('Not Weird')
