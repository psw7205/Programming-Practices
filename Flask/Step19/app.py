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
    db.addDb_country(c_code, c_name, c_gnp)

    # return 'sucess'
    return render_template('index.html')


@app.route('/delete_country')
def delete_country():
    # 전체 목록 리스트 저장
    country_list = db.get_country_list()
    return render_template('delete_country.html', country_list=country_list)


@app.route('/deleteDb', methods=['GET'])
def deleteDb():
    # 하이퍼링크 버튼의 주소에서 넘어온 변수
    c_name = request.args['c_name']
    # 삭제하는 함수
    db.deleteDb_country(c_name)
    country_list = db.get_country_list()
    # return 'sucess'
    return render_template('country_list.html', country_list=country_list)


@app.route('/update_country')
def update_country():
    country_list = db.get_country_list()

    return render_template('update_country.html', country_list=country_list)


@app.route('/updateDb', methods=['GET'])
def updateDb():
    c_code = request.args['c_code']
    c_name = request.args['c_name']
    c_gnp = request.args['c_gnp']

    # return 'sucess'
    return render_template('update_form.html', c_code=c_code, c_name=c_name, c_gnp=c_gnp)


@app.route('/update_country_pro', methods=['post'])
def update_country_pro():
    # 제작해야함
    # return 'sucess'
    c_name = request.form['c_name']
    c_gnp = request.form['c_gnp']
    db.updateDb_country(c_gnp, c_name)
    return render_template('index.html')


# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)
