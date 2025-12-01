a = float(input("1 число:"))
b = float(input("2 число:"))
if a < b:
    aralyk = b - a
else:
    aralyk = a - b

if aralyk <= 0.001:
    print("Близко")
else:
    print("Далеко")