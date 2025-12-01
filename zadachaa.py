import random

trials = 10000

results = {i: 0 for i in range(2, 13)}

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    results[total] += 1

print("Сумма | Процент выпадений")
print("--------------------------")
for total in range(2, 13):
    percent = results[total] / trials * 100
    print(f"{total:>5} | {percent:5.2f}%")
