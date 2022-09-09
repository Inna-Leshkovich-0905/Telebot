class Class:
    def __init__(self):
        self.vvod()

    def str(self):
        w = 'eyuioa'
        y = 'EYUIOA'
        g = 0
        s = 0
        for i in self.a:
            if i in w or i in y:
                g += 1
            else:
                s += 1
        print('Гласных: ', g)
        print('Согласных: ', s)
        return 'Произведение гласных и согласных: ', g * s

            # for i in self.a:
            #     if (g * s) <= len(a):
            #         print(g)
            #     else:
            #         print(s)

    def Number(self):
        return 'Длина:', len(self.a)

    def vvod(self):
        self.a = input("Введите строку или число: ")

while True:
    ex = Class()
    c = input("Введите 1, если вы ввели строку, введите 2, если вы ввели число, введите n для выхода: ")
    if c == '2':
        print(ex.Number())
    elif c == "1":
            print(ex.str())
    elif c == 'n':
        break