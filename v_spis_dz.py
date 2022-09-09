k = [7,3,18,'new','student']
print(k)
l = [1,2,3]
k[0]=l
print(k)
v = l[0]+l[1]+l[2]
print('Cумма элементов вложенного списка: ', v)
k.insert(5,v)
print(k)