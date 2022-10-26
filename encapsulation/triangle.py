n = int(input())

for i in range(0, n + 1):
    symbol = ''
    for _ in range(1, n + 1 - i):
        print(" ", end='')
    if i % 2 != 0:
        symbol = '#'
    else:
        symbol = '$'

    for j in range(0, i):
        print(f'{symbol}', end=' ')

    print()
