# # 1 задача
# def sum (a, b):
#     return a+b
#
# def difference (a, b):
#     return a-b
#
# def increase (a, b):
#     return a*b
#
# def splitting (a, b):
#     return a/b
#
# while True:
#     a = float(input('Введите первое вещественное число: '))
#     b = float(input('Введите второе вещественное число: '))
#     d = input('Какая операция с числами вас интересует (1-сумма,2-разность,3-умножение,4-деление), или введите 0 для выхода: ')
#     if d == '0':
#         break
#     for i in d:
#         if d == '1':
#             s = sum(a, b)
#             print(f'Сумма чисел {a} и {b} равна {s}')
#         elif d == '2':
#             s = difference(a, b)
#             print(f'Разность чисел {a} и {b} равна {s}')
#         elif d == '3':
#             s = increase(a, b)
#             print(f'Произведение чисел {a} и {b} равно {s}')
#         elif d == '4':
#             if b == 0:
#                 print('Делить на 0 нельзя')
#                 break
#             s = splitting(a, b)
#             print(f'Частное чисел {a} и {b} равно {s}')

# 2 задача
def q(p):
    if type(p) == tuple:
        print(type(p))
        print('Всего слов: ', len(p))
        for i in p:
            print('Слово: ', i)
            print('Длина слова: ', len(i))
    elif type(p) == list:
        print(p)
        print(type(p))
        print('Кол-во букв: ', len(list(filter(lambda x: type(x) == str, p))), ', Кол-то чисел: ', len(list(filter(lambda x: type(x) in (int, float), p))))
    elif type(p) == str:
        print(type(p))
        print('Количество букв: ', len(p))
    else:
        print(type(p))

q(('hello', 'friend', '321', 'good'))
q([7, 12, 15, 'oops', 'wow'])
q('abcd')
q({1: 2})



