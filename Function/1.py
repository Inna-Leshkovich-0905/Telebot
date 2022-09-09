# def func_1():
#     print('hello') #может быть и сложение, и вычитание, и подсчет гласных, и т.д.
#
# def func_2():
#     c = 3+4
#     print(c)
#
# def func_3():
#     pass # ключевое слово, ошибки не будет!
#
#
# func_1()
# func_2()
# func_3()



# def func_1():
#     print('hello') #может быть и сложение, и вычитание, и подсчет гласных, и т.д.

# def func_2(c, d, a = 5, b = 4):
#     return a+b+c+d
# print(func_2())


def func_3(*args,**kwargs):
    def func_3(*args, **kwargs):
        print(args)
        print(kwargs)

func_3(1, 2, 3, 5, 5, 8, 9, a=2, b=5, g=8, t=6)

# print(func_2(2, 5, a=, b=))
# func_1()
# print(func_2(int(input()),int(input())))
