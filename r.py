from http.cookiejar import uppercase_escaped_char

text = input("Введите текст: ")
#print(len(text))
for i in range(10):
    print( i ,text)

print(text[0])
print(text[:3])
print(text[-3:])
print(text[::-1])

if len(text) > 7:
    print(text [6])
else:
    print("туура эмес укам")

print(text[1:-1])

print(text.upper())
print(text.replace("a","e").replace("b","B"))
for i in text:
    if i.isalpha():
       print("_",end="")
    else:
       print(i, end="")
