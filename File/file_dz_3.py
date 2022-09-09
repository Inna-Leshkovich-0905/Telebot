f = open('1_dz.txt', 'r')
b = f.readlines()
print(b)

a = 0
for i in b:
    a += 1
print('Количество строк: ', a)

c = []
for i in b:
    i = i[:-1] #обрезка \n
    print('Строка: ', i)
    c= len(i)
    print('Количество символов в строке: ', c)
    continue

f.close()
