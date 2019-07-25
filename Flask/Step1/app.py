# flask 모듈 임포트
from flask import Flask

# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
# 함수 등록
def hello():
    return 'Hello world <a href="http://google.com" target="_blank">Google</a>'


# 앱 실행
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)

# 결과 확인은?
# 터미널창에서 python app.py
# 주소가 표시되면 [Ctrl]누른 상태에서 클릭
# 서버종료시에는
# 터미널창에서 [Ctrl]+[C]
