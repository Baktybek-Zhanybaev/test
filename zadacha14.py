n = 8
x = 0
y = 0

for i in range(n):
    for j in range(n):
        if i == x and j == y:
            print('L', end=' ')
        elif abs(i - x) == abs(j - y):   # Диагональ шарт
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()
