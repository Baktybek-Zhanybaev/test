while True:
    print("\n--- МЕНЮ ---")
    print("1 - Килограмманын фунтка айланышы")
    print("2 - Үч санды кошуу жана орточо маанисин табуу")
    print("3 - Чай акча (чаевые) эсептөө")
    print("4 - Фаренгейт → Цельсийге айлантуу")
    print("5 - Цельсий → Фаренгейтке айлантуу")
    print("6 - Программадан чыгуу")

    choice = input("Тандооңузду жазыңыз (1-6): ")

    if choice == "1":
        kg = float(input("Салмагыңызды килограмм менен жазыңыз: "))
        pounds = kg * 2.2
        print("Салмак фунт менен:", pounds)

    elif choice == "2":
        a = float(input("Биринчи санды жазыңыз: "))
        b = float(input("Экинчи санды жазыңыз: "))
        c = float(input("Үчүнчү санды жазыңыз: "))
        summa = a + b + c
        average = summa / 3
        print("Жыйынтык (сумма):", summa)
        print("Орточо мааниси:", average)

    elif choice == "3":
        price = float(input("Тамактын баасын жазыңыз: "))
        tip_percent = float(input("Канча пайыз чай акча калтыргыңыз келет?: "))
        tip = (price * tip_percent) / 100
        total = price + tip
        print("Чай акча суммасы:", tip)
        print("Жалпы эсеп (чай акча менен):", total)

    elif choice == "4":
        f = float(input("Температураны Фаренгейт менен жазыңыз: "))
        c = (f - 32) * 5 / 9
        print("Температура Цельсий менен:", c)

    elif choice == "5":
        c = float(input("Температураны Цельсий менен жазыңыз: "))
        f = (c * 9 / 5) + 32
        print("Температура Фаренгейт менен:", f)

    elif choice == "6":
        print("Программа аяктады. Көрүшкөнчө!")
        break

    else:
        print("Туура эмес тандоо. 1ден 6га чейинки санды тандаңыз.")

