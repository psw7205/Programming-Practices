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
    # login.html의 폼필드의 데이터값 확인
    userId = request.form['userId']
    password = request.form['password']
    print(userId, password)
    # DB의 레코드를 리스트로 저장
    member_list = db.get_member_list()

    # 레코드의 아이디와 패스워드의 아이디가 있으면 True
    # 없으면 False 역할을 하는 변수
    userIdCheck = userPwdCheck = False

    idx = 0
    # DB의 전체 레코드 값과 비교
    # len(member_list) => DB의 전체 레코드수
    # DB의 아이디값과 같으면 True
    for i in range(0, len(member_list)):
        if userId in member_list[i]['user_id']:
            userIdCheck = True
            print('userIdCheck = > ', userIdCheck)
            # 패스워드 비교를 위해서 idx 변수에 저장
            idx = i
            break
        else:
            continue

    # 폼필드의 패스워드랑 DB의 패스워드랑 비교
    if member_list[idx]['user_password'] == password:
        userPwdCheck = True
        print('userPwdCheck => ', userPwdCheck)

    # 아이디랑 비밀번호가 모두 맞다면(True) 세션 설정
    if userIdCheck and userPwdCheck:
        session['logged_in'] = True

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
