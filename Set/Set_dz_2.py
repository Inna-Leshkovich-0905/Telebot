a=[1,1,5,7,7,12,15,17,15]
print(a)
b=frozenset(a)
print(b)
c=[]
for i in a:
    if a.count(i)>1:
        c.append(i)
print('Дубликаты: ',c)