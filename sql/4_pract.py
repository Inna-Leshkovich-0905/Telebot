# # 1 задача
# import sqlite3
# import random
#
# conn = sqlite3.connect('z_2.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER,col_2 INTEGER) ''')
# a = random.randint(0,9)
# b = random.randint(0,9)
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES(?,?)''',(a,b))
# conn.commit()
# # cursor.execute('''SELECT*FROM tab_1''') # будет выводиться номер id
# cursor.execute('''SELECT col_1,col_2 FROM tab_1''')
# k = cursor.fetchall()
# print(k)
# print(len(k))
# sum = 0
# for i in k:
#     for j in i:
#         sum+=j
# aver = sum/(len(k)*2)
# print(sum)
# print(aver)
# if aver > len(k):
#     cursor.execute('''DELETE FROM tab_1 WHERE id = 4''')
#     conn.commit()
# cursor.execute('''SELECT col_1,col_2 FROM tab_1''')
# k = cursor.fetchall()
# print(k)


# 2 задача
import sqlite3
import random

conn = sqlite3.connect('z_3.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER) ''')
r = random.randint(1,20)
cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''',(r,))
conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)
class A:
    def baz(self, a =None,b=None,c=None):
        if a is not None and b is None and c is None:
            cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (3)''')
            conn.commit()
        elif a is not None and b is not None and c is None:
            if type(b) is int:
                cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
                conn.commit()
        elif a is not None and b is not None and type(c) is int :
            cursor.execute('''UPDATE tab_1 SET col_1 = 77 WHERE id = 3''')


example = A()
example.baz(3,'hello',9)
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)