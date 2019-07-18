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
# 전체 레코드
# cursor.execute('SELECT * FROM usertbl;')
# 특정 컬럼명으로 추출
cursor.execute('SELECT userID, name, addr FROM usertbl;')

# 2차원 리스트에 저장하기
# 리스트이름 = 작업변수.fetchall() : 전체레코드
# 리스트이름 = 작업변수.fetchone() : 한개
# 리스트이름 = 작업변수.fetchmany(레코드갯수)  : 레코드숫자만큼

result_list = cursor.fetchall()
print(result_list)
print('-'*20)
for i in result_list:
    print(i)
print('-'*20)
print(result_list[0]) # 1행
print(result_list[0][0]) # 1행 1열

# 퀴즈 1:
# buyTbl에서 1열만 출력하기
cursor.execute('SELECT * FROM buyTbl;')
list1 = cursor.fetchall()
print('-'*10)

for i in range(0, len(list1)-1):
    print(list1[i][0])
print('-'*10)

# 퀴즈 2:
# buyTbl에서 마지막행만 출력하기
print(list1[-1])

print('-'*10)
# 퀴즈 3:
# buyTbl에서 3행3열의 값 출력하기
print(list1[2][2])

# 퀴즈 4:
# userTbl에서 지역(addr)값이 '서울'인 레코드만 표시하기
cursor.execute("SELECT * FROM userTbl WHERE addr='서울';")
list2 = cursor.fetchall()
for i in list2:
    print(i)
print('-'*10)

# 퀴즈 5:
# buyTbl에서 아이디(uesrID)값이 'KBS'인 레코드만 표시하기

cursor.execute('SELECT * FROM buyTbl WHERE userID="KBS";')
list3 = cursor.fetchall()
for i in list3:
    print(i)
print('-'*10)



# ------ 테이블 생성
# 테이블 sql
cursor.execute('''
                CREATE TABLE IF NOT EXISTS bookTBL (
                    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    title TEXT NOT NULL,
                    writer TEXT NOT NULL,
                    page INTEGER NOT NULL,
                    price INTEGER NOT NULL
                );
              ''')


# DB 종료
conn.close()

