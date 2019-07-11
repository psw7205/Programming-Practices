# 자료선언
# 변수 < 콜렉션 (리스트, 튜플, 집합, 딕셔너리) <
# 함수 < 클래스 < 모듈(파일단위) < 패키지(폴더 단위)
# 모듈(Module)이란?
# 함수, 클래스의 집합 => 별도의 파일(*.py)로 생성
# 모듈의 종류
# - 내부모듈 : 파이썬에서 기본적으로 제공
# - 외부 모듈 : pip/pip3(파이썬), conda(아나콘다)를 이용해서 별도 설치
# - 사용자정의 모듈 : 필요에 의해서 직접 모듈로 등록한 후 사용

# 모듈의 호출방법 1
# import 모듈이름
# 모듈이름.함수(인자)

# 모듈의 호출방법 2
# import 모듈이름 as 별칭
# 호출된 모듈의 함수 호출방법2
# 별칭.함수(인자)

# 모듈의 호출방법 3
# from 모듈이름 import 모듈함수
# 호출된 모듈의 함수 호출방법3
# 모듈함수(인자)

# ---->
# 모듈 이용방법 1
# math 모듈
# : 내부모듈, 수학함수 sin(), cos(), tan(), pi ...
# import math
# print('sin(10) => ', math.sin(10))
# print('pi => ', math.pi)

# 모듈 이용방법 2 : 별칭(Alias) 방식
# import math as m
# print('sin(10) => ', m.sin(10))
# print('pi => ', m.pi)

# 모듈 이용방법 3 : from 방식
# 주의사항 : 함수이름만 import 뒤에 쉼표(,)를 이용하여 나열
from math import sin, pi

print('sin(10) => ', sin(10))
print('pi => ', pi)

# -------------->
# 난수(random) 발생 모듈 => 내부 모듈
# 모듈 임포트
import random

# 관련 함수
# random.random() : 0~1 사이의 소수점 방식으로 난수 발생
# random.randrange(star,end,step)
# : 범위를 지정해서 정수 난수 발생
# : 짝수와 홀수로 조건 제한 가능
# random.randint(star,end) : 0~숫자까지 정수난수 발생
# random.choice(리스트) : 리스트요소를 무작위로 추출
# random.shuffle(리스트) : 리스트안의 아이템을 무작위로 섞는다.
print(random.random())  # 0.7484246388455121
print(random.randrange(1, 30))  # 18
print(random.randint(50, 100))  # 92
print(random.choice(['꽝', '꽝', '이마트 10만원', '스타벅스 20만원', 'BMW']))
myList = [30, 60, 89, 78, 56]
# random.shuffle() 출력문과 사용시 None
# print(random.shuffle([30, 60, 89, 78, 56])) # None
random.shuffle(myList)
print(myList)

# 퀴즈 : 로또번호 생성하기
# 조건 :
# 1~45 의 숫자중에서 6개로 구성
# 숫자는 중복되면 안된다.
# 로또리스트는 빈 리스트 생성
# 반복문에서
#   : 번호의 갯수가 6개라면 반복문 탈출
#   : 1~45까지 번호중에서 1개 생성
#   : 리스트안에 이미 번호가 있다면 다시 번호 생성
#   : 중복번호가 아니라면 리스트에 추가
# 로또 리스트를 출력한다.
lottoList = []
while True:
    # 탈출 조건: 번호 6개인지 확인
    if len(lottoList) >= 6:
        break
    else:
        # 로또번호 생성
        data = random.randint(1, 45)
        # 로또번호가 리스트가 없는지 있는지 확인
        if data not in lottoList:
            lottoList.append(data)
print('금주의 로또번호 : ', lottoList)

# ----------------------
# calendar 모듈 => 특정 년도의 월 출력, 내부 모듈
import calendar as c

# 특정 년도의 전체 달력 출력
# calendar(년도)
print(c.calendar(2019))
print(type(c.calendar(2019)))  # <class 'str'>

# 특정 년도의 특정 월 출력
# prmonth(년도, 월)
# print() 구문안에 삽입시 마지막에 None 출력
# print(c.prmonth(2019,7))
c.prmonth(2020, 1)

# 요일을 인덱스로 출력
# weekday(년도,월,일) => 0~6 숫자로 표기
print('2020년 1월 1일은 무슨요일? ', \
      c.weekday(2020, 1, 1))  # 2

# 인덱스값을 이용하여 요일 출력하기
dayList = ['월', '화', '수', '목', '금', '토', '일']
print(dayList[c.weekday(2019, 7, 10)], '요일')

# 사용자정의 모듈
# step1 - 같은 폴더에 모듈명.py 생성
# step2 - 모듈명.py에 모듈함수(인자)를 정의


# 같은 폴더에 test.py 파일 생성
'''
def test():
    return 'test Module'
'''
import MyModule.test as test

# test.py 안의 함수를 사용할 수 있도록
# 모듈로 임포트
# import 모듈파일명

# 모듈명.함수로 호출
print(test.test())
print(test.sumPrint(10, 40))

# 퀴즈 - gugu.py 파일을 생성한 후
# gugu.py 파일안에 구구단을 호출하는
# 모듈함수 guguPrint(숫자) 를 정의하여라
# 현재파일에서
# gugu 모듈을 임포트한 후
# 모듈 함수 guguPrint(숫자)를 호출하여라
'''
import gugu 

gugu.guguPrint(7)
'''

from MyModule import gugu

gugu.guguPrint(7)

# 패키지(Package)
# 특정 모듈 파일을 저장하는 폴더 개념
# 패키지 폴더의 경우에는
# __init__.py 파일이 폴더안에 저장되어 있어야 한다.
# 파이참 에디터에서는 프로젝트 폴더에서
# 마우스 우측 -> Python Package 명령을 실행하면
# 자동으로 __init__.py 파일이 생성된다.
# 패키지안의 모듈 임포트
# import 패키지명.모듈
# 모듈함수 호출은?
# 패키지명.모듈.모듈함수(인자)

# import 패키지명.모듈 as 별칭
# 모듈함수 호출은?
# 별칭.모듈함수(인자)

# from 패키지명.모듈 import 모듈함수
# 모듈함수 호출은?
# 모듈함수(인자)

# 패키지 테스트
# AAA : 패키지 폴더
# AAA/a.py : 모듈 파일

# import AAA.a
# print(AAA.a.test_a())

import MyModule.AAA.a as aM

print(aM.test_a())

# 퀴즈
# AAA 패키지안의 BBB 패키지안의 모듈 b 임포트
# test_b()를 호출

# import AAA.BBB.b as bb
# print(bb.test_b())

from MyModule.AAA.BBB.b import test_b

print(test_b())

# 퀴즈 :
# 로또번호가 생성되는 lottoNum 모듈을
# lotto 패키지로 구성해서 작성한 후
# 모듈 함수를 호출하여라
# 모듈 파일 위치 : lotto/lottoNum.py
# lottoNumPrint() : 모듈 함수명
'''
import lotto.lottoNum

lottoNumPrint()
'''
# csv
# Comma Seperate Value
# 콤마(,)로 데이타가 분리된 파일
# 엑셀양식의 데이터를
# 프로그램에 상관없이 쓰기 위한 데이터 형식

# csv 사용을 위한 임포트
import csv

# 작업폴더 위치 확인
import os

print(os.getcwd())

# csv 파일 읽기
# 파일변수 = open(csv파일경로, 'r', encoding='cp949/uft-8')
# csv 객체
# csv.reader(파일변수)
# for i in csv.reader(파일변수):
#   print(i)
# 파일변수.close()

f = open('data/data.csv', 'r', encoding='utf-8')
resultCSV = csv.reader(f)
print(resultCSV)  # _csv.reader object

# 한줄로 출력하기
# for i in resultCSV :
#     print(i)
#     print(type(i)) # <class 'list'>

print('-' * 20)

# 리스트 구조로 변경하기
# 빈리스트를 생성하고 리스트요소로 추가하는 방식
resultList = []
for i in resultCSV:
    resultList.append(i)

# 리스트안에 리스트가 삽입된 구조
print(resultList)
print(len(resultList))
print(type(resultList))

# 첫번째 행
print(resultList[0])
# 첫번째 행의 두번째 열의 값
print(resultList[0][1])
# 마지막행의 마지막 열 값
print(resultList[-1][-1], type(resultList[-1][-1]))

# 퀴즈
# 첫번째 국어점수의 인덱스는? [1][2]
# 첫행은 제목행이므로 리스트에서 삭제
print(resultList)
resultList = resultList[1:]
print(resultList)

# 데이타값이 문자열이다. => float(), int() 숫자형으로 변경
# 국어점수만 리스트로 생성하기
# 모든 행에서 3번째(인덱스는 2)의 데이타만 추출
# 새로운 리스트에 정수형으로 변환하여 추가한다.
korList = []
for i in range(0, len(resultList)):
    korList.append(int(resultList[i][2]))
print('국어점수리스트 =>', korList)

# 국어점수의 합계 구하기
print('국어점수 합계 =>', sum(korList))
# 국어점수의 평균 구하기
print('국어점수 평균 =>', sum(korList) / len(resultList))

# 파일 닫기
f.close()

print('-' * 10)
# 퀴즈
# with 문으로 csv 파일 불러오기
# 가장 인구가 많은 주 ?
# 문자열에서 콤마 제거는? 문자열.replace(',','')
with open('data/population.csv', 'r', encoding='utf-8') as f:
    # resultCSV = csv.reader(f)
    # for i in csv.reader(f):
    #     print(i)
    # 빈 리스트 생성
    pList = []
    for i in csv.reader(f):
        pList.append(i)
    # 1행은 제거
    pList = pList[1:]
    print(pList)
    # 콤마가 있는 숫자 문자 => 정수형 => 데이타 교체
    for i in range(0, len(pList)):
        pList[i][1] = int(pList[i][1].replace(',', ''))
    print(pList)
    # 첫번째 데이타를 초기값 지정
    maxCountry = pList[0][0]
    maxPopulation = pList[0][1]
    for i in range(0, len(pList)):
        if maxPopulation < pList[i][1]:
            maxCountry = pList[i][0]
            maxPopulation = pList[i][1]
    print('인구가 가장 많은 미국의 주는? ... ', maxCountry)
    print('인구가 가장 많은 미국의 주의 인구는? ... ', maxPopulation)

import csv

# 리스트 데이타를 csv 파일 쓰기
# 리스트는 2차원이어야 한다.
# [[1행...], [2행...] ]
# 파일변수 = open(csv파일경로, 'w', encoding='uft-8')
# csv변수 = csv.writer(파일변수)
# for i in 리스트:
#   csv변수.writerow(i)
# 파일변수.close()

myList = [['이름','주소','전화번호'],
          ['김영희','부산시','010-6374-90874'],
          ['홍길동','춘천시','010-5463-9403'],
          ['성은희','서울시','010-4646-9403']]
f = open('data/addr.csv','w', newline='', encoding='cp949')
csvline = csv.writer(f)
for i in myList:
    csvline.writerow(i)
print('파일쓰기가 완료되었습니다.')
f.close()

# with 문으로 교체
# 기존 파일에 데이타 추가
with open('data/addr2.csv','a', newline='', encoding='cp949') as f:
    csvline = csv.writer(f)
    for i in myList:
        csvline.writerow(i)
    print('파일쓰기가 완료되었습니다.')

# 오류?
# 오류의 종류
# NameError: 함수이름, 변수, 리스트 이름등이 잘못된 경우
# IndexError :  튜플,리스트의 잘못된 인덱스 접근
# ZeroDivisionError : 0으로 나눈 경우
# FileNotFoundError : 잘못된 파일 경로
# SyntaxError 제외 => 예외처리 try: ~ Except 구문에서 제외

# 예외처리(Exception) 란?
# 오류가 발생을 하면 메세지를 출력하거나
# 오류를 무시하는 기능

# 에러처리 문법 1
# try:
#   명령어
# except 에러코드 as e:
#   에러처리명령

# 0으로 나눈 경우

#  에러코드 출력
try:
    23/0
except ZeroDivisionError as e:
    print(e, '가 발생')

# 에러코드를 모르는 경우
try:
    23/0
except:
    print('오류 발생, 0으로 나누지 못함 ')

print('Hello Python')

# 에러처리 문법 2
# try:
#   명령어
# except 에러코드 as e:
#   에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어

myList = [1,2,3]
try:
    # print(myList[3])
    print(myList[0])
except IndexError as e:
    print(e, '가 발생')
else:
    print('정상적으로 접근이 가능합니다.')

# 에러처리 문법 3
# try:
#   명령어
# except 에러코드 as e:
#   에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어
# finally:
#   무조건 실행되는 명령어

try:
    # pint('dkdkk')
    print('dkdkk')
except NameError as e:
    print(e,'가 발생')
else:
    print('에러가 없습니다.')
finally:
    print('에러 처리 완료')

# 에러 무시 : pass 키워드 사용
# try:
#   명령어
# except:
#   pass

try:
    f = open('d.txt', 'r')
except:
    pass
print(' 명령 실행 끝')

# 퀴즈 1
# 2개의 데이타값을 입력받은 후 나누기 명령을 실행한다.
# 에러가 발생하면
#   에러 메세지 출력 : '데이타 오류 ...'
# 에러가 발생하지 않으면
#   결과 수행 : n1 / n2 = ?

a = int(input('숫자를 입력하세요?   ...'))
b = int(input('숫자를 입력하세요?   ...'))
try:
    a/b
except ZeroDivisionError:
    print('0 으로 나눌 수 없습니다')
else:
    print('{} / {} = {} '.format(a,b,a/b))
finally:
    print('명령을 완료했습니다.')

# 퀴즈 2
# data_eng.txt 파일을 파일 변수로 저장한다.
# data_eng.txt 파일이 없다면 (에러발생)
#   메세지 출력. => '파일없음'
# 파일이 있다면 (에러가발생하지 않는다면)
#   총합과 평균을 구하여 출력한다.

try:
    # f = open('data_eng.txt', 'r')
    f = open('data/data_eng.txt', 'r')
except:
    print('파일 없음')
else:
    resultList = f.readlines()
    print(resultList)
    total = 0
    for i in range(0,len(resultList)):
        total += int(resultList[i])
    print('총합계 : ', total)
    print('평균 : ', total/len(resultList))

# 모든 예외의 에러 메시지를 출력할 때는 Exception 키워드
# try:
#     명령
# except Exception as e:
#     print(e)

try:
    23/0
except Exception as e:
    print(e)
