
pos_x = int(input())
pos_y = int(input())

for i in range(8):
    for j in range(8):
        if i  == pos_x and j == pos_y:
            print('K', end=' ')
        elif (abs(i - pos_x) == 2 and abs(j - pos_y) == 1) or (abs(i - pos_x) == 1 and abs(j - pos_y) == 2):
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()

