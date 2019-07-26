# 데이타베이스 관리 파일
import mysql.connector


# 데이타베이스 접속 함수
def get_connection():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='test',
        password='0000',
        # 사용할 DB명 확인
        db='sample',
        charset='utf8')
    return conn


# 레코드를 출력하는 함수
def get_member_list():
    # 데이타베이스 접속함수 호출
    conn = get_connection()
    # 작업변수 생성
    cursor = conn.cursor()
    # 쿼리문 생성
    sql = ''' SELECT *
                FROM sample.member  '''
    cursor.execute(sql)
    # 리스트 생성
    member_list = cursor.fetchall()
    # 리스트안에 딕셔너리 스타일로  구조 변경
    temp_list = []
    for i in member_list:
        temp_dic = {}
        # 키값으로 저장
        temp_dic['user_id'] = i[0]
        temp_dic['user_password'] = i[1]
        temp_list.append(temp_dic)
    # 데이타베이스 종료
    conn.close()
    return temp_list


# 레코드 추가 함수
def addDb_member(user_id, user_password):
    sql = '''
            insert into sample.member
                values (%s, %s)
            '''
    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()
    cursor.execute(sql, (user_id, user_password))
    conn.commit()
    conn.close()
