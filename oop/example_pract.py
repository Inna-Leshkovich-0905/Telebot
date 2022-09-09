# # 1 задача
# class Example:
#     a = 2 #статические переменные
#     b = 3
#
#     def __init__(self, t, r):
#         self.t = t #динамические переменные
#         self.r = r
#
#     def func(self):
#         self.c = 5
#         print(self.c)
#
#     def func1(self):
#         return self.a + self.b
#
#     def func2(self):
#         return self.t**self.r
#
# ex = Example(5,6) #стадия создания объекта
#
# print(ex.a)
# print(ex.func1())
# print(ex.func2())
# ex.func()

# 2 задача
class Calc:
    def __init__(self):
        self.vvod()

    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def dele(self):
        if self.b == 0:
            return "error"
        else:
            return self.a / self.b

    def umn(self):
        return self.a * self.b

    def vvod(self):
        self.a = int(input("Введите первое число: "))
        self.b = int(input("Введите второе число: "))


while True:
    ex = Calc()
    c = input("Введите операцию(+,*,/,-): ")
    if c == '+':
        print(ex.plus())
    elif c == "-":
        print(ex.minus())
    elif c == '*':
        print(ex.umn())

    elif c == '0':
        break
    else:
        print(ex.dele())