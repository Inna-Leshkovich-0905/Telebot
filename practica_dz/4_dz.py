a=input("Введите числа через пробел: ").split()
c=[]
for i in a:
    if a.count(i)==1:
        c.append(i)
print("Список уникальных чисел: ", c)