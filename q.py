import random
from random import randint

x = int(input())
y = int(input())
result =  abs(x - y) / ( x + y )
print(result)

for i in range(50):
    some_namber = randint(1, i + 2)
    print(some_namber, end=' ' )