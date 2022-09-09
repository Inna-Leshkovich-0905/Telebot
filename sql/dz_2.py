# import sqlite3
# import random
#
# query1 = 'CREATE TABLE IF NOT EXISTS `WORDS` (`word` TEXT)'
# query2 = 'CREATE TABLE IF NOT EXISTS `DIGITS` (`digit` INTEGER)'
#
# # создаем БД на sqlite
# with sqlite3.connect('test.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute(query1)
#     cursor.execute(query2)
#     connection.commit()
#     cursor.close()
#
# def rnd(n):
#     seed = random.randint(1, 10)
#     number = random.randint(0, 100)
#     return number if seed % 2 else f'txt'*(seed//2)
#
# # генерация элементов списка
# elements = [rnd(i) for i in range(50)]
# random.shuffle(elements)
#
# # пока что вставляем всё подряд
# with sqlite3.connect('test.db') as connection:
#     cursor = connection.cursor()
#     for element in elements:
#         if isinstance(element, str):
#             cursor.execute(f'INSERT INTO WORDS VALUES ("{element}")')
#             cursor.execute(f'INSERT INTO DIGITS VALUES ("{len(element)}")')
#         elif element % 2:
#             cursor.execute(f'INSERT INTO WORDS VALUES ("нечётное")')
#         else:
#             cursor.execute(f'INSERT INTO DIGITS VALUES ("{element}")')
#     connection.commit()
#     cursor.close()
#
# # подсчет количества для проверки
# with sqlite3.connect('test.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute('SELECT COUNT(*) FROM `WORDS`')
#     result_words = cursor.fetchall()
#     cursor.execute(query2)
#     cursor.execute('SELECT COUNT(*) FROM `DIGITS`')
#     result_digits = cursor.fetchall()
#     cursor.close()

import sqlite3
conn = sqlite3.connect('dz_2.db')
cursor = conn.cursor()

# Создадим 2 таблицы, 1 с текстовой колонкой, 2 с числовой
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT) ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER) ''')

# Заполняем таблицу данными
a = [8, 15, 25, 'orange', 'apple']
for i in a:
    if type(i) is int:
        if i % 2 == 0:
            n = int(i)
            cursor.execute('''INSERT INTO tab_2 (col_1) VALUES (?)''', [n])
            conn.commit()
        elif i % 2 != 0:
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', ['нечетное'])
            conn.commit()
    elif type(i) is not int:
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''',[i])
        conn.commit()
        b = len(i)
        cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''',[b])
        conn.commit()


# cursor.execute('SELECT COUNT(*) FROM `tab_1`')
# conn.commit()


cursor.execute('''SELECT*FROM tab_1''') # * означает, что из таблицы достается всё из таблицы 1
k = cursor.fetchall() # указатель, чтобы получить атрибуты
print(k)
cursor.execute('''SELECT*FROM tab_2''') # * означает, что из таблицы достается всё из таблицы 2
m = cursor.fetchall()
print(m)




