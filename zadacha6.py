a = float(input("Биринчи санды жазыңыз: "))
b = float(input("Экинчи санды жазыңыз: "))

summa = a + b

if summa > 100:
    print("Бул сан 100дөн чоң!")
else:
    print("бул сан 100дон чон эмес ")

a = float(input("Биринчи санды жазыңыз: "))
b = float(input("Экинчи санды жазыңыз: "))

if a > b:
    print("Биринчи сан экинчисинен чоң!")

a = float(input("Биринчи санды жазыңыз: "))
b = float(input("Экинчи санды жазыңыз: "))

if a > b:
    print("Биринчи сан экинчисинен чоң!")
else:
    print("Экинчи сан биринчисинен чоң!")

cm = float(input("Узундукту сантиметр менен жазыңыз: "))

if cm < 0:
    print("Мындай сан жараксыз!")
else:
    inch = cm / 2.54
    print("Узундук дюйм менен:", inch)

temp = float(input("Температураны жазыңыз: "))
unit = input("Бул Цельсийби же Фаренгейтпи? (C/F): ")

if unit.upper() == "C":
    f = (9/5) * temp + 32
    print("Бул", f, "градус Фаренгейт.")
elif unit.upper() == "F":
    c = (5/9) * (temp - 32)
    print("Бул", c, "градус Цельсий.")
else:
    print("Туура эмес бирдик! 'C' же 'F' жазыңыз.")

temp = float(input("Температураны Цельсий менен жазыңыз: "))

if temp < 0:
    print("Абдан суук!")
elif temp < 10:
    print("Салкын аба.")
elif temp < 25:
    print("Жагымдуу аба.")
elif temp < 35:
    print("Жылуу аба.")
else:
    print("Абдан ысык!")
