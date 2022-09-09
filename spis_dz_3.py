a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', ['world', 5.7], 3, 6]

a.extend(b)
print(a)

d = 6
a.insert(2,d)
print(a)

print(a.count(6))

print(len(a))

r = a[10][0]
print(r)