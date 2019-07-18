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

# 레코드 보기
def showBook():
    print('-' * 10)
    print('BOOK LIST')
    cursor.execute('SELECT * FROM bookTBL;')
    bookList = cursor.fetchall()
    for i in bookList:
        print(i)
    print('-' * 10)

# showBook()

# 레코드 삽입
def insertBook():
    print('-' * 10)
    print('INSERT DATA')
    title = input(" 책 이름 => ")
    writer = input(" 저자 => ")
    page = int(input(" 페이지 수 => "))
    price = int(input(" 가격 => "))
    # title, writer, page, price
    sql = '''
            INSERT INTO bookTBL(title, writer, page, price)
                VALUES(%s, %s, %s, %s)
          '''
    cursor.execute(sql, (title, writer, page, price))
    conn.commit()

# insertBook()
# showBook()

# 레코드 삭제
showBook()
'''
삭제할 책 번호는?  
데이타가 삭제되었습니다.
책목록 모두 표시 
'''

# 레코드 삭제
def deleteBook():
    print('-' * 10)
    print('DELETE DATA')
    id = input(" 삭제할 책 번호는?   ")

    sql = '''
            DELETE FROM bookTBL
                WHERE id = %s
          '''
    cursor.execute(sql, (id))
    conn.commit()
    print('데이타가 삭제되었습니다.')

# deleteBook()
# showBook()

# DB 종료
# conn.close()

def end():
    # DB 종료
    conn.close()

def update():
    # 수정할 책 번호는?
    # 선택? (1.책제목 2.저자  3.페이지수  4.가격 )
    # 1
    # 변경내용 => 파이썬
    # 내용이 수정되었습니다.
    pass

# 선택에 따라서 함수가 호출되도록 무한루프 작성
while(True):
    choice = int(input('1.목록보기 2.추가 3. 수정 4. 삭제  0. 종료 \n =>  '))
    if choice == 1:
        showBook()
    elif choice == 2:
        insertBook()
    elif choice == 3:
        update()
    elif choice == 4:
        deleteBook()
    elif choice == 0:
        end()
        break




