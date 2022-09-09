# a = {'hello','world','sunny'} # !скобки не могут быть пустыми
# print(type(a))
# print(a) #каждый раз будет выводиться в разном порядке, предугадать нельзя

# b = set() #создание пустого множества
# print(type(b))

# b = {1,2,3,4,4,4,4,5,7,7,7}
# print(b) #дубликаты не выведутся, но нарушится порядок

# a = {'hello','world','sunny'}
# a.add('red')
# print(a)

# a = {'hello','world','sunny','red'}
# a.remove('red')
# print(a)

# a = {'hello','world','sunny','red'}
# a.discard('red')
# print(a)
#
# a = {'hello','world','sunny','red'}
# a.discard('blue')
# print(a)

# a = {'hello','world','sunny','red'}
# print(a.clear())

# b = {1,2,3,4,4,4,4,5,7,7,7,10}
# c = {1,2,4,7,9,9,13,19}
# print(c.union(b))

# a = {'hello','world','sunny'}
# b = {1,2,3,4,4,4,4,5,7,7,7,10}
# c = {1,2,4,7,9,9,13,19}
# print(c.union(a,b)) #можно объед.много множеств

# a = {'hello','world','sunny'}
# b = {1,2,3,4,4,4,4,5,7,7,7,10}
# c = {1,2,4,7,9,9,13,19}
# print(b.intersection(c))

# a = {'hello','world','sunny'}
# b = {1,2,3,4,4,4,4,5,7,7,7,10}
# c = {1,2,4,7,9,9,13,19}
# print(b&c)

# a = {'hello','world','sunny'}
# b = {1,2,3,4,4,4,4,5,7,7,7,10}
# c = {1,2,4,7,9,9,13,19}
# print(c-b)

# a = {'hello','world','sunny'}
# b = {1,2,3,4,4,4,4,5,7,7,7,10}
# c = {1,2,4,7,9,9,13,19}
# print(b.isdisjoint(a))

# a =frozenset(['hello','world','sunny'])
# print(type(a))

# s = {'hello', 'world', 'foo', 'sunny'}
# if 'foo' in s:
#     print('True')

# class Dog:
#     def walk(self):
#         return "*walking*"
#     def speak(self):
#         return "Woof!"
# class jackrussellterrier(Dog):
#     def speak(self):
#         return "Arff!"
# bobo = jackrussellterrier()
# print(bobo.speclass)

# class Dog:
#     def walk(self):
#         return "*walking*"
#     def speak(self):
#         return "Woof!"
#
# class Sobaca(Dog):
#     def talk(self):
#         return super().speak()
# bobo=Sobaca()
# print(bobo.talk())

class A:
    _a = 4


class B(A):
    pass


print(B._a)
