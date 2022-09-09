# class Myclass():
#     @staticmethod
#     def staticmethod():
#         print('static method called')
#
#
# class children_My_class(Myclass):
#     pass
#
#
# my_obj = Myclass()
# my_obj.staticmethod()
# my_obj_1 = children_My_class()
# my_obj_1.staticmethod()
#
# class Person():
#     @staticmethod
#     def is_adult(age):
#         if age > 18:
#             return True
#         else:
#             return False
#
# print(Person.is_adult(23)) #обращение к имени класса и передача возраста

# class MyClass():
#     TOTAL_OBJECTS = 0 #объявлена переменная, статическая, изначально равно 0
#
#     def __init__(self):
#         MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS + 1 #объект, который выводит количество объектов класса
#
#     @classmethod
#     def total_objects(cls):
#         print("Total objects: ", cls.TOTAL_OBJECTS)
#
#
# class ChildClass(MyClass):
#     TOTAL_OBJECTS=0
#     def __init__(self):
#         ChildClass.TOTAL_OBJECTS = ChildClass.TOTAL_OBJECTS + 1
#
#     pass
#
# # Создаем объекты
# my_obj1 = ChildClass()
# # my_obj1 = MyClass()
# my_obj2 = MyClass()
# my_obj3 = MyClass()
# # Вызываем classmethod
# ChildClass.total_objects()
# # MyClass.total_objects()