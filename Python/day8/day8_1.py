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
