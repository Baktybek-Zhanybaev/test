kg = float(input("Введите вес в килограммах: "))
pounds = kg * 2.2
print("Вес в фунтах:", pounds)

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

summa = a + b + c
average = summa / 3

print("Сумма:", summa)
print("Среднее:", average)

price = float(input("Введите цену еды: "))
tip_percent = float(input("Введите процент чаевых: "))

tip = (price * tip_percent) / 100
total = price + tip

print("Сумма чаевых:", tip)
print("Общий счёт с чаевыми:", total)

f = float(input("Введите температуру в Фаренгейтах: "))
c = (f - 32) * 5 / 9
print("Температура в Цельсиях:", c)

c = float(input("Введите температуру в Цельсиях: "))
f = (c * 9 / 5) + 32
print("Температура в Фаренгейтах:", f)

