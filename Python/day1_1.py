# 한줄 주석
'''
여러줄 주석 입니다.
주석 단축키는 ctrl + /
'''
# 출력문 print(value/variable, end='대체문자나 공백')
print('Hello world')
print(100+200)
print(True)
print(100,'+',200,'=',100+200)

# 한줄로 출력하기
# print( 수식/값, end='')
a = 100
b = 200
print('----------')
print(a)
print(b)
print(a, end='')
print(b, end='')
print(a+b)
# 문자열 연산자
# + 연결
# * 반복 : 문자열*반복횟수
txt1 = '안녕하세요...'
txt2 = ' 홍길동입니다.'
print( txt1 + txt2)
print('-'*10)

# 이스케이프 코드 : p49 참조
# \n  : 줄바꿈
# \t : 탭공백
# \\ : \ 표시
# \', \" : 인용부호 표시
print('\n'*3)
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
user1,user2 = user2, user1
print('-'*10)
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
import keyword
print('키워드 목록 ')
print(keyword.kwlist)
print('키워드 갯수 : ', len(keyword.kwlist) )

# len() : 문자열, 리스트 등의 길이를 표시한다.
today = '오늘은 화요일입니다.'
print('today 길이:', len(today))





































