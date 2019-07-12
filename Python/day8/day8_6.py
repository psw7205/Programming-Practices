# 입력받은 데이타를 데이타베이스에 삽입
# sqlite 임포트
import sqlite3

# 데이타베이스 연결
conn = sqlite3.connect('../data/addrDb.db')

# 작업변수(cursor) 생성
cursor = conn.cursor()

# ------ 테이블 생성
# 테이블 sql
cursor.execute('''
                CREATE TABLE IF NOT EXISTS addr1 (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    address TEXT NOT NULL,
                    email TEXT NOT NULL
                );
              ''')
# db에 테이블 생성 반영
conn.commit()


# ------ 테이블 데이타 출력
def printAddr():
    cursor.execute('SELECT * FROM addr1')
    resultList = cursor.fetchall()
    print('-' * 30)
    print('레코드 갯수 : ', len(resultList))
    print('id\tname\tphone\taddress\t\temail')
    print('-' * 50)
    # 한 행씩 출력
    for i in resultList:
        print('-' * 50)
        print(i)


# ---------------------
# 데이타입력함수
# 데이타 입력을 종료하시겠습니까?
# y 입력시 데이타 입력 종료
# 문자열변수.strip() => 공백제거
def inputData():
    while True:
        # 데이타 입력
        print('-' * 50)
        print(' 주소 추가 \n')
        print('-' * 50)
        # inName, inPhone, inAddress, inEmail
        inName = input('이름 = > ')
        inPhone = input('전화번호 = > ')
        inAddress = input('주소 = > ')
        inEmail = input('이메일 = > ')
        sql = " INSERT INTO addr1(name,phone,address,email)  VALUES(?,?,?,?); "
        # cursor.execute(sql, (inName,inPhone,inAddress,inEmail))
        # 공백제거후 데이타 삽입
        cursor.execute(sql, (inName.strip(), inPhone.strip(), inAddress.strip(), inEmail.strip()))
        # db에 테이블 생성 반영
        conn.commit()
        print('1개의 데이타가 추가되었습니다.')
        # 입력 종료
        qSign = input('입력을 종료하시겠습니까?(y).......    ')
        if qSign.strip() == 'y':
            break


# ---------------------
# 데이타 삭제 함수
def delData():
    num = input('삭제할 아이디를 입력하세요')
    sql = " delete from addr1 where id=?;"
    cursor.execute(sql, num)


# ---------------------
# 메뉴 선택
while True:
    print('= 주소록 =')
    print('1. 주소 입력 ')
    print('2. 주소 출력 ')
    print('3. 주소 삭제 ')
    print('4. 종료 ')
    choice = int(input('메뉴를 선택해주세요?......  =>  '))
    if choice == 1:
        # 주소입력함수 호출
        inputData()
    elif choice == 2:
        # 출력함수 호출
        printAddr()
    elif choice == 3:
        # 삭제함수 호출
        delData()
    elif choice == 4:
        break

# Db 종료
conn.close()
