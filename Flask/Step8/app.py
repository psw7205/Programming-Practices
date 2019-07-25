# flask 모듈 임포트
from flask import Flask, render_template, request

# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    # 리스트 생성
    test_list = [100, 200, 300, 400]
    print(test_list, type(test_list))
    # 튜플 생성
    test_tuple = ('가', '나', '다', '라')
    print(test_tuple, type(test_tuple))
    # 딕셔너리 생성
    test_dict = {'key1': 70, 'key2': 1000, 'key2': 55, }
    print(test_dict, type(test_dict))
    # 변수 생성
    userName = '홍길동'
    return render_template('index.html',
                           test_list=test_list, test_tuple=test_tuple,
                           test_dict=test_dict, userName=userName)


# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)
