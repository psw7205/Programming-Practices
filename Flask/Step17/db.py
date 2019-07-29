# 데이타베이스 관리 파일
import mysql.connector

# 데이타베이스 접속 함수


def get_connection():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='test',
        password='0000',
        db='world',
        charset='utf8')

    return conn

# 레코드를 출력하는 함수


def get_country_list():

    # 데이타베이스 접속함수 호출
    conn = get_connection()

    # 작업변수 생성
    cursor = conn.cursor()

    # 쿼리문 생성
    sql = 'SELECT Code, Name, GNP FROM world.country ORDER BY GNP DESC'
    cursor.execute(sql)

    # 리스트 생성
    country_list = cursor.fetchall()

    # 데이타베이스 종료
    conn.close()

    return country_list
