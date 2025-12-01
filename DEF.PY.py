def koshuu():
    a = float(input("Биринчи сан: "))
    b = float(input("Экинчи сан: "))
    print("Жыйынтык:", a + b)

def kemituu():
    a = float(input("Биринчи сан: "))
    b = float(input("Экинчи сан: "))
    print("Жыйынтык:", a - b)

def koboytuu():
    a = float(input("Биринчи сан: "))
    b = float(input("Экинчи сан: "))
    print("Жыйынтык:", a * b)

def boluu():
    a = float(input("Биринчи сан: "))
    b = float(input("Экинчи сан: "))
    if b == 0:
        print("Нөлгө бөлүүгө болбойт!")
    else:
        print("Жыйынтык:", a / b)

print("1 — Кошуу")
print("2 — Кемитүү")
print("3 — Көбөйтүү")
print("4 — Бөлүү")

x = input("Танда (1-4): ")

if x == "1":
    koshuu()
elif x == "2":
    kemituu()
elif x == "3":
    koboytuu()
elif x == "4":
    boluu()
else:
    print("Туура эмес тандоо!")