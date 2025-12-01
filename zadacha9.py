hour = int(input("Введите час (от 1 до 12): "))
period = int(input("Утра (1) или вечера (2)? "))
ahead = int(input("На сколько часов впереди? "))


if period == 2:
    hour += 12


new_hour = (hour + ahead) % 24


if new_hour == 0:
    new_hour = 12
    period_str = "ночи"
elif new_hour < 12:
    period_str = "утра"
elif new_hour == 12:
    period_str = "дня"
else:
    if new_hour > 12:
        new_hour -= 12
    period_str = "вечера"


print(f"Новый час: {new_hour}:00 {period_str}")