def simple_decore(fn):
    print("Start function")
    fn()
    print("Stop function")

@simple_decore #вызов декоратора, функцию вызывать не нужно
def first_test():
    print("Test function 1")

@simple_decore
def second_test():
    print("Test function 2")

# simple_decore(first_test)
# simple_decore(second_test)