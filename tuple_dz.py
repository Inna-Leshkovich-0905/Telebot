import random
a = [random.randint(0,9) for i in range(9)]
a = tuple(a)
print(a)
print(sum(a))