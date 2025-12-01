from os import remove

#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#a.remove(10)
#print(a)


#a = [10,20,30,40,50,60,70,80,90,100]
#a.pop()
#print(a)

a = [5, 10, 15, 20, 25, 30]
c = [10, 20, 30, 40]
average = sum(c) / len(c)
print(average)

spisok = []
spisok.append(1)
spisok.append(2)
spisok.append(3)
print(spisok)

l = []
l.extend([1,2,3,4,5,6])
print(l)

nums = [9, 1, 5, 3, 8]
nums.sort()
print(nums)


n = [2, 1, 2, 3, 4, 2, 5]
print(n.count(2))

fruits = ["apple", "banana", "cherry", "kiwi"]
print(fruits.index("cherry"))
print(fruits.index("apple"))


letters = ['a', 'b', 'c', 'd']
letters.reverse()
print(letters)

numbers = [1, 4, 2, 4, 3]
numbers.remove(4)
print(numbers)


data = [100, 200, 300, 400]
data.pop(1)
print(data)
print(len(a))

b = [3, 7, 1, 9, 12]
print(sum(b))
