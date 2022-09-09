# задача 2

n = {'number1': 7, 'number2': 9, 'number3': 18, 'number4': 26, 'number5': 55}

f = 1
for i in n.values():
    f = f * i
print('Произведение значений словаря: ', f)