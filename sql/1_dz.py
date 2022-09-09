import sqlite3
conn = sqlite3.connect('dz_1.db')
cursor = conn.cursor()
# Создадим таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')
# Заполняем таблицу данными
cursor.execute('''INSERT INTO book(col_1,col_2) VALUES ('Поле','Тип, описание'), ('book_id','INT PRIMARY KEY AUTO_INCREMENT'), ('title','VARCH(50)'), ('author','VARCHAR(30)'), ('price','DECIMAL(8, 2)'), ('amount','INT')''')
# Сохраняем изменения
conn.commit()

n = "new"
m = "str"
cursor.execute('''CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT) ''')
cursor.execute('''INSERT INTO book(col_1,col_2) VALUES (?,?)''', (n, m))
conn.commit()

cursor.execute('''SELECT*FROM book''')
f = cursor.fetchall()
print(f)

# чтобы было в оттдельной строке:
for i in f:
    i = list(i)
    s = 0
    print(' '.join(str(s) for s in i))
