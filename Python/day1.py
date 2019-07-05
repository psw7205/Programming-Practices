# 한줄 주석
'''
여러줄 주석 입니다.
주석 단축키는 ctrl + /
'''
# 출력문 print(value/variable, end='대체문자나 공백')
import keyword

print('Hello world')
print(100 + 200)
print(True)
print(100, '+', 200, '=', 100 + 200)

# 한줄로 출력하기
# print( 수식/값, end='')
a = 100
b = 200
print('----------')
print(a)
print(b)
print(a, end='')
print(b, end='')
print(a + b)
# 문자열 연산자
# + 연결
# * 반복 : 문자열*반복횟수
txt1 = '안녕하세요...'
txt2 = ' 홍길동입니다.'
print(txt1 + txt2)
print('-' * 10)

# 이스케이프 코드 : p49 참조
# \n  : 줄바꿈
# \t : 탭공백
# \\ : \ 표시
# \', \" : 인용부호 표시
print('\n' * 3)
print('\t\t 점심 시간 안내')
print('시간 \" \\ 12-1 \\ \"  ')

# 변수 할당
user1 = '철수'
user2 = '영희'
# 서로 다른 변수에 동일한 값 할당
user1Age = user2Age = 22

print('user1 : ', user1)
print('user2 : ', user2)
print('user1Age : ', user1Age)
print('user2Age : ', user2Age)

# 퀴즈 : user1과 user2의 변수값을 서로 변경하여 보세요
'''
user1 :  영희
user2 :  철수
'''
# 방법1 - 중간 변수를 이용한다.
'''
temp = user1
user1 = user2
user2 = temp
print('user1 : ', user1)
print('user2 : ', user2)
'''
# 방법2
# 변수1,변수2 = 값1,값2
print('user1 : ', user1)
print('user2 : ', user2)
user1, user2 = user2, user1
print('-' * 10)
print('user1 : ', user1)
print('user2 : ', user2)

# 변수명 규칙
# 카멜기법 : 대문자 이용 방식 예) userAge
# 스네이크기법 : _, - 이용  예) user_age
# 클래스명은 첫글자를 대문자로 한다.
# 함수명은 소문자로 한다.
# 변수명은 소문자로 시작한다.
# 예약어는 변수명으로 사용할 수 없다.

# 키워드 출력하기

print('키워드 목록 ')
print(keyword.kwlist)
print('키워드 갯수 : ', len(keyword.kwlist))

# len() : 문자열, 리스트 등의 길이를 표시한다.
today = '오늘은 화요일입니다.'
print('today 길이:', len(today))

# 입력문
# 변수명 = input(메세지)
# 변수명의 데이타형은 문자열이다.
inData1 = input('숫자1 입력 : ')
inData2 = input('숫자2 입력 : ')
print('입력값 출력 : ', inData1, inData2)

# 데이타형 확인하기
print('데이타 형 : ', type(inData1), type(inData2))
# 기본자료형 : 숫자, 문자열, 논리형
print(type(100))  # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type('문자열 자료'))  # <class 'str'>
print(type(True))  # <class 'bool'>
print(type(False))  # <class 'bool'>

# 자료형 변환 - Casting
# int(), float(), str()
num1 = 123
num2 = '500'
print('-' * 10)
print(num1, num2)
print(type(num1), type(num2))
print('-' * 10)
num3 = float(num1)
num4 = int(num2)
print(num3, num4)
print(type(num3), type(num4))

# 퀴즈 : 2개의 숫자값을 입력받은 후 사칙연산을 수행한다.
'''
첫번째 숫자를 입력하세요 ... 10
두번째 숫자를 입력하세요 ... 20
-------------
10 + 20 = 30
10 - 20 = -10
10 * 20 = 200
10 / 20 = ?

'''
myNum1 = int(input('첫번째 숫자를 입력하세요 ... '))
myNum2 = int(input('두번째  숫자를 입력하세요 ... '))
print(myNum1, ' + ', myNum2, ' = ', myNum1 + myNum2)
print(myNum1, ' - ', myNum2, ' = ', myNum1 - myNum2)
print(myNum1, ' * ', myNum2, ' = ', myNum1 * myNum2)
print(myNum1, ' / ', myNum2, ' = ', myNum1 / myNum2)

# 산술연산자
# +, - , *, /, //(정수형 몫), %(나머지), **(제곱)
print(100 / 7)  # 실수형 14.285714285714286
print(100 // 7)  # 정수형 14
print(100 % 7)  # 나머지  2
print(10 ** 3)  # 1000

# 대입연산자
# 변수명 +=/-=/*= 숫자
# 변수명 = 변수명 (+/-/*) 숫자
myNum3 = 100
print(myNum3)
myNum3 += 1
print(myNum3)

# 관계 연산자
# 결과값이 True, False
# == , !=, >, <, >=, <=
# 변수1 is 변수2
print(100 > 10)
print(100 <= 10)
print(100 == 10)
print(100 is 10)  # is 는 ==

# 논리 연산자
# and, or, not
x = 10
y = 100
print((x < y) and (x == y))  # False
print((x < y) or (x == y))  # True
print(not (x < y))  # False

################
# 문자열 인덱싱 - p51
# - 인덱싱 첫위치 값은 0
# - 인덱싱 숫자값이 음수면 역순 : -1 (마지막위치값)
# 문자열변수[인덱스값]
myString = 'abcdefg'
print('myString : ', myString)
print('myString[0] : ', myString[0])
print('myString[-1] : ', myString[-1])
print('myString[3] : ', myString[3])
print('myString[-2] : ', myString[-2])

# 문자열 슬라이싱
# 문자열변수[start:end]  : start 부터 end-1
# 문자열변수[start:end:step] : start 부터 end-1 까지 step 수만큼 건너뛰기
# 문자열변수[start:] : start 부터 끝까지
# 문자열변수[:end] : 첫번째 부터 end-1
myString2 = 'abcdefghijklmn'
print('myString2 : ', myString2)
print('myString2[0:3] : ', myString2[0:3])
print('myString2[:3] : ', myString2[:3])
print('myString2[5:] : ', myString2[5:])
print('myString2[0:5:2] : ', myString2[0:5:2])
print('myString2[-1:] : ', myString2[-1:])
print('myString2[-5:-1] : ', myString2[-5:-1])

print('\n' * 5)
# %를 이용한 포맷팅 : p58
# style : 문자열안에 입력, %s, %d, %전체자리수.소숫점자리f
# ' style ' % 변수나값
today = '수요일'
yesterday = '화요일'
print('오늘은 ', today, ' 입니다.')
print('오늘은  %s  입니다. ' % today)
print('오늘은  %s  입니다. 어저께는 %s 입니다. ' % (today, yesterday))
myNum1 = int(input('숫자를 입력하세요'))
myNum2 = float(input('숫자를 입력하세요'))
print('입력받은 값은 %d 입니다.' % myNum1)
print('입력받은 값은 %f 입니다.' % myNum2)

# %전체자릿수.소수점이하자릿수f
pi = 3.14156748
print('pi : %f' % pi)  # 3.141567
print('pi : %.3f' % pi)  # 3.142 (반올림)
print('pi : %10.2f' % pi)  # 3.14
print('pi : %3.5f' % pi)  # 3.14157
print('pi : %15.1f' % pi)  # 3.1

# % 퍼센트 기호 표시
# 오늘의 미세농도는 0.0005 % 입니다.
todayM = 0.0005
# 아래는 에러발생
# print( '오늘의 미세농도는 %f % 입니다.' % todayM)
print('오늘의 미세농도는 %f %% 입니다.' % todayM)

# %로 공백 지정
# %양수숫자Style(s,f,d) : 왼쪽에 공백 생성
# %음수숫자Style(s,f,d) : 오른쪽에 공백 생성
userName = '홍길동'
print('user Name : %10s ** ' % userName)
print('user Name : %-10s ** ' % userName)

# format 을 이용한 출력방식
# ' 문자열 {} {}'.format(변수1, 변수2)
# ' 문자열 {index1} {index2}'.format(변수1, 변수2)
color = 'blue'
myNumber = 7
# 인덱스 생략
print(' color {} number {} '.format(color, myNumber))
# 인덱스 지정
print(' 순서교체 : number {1} color {0} '.format(color, myNumber))
# 초기값 다시 지정
# 여러줄 명령 작성시는 백슬라시(\)로 연결한다.
print(' 이름지정 : number {myNumber} color {color} '
      .format(myNumber=100, color='red'))

# :>숫자 (앞에 공백생성) , :<숫자(뒤에 공백생성), :^숫자(좌우에 여백생성) : {}안에 입력
# :대체문자>숫자 (앞에 대체문자생성) , :대체문자<숫자(뒤에대체문자생성)
# :대체문자^숫자(좌우에 대체문자)
print('... {} ...'.format('hello world'))
print('... {:>30} ...'.format('hello world'))
print('... {:<30} ...'.format('hello world'))
print('... {:^30} ...'.format('hello world'))
print('... {:*^30} ...'.format('hello world'))

# 문자열 함수
# 샘플문자열 만들기 : https://www.lipsum.com/
# Lorem Ipsum 키워드 검색
sampleTxt = '''
It is a long established fact t
hat a reader will be distracted by the readable 
content of a page when looking at its layout. 
The point of using Lorem Ipsum is 
that it has a more-or-less normal distribution 
of letters, as opposed to using 'Content here, c
ontent here', making it look like readable English. 
Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, 
sometimes on purpose (injected humour and the like).
'''

# 특정 문자열의 갯수 출력
# 문자열.count(찾고자하는문자열)
print('t의 갯수 : ', sampleTxt.count('t'))
print('here의 갯수 : ', sampleTxt.count('here'))

# 특정글자의 위치값 반환
# 문자열.find(찾고자하는문자열)
# 문자열.index(찾고자하는문자열)
print(' f => ', sampleTxt.find('f'))
print(' f => ', sampleTxt.index('f'))
# 찾고자하는 문자열 없다면 -1
print(' 가 => ', sampleTxt.find('가'))
# 찾고자하는 문자열 없다면 ValueError 에러 발생
# print(' 가 => ', sampleTxt.index('가'))
