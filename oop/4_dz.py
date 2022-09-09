# # методы экземпляра класса
# class Summer:
#     def June(self): #обычный метод
#         return('Июнь')
#     def July(self): #обычный метод
#         return ('Июль')
#     def August(self): #обычный метод
#         return ('Август')
# ex = Summer()
# a = input("Введите число месяца (6, 7 или 8): ")
# if a == '6':
#     print(ex.June())
# elif a == '7':
#     print(ex.July())
# elif a == '8':
#     print(ex.August())

# cтатические методы
class MyYear:
    @staticmethod
    def staticmethod():
        print('Year')
    def my_year(year):
        if year < 1991:
            return 'USSR'
        else:
            return 'no_USSR'
print(MyYear.my_year(2022))




