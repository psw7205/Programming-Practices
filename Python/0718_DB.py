import mysql.connector as db

try:
    conn = db.connect(user='test', password='0000', host='localhost', database='sqlDB')
except Exception as e:
    print(e)


cursor = conn.cursor()
query = "select * from usertbl where addr='서울'"

cursor.execute(query)

for line in cursor.fetchall():
    print(line)

cursor.close()
conn.close()
