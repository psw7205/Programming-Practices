# mySQL 연동을 위한 모듈 임포트
import pymysql

# DB 연결변수 설정
conn = pymysql.connect( host='localhost',
                        port=3306, user='root',
                        passwd='12345678',
                        db='sqldb',
                        charset='utf8')

# 작업변수 커서 생성
cursor = conn.cursor()

# 작업변수 커서 실행
# 작업변수.execute(sql 명령)

# 2차원 리스트에 저장하기
# 리스트이름 = 작업변수.fetchall() : 전체레코드
# 리스트이름 = 작업변수.fetchone() : 한개
# 리스트이름 = 작업변수.fetchmany(레코드갯수)  : 레코드숫자만큼

# ------ 테이블 생성
# 테이블 sql
# cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS bookTBL (
#                     id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
#                     title VARCHAR(20) NOT NULL,
#                     writer TEXT NOT NULL,
#                     page INT(5) NOT NULL,
#                     price INT(5) NOT NULL
#                 );
#               ''')


# -------- 레코드 삽입  - 컬럼명 지정 없음
# INSERT INTO 테이블명 VALUES(값1, 값2 ...);
# cursor.execute(''' INSERT INTO bookTBL
#                         VALUES(NULL, '파이썬1', '박응용', 300, 25000);
#                 ''' )

# ------ 레코드 삽입  - % 방식
# sql변수 = " INSERT INTO 테이블명(컬럼명1, 컬럼명2...)
#               VALUES(%s, %s, ...  ); "
# cursor.execute(sql변수, (값1, 값2 ...))

# sql = '''
#         INSERT INTO bookTBL(title, writer, page, price)
#             VALUES(%s, %s, %s, %s)
#       '''
# cursor.execute(sql, ('C 언어', '김C', 450, 4500))

# ------ 여러 레코드 삽입  - % 방식
# data = (
#           ('자바', '김C', 550, 5500),
#           ('포토샵', '이몽룡', 700, 3500),
#           ('일러스트레이터', '김홍도', 800, 2500) )
#
# sql = '''
#         INSERT INTO bookTBL(title, writer, page, price)
#             VALUES(%s, %s, %s, %s)
#       '''
#
# cursor.executemany(sql, data);

# ------ 레코드 수정 - % 방식
# sql = '''
#         UPDATE 테이블명
#             SET 컬럼명1 = %s
#             WHERE 컬럼명2 = %s
#       '''
#
# cursor.execute(sql, (컬럼명1값, 컬럼명2값))

sql = '''
        UPDATE bookTBL 
            SET page = %s
            WHERE id = %s
      '''

cursor.execute(sql, (1000, 1))

# ------ 레코드 삭제 - % 방식
# sql = '''
#         DELETE FROM 테이블명
#             WHERE 컬럼명 = %s
#       '''
#
# cursor.execute(sql, (값))

# sql = '''
#         DELETE FROM bookTBL
#             WHERE id = %s
#       '''
#
# cursor.execute(sql, (3))



# db에 테이블 반영
conn.commit()

cursor.execute('SELECT * FROM bookTBL;')
bookList = cursor.fetchall()
for i in bookList:
    print(i)
print('-'*10)



# DB 종료
conn.close()

