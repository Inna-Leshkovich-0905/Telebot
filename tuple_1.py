import random
a = [random.randint(1,100) for i in range(10)]
a = tuple(a) #преобразование списка в кортеж
print(a)
print(a.index(min(a)), a.index(max(a)))