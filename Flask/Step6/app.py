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
def formGet():
    return render_template('formPost.html')


@app.route('/result', methods=['POST'])
def result():
    # POST로 전달한 데이타값을 변수에 저장
    # 변수명1 = request.form['변수명2']
    data1 = request.form['data1']
    data2 = request.form['data2']
    # return 'data1 : ' + data1 + ' / data2 :  ' + data2
    # f함수로 출력하기
    # f' 문자열 {데이타변수} '
    return f'data1 :  {data1} ,  data2 :   {data2}'


# 앱 실행
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)

# 결과 확인은?
# 터미널창에서 python app.py
# 주소가 표시되면 [Ctrl]누른 상태에서 클릭
# 서버종료시에는
# 터미널창에서 [Ctrl]+[C]
