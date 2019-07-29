# flask 모듈 임포트
from flask import Flask, render_template, request
# 세션 기능을 위한 모듈
from flask import session
# DB 파일 연결
import db

# flask 객체 생성
app = Flask(__name__)

# 세션을 위한 비밀키 설정
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    # 세션이 있는지 없는지에 따라 html 분기
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('logout.html')


# login.html 페이지에서 버튼을 눌렀을때 이동하는 라우터
@app.route('/login', methods=['POST'])
def login():
    # login.html의 폼필드의 데이값 확인
    userId = request.form['userId']
    password = request.form['password']
    print(userId, password)
    # DB의 레코드를 리스트로 저장
    member_list = db.get_member_list()
    # DB 레코드에서 첫번째 레코드값 출력 확인
    print(member_list[0][0], member_list[0][1])
    # DB 레코드의 아이디값, 비번값이 폼에서 입력한 값과 같은지 확인
    if userId == member_list[0][0] and password == member_list[0][1]:
        session['logged_in'] = True
    # return 'Success'
    # 첫페이지로 이동해서 세션 판단
    return index()


# 로그인 상태에서 로그아웃 하이퍼링크 클릭시 적용되는 라우터
@app.route('/logout')
def logout():
    session.clear()
    return index()


# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)
