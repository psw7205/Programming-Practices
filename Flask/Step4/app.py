# flask 모듈 임포트
from flask import Flask
# html 연결 페이지 기능 모듈 임포트
from flask import render_template
# request 모듈 임포트
from flask import request

# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def form():
    return render_template('form.html')

# 라우터 등록시 메소드 지정하기
# methods=['GET']
# methods=['POST']
# methods=['GET','POST']


@app.route('/result', methods=['GET', 'POST'])
def result():
    # request.method는 입력되는 메소드의 방식을 표시한다.
    print('요청방식 확인하기', request.method)
    # GET, POST 방식에 따라 서로다른 페이지로 분기된다.
    if request.method == 'POST':
        return render_template('post.html')
    else:
        return render_template('get.html')


# 앱 실행
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)

# 결과 확인은?
# 터미널창에서 python app.py
# 주소가 표시되면 [Ctrl]누른 상태에서 클릭
# 서버종료시에는
# 터미널창에서 [Ctrl]+[C]
