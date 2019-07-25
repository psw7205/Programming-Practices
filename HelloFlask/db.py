import mysql.connector as db


def get_connection():
    conn = db.connect(user='test', password='0000', host='localhost', database='world')
    return conn


def get_list(start=0, end=30):
    conn = get_connection()
    cursor = conn.cursor()
    # cursor.execute(f'select code, name from Country limit {start}, {end}')
    cursor.execute(f'select code, name, population from country '
                   f'order by population desc limit {start}, {end}')
    return cursor.fetchall()


def find_list(code):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'select code, name, population from country '
                   f'where code=\'{code}\'')

    return cursor.fetchall()
