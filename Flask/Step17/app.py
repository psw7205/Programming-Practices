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


# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)
