num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

while num1 < num2:
    print(f'Биздин биринчи сан => {num1}')
    print(f'{num1} < {num2}')
    num1 = num1 + 10


print(num1)
print('FINISHED')
