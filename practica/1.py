# 1 задача
str_ = input("Введите текст: ")
a = 'аеёиоуыэюя' #все гласные буквы русского алфавита
b = 0
c = 0
e = ''
for i in str_:
    if i in a:
        b+=1
        e+=i
    else:
        c+=1
if b == c:
    print(e)

print(b)
print(c)