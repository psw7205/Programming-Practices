# 함수 정의 1
# 인자가 없다. return이 없다.
'''
# 함수 정의
def 함수명():
    명령문

# 호출시
함수명()

'''


# 3번 Hello world 출력하는 함수 정의
def helloWorld():
    print('Hello World')
    print('Hello World')
    print('Hello World')
    print('-' * 30)


# 함수 호출
helloWorld()
helloWorld()

# 함수 정의 2
# 인자가 있다. return이 없다.
'''
# 호출
def 함수명(인자1,인자2..):
    인자가 있는 명령문
    
# 정의
함수명(인자1,인자2..)    
'''


def helloWorld2(word):
    print(word)
    print('Hello ', word)
    print('Hello ', word)
    print('Hello ', word)
    print('-' * 30)


helloWorld2('Python')
helloWorld2('World')


# 두개의 값을 인자로 전달한 후
# 사칙연산과 나머지 결과값 출력
def cal(a, b):
    print(' a + b = ', a + b)
    print(' a - b = ', a - b)
    print(' a * b = ', a * b)
    print(' a / b = ', a / b)
    print(' a % b = ', a % b)
    print('-' * 30)


cal(10, 3)
cal(100, 20)


# 퀴즈 :
# 위에서 정의한 cal() 함수의 결과값을
# 아래와 같이 출력되도록 한다.
# '%d 나 %.소숫점f'% (변수1, 변수2) 이용한다
# 결과 =>
# 10 + 3 =  13
# 10 - 3 =  7
# 10 * 3 =  30
# 10 / 3 =  3.33
# 10 % 3 =  1

def cal2(a, b):
    print(' %d + %d = %d ' % (a, b, a + b))
    print(' %d - %d = %d ' % (a, b, a - b))
    print(' %d * %d = %d ' % (a, b, a * b))
    print(' %d / %d = %.2f' % (a, b, a / b))
    # %% 는 2번 입력
    print(' %d %% %d = %d ' % (a, b, a % b))
    print('-' * 30)


cal2(10, 3)
cal2(33, 5)

# 함수 정의 3
# 인자가 있다. return이 있다.
'''
# 호출
def 함수명(인자1,인자2..):
    인자가 있는 명령문
    return 변수/수식 

# 정의
함수명(인자1,인자2..)    
'''


def helloWorld3(word):
    # return 아래의 명령은 실행되지 않는다.
    # return
    print('-' * 30)
    return print('Hello  ' + word)


helloWorld3('Java')
helloWorld3('C')
helloWorld3('Python')


# 3수의 합을 return 하여라
def sumThree(n1, n2, n3):
    return n1 + n2 + n3


print('3수의 합 = ', sumThree(23, 55, 100))

print('-' * 30, '\n\n')
# 1~100 까지의 합 구하기
resultSum = 0
for i in range(1, 101):
    resultSum += i
print(resultSum)

print('-' * 30, '\n\n')


# 1~ n 까지의 합 구하기 함수 정의
def sumN(n):
    resultSum2 = 0
    for i in range(1, n + 1):
        resultSum2 += i
    return resultSum2


print('1 부터 {} 까지의 합 : {}'.format(50, sumN(50)))
print('1 부터 {} 까지의 합 : {}'.format(100, sumN(100)))

# 퀴즈 : 별찍기
# 함수로 정의한 후 호출하여라.
# for i in range(1,6):
#     print('* '*i)

'''
starPrint(5) 

결과 :
*
**
***
****
*****

starPrint(3) 

결과 :
*
**
***
'''
# 함수 사용전
for i in range(1, 6):
    print('* ' * i)


# 함수 정의
def starPrint(n):
    print('-' * 30)
    for i in range(1, n + 1):
        print('* ' * i)


starPrint(10)
starPrint(5)

# 퀴즈 :
# 리스트 각각 아이템을 출력하는 함수를 정의하여라
#
# 함수를 사용하지 않은 경우
# for 인덱스변수 in 리스트/튜플/집합/문자열:
#   print(인덱스변수)

# 함수 사용전
cnt = 0
for i in ['초밥', '햄버거', '스테이크', '떡국']:
    print(cnt, ' : ', i)
    cnt += 1


#
# 결과 =>
# printList(['초밥', '햄버거', '스테이크', '떡국'])
# 0  :  초밥
# 1  :  햄버거
# 2  :  스테이크
# 3  :  떡국

# 함수 정의
def printList(food):
    print('\n\n   Result   ')
    cnt = 1
    for i in food:
        print(cnt, ' : ', i)
        cnt += 1


# 함수 호출
printList(['라면', '빙수'])
printList(['모밀', '탕수육', '육계장'])

# 함수 정의 4
# return 결과값이 다중인 함수
'''
# 정의
def 함수명(인자1,인자2..):
    인자가 있는 명령문
    return 결과1, 결과2 ...

# 호출
함수명(인자1,인자2..)
'''


# 두개의 숫자값을 인자로 전달해서
# 합과 차를 return 한다.
def sumAndDef(n1, n2):
    return n1 + n2, n1 - n2


print('두수의 합과 차 ', sumAndDef(100, 50))
print('두수의 합과 차 ', sumAndDef(55, -20))

# 함수 정의 5
# 인자에 초기값이 있다
'''
# 정의
def 함수명(인자1=초기값1, 인자2=초기값2):
    인자가 있는 명령문
    return 결과

# 호출
함수명()
함수명(인자1,인자2..)
'''


# 하나의 인자값을 받아서 출력한다.
# 인자값이 없으면 '없다' 로 출력
def printWord(word='없다'):
    print('오늘의 키워드 --- ', word)


# 인자가 있는 경우에는 인자값으로 출력
printWord('함수')
# 인자가 없다면 초기값이 출력
printWord()


# 두개의 인자값을 받아서 더한다
# 두개 모두 인자의 초기값을 지정한 경우
def sumTwo(n1=0, n2=5):
    return n1 + n2


print(sumTwo(10, 20))  # 30
print(sumTwo(20))  # 25
print(sumTwo())  # 5


#
# 두개의 인자중 하나만 초기값을 지정한 경우
# 주의 사항1  : 마지막 인자 부터 초기값을 지정한다.
# 주의 사항2
# : 인자가 모두 없는 경우에는 오류 발생
# : 초기값을 지정한 외의 인자는 값을 전달해야한다.
def sumTwo2(n1, n2=0):
    return n1 + n2


print(sumTwo2(10, 20))  # 30
print(sumTwo2(20))  # 20
# 오류 발생
# print(sumTwo2())

# 퀴즈 :
# 세수의 곱을 출력한다.
# 출력 양식
# ? X ? X ? = 20

# def multiTest(n1=?, n2=?, n3=?):
# 명령어

# def multiTest()
# def multiTest(20)
# def multiTest(30,20)
# def multiTest(30,20,70)
# 함수 정의 6
# 가변인자를 이용한 함수 정의
# 인자가 정해지지 않은 함수
# 결과값은 튜플
'''
# 정의
def 함수명(*args):
    인자 args 있는 명령문
    return 결과

# 호출
함수명(인자)
함수명(인자1,인자2..)
함수명(인자1,인자2,인자3)
'''


# 가변인자를 받아서 출력한다.
def printM(*args):
    print(args)
    print(type(args))
    # 한개씩 출력
    for i in args:
        print(i)


printM(100)
printM('함수', '제어문', '클래스')


# 가변인자를 이용해서 n개의 합 구하기
def sumArgs(*args):
    result = 0
    for i in args:
        result += i
    return result


print(sumArgs(10, 20, 30))
print(sumArgs(10, 20))
print(sumArgs(10, 20, 100, 300, -20))

# 함수 정의 7
# 인자와 가변인자가 함께 정의된 경우
# 가변인자가 마지막에 정의되어야 한다.
'''
# 정의
def 함수명(인자, *args):
    인자가 있는 명령문 
    인자 args 있는 명령문
    return 결과

# 호출
함수명(인자, 가변인자)
함수명(인자, 가변인자1, 가변인자2 ...)
'''


def printTest(symbol, *args):
    print('인자 = ', symbol)
    print('가변인자 = ', args)
    print('-' * 30)


printTest('*', 10)
printTest('-', 10, '가나다')
printTest('+', '파이썬', '자바', '자바스크립트')

# 퀴즈
# 다음 함수를 호출하면 계산 결과가 출력되도록
# 가변인자와 인자를 정의하여라

# def calChoice(계산기호인자, *args) :
#     if 계산기호인자 == *:
#           명령문1
#     elif 계산기호인자 == +:
#           명령문2
#     else:
#           명령문3

# calChoice('*', 20,30)
# 계산결과 : 곱 : 600
# calChoice('+', 20,30,50)
# 계산결과 : 합 : 100

# 스코프(Scope) ?
# 변수의 범위
#   - 함수안의 정의된 변수와 함수밖의 변수 범위
# 전역변수 : 파일 전체에서 사용되는 변수
# 지역변수 : 함수내에서 사용되는 변수
# global 변수 : 함수안에서 전역변수를 사용할 때 사용

# 전역변수 정의
v = 10
print('테스트1 : v 값은?', v)  # 10


# 함수내의 같은 변수값 테스트
def testScope():
    # 지역 변수
    v = 20
    print('함수내의 v 값은?', v)


# 함수 호출
testScope()  # 20

print('테스트2 : v 값은?', v)  # 10

print('-' * 20)

# 전역변수 정의
v1 = 10
print('테스트1 : v1 값은?', v1)  # 10


# 함수내의 같은 변수값 테스트
def testScope2():
    # 전역 변수 정의
    # global 변수명
    global v1

    print('함수내의 v 값은?', v1)  # 10

    # 전역 변수에 값 할당
    v1 = 20
    print('함수내의 v 값은?', v1)  # 20


# 함수 호출
testScope2()  # 20

print('테스트2 : v1 값은?', v1)  # 20

# 람다함수 정의
# lambda 함수 = 익명함수
# define 정의문이 없다.
# 한줄로 코딩한다.
# 축약형 함수
# lambda 함수로 정의
# 함수변수 = lambda 인자:명령문
# lambda 함수 호출
# 함수변수(인자)

# 인자를 출력하는 lambda 함수 정의
f1 = lambda x: x + x
# lambda 함수 호출
print(f1(10))  # 20
print(f1('Python / '))  # Python / Python /

# 세수의 합을 구하는 lambda 함수 정의
f2 = lambda x, y, z: x + y + z
# lambda 함수 호출
print(f2(10, 20, 40))
print(f2('알라딘 ', '로미오와 줄리엣 ', '기생충 '))

# 내장함수
# 수학관련 함수
# 절대값 출력 : abs(숫자)
print('-1 =>', abs(-1))
print('10 =>', abs(10))

# 리스트의 최대값과 최소값 출력하기
# max(리스트/튜플/집합...)
# min(리스트/튜플/집합...)
print('[20, 40, 56, 100]')
print('최대값 =>', max([20, 40, 56, 100]))
print('최소값 =>', min([20, 40, 56, 100]))

print('(20, 40, 56, 100)')
print('최대값 =>', max((20, 40, 56, 100)))
print('최소값 =>', min((20, 40, 56, 100)))

# 나누기 연산자 /, //
# 나머지 연산자 %
# divmod(n1,n2) => 몫과 나머지 값을 구한다. => 튜플
print(10 / 3.2)  # 3.125
print(10 // 3.2)  # 3.0
result = divmod(100, 20)
print(result, type(result))  # (5, 0) <class 'tuple'>
# 튜플 인덱싱
print(result[0])
print(result[1])
# 값 1개씩 출력
for i in result:
    print(i)

# 5개의 값을 입력문을 이용하여 리스트로 저장한 후
# 최대값과 최소값을 출력한다.
# 빈 리스트 생성

# result = []
# for i in range(0,5):
#     # 정수 데이터로 변환
#     data = int(input('숫자를 입력해주세요 ... '))
#     result.append(data)
# print('전체 리스트 => ', result)
# print('최대 값 => ', max(result) )
# print('최소 값 => ', min(result) )

# eval(문자열계산식)
# 입력받은 수식을 계산하여라
# result = input('수식을 입력하세요? ... ')
# print(result, ' = ', eval(result))

# enumerate(리스트/튜플/문자열 , 인덱스숫자 )
# 인덱스숫자로 구성된 리스트/튜플/문자열
# => enumerate 객체 생성
# => for .. in 하나씩아이템 출력 가능
# => 각각 튜플아이템으로 생성 (인덱스, 값)
listA = ['a', 'b', 'c']
enumResult = enumerate(listA, 5)
print(enumResult, type(enumResult))
for i in enumResult:
    print(i)  # (인덱스번호, 값)

# 한개씩 출력하기
for i, v in enumerate(listA, 5):
    print(i, ' => ', v)

# 문자열 변환
for i, v in enumerate('abcd', 1):
    print(i, ' => ', v)


# map() 함수

# 제곱을 구하는 함수 정의
def doubleMulti(x):
    return x ** 2


print(doubleMulti(3))  # 9
print(doubleMulti(-10))  # -10
print(doubleMulti(5))  # 25
print(doubleMulti(7))  # 49

# map() 사용
mapResult = map(doubleMulti, [3, -10, 5, 7])
print(mapResult, type(mapResult))
# <map object at 0x00A4FA10> <class 'map'>

# 한개씩 값 출력하기
for i in map(doubleMulti, [3, -10, 5, 7]):
    print(i, end=' ')

print('\n\n')
# 리스트화
print(list(map(doubleMulti, [3, -10, 5, 7])))
