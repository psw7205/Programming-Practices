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
