# flask 모듈 임포트
from flask import Flask, render_template, request
# 세션 기능을 위한 모듈
from flask import session

# flask 객체 생성
app = Flask(__name__)

# 세션을 위한 비밀키 설정
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    return '세션이 있는가? <a href="/session_set">세션설정</a>'


@app.route('/session_set')
def session_set():
    # 자동 세션
    # session[변수] = 값
    session['ID'] = 'test1234'
    return '세션이 설정됨. <a href="/session_out">세션해제</a>'


@app.route('/session_out')
def session_out():
    # 세션제거 명령어 del session[변수]
    del session['ID']
    return '세션이 제거됨.  <a href="/">처음으로 이동</a>'


# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)
