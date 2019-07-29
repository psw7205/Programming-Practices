# flask 모듈 임포트
from flask import Flask, render_template, request
# db 모듈 임포트
import db

# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/country_list')
def country_list():
    # 데이타베이스 레코드 출력 함수 호출
    country_list = db.get_country_list()
    # print(country_list)
    # return 'Success'
    return render_template('country_list.html', country_list=country_list)


@app.route('/add_country')
def add_country():
    return render_template('add_country.html')


@app.route('/add_country_pro', methods=['post'])
def add_country_pro():
    c_code = request.form['c_code']
    c_name = request.form['c_name']
    c_gnp = request.form['c_gnp']
    print(c_code, c_name, c_gnp)
    # db.py 에 레코드를 추가하는 함수 등록
    db.addDb_country(c_code, c_name, c_gnp)

    return render_template('index.html')


# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)
