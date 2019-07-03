# 입력문
# 변수명 = input(메세지)
# 변수명의 데이타형은 문자열이다.
inData1 = input('숫자1 입력 : ')
inData2 = input('숫자2 입력 : ')
print( '입력값 출력 : ' , inData1, inData2)

# 데이타형 확인하기
print('데이타 형 : ' , type(inData1), type(inData2))
# 기본자료형 : 숫자, 문자열, 논리형
print(type(100)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type('문자열 자료')) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type(False)) # <class 'bool'>

# 자료형 변환 - Casting
# int(), float(), str()
num1 = 123
num2 = '500'
print('-'*10)
print(num1, num2)
print(type(num1), type(num2))
print('-'*10)
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
print(myNum1 , ' + ', myNum2, ' = ', myNum1+myNum2)
print(myNum1 , ' - ', myNum2, ' = ', myNum1-myNum2)
print(myNum1 , ' * ', myNum2, ' = ', myNum1*myNum2)
print(myNum1 , ' / ', myNum2, ' = ', myNum1/myNum2)

# 산술연산자
# +, - , *, /, //(정수형 몫), %(나머지), **(제곱)
print(100/7) # 실수형 14.285714285714286
print(100//7) # 정수형 14
print(100%7) # 나머지  2
print(10**3) # 1000

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
print( 100 > 10 )
print( 100 <= 10 )
print( 100 == 10 )
print( 100 is 10 ) # is 는 ==

# 논리 연산자
# and, or, not
x = 10
y = 100
print( (x<y) and (x==y) ) # False
print( (x<y) or (x==y) ) # True
print( not(x<y) ) # False
























