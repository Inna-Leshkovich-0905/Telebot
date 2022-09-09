def funk(*args,**kwargs):
        for i in args:
                if i % 2 != 0:
                        print('Нечетный элемент:', i)
funk(1,2,2,3,4,5,6,7,8)