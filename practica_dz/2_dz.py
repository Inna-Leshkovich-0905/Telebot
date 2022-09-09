import random
a = int(input('Введите любые числа: '))
f = (random.randint(0,a))
print(f)
b = (input('Введите искомую  цифру: '))
b=str(b)
f=str(f)
print('Встречается раз: ', f.count(b))