import sqlite3

conn = sqlite3.connect('./data/students.db')
cursor = conn.cursor()
cursor.execute('select * from student')

for line in cursor.fetchall():
    print(line)

conn = sqlite3.connect('./data/chinook.db')
cursor = conn.cursor()
cursor.execute('select * from customers limit 10')

for line in cursor.fetchall():
    print(line)

conn = sqlite3.connect('./data/test.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master "
               "WHERE type ='table' AND "
               "name NOT LIKE 'sqlite_%';")

for line in cursor.fetchall():
    print(line)

cursor.close()
conn.close()
