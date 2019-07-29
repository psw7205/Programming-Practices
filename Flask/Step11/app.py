# flask 모듈 임포트
from flask import Flask, render_template, request

# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    return render_template('index.html')

# POST 방식으로 값을 전달받아서 특정 변수에 저장하기
# 데이타변수1 = request.form['텍스트필드이네임값변수']
@app.route('/result', methods=['POST'])
def result():
    data1 = request.form['data1']
    data2 = request.form['data2']
    print(data1, data2)
    return render_template('result.html', data1=int(data1), data2=int(data2))


# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)
