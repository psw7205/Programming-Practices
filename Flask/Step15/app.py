# flask 모듈 임포트
from flask import Flask, render_template, request

# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/bbs')
def bbs():
    return render_template('bbs.html')


@app.route('/news')
def news():
    return render_template('news.html')


# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)
