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
