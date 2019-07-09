# 함수의 종류
# 사용자정의 함수
# - def 명령으로 함수명 정의
# - lambda 함수 : 익명함수
# 외장함수 : import 외장모듈이나 패키지
# 내장함수 : import 명령없이 사용할 수 있는 함수
# abs(), max(), min(), divmod()
# eval()
# enumerate(), map()

# sorted(리스트/튜플/집합..)
# : 데이타 정렬
# : 결과값을 리턴한다. => print()로 바로 출력
# 리스트이름.sort() : 리스트정렬
# 리스트이름.reverse() : 리스트 역정렬
myList = ['b', 'a', 'c', 'x']
print(myList.sort())  # None
myList.sort()
print(myList)  # ['a', 'b', 'c', 'x']
myList.reverse()
print(myList)  # ['x', 'c', 'b', 'a']

# 바로 출력 가능
print(sorted(['b', 'a', 'c', 'x']))  # ['a', 'b', 'c', 'x']

# 유효성 검사?
# 데이터(숫자, 문자...)가 조건에 맞는지 검사하는 기능
# 문자열변수.isalpha() : 모두 문자인가? 숫자문자제외 , True/Fasle
# 문자열변수.isdigit() : 모두 숫자문자인가?  , True/Fasle
str1 = 'fkfkfk'
str2 = '12345'
str3 = '1fdkjfsl2345'
print(str1.isalpha())  # True
print(str2.isalpha())  # False
print(str3.isdigit())  # False
print(str1.isdigit())  # False
print(str2.isdigit())  # True

# 퀴즈
# 빈 리스트를 생성한다.
# 입력문이 실행된다.
# 입력값이 숫자이면 리스트에 추가한다.
# 입력값이 숫자가 아니면 다시 입력문이 실행된다.
# 리스트의 전체길이가 5이면 입력을 종료한다.
# 리스트를 출력한다.

# resultList = []
# print(resultList, type(resultList)) # [] <class 'list'>
# # 입력값을 받을 수 있게 while 문 생성
# while True:
#     data = input('데이타를 입력해주세요?....')
#     # # 입력 데이타를 리스트에 추가한다.
#     # resultList.append(data)
#     # 숫자이면 리스트 추가
#     if data.isdigit():
#         resultList.append(data)
#         print('리스트가 추가되었습니다.')
#     else:
#         print('숫자가 아닙니다. 다시 입력해주세요 ')
#     # 탈출 조건
#     if len(resultList) == 5:
#         break
# # 리스트 출력
# print(resultList)

# 퀴즈 : 문자열에서 숫자와 숫자가아닌문자의 갯수를 출력하여라
# testWord = 'Python1234Java4774'
'''
결과 >>
숫자 갯수 : ? 
문자 갯수 : ?
'''
# 문자열변수 정의
# 숫자갯수를 저장할 변수 정의 : cnt
# 반복문 생성 : 문자열에서 숫자라면 : cnt += 1 값을 증가시킨다.
# 숫자갯수 출력
# 문자갯수는? len(문자열변수)-cnt

testWord = 'Python1234Java4774'
cnt = 0
for i in testWord:
    if i.isdigit():
        cnt += 1
print('숫자갯수 : ', cnt)
print('문자갯수 : ', len(testWord) - cnt)

# zip(리스트1, 리스트2 .. )
# : 리스트의 각 아이템요소를 튜플화 구조로 묶어준다.
# : [(아이템1,아이템2) ...]
# zip(*zip객체)
# : zip으로 묶어준 객체를 원래대로 풀어준다.
p1 = ['길동', '동미', '미영', '영철']
p1Gender = ['남', '여', '여', '남']
# zip 객체로 출력
print(zip(p1, p1Gender))
# 하나씩 출력
for i in zip(p1, p1Gender):
    print(i)

# 각각 구분자로 분리해서 출력
for i, j in zip(p1, p1Gender):
    print(i, '-', j)
# 리스트화
print(list(zip(p1, p1Gender)))

# zip으로 리스트안의 튜플구조 해제하기 - unzip
# 변수1, 변수2 = zip(*리스트튜플이름)
# 결과물은 같은 인덱스의 값만 튜플로 다시 생성
myList2 = [('a', 'apple'), ('b', 'banana'), ('c', 'cat')]
print(myList2, type(myList2))
x, y = zip(*myList2)
print(x)  # ('a', 'b', 'c')
print(y)  # ('apple', 'banana', 'cat')


# filter()
# filter(함수명, 리스트) => 참인조건의 리스트만 출력
# 사용할 함수는 결과값이 True/False

# 양수인지 판독하는 함수 정의
def positive(x):
    return x > 0


print(positive(-10))  # False
print(positive(10))  # True

numlist = [10, -30, 20, 5, -100]
# 객체 출력 : <filter object at 0x01DAFB30>
print(filter(positive, numlist))
# 리스트화 : 양수만 추출
print(list(filter(positive, numlist)))
# for .. in 으로 출력
for i in filter(positive, numlist):
    print(i)

# 리스트 중 짝수만 출력하기 = filter() 함수 이용
# 짝수인지 판독하는 함수 정의
# 리스트 정의
# filter() 함수 적용 => filter 객체
# filter 객체를 리스트화

print('-' * 30)


def evenJudge(x):
    return x % 2 == 0


numList2 = [12, 5, 30, 44, 33]
print(list(filter(evenJudge, numList2)))
for i in filter(evenJudge, numList2):
    print(i)

# 현재 작업폴더 위치 확인하기
# python.exe 위치 , 현재 파이썬 파일 정보 출력
import os

print(os.getcwd())

# 파일입출력
# 파일읽기
# read() : 파일전체 문자열 구조
# readline() : 파일에서 첫줄만 읽기
# readlines() : 각행이 리스트 구조로 변경
# 파일변수 생성
# 파일변수  = open(파일경로, 'r')
f = open('data/Yesterday.txt', 'r')
# io 객체 출력
# <_io.TextIOWrapper name='data/Yesterday.txt' mode='r' encoding='cp949'>
print(f)
# 문서 전체가 출력
data = f.read()
print(data)
# <class 'str'> 문자열
print(type(data))
# 첫글자만 추출
print(data[0])
# 10글자만 추출
print(data[0:10])

# 문서는 몇개의 단어로 구성되어 있을까?
# 단어별로 구성해서 리스트 구조로 변경
# 문자열변수.split() => 공백기준으로 리스트로 변경
dataList = data.split()
# 10개만 출력
print(type(dataList))
print(dataList[:3])
print('단어 수? => ', len(dataList))
# 파일 닫기 - 명령실행 뒤에 배치
f.close()

# 퀴즈
# 파일의 단어전체수와 3개의 단어가
# 표시되는 함수를 정의하여라
'''
>> 함수호출
printWord('data/sample.txt')
printWord('data/Yesterday.txt')

>> 결과값 
파일명 : data/sample.txt
단어 갯수 : 134
단어 3개 출력 
['Yesterday', 'All', 'my']
'''

# def printWord(fileUrl):
#     f = open(fileUrl, 'r')
#     data = f.read()
#     ?
#     f.close()

# printWord('data/sample.txt')
# printWord('data/Yesterday.txt')

# 파일 쓰기
# 새로운 파일이 생성되면서 내용이 추가된다.
# 기존에 파일이 있다면 덮어쓰기된다.
# 파일변수 = open( 생성파일경로, 'w')
# 파일변수.write(문자열)
# 파일변수.close()

import os

print(os.getcwd())

# 빈파일 만들기
f = open('data/test1.txt', 'w')
print(' 파일이 생성되었습니다. ')
f.close()

# 파일 생성후 내용 추가하기
f = open('data/test1.txt', 'w')
print(' 파일이 생성되었습니다. ')
f.write('-' * 10)
f.write('\n 테스트 중입니다.\n')
f.write('-' * 10)
# 10 줄 추가하기
for i in range(1, 11):
    f.write('\n %d 번째 줄입니다. ' % (i))
f.close()

# 리스트요소를 정의한 후
# 리스트요소를 파일에 행단위로 저장한다.
myFoodList = ['라면', '김치전', '모밀', '초밥', '샐러드']
line = open('data/myFoodList.txt', 'w')
line.write('\n음식 메뉴\n')
for i in myFoodList:
    print(i)
    data = i + '\n'
    line.write(data)
    print('내용이 추가되었습니다.')
line.close()

# 파일을 읽은후 결과값 출력하기
# Yesterday.txt 파일에서 5줄만 추출해서
# resultYesterday.txt 파일에 저장하기
# 파일변수1 = open(읽을파일경로, 'r')
# 리스트변수 = f.readlines()
# 파일변수2 = open(저장할파일경로, 'w')
# for i in ?:
#   파일변수2.write(i)
# 파일변수1.close()
# 파일변수2.close()

f1 = open('data/Yesterday.txt', 'r')
f2 = open('data/resultYesterday.txt', 'w')
resultList = f1.readlines()
for i in resultList[0:5]:
    dataLine = i + '\n'
    f2.write(dataLine)
    print('퀴즈 내용이 추가되었습니다.')
f1.close()
f2.close()

# 내용추가하기
# 기존 파일에 내용이 추가된다.
# 파일변수 = open( 생성파일경로, 'a')
# 파일변수.write(문자열)
# 파일변수.close()

f = open('data/test1.txt', 'a')
f.write('\n\n 내용 추가 테스트')
print('새로운 내용이 추가되었습니다.')
f.close()

f = open('data/test1.txt', 'a')
f.write('\n\n 또 내용 추가 테스트')
print('또 새로운 내용이 추가되었습니다.')
f.close()

# with 문과 파일 입출력
# 파일.close() 를 사용할 필요가 없다.
# with open(파일경로, 'a'/'w'/'r') as 파일변수:
#   명령문

with open('data/Yesterday.txt', 'r') as f:
    result = f.read()
    print(result[:10])

print('\n\n파일 읽기 테스트 완료 \n\n')

with open('data/test2.txt', 'w') as f:
    f.write('파일 쓰기 테스트 \n' * 10)

print('\n\n파일 쓰기 테스트 완료 \n\n')

with open('data/test2.txt', 'a') as f:
    f.write('내용 추가 테스트 \n' * 3)

print('\n\n 내용 추가 테스트 완료 \n\n')


# 클래스 : 특별한 자료구조
# 관련 키워드 => OOP, 인스턴스=객체
# 기본자료형(숫자, 문자열, 불른)
# 콜렉션형 (리스트, 집합, 튜플, 딕셔너리)
# 클래스 ( 속성, 함수 ...) => 틀
# 인스턴스=객체=Object
#   => 클래스에 의해서 만들어진 산출물

# 클래스 생성 문법
# 클래스이름은 첫글자는 대문자로 지정
# class 클래스이름:
#   명령문

# 빈 클래스 생성하기
class Test:
    pass


# <class '__main__.Test'> <class 'type'>
print(Test, type(Test))

# 인스턴스 생성하기
# 인스턴스명은 첫글자는 소문자로 지정
# 인스턴스변수 = 클래스이름()
# isinstance(인스턴스변수, 클래스이름)
# 특정클래스에 의해서 생성된 인스턴스가 맞는지 출력
# True / False 로 출력
testObj1 = Test()
testList = []
# <__main__.Test object at 0x02C7BE90> <class '__main__.Test'>
print(testObj1, type(testObj1))
print(isinstance(testObj1, Test))  # True
print(isinstance(testList, Test))  # False


# 생성자 함수 (Constructor)
# => 속성값 정의
# 사각형에 관련된 클래스 속성 => 가로, 세로, 색상
# 사람에 대한 클래스 속성 => 이름, 성별, 키, 몸무게
# 붕어빵에 대한 클래스 속성 => 재료, 생산시간

# 생성자함수 문법
# class 클래스명:
#   def __init__(self, 인자):
#       self.인자 = 인자값
# 인스턴스 생성
# 인스턴스명 = 클래스이름(인자값,..)
# 실제 속성값 출력
# 인스턴스명.속성

# 사각형 도형의 클래스와 생성자 함수 정의
class Square:
    # 속성을 정의하는 생성자 함수
    def __init__(self, width, height):
        self.width = width
        self.height = height


# 인스턴스화
squareObj1 = Square(100, 100);
squareObj2 = Square(40, 80);

# 실제 속성값 출력
# 인스턴스명.속성
print('squareObj1 => ', \
      squareObj1.width, squareObj1.height)
print('squareObj2 => ', \
      squareObj2.width, squareObj2.height)

print('squareObj2 => 면적 ', squareObj2.width * squareObj2.height)


# Car 클래스 생성하기
# 클래스 메소드란?
# def 메소드이름(self,인자):
#   명령어
#   return 값
# 메소드 호출
# 인스턴스명.메소드이름(인자)

class Car:
    # 생성자함수 - 속성 정의
    def __init__(self, brand, name, color, year):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year

    # 메소드 정의
    def play(self, name):
        print(name, '자동차가 달린다.')

    def stop(self, name):
        print(name, '자동차가 멈춘다')


# 인스턴스 생성 후 속성 값 할당
car1 = Car('현대', '스타렉스', '회색', '2010')
car2 = Car('기아', '레이', '검정', '2017')
# 속성 출력
print('car1: %s, %s, %s, %s' % \
      (car1.brand, car1.name, car1.color, car1.year))
print('car2: %s, %s, %s, %s' % \
      (car2.brand, car2.name, car2.color, car2.year))
# 메소드 호출
car1.play('car1')
car2.stop('car2')


# 사각형 속성(가로, 세로),
# 속성 출력 메소드,
# 면적을 출력하는 메소드 정의

class Square2:
    # 속성을 정의하는 생성자 함수
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 속성을 출력하는 메소드 정의
    def info(self, width, height):
        print('가로 크기 - ', width)
        print('세로 크기 - ', height)

    # 면적을 출력하는 메소드 정의
    def area(self, width, height):
        print('사각형 면적 - ', width * height)


# 인스턴스화
squareA = Square2(50, 40)
squareB = Square2(70, 70)
print('-' * 10, '\n')
squareA.info(50, 40)
squareA.area(50, 40)

'''
퀴즈 : 
    1. 타원 클래스 생성 
    2. 속성 : ?
    3. 속성을 출력하는 메소드 정의
    4. 타원의 면적을 출력하는 메소드 정의 : 3.14*반지름**2 
    5. 인스턴화 
    6. 속성과 면적 메소드 호출 
'''


class Circle:
    def __init__(self, objName, radius):
        self.objName = objName
        self.radius = radius

    def info(self, objName, radius):
        print('\n\n', '-' * 20)
        print('원의 이름 : ', objName)
        print('원의 반지름 : ', radius)

    def area(self, radius):
        print('원의 면적 : ', 3.14 * radius ** 2)


c1 = Circle('c1', 5)
c1.info('c1', 5)
c1.area(5)

c2 = Circle('c2', 15)
c2.info('c2', 15)
c2.area(15)


# 상속이란?
# 부모클래스의 속성이랑 메소드를 그대로 가진다.
# class 클래스이름(부모클래스1,부모클래스2...)

# 부모클래스1 - 아파트, 차
# 부모클래스2 - 오피스텔, 전동스쿠터
# 자식클래스 - 아파트, 차 , 오피스텔, 전동스쿠터

# 부모 클래스 정의
class Papa:
    def __init__(self):
        pass

    def info1(self):
        return '아파트, 차'


class Mama:
    def __init__(self):
        pass

    def info2(self):
        return '오피스텔, 전동스쿠터'


# 자식 클래스 정의
class Me(Papa, Mama):
    pass


# 자식 클래스의 객체화
m = Me()
print('상속 => ', m.info1(), m.info2())


# 퀴즈 : 계산기 만들기
# 2개의 숫자를 속성으로 가진 계산기 클래스 만들기
# 인스턴스화 시킨 후 다음과 같이 출력한다
#
# [ 출력형태 : ]
# 첫번째 숫자 : ?
# 두번째 숫자 : ?
# 더하기 : ?
# 빼기 : ?
# 곱하기 : ?
# 나누기 : ?

# 클래스 선언 -  Calculator
# 생성자함수를 이용하여 속성 정의
# 더하기 메소드 정의
# 빼기 메소드 정의
# 곱하기 메소드 정의
# 나누기 메소드 정의
# 클래스를 이용하여 인스턴스 생성
# 출력형태로 메소드 호출하여 출력


class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def info(self, n1, n2):
        print('첫번째 숫자 : ', n1)
        print('두번째 숫자 : ', n2)

    def c_method1(self, n1, n2):
        print('더하기 : ', n1 + n2)

    def c_method2(self, n1, n2):
        print('빼기 : ', n1 - n2)

    def c_method3(self, n1, n2):
        print('곱하기 : ', n1 * n2)

    def c_method4(self, n1, n2):
        print('나누기 : ', n1 // n2)


print('-' * 10, '\n 인스턴스화 결과 \n')
cObj = Calculator(10, 20)
cObj.info(10, 20)
cObj.c_method1(10, 20)
cObj.c_method2(10, 20)
cObj.c_method3(10, 20)
cObj.c_method4(10, 20)
