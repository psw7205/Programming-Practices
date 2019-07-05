# 자료형의 종류
# 기본 자료형 - 문자열, 정수, 실수, 불린형
# 콜렉션 : 여러개의 구성요소로 조직화
#       : 리스트 [], 튜플 (), 딕셔너리 { }, 집합
# CRUD : Create Read Update Delete

# 리스트
# 다른 데이터형 가능
# 순차적으로 생성
# 빈 리스트
listA = []
print(listA, type(listA))
# 초기값 지정
listB = ['a', 1, True, 'Python']
print(listB, type(listB))
# 인덱싱
# 리스트이름[숫자] : 0부터 시작
print(listB[0], listB[-1])
# 슬라이싱
# 리스트이름[start:end:step]
print(listB)
print(listB[0:2])
print(listB[2:])
print(listB[0::2])
# 리스트 전체길이 : len(리스트이름)
print('listB의 전체길이 ', len(listB))

# 리스트 연산
# 리스트1 + 리스트2 : 같이 표시
# 리스트이름*숫자 : 반복
movieList = ['알라딘', '엔드게임', '토이스토리']
dramaList = ['남자친구', '으랴차차 와이키키2']
print(movieList)
print(dramaList)
print(dramaList + movieList)
print(dramaList * 3)

# 리스트 값 교체
# 리스트이름[인덱스] = 값
print(movieList)
movieList[0] = '토토로'
print(movieList)
# 마지막 리스트 값 교체
# movieList[-1] = '기생충'
movieList[len(movieList) - 1] = '기생충'
print(movieList)

# 리스트 추가1
# 맨뒤에 추가된다.
# 리스트이름.append(값)
myList1 = []
print(myList1)
myList1.append('black')
myList1.append('white')
myList1.append(100)
print(myList1)

# 리스트 추가2
# 위치를 지정해서 값을 추가할 수 있다.
# 리스트이름.insert(위치인덱스, 값)
print(myList1)
myList1.insert(0, '사과')
myList1.insert(2, '수박')
print(myList1)

# 퀴즈 : 입력받은 값을 이용해서 3개로 구성된 리스트 생성하기
'''
myList2 = []
리스트 값1을 입력해주세요? ... 블랙핑크
리스트 값2을 입력해주세요? ... 트와이스
리스트 값3을 입력해주세요? ... 방탄소년단

myList2 => [ '블랙핑크', '트와이스', '방탄소년단']

'''
# print('\n'*3, '-'*10)
# myList2 = []
# print('Before : ', myList2)
# myList2.append(input('리스트 값1을 입력해주세요? ... '))
# myList2.append(input('리스트 값2를 입력해주세요? ... '))
# myList2.append(input('리스트 값3을 입력해주세요? ... '))
# print('After : ', myList2)

# 리스트 삭제
# 리스트이름.remove(요소값) :  값으로 삭제
# 리스트이름.pop(인덱스) : 위치로 삭제 후 결과 출력
# del 리스트이름[인덱스] : 위치로 삭제
# 리스트이름.clear() : 요소 모두 삭제
myList3 = [1, 2, 3, 4, 5, 6, 7]
print('Before : ', myList3)  # [1, 2, 3, 4, 5, 6, 7]
myList3.remove(5)
print('Step1 : ', myList3)  # [1, 2, 3, 4, 6, 7]
# pop() : 마지막 요소 삭제
print(myList3.pop())  # 7
print('Step2 : ', myList3)  # [1, 2, 3, 4, 6]
print(myList3.pop(0))  # 1
print('Step3 : ', myList3)  # [2, 3, 4, 6]
del myList3[0]
print('Step4 : ', myList3)  # [3, 4, 6]
myList3.clear()
print('Step5 : ', myList3)  # []

# 리스트 아이템값 정렬
# 리스트이름.sort() / 리스트이름.reverse()
# 정렬시킬 리스트의 자료형이 같아야한다. => Type Error 발생
myList4 = ['파이썬', 'banana', '100', 'apple', 'xlay']
# myList4 = ['파이썬' , 'banana', 100, 'apple', 'xlay']
myList4.sort()
print(myList4)
myList4.reverse()
print(myList4)

# 중복 아이템값의 갯수 찾기
# 리스트이름.count(아이템값) => 정수
myList5 = [100, 200, 100, '파이썬', 300, 100]
print('100의 중복 횟수 => ', myList5.count(100))

# 인덱스로 값 찾기
print('3번째 위치한 값은?', myList5[2])

# 값으로 인덱스 위치 찾기
# 리스트이름.index(아이템값) => 인덱스값
# 찾고자 하는 아이템값이 중복일 경우 첫번째 인덱스값이 반환된다.
print('파이썬의 인덱스는? ', myList5.index('파이썬'))  # 3
print('100의 인덱스는? ', myList5.index(100))  # 0
# 찾고자하는 값이 없다면 ValueError 에러 발생
# print( '500의 인덱스는? ', myList5.index(500) )

# 리스트 확장. 여러 아이템값 추가 가능
# 리스트이름.extend(새로운리스트)
foodList = ['라면', '김밥']
print('Before = > ', foodList)
foodList.extend(['초밥', '우동', '샌드위치'])
print('After = > ', foodList)

# 캐스팅
# 문자열 => 리스트
# 문자열변수.split() : 공백을 기준으로 해서 리스트화
# list(문자열변수) : 공백도 모두 리스트화. 낱글자가 아이템요소로 변경
myString = '도 레 미   파 솔 라 시 솔라시도'
print(myString)
print(myString.split())
print(list(myString))

# 리스트 => 문자열
# str(리스트이름) : [ ], 쉼표(,) 도 포함해서 모두 문자열화
# '구분자'.join(리스트이름) : 구분자가 아이템요소 사이에 모두 추가된 후 문자열화
myList6 = ['김씨', '박씨', '남궁씨', '신씨', '이영자', '박소영']
print(myList6, type(myList6))
result1 = str(myList6)
print(result1, type(result1))
print(result1[0:3])

result2 = ' '.join(myList6)
print(result2, type(result2))
result3 = ','.join(myList6)
print(result3, type(result3))

# 중첩 리스트 구조 1
# 리스트안에 리스트가 있다
# 중첩리스트의 인덱싱은?
# 리스트이름[index1][index2]
listMulti1 = [1, 2, ['a', 'b', 'c'], ['포도', '수박']]
print(listMulti1, type(listMulti1))
print(listMulti1[0])
print(listMulti1[2])
print(listMulti1[2][0])
print(listMulti1[3][-1])

# 중첩 리스트 구조 2
# 1차원 리스트 정의 후 1차원 리스트를 다시 리스트로 구성
userName = ['홍길동', '박지민', '이미연']
userAge = [20, 25, 34]
userGender = ['남', '남', '여']
userAddr = [userName, userAge, userGender]
print(userAddr)
print(userAddr[0][1])
print(userAddr[1][-1])
print(userAddr[-1])

# 퀴즈 :
'''
아래의 리스트를 이용하여 grade 리스트를 생성하고 합계와 평균을 
과목별로 출력한다. 

kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]
------------
result 
kor : 합계 = ? , 평균 = ?
math : 합계 = ? , 평균 = ?
eng : 합계 = ? , 평균 = ?
python : 합계 = ? , 평균 = ?
'''
kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]
grade = [kor, math, eng, python]

pythonTot = grade[3][0] + grade[3][1] + grade[3][2]
pythonAvg = pythonTot / 3

print('kor : 합계 = %d , 평균 = %.2f' % (
    grade[0][0] + grade[0][1] + grade[0][2], (grade[0][0] + grade[0][1] + grade[0][2]) / 3))
print('python : 합계 = %d , 평균 = %.2f' % (pythonTot, pythonAvg))

# 튜플(Tuple)
# CRUD
# 생성, 읽기, 교체는 않되고 추가 가능, 삭제 불가능
# 생성 방법 1
# 튜플이름 = (아이템값1,아이템값2...)
# 쉼표(,)를 이용한 튜플 1개 아이템 생성
# 튜플이름 = (아이템값,)
# 튜플이름 = ()
t1 = ('장미', '백합', '무궁화')
print(t1, type(t1))
# t2 = ('수박') # 수박 <class 'str'>
t2 = ('수박',)  # ('수박',) <class 'tuple'>
print(t2, type(t2))
t3 = ()
print(t3, type(t3))  # () <class 'tuple'>

# 생성 방법 2 : () 생략 가능
# 튜플이름 = 아이템값1,아이템값2...
myTuple1 = 'a', 'b', 'c', 'd', 'e'
print(myTuple1, type(myTuple1))

# 인덱싱과 슬라이싱
print(myTuple1[0])
print(myTuple1[-1])
print(myTuple1[1:3])
print(myTuple1[::2])

# 전체 길이
print('전체 길이는? ', len(myTuple1))

# *, + 연산
myTuple2 = (1, 2, 3, 4, 5)
print(myTuple1)
print(myTuple2)
print(myTuple1 + myTuple2)
print(myTuple1 * 3)

# 교체되는지 확인?
# 튜플 아이템값은 교체 불가능
# TypeError: 'tuple' object does not support item assignment
# myTuple1[0] = 'new item'

# 튜플 아이템 추가
# 튜플이름 += (아이템한개,)
# 튜플이름 += (아이템1, 아이템2, ...)
print(myTuple1)
myTuple1 += ('new Item',)
print(myTuple1)
myTuple1 += ('new Item2', 'new Item3')
print(myTuple1)

# 튜플 아이템 삭제는 될까요?
# 삭제 불가능
# 튜플은 정렬이 가능할까요?
# 정렬 불가능

# 튜플 아이템값의 위치 반환
# 튜플이름.index(아이템값)
print(myTuple1)
print(myTuple1.index('c'))

# 튜플 아이템값의 중복  횟수
# 튜플이름.count(아이템값)
myTuple3 = (100, 200, 300, 100, 100)
print(myTuple3)
print(myTuple3.count(100))

# 캐스팅
# 리스트 => 튜플
# tuple() : 튜플로 자료 구조 변경시 사용
myList = ['줄리아', '존', '제레미']
print(myList, type(myList))
myListTuple = tuple(myList)
print(myListTuple, type(myListTuple))

# 튜플 => 리스트
# list(튜플이름)
print(myTuple3, type(myTuple3))
myTupleList = list(myTuple3)
print(myTupleList, type(myTupleList))

# 튜플 => 문자열
myTuple4 = ('영국', '대한민국', '미국', '중국')
print(myTuple4, type(myTuple4))
myCountry1 = str(myTuple4)
myCountry2 = ' '.join(myTuple4)
print(myCountry1, type(myCountry1))
print(myCountry1[0])
print(myCountry2, type(myCountry2))

# 문자열 => 튜플
myCountry3 = '아름다운 우리나라 푸르게 푸르게'
myCountry3Tuple = tuple(myCountry3)
print(myCountry3Tuple, type(myCountry3Tuple))

# 딕셔너리 생성 1
# 딕셔너리이름 = {키1:값1, 키2:값2 ...}
dict1 = {'a': 'apple',
         'c': 'cat',
         'd': 'dog',
         'x': 'xlay'}
print(dict1, type(dict1))  # <class 'dict'>

# 딕셔너리 생성 2
# 딕셔너리이름 = dict() # 빈 딕셔너리 생성
# 딕셔너리이름[키값]=값
dict2 = dict()
print(dict2, type(dict2))  # {} <class 'dict'>
# 아이템 추가
dict2['b'] = 'banana'
dict2['s'] = 'superman'
print(dict2)  # {} <class 'dict'>

# 인덱싱 : 키값으로 호출
# 딕셔너리이름[키값]
print(dict1)
print(dict1['c'])

# 딕셔너리 키값은 중복이 될까요?
# 키값은 중복되지 않는다.
# 만약 키값을 중복되게 정의하면 마지막에 정의한 아이템값이 호출
# 딕셔너리 아이템값은 중복이 될까요? yes
dict3 = {'one': '하나',
         'one': '일',
         'color1': 'black',
         'color2': 'black'}
print(dict3)
print(dict3['one'])
print(dict3['color1'])
print(dict3['color2'])

# 딕셔너리 요소 추가
# 딕셔너리이름[키값]=아이템값
print(dict3)
dict3[10] = '십'
print(dict3)

# 딕셔너리 아이템값 변경
# 딕셔너리이름[키값]=아이템값
dict3['color1'] = '검정'
print(dict3)

# 딕셔너리 아이템 삭제
# del 딕셔너리이름[키값]
# 딕셔너리이름.pop(키값)
# 딕셔너리이름.clear()
print(dict3)
del dict3['one']
print(dict3)
dict3.pop(10)
print(dict3)
dict3.clear()
print(dict3)

# 딕셔너리 함수
# values(), keys(), items()
dict4 = {100: '구로구', 200: '광진구', 400: '종로구'}
print('키값만 추출 : ', dict4.keys())
print('아이템값만 추출 : ', dict4.values())
print('키와 아이템값 추출 :', dict4.items())

# keysList = dict4.keys()
# 'dict_keys' object is not subscriptable
# print(keysList[0])
keysList = list(dict4.keys())
print(keysList[0])

# 딕셔너리의 아이템값 표시
# 딕셔너리이름.get(키값)
# 딕셔너리이름[키값]
print(dict4)
# 키값이 있는 경우
print(dict4[100])
print(dict4.get(100))
# 키값이 없는 경우 KeyError
# print(dict4[500])
# 키값이 없는 경우 None
print(dict4.get(500))

# 키값 in 딕셔너리
# 키값이 있는지 확인 => True / False
print(dict4)
print(100 in dict4)  # True
print(500 in dict4)  # False

# 집합 생성
# 집합이름 = set(리스트|문자열|튜플)
# { 아이템1 , 아이템2 .. }
# 순서가 없다 => 인덱싱 불가
# 중복값이 없다
# 교체 불가, 아이템 추가 가능, 아이템 삭제 가능
set1 = set(['a', 'b', 'b', 'a', 'c'])
print(set1, type(set1))
# 순서가 없다 => 인덱싱 불가 : TypeError
# print(set1[0])
print('전체 길이 : ', len(set1))
# 문자열구조 => 집합구조
set2 = set('abcd100100')
print(set2, type(set2))
# 튜플구조 => 집합구조
set3 = set(('부산', '울산', '광주', '광주', '전주'))
print(set3, type(set3))

# 아이템 추가
# 집합이름.add(값)
# 집합이름.update(리스트)
print(set3)
set3.add('춘천')
print(set3)
set3.update(['대구', '서울'])
print(set3)

# 아이템 삭제
# 집합이름.remove(아이템값)
# 집합이름.discard(아이템값)
print(set3)
set3.remove('광주')
set3.discard('전주')
print(set3)
# 아이템값이 없다면 keyError 발생
# set3.remove('전주')
# 아이템값이 없어도 에러가 발생하지 않는다.
set3.discard('제주')

# 교집합 : 두집합의 중복 데이타 추출
# 집합1 & 집합2
# 집합1.intersection(집합2)
s1 = set([1, 100, 200, 5, 300])
s2 = set([10, 100, 200, 50, 500])
print('s1 => ', s1)
print('s2 => ', s2)
print(s1 & s2)
print(s1.intersection(s2))

# 합집합 : 두집합의 모든 데이타
# 집합1 | 집합2
# 집합1.union(집합2)
print(s1 | s2)
print(s1.union(s2))

# 차집합 : 집합1에서 집합2의 중복 데이타 삭제
# 집합1 - 집합2
# 집합1.difference(집합2)
print(s1 - s2)
print(s1.difference(s2))

# 제어문의 종류
# 조건문
# 반복문
# {} 사용하지 않고 탭1개 나 공백4칸 으로 블록 지정
# switch 문이 없다
# elif 문이 있다

# 단순 조건문
# if 조건식:
#     수행명령

a = 10
b = 20
print(a > b)  # False
print(a <= b)  # True

if a <= b:
    # if a > b :
    # IndentationError: 에러 발생
    # print('a 가 b 보다 작다')
    print('a 가 b 보다 작다')

# 짝수인지 홀수인지 판단 ?
myNum = 45
if myNum % 2 == 0:
    print('짝수')
if myNum % 2 != 0:
    print('홀수')

# 퀴즈1 :
# 숫자를 입력받아서
# 숫자값이 3의 배수이면 3의 배수이다.
# 그렇지 않으면 3의 배수가 아니다.
'''
숫자를 입력해주세요 ? ... 
3의 배수이다. 
3의 배수가 아니다.
'''

# 퀴즈2 :
# 나이를 입력받아서
# 나이에 따라서 서로다른 메세지 출력
'''
당신의 나이를 입력해주세요? ...  
14 ~ 16 : 중학생 
17 ~ 19 : 고등학생 
20 ~ : 성인
'''
userAge = int(input('당신의 나이를 입력해주세요 ? ... '))
if userAge > 19:
    print('성인')

if 17 <= userAge <= 19:
    # if (userAge >= 17) and (userAge <= 19) :
    print('고등학생')

if 14 <= userAge <= 16:
    print('중학생')
