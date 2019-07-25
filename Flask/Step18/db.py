# 데이타베이스 관리 파일
import mysql.connector

# 데이타베이스 접속 함수


def get_connection():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='test',
        password='0000',
        db='sample',
        charset='utf8')

    return conn

# 레코드를 출력하는 함수


def get_country_list():

    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()

    # 쿼리문 생성
    sql = ''' SELECT Code, Name, GNP 
                FROM sample.GNPCountry 
                ORDER BY GNP DESC   '''

    cursor.execute(sql)

    # 리스트 생성
    country_list = cursor.fetchall()

    # 데이타베이스 종료
    conn.close()

    return country_list


# print(get_country_list())

# 레코드 추가 함수
def addDb_country(c_code, c_name, c_gnp):
    sql = '''
            insert into sample.GNPCountry
                (code, name, gnp)
                values (%s, %s, %s)
            '''
    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()
    cursor.execute(sql, (c_code, c_name, c_gnp))
    conn.commit()

    conn.close()
