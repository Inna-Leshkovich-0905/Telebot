f = open('1.txt', 'r')
s = f.readlines()
# print(s)
a = []
b = []
for i in s:
    i = i[:-1] #обрезка \n
    if i.isalpha(): #разграничение чисел и строк
        b.append(i)
    elif i.isdigit():
        i = int(i) #превращение строки в число
        a.append(i)
a.sort()
b.sort()
# print(a)
# print(b)
mas = a+b #сложение в один массив
print(mas)
f.close()