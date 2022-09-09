class Money:
    def start(self, a, b=None):
        if b is not None and a > b:
            print('Остаток: ', a - b)
        else:
            print('Остаток: ', a)
        if b is not None and a < b:
            print('У вас недостаточно денег!')


Money_a = Money()
Money_a.start(142, 164)
