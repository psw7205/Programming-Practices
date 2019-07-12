# sqlite 임포트
import sqlite3

# 데이타베이스 연결
# 연결변수(conn) = sqlite3.connect(데이타베이스경로)
# Db 연결
# DB가 없으면 지정한 경로에 새로 생성
conn = sqlite3.connect('data/bookDb.db')

# 작업변수(cursor) 생성
cursor = conn.cursor()

# ------ 테이블 생성
# 테이블 sql
cursor.execute('''
                CREATE TABLE IF NOT EXISTS book1 (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    writer TEXT NOT NULL,
                    page INTEGER NOT NULL,
                    price INTEGER NOT NULL
                );
              ''')

# ------ 레코드 삭제 1
# DELETE FROM 테이블명 WHERE 절;
# cursor.execute(''' DELETE FROM 테이블명
#                   WHERE 절;''')

# id가 1인 레코드를 삭제하여라
cursor.execute(''' DELETE FROM book1
                  WHERE id=1;''')

# ------ 레코드 삭제 2 - sql 변수
# sql변수 = DELETE FROM 테이블명 WHERE 절에서 데이타값은 물음표? ;
# 물음표(?)에 해당하는 값지정시에는 리스트형태로 삽입
# cursor.execute(sql변수, [값])

# id가 5인 레코드를 삭제하여라
sql3 = 'DELETE FROM book1 WHERE id=?;'
cursor.execute(sql3, [5])

# db에 테이블 생성 반영
conn.commit()

# ------ 테이블 출력
# 테이블의 레코드를 리스트로 저장한 후 출력

# 작업변수(cursor).execute(selec sql 명령 )
# 리스트변수 = 작업변수(cursor).fetchall()
# 리스트변수 = 작업변수(cursor).fetchone()
# 리스트변수 = 작업변수(cursor).fetchmany(레코드갯수)


cursor.execute('SELECT * FROM book1')
resultList = cursor.fetchall()
print('-' * 30)
print('레코드 갯수 : ', len(resultList))
# 한 행씩 출력
for i in resultList:
    print('-' * 30)
    print(i)

# Db 종료
conn.close()
