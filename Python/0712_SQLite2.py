import sqlite3

conn = sqlite3.connect('./data/0712.db')
cursor = conn.cursor()

sql = '''create table if not exists book1 (
        id integer primary Key AUTOINCREMENT not null,
        title text not null,
        author text not null,
        page integer not null,
        price integer not null);
        '''

cursor.execute(sql)
conn.commit()

# sql = '''
# insert into book1(title, author, page, price)
# values('python', 'Guido van Rossum', 100, 10000);
# '''
# cursor.execute(sql)
# conn.commit()


# sql = '''
# insert into book1
# values(2, 'C', 'Dennis Ritchie', 100, 10000);
# '''
# cursor.execute(sql)
# conn.commit()

# cursor.execute('select * from book1')
# result = cursor.fetchall()
#
# for row in result:
#     print(row)
#
# sql = '''delete from book1 where id=1'''
#
# cursor.execute(sql)
# conn.commit()
#
#
# sql = '''delete from book1 where id=?'''
#
# cursor.execute(sql, [1])
# conn.commit()

# sql = '''update book1 set price=2000 where id=2'''
# cursor.execute(sql)
# conn.commit()

print('-'*30)
cursor.execute('select * from book1')
result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
conn.close()
