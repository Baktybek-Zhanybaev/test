import random

for i in range(50):
    print(random.randint(3, 6), end=' ')
print()

number = random.randint(1, 10)
guess = int(input("Угадайте число от 1 до 10: "))
if guess == number:
    print("Правильно! 🎯")
else:
    print(f"Неправильно 😅. Правильное число было {number}.")
print()


x = random.randint(1, 50)
y = random.randint(2, 5)
print(f"{x}^{y} = {x ** y}")
print()

for i in range(1, 51):
    print(random.randint(1, i + 1), end=' ')
print()