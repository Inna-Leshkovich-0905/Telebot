class Example:
    def print(self):
        print("Hello world")
    def print_1 (b):
        global a
        a = [3, 8, 11, 'my name']
        b = len(a)
        print(b)
    def print_2 (f):
        f = a[3]
        print(f)
    def print_3 (s):
        v = 'is Inna'
        a.append(v)
        print(a)

print(dir(Example))
ex = Example()
ex_1 = Example()
ex_1.print()
ex_2 = Example()
ex_2.print_1()
ex_3 = Example()
ex_3.print_2()
ex_4 = Example()
ex_4.print_3()