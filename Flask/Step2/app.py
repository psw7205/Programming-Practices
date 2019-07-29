# flask 모듈 임포트
from flask import Flask
# html 연결 페이지 기능 모듈 임포트
from flask import render_template

# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
# 함수 등록
# def hello():
#     return 'Hello world  <a href="http://google.com" target="_blank">Google</a>'
# 루트주소와 연결된 html 페이지 등록 함수.
# html 파일의 기본 폴더 위치는 templates
def index():
    return render_template('index.html')

# 라우터 등록 2
@app.route('/first')
def first():
    return render_template('first.html')

# 라우터 등록 3
@app.route('/second')
def second():
    return render_template('second.html')

# 라우터 등록 4
@app.route('/third')
def third():
    return render_template('third.html')


# 앱 실행
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)

# 결과 확인은?
# 터미널창에서 python app.py
# 주소가 표시되면 [Ctrl]누른 상태에서 클릭
# 서버종료시에는
# 터미널창에서 [Ctrl]+[C]
