# # задание 1
# def func_1():
#     global f
#     f = 7
#     return f+5
# def func_2():
#     return f-2
# print(func_1())
# print(func_2())

# задание 2
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    m = n ** (1 / 2)
    i = 2
    while i <= m:
        if n % i == 0:
            return False
        i += 1
    return True
print(is_prime(int(input("Введите целое число от 1 до 1000: "))))





# def is_prime(f):
#     if f%1==1 and f%f==1:
#         return True
#     f+=1
#     if not f%1==1 and f%f==1:
#         return False
# print(is_prime(int(input("Число: "))))

# def is_prime(b):
#     a = True
#     if i in raprint(is_prime(int(input("Число: "))))nge (2, int(b**0.5)):
#         if b%i == 0:
#             a = False
# f = int(input('Введите число: '))
# print(is_prime(f))