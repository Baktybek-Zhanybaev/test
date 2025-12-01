# 1-Көнүгүү: Жай dict түзүү
student = {"name": "Айгерим", "age": 20, "city": "Ош"}
print("1:", student)

# 2-Көнүгүү: Маанини алуу (жаш)
print("2: Жаш =", student["age"])

# 3-Көнүгүү: Маанини өзгөртүү (жаш 21ге)
student["age"] = 21
print("3: Жаш өзгөртүлгөн =", student["age"])

# 4-Көнүгүү: Жаңы элемент кошуу (phone)
student["phone"] = "0777123456"
print("4: Жаңы элемент кошулду =", student)

# 5-Көнүгүү: Бардык ачкычтарды чыгаруу
print("5: Ачкычтар =", student.keys())

# 6-Көнүгүү: Бардык маанилерди чыгаруу
print("6: Маанилер =", student.values())

# 7-Көнүгүү: Бардык (key, value) жуптарын чыгаруу
print("7: Жуптар =", student.items())

# 8-Көнүгүү: Ачкыч бар экенин текшерүү
print("8: 'city' барбы?", "city" in student)

# 9-Көнүгүү: get() колдонуу
print("9: email =", student.get("email", "Email жок"))

# 10-Көнүгүү: dict узундугун табуу
print("10: Элемент саны =", len(student))
