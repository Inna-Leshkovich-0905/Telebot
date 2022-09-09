# # 1 задача
# import math #2 вариант решения
#
# def square(a):
#     b = 4 * a
#     c = a**2
#     d = math.sqrt(2*(a**2)) #встроенная функция sqrt-вычисление корня кважратного
#     return b,c,d
#
# print(square(4))

# def square(a): #1 вариант решения
#     b = 4*a
#     c = a**2
#     d = ((2*a**2))**(1/2)
#     return b,c,d
# print(square(4))

# 2 задача
def season(a):
    if a == 12 or 1 <= a <= 2:
        print("Зима")
    elif 3 <= a <= 5:
        print("Весна")
    elif 6 <= a <= 8:
        print("Лето")
    elif 9 <= a <= 11:
        print("Осень")

d = int(input())
season(d)