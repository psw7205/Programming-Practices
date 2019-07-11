# 정규표현식 (Regular Expression)
# 유효성 검사
# 특정 문자열이 특정 조건(패턴)에 맞는지 검사

# https://docs.python.org/3.7/howto/regex.html
# 파이썬에서 정규표현식 모듈 => re (내장모듈)
import re

# 관련 모듈함수
# re.findall()
# re.compile()
# 정규표현식패턴컴파일객체.match()
# group()

# 문자열 샘플 사이트 =? https://www.lipsum.com
# 특정 글자를 포함하고 있는가?
# re.findall(문자열, 문자열대상) => 리스트
sampleTxt = 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.'
print(re.findall('a', sampleTxt))
print(re.findall('ab', sampleTxt))
resultA = re.findall('a', sampleTxt)
print(type(resultA), 'a의 갯수 => ', len(resultA))

# 정규표현식 패턴 - 대문자, 소문자, 숫자, 한글
# [문자클래스스타일]  => 한글씩
# [문자클래스스타일]+ => 단어단위
# [a-z] : 영어소문자
# [A-Z] : 영어대문자
# [0-9] : 숫자
# [가-힣] : 한글
# 영어소문자대문자 : [a-zA-Z]
print(re.findall('[a-z]', 'ab 1234 가나다 ABDJS abc가 123ab'))
print(re.findall('[A-Z]', 'ab 1234 가나다 ABDJS abc가 123ab'))
print(re.findall('[가-힣]', 'ab 1234 가나다 ABDJS abc가 123ab'))
print(re.findall('[가-힣]+', 'ab 1234 가나다 ABDJS abc가 123ab'))
print(re.findall('[0-9]', 'ab 1234 가나다 ABDJS abc가 123ab'))
print(re.findall('[a-zA-Z]', 'ab 1234 가나다 ABDJS abc가 123ab'))

# 정규표현식 패턴 - 대문자, 소문자, 숫자 : \지원문자
# [\d] : 10진수, [0-9]와같음
# [\D]: 10진수외 [^0-9]
# [\s] :공백문자, [ \t\n\r\f\v]
# [\S]: 공백 문자 외, [ \t\n\r\f\v]
# [\w] : 영문자숫자 , [a-zA-Z0-9]
# [\W]: 영문자숫자외 , [^a-zA-Z0-9]

print(re.findall('[\d]', 'ab 1234 가나다 ABDJS abc가 123ab'))
print(re.findall('[\d]+', 'ab 1234 가나다 ABDJS abc가 123ab'))
print(re.findall('[\s]+', 'ab 1234\t 가나다\n\n ABDJS abc가 123ab'))

# 퀴즈 : 비밀번호 유효성 검사 함수1
# 조건 :
# 전체길이는 6~12
# 비밀번호는 특수문자는 제외, 영문자와숫로만 구성시켜라
'''
def pwdCheck(비밀번호):
    명령어 

pwdCheck('123') 
=> 비밀번호 길이가 적당하지 않습니다. 

pwdCheck('#@563223') 
=> 숫자와 영문자로만 구성되어야 합니다. 

pwdCheck('cojhs1234') 
=> 비밀번호로 적당합니다. 

'''


def pwdCheck(pwd):
    # 비밀번호 길이 체크
    if len(pwd) < 6 or len(pwd) > 12:
        print(pwd, '비밀번호 길이가 적당하지 않습니다.')
        # 함수에서 탈출
        return False

    # 숫자와 영문자 구성인지 체크
    # re.findall() => 결과는 리스트
    if re.findall('[a-zA-Z0-9]+', pwd)[0] != pwd:
        print(pwd, '==> 숫자와 영문자로만 구성되어야 합니다.')
        return False

    # 비밀번호에 영어소문자, 영어대문자, 숫자가 꼭 1글자씩은 필요

    # pass
    print(pwd, '=> 비밀번호로 적당합니다. ')


# 실제함수 호출
pwdCheck('#@563223')
pwdCheck('cojhs1234')
pwdCheck('123')

# 퀴즈 : 비밀번호 유효성 검사 함수2
# 조건 :
# 전체길이는 6~12
# 비밀번호는 특수문자는 제외, 영문자와숫로만 구성시켜라
# 비밀번호에 영어소문자, 영어대문자, 숫자가 꼭 1글자씩은 필요
'''
def pwdCheck2(비밀번호):
    명령어 

pwdCheck('123') 
=> 비밀번호 길이가 적당하지 않습니다. 

pwdCheck('#@563223') 
=> 숫자와 영문자로만 구성되어야 합니다. 

pwdCheck('cojhs1234') 
=> 비밀번호로 적당하지 않습니다.

pwdCheck('A234cfdgs') 
=> 비밀번호로 설정되었습니다. 


'''


def pwdCheck2(pwd):
    # 비밀번호 길이 체크
    if len(pwd) < 6 or len(pwd) > 12:
        print(pwd, '비밀번호 길이가 적당하지 않습니다.')
        # 함수에서 탈출
        return False

    # 숫자와 영문자 구성인지 체크
    # re.findall() => 결과는 리스트
    if re.findall('[a-zA-Z0-9]+', pwd)[0] != pwd:
        print(pwd, '==> 숫자와 영문자로만 구성되어야 합니다.')
        return False

    # 비밀번호에 영어소문자, 영어대문자, 숫자가 꼭 1글자씩은 필요
    # 비밀번호가 아닌 조건
    if len(re.findall('[a-z]', pwd)) == 0 \
            or len(re.findall('[A-Z]', pwd)) == 0 \
            or len(re.findall('[0-9]', pwd)) == 0:
        print(pwd, '대문자, 소문자, 숫자 모두 필요합니다.')
        return False

    # pass
    print(pwd, '=> 비밀번호로 적당합니다. ')


pwdCheck2('123')
pwdCheck2('#@563223')
pwdCheck2('cojhs1234')
pwdCheck2('dhdhdhfs')
pwdCheck2('AAA3456')
pwdCheck2('A234cfdgs')

# re.compile(정규표현식패턴)
# 정규표현식을 컴파일한다. 객체로 생성

# 정규표현식패턴컴파일객체.match()
# re.compile(정규표현식패턴) 로 생성된 객체를
# 정규표현식과 맞는지 검사한다. => re.Match 객체 / None
# p = re.compile(정규표현식패턴)
# m = p.match(대상문자열)

p = re.compile('[a-z]')
print(p, type(p))

# <re.Match object; span=(0, 1), match='f'>
print(p.match('fjjkf'))
print(p.match('1234'))  # None
print(p.match('ABVCD'))  # None


# 데이타가 숫자로 시작하면  => OK
# 그렇지않다면 => Fail

# if 조건: => False
# 조건 => None, '', False, 0

def checkDigit(word):
    pattern = re.compile('[0-9]')
    m = pattern.match(word)
    if m:
        print(word, 'OK')
    else:
        print(word, 'Fail')


checkDigit('dkdk')  # dkdk Fail
checkDigit('9478')  # 9478 OK

# match객체.group()
# => match()의 결과로 추출된 문자열 표시
# match객체.span()
# => 튜플형태. 결과로 추출된 문자열의 인덱스 표시
# (start,end+1)

# 컴파일
pattern2 = re.compile('[0-9]+')
# re.Match object, None
m1 = pattern2.match('1234ogjf')
# 패턴과 맞는 문자열 추출
print(m1.group())
# 패턴과 맞는 문자열 시작위치, 끝+1
print(m1.span())

# 정규표현식 메타문자
# +:바로 앞의 문자가 하나 이상 있음
# ^:문자열의 처음을 나타냄
# $:문자열의 끝
# . :임의의 문자가 와도 됨
# *:바로 앞의 문자가 없거나 하나 이상 있음
# ?:앞의 문자가 없거나 하나임

# 이메일 형식이면 True, False
# 컴파일
p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

emails = ['python@mail.example.com',
          'python+kr@example.com',
          '@example.com',
          'python@example',
          'python@example-com']
# 정규패턴과 맞으면 True
# p.match(email) != None
for email in emails:
    print(email, p.match(email) != None)


# 위의 퀴즈를 참고해서
# 리스트에서 True 값인 이메일만 리스트 요소를 표시하여라

def checkEmail(emailList):
    # 패턴 컴파일
    p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    print('결과 ====>')

    for i in emailList:
        # 이메일 형식이 아니라면 함수 탈출
        if p.match(i) == None:
            return False
        print(i)


checkEmail(emails)

print('\n' * 10)

# sqlite3 모듈 임포트 => 내부모듈
import sqlite3

# SQLITE3 파이썬 모듈 버전
print(sqlite3.version)  # 2.6.0

# 데이타베이스 연결
# 연결변수(conn) = sqlite3.connect(데이타베이스경로)

conn = sqlite3.connect('data/chinook.db')
print('data/chinook.db 로 연결되었습니다.')

# 작업변수(cursor) = 연결변수.cursor()
cursor = conn.cursor()

# 연결된 DB에서 특정테이블의 레코드 조회하기
# 작업변수(cursor).execute(레코드조회sql명령문)
cursor.execute('SELECT * FROM CUSTOMERS;')

# 파이썬의 리스트 구조로 저장하기
# 한개만 레코드 저장
# 리스트이름 = 작업변수(cursor).fetchone()
# 특정갯수 레코드 저장
# 리스트이름 = 작업변수(cursor).fetchmany(레코드수)
# 전체 레코드 저장
# 리스트이름 = 작업변수(cursor).fetchall()

resultList1 = cursor.fetchone()
print(resultList1)

resultList2 = cursor.fetchmany(10)
print(resultList2)

resultList3 = cursor.fetchall()
print(resultList3)

cursor.execute('SELECT CustomerId, FirstName,  LastName FROM CUSTOMERS limit 10;')
resultList4 = cursor.fetchall()
print(resultList4)
print('\n' * 5)
print('Id', '\t', 'FirstName', '\t', 'LastName')
for i in resultList4:
    print('-' * 30)
    # 각 데이타값 접근시에는 인덱스변수[컬럼인덱스]...
    print(i[0], '\t', i[1], '\t', i[2])
    # 각 행의 레코드는 튜플구조
    # (데이타값1, 데이타값2 ...)
    # print(i)

# 퀴즈 :
# albums 테이블의 전체 레코드 갯수는?

# employees 테이블에서 title 컬럼명이 'IT Staff'인
# 레코드만 추출하여 한행 씩 표시하여라

# albums 테이블에서 AlbumId가 5보다 크고
# ArtistId가 12보다  작은 레코드만 한행 씩 표시하여라

# albums 테이블에서 마지막 레코드의 마지막 컬럼의 데이타값만
# 표시하여라


# end DB
conn.close()
