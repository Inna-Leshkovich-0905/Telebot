# a = ()
# b = tuple([1, 2, 3, 4, 5, 6])
# print(b)
# print(type(b))

a = ('hello', 'world', ['e', 'r'])
b = (1, 2, 3, 4, 5, 6, 7)
# c = a + b #сложение кортежей
c = a * 3 #умножение
a[2][1]='red' #изменение эл-та кортежа, если это список внутри кортежа
print(c)
print(a)
print(b.count(2)) #кол-во опр. эл-та
print(len(a)) #длина
print(min(b), max(b), sum(b)) #мин. и макс. элемент, сумма