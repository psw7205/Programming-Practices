# flask 모듈 임포트
from flask import Flask, render_template, request

# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    return render_template('index.html')

# 라우터 등록
@app.route('/test1')
def test1():
    return 'test1 <a href="/">처음으로 이동 </a>'

# 라우터 등록
@app.route('/test1/sub1')
def test1_sub1():
    return 'test1 sub1 <a href="/">처음으로 이동 </a>'

# 라우터 등록
@app.route('/test1/sub2')
def test1_sub2():
    return 'test1 sub2 <a href="/">처음으로 이동 </a>'

# 값 전송받아서 출력하기
# 라우터 등록
@app.route('/test2/<data1>')
def test2_sub1(data1):
    # return 'data1 =>' +data1 + '<a href="/">처음으로 이동 </a>'
    return f'data1 => {data1} <a href="/">처음으로 이동 </a>'

# 라우터 등록
@app.route('/test2/<data1>/<data2>')
def test2_sub2(data1, data2):
    return f'data1 => {data1} <br> data2 => {data2} <br> <a href="/">처음으로 이동 </a>'

# 같은 주소에 라우터 함수 사용하기
@app.route('/test3')
@app.route('/test4')
def test3_or_test4():
    return 'test3 또는 test4 <br> <a href="/">처음으로 이동 </a>'


# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)
