import mysql.connector as db
import datetime

try:
    conn = db.connect(user='test', password='0000', host='localhost', database='employees')
except Exception as e:
    print(e)

cursor = conn.cursor()
query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1994, 6, 15)
hire_end = datetime.date(1994, 6, 15)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
    print("{}, {} was hired on {:%d %b %Y}".format(
        last_name, first_name, hire_date))

cursor = conn.cursor(dictionary=True)
cursor.execute(query, (hire_start, hire_end))
rows = cursor.fetchall()
for row in rows:
    print(row['last_name'], row['first_name'], row['hire_date'])

cursor.close()
conn.close()
