# Декоратор-счётчик
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

# Функция, вызовы которой нужно считать
@counter
def f():
    print("Summer")
f()
f()
f()
f()
print('Функция вызывалась:', f.count, 'раз.')