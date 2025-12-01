import time

hp = 100
level = 1
game_over = False

print("Оюнга кош келдиң!")
print("Баштапкы HP:", hp)
print("Баштапкы Level:", level)
print("--------------------------")

while not game_over:
    if hp <= 0:
        print("HP түгөндү!  Оюн утулду.")
        break
    # LEVEL 1
    if level == 1:
        print("\n LEVEL 1: Башталыш")
        time.sleep(0.5)
        print("Алдыңда 3 жол бар:")
        time.sleep(0.5)
        print("1 - Солго ")
        time.sleep(0.5)
        print("2 - Түз ")
        time.sleep(0.5)
        print("3 - Оңго ")
        time.sleep(1)
        choice = input("Тандооңду жаз (1,2,3): ") #choice-тандоо

        if choice == "1":
            print("Суудан өттүң, суу муздак экен...")
            time.sleep(0.5)
            hp -= 20
            print("HP -20. Азыркы HP:", hp)
            time.sleep(0.5)
            level = 2

        elif choice == "2":
            print("Түз жол менен кеттиң. Арстан чыкты! ")
            time.sleep(0.5)
            print("1 ")
            time.sleep(0.5)
            print("2 ")
            time.sleep(0.5)
            sub = input("1 же 2 танда: ")
            if sub == "1":
                print("Арстанды атып өлтүрдүң!")
                time.sleep(0.5)
                print("Level 2ге өттүң.")
                time.sleep(0.5)
                level = 2
            elif sub == "2":
                print("Арстандан качтын!")
                time.sleep(0.5)
                hp -= 60
                print("HP -50. Азыркы HP:", hp)
                time.sleep(0.5)
                level = 2
            else:
                print("Туура эмес тандоо. Арстан сени жеп койду ")
                time.sleep(0.5)
                game_over = True

        elif choice == "3":
            print("Оң жактагы жол менен өттүң. Жолуң ачык экен.")
            time.sleep(0.5)
            print("Дароо Level 2ге өттүң.")
            time.sleep(0.5)
            level = 2
        else:
            print("1, 2 же 3 ")
            time.sleep(0.5)

    # LEVEL 2
    elif level == 2:
        print("\n LEVEL 2: Жаңы тандоолор")
        print("1 - жол")
        print("2 - жол")
        print("3 - жол")
        time.sleep(1)
        choice = input("Тандооңду жаз (1,2,3): ")

        if choice == "1":
            print("Жөн эле басып барасың -20 ХП кетет")
            time.sleep(0.5)
            hp -= 20
            print("HP -20. Азыркы HP:", hp)
            time.sleep(0.5)

        elif choice == "2":
            print("Ийгиликтүү жолду таптың!")
            time.sleep(0.5)
            print("Level 3ке өттүң.")
            time.sleep(0.5)
            level = 3

        elif choice == "3":
            print("Айланып узун жол менен өттүң...")
            time.sleep(0.5)
            hp -= 30
            print("HP -30. Азыркы HP:", hp)
            time.sleep(0.5)
            print("Кайра эле Level 2нин башына келип калдың.")
            time.sleep(0.5)

        else:
            print("1, 2 же 3 гана тер!")
            time.sleep(0.5)

    # LEVEL 3
    elif level == 3:
        print("\nLEVEL 3: Согуш Жолу")
        time.sleep(0.5)
        print("Душман тосуп турат!")
        time.sleep(0.5)
        print("1 - Чабуул")
        time.sleep(0.5)
        print("2 - Коргонуу")
        time.sleep(0.5)
        print("3 - Качуу")
        time.sleep(0.5)
        choice = input("Тандооңду жаз (1,2,3): ")

        if choice == "1":
            print("Чабуул кылдың! Душманды жеңдиң! ")
            time.sleep(0.5)
            hp -= 25
            print("HP -25. Азыркы HP:", hp)
            time.sleep(0.5)
            print("Level 4ке өттүң.")
            time.sleep(0.5)
            level = 4

        elif choice == "2":
            print("Коргонуп калдың, бирок бир аз жаракат алдың.")
            time.sleep(0.5)
            hp -= 15
            print("HP -10. Азыркы HP:", hp)
            time.sleep(0.5)
            print("Level 4ке өттүң.")
            time.sleep(0.5)
            level = 4

        elif choice == "3":
            print("Качып бара жатып сени атып салды...")
            time.sleep(2)
            print(" Ты умер. Оюн бүттү.")
            time.sleep(0.5)
            game_over = True

        else:
            print("1, 2 же 3 гана тер!")
            time.sleep(0.5)

    # LEVEL 4
    elif level == 4:
        print("\n LEVEL 4:")
        time.sleep(0.5)
        print(" 1ден 3ко чейин танда :")
        time.sleep(0.5)
        choice = input("Тандооңду жаз (1,2,3): ")
        time.sleep(0.5)

        if choice == "1":
            print(" сага белек ")
            time.sleep(2)
            hp += 10
            print("HP +10. Азыркы HP:", hp)
            time.sleep(0.5)

        elif choice == "2":
            print("ката жолго түшүп калдың...")
            time.sleep(2)
            hp -= 20
            print("HP -15. Азыркы HP:", hp)
            time.sleep(0.5)

        elif choice == "3":
            print("Куттуктайм...")
            time.sleep(0.5)
            print("Level 5ке өттүң!")
            time.sleep(0.5)
            level = 5
        else:
            print("1, 2 же 3 гана тер!")
            time.sleep(0.5)

    # LEVEL 5
    elif level == 5:
        print("\n LEVEL 5: Победа !!!!!")
        time.sleep(0.5)
        print("Оюн бутту!")
        time.sleep(0.5)
        print("Сенин акыркы HP" , hp)
        time.sleep(0.5)

        if hp > 0:
            print(" Сен бардык сыноолордон өттүң! ЖЕҢИШ!")
            time.sleep(0.5)
        else:
            print(" HP түгөнүп калган экен. Оюн утулду.")
            time.sleep(0.5)
        game_over = True

    else:
        print("Белгисиз level. Оюн токтойт.")
        time.sleep(0.5)
        game_over = True