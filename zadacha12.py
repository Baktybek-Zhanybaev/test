
height = int(input("Буква Анын бийиктигин киргизиңиз: "))

for i in range(height):
    for j in range(height - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        if i == 0 or i == height // 2 or j == 0 or j == 2 * i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

    # Колдонуучудан сан сурайбыз
    n = int(input("Сан жазыңыз: "))

    # Факториалды эсептөө
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Натыйжаны чыгарыбыз
    print(f"{n}! =", factorial)
