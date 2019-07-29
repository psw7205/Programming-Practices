# flask 모듈 임포트
from flask import Flask, render_template, request

# flask 객체 생성
app = Flask(__name__)

# 라우터 등록 => 웹상 루트 주소 생성
@app.route('/')
def index():
    return render_template('index.html')

# GET 방식으로 값을 전달받아서 특정 변수에 저장하기
# 데이타변수1 = request.args['데이타변수']
@app.route('/result', methods=['GET'])
def result():
    userAge = request.args['userAge']
    print(userAge, type(userAge))
    return render_template('result.html', userAge=userAge)


@app.route('/result2', methods=['GET'])
def result2():
    num = request.args['num']
    print(num, type(num))
    sum = 0
    for i in range(1, int(num)+1):
        sum += i
    print(sum)
    return render_template('result2.html', num=num, sum=sum)


@app.route('/result3', methods=['GET'])
def result3():
    num1 = request.args['num1']
    num2 = request.args['num2']
    num3 = request.args['num3']
    print(num1, num2, num3)
    return render_template('result3.html', num1=int(num1),
                           num2=int(num2), num3=int(num3))


# 앱 실행  --> 마지막 위치 유지
# 웹주소와 포트 지정
app.run(host='127.0.0.1', port=5000, debug=True)
