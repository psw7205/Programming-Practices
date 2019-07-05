# 조건문 1
# if 조건:
#   명령문

# 조건문 2
# if 조건:
#   명령문1
# else:
#   명령문2

# 조건문 3
# if 조건:
#   명령문1
# elif 조건:
#   명령문2
# else:
#   명령문3

# False 조건
'', None, False, 0

# True
# True, 1, 문자열

# if 0: # False
# if '참': # True
# if None: # False
if '':  # False
    print('test 중...')
print('test 끝')

# 양수인지 음수인지 구별하기
status = -10
if status > 0:
    print('양수')
else:
    print('음수')

print('양수음수 판독 끝')

# 홀수니 ? 짝수니?

# num = int(input('숫자를 입력해주세요... ? ... '))
# status2 = num%2
# print(' 나머지 : ' , status2)

# if status2 == 1:
# if status2:
#     print('홀수')
# else:
#     print('짝수')

# 다중 조건
# 0, 음수, 양수
status3 = 0

if status3 > 0:
    print('양수')
    print('-' * 10)
elif status3 < 0:
    print('음수')
    print('*' * 10)
else:
    print('0')
    print('#' * 10)
print('다중 조건 테스트 끝')

# 띠 테스트
# 띠 = 태어난년도%12
# 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양
# (0  ........  11)
result = 2009 % 12
animalList = ['원숭이', '닭', '개', '돼지',
              '쥐', '소', '범',
              '토끼', '용', '뱀', '말', '양']
print(result, animalList[result])

'''
if .. elif .. else 퀴즈 
태어난 년도를 입력하세요 ...? 2009
-------------------
태어난 년도 : 2009
당신은 소띠입니다. 
오늘의 운세:
  오늘은 독서하기에 좋은 날이다. 

'''
#  in / not in 연산자
# 아이템 in 그룹(튜플, 리스트, 문자열) => True / False
# 아이템 not in 그룹(튜플, 리스트, 문자열) => True / False

groupA = [10, 20, 30]
groupB = (10, 20, 30)
groupC = 'abcdef'
groupD = set(['사과', '포도', '수박'])

print(groupA, type(groupA))
print(groupB, type(groupB))
print(groupC, type(groupC))
print(groupD, type(groupD))

print(10 in groupA)
print(0 in groupB)
print('a' in groupC)
print('사과' in groupD)
print(10 not in groupA)
print(0 not in groupB)
print('a' not in groupC)
print('사과' not in groupD)

# if ... in
# if 아이템요소 in 그룹(문자열,튜플,집합,리스트):
#     명령문1
# elif 아이템요소 in 그룹(문자열,튜플,집합,리스트):
#    명령문2
# else:
#   명령문

t1 = ('바나나', '포도', '수박', '자두')
if '체리' in t1:
    print('바나나가 우리집 냉장고에 있다')
elif '포도' in t1:
    print('포도가 많이 우리집 냉장고에 있다')
else:
    print('냉장고에 과일이 없다')

# 집합구조 만들기
# set(리스트,튜플) , {아이템1, 아이템2 ...}
myClas = {'python', 'c', 'java', 'c++'}
print(myClas, type(myClas))
if '어셈블리' not in myClas:
    print('어셈블리 미수강')
if 'python' not in myClas:
    print('python 미수강')
else:
    print('python 수강')

# pass
print('-' * 10)
if True:
    pass
print('pass Test end', '-' * 10)

myList = ['지페', '핸드폰', '카드']
print('집에 어떻게 갈까?...')
if '게임머니' in myList:
    pass
else:
    print('걸어가야 한다.')

# 반복문
# while 문
# for ... in
# for .. range()

# while 문 공식
# 초기값
# while 조건 :
#   명령문
#   조건이False?

# 1~10까지 출력하기
count = 1
while count < 11:
    print('count : ', count)
    # 빠져나가는 조건
    # count = count + 1
    count += 1

# 퀴즈 : 1~100 까지 합 구하기
total = 0
cnt = 1

while cnt <= 100:
    total += cnt
    # 빠져나가는 조건
    cnt += 1

print('1~100 까지 합은? ', total)

print('*' * 10)
# * 증가해서 찍기
cnt2 = 1
while cnt2 < 11:
    print('* ' * cnt2, cnt2)
    # cnt2 증가
    cnt2 += 1

# * 감소해서 찍기
'''
*******
******
*****
****
***
**
*
'''
print('\n' * 4)
cnt3 = 7
while cnt3 > 0:
    print('* ' * cnt3, cnt3)
    # cnt3 감소
    cnt3 -= 1

# 구구단 출력하기
'''
숫자 X 1 = ?
숫자 X 2 = ?
숫자 X 3 = ?
...
숫자 X 9 = ?

'''
guguNum = int(input('원하는 단을 입력하세요? ... '))
cnt4 = 1
while cnt4 < 10:
    print('%d X %d = %d' % (guguNum, cnt4, guguNum * cnt4))
    cnt4 += 1

# 무한루프와 if
# while True:
#   명령문
#   if 문으로 무한루프 제어 , break
# break 문은 제어문에서 빠져나갈때 사용

while True:
    ans = input('q를 입력하면 종료')
    if ans == 'q':
        break
print('무한루프 종료')

# 퀴즈
# 입력받은 값을 리스트에 추가한다.
# q 입력시 입력문 종료후 리스트 출력
# 빈 리스트 생성
resultList = []
while True:
    item = input('리스트에 추가할 요소를 입력하세요 ... (q:종료)')
    # ... 리스트 추가 명령어 append(), insert()
    resultList.append(item)
    if item == 'q':
        break
print('무한루프 종료')
print('리스트 출력', resultList)

# for 인덱스 in 리스트,문자열,튜플:
#   명령문
# 리스트 요소 순차적으로 출력
# 인덱스 : 리스트아이템
foodList = ['초밥', '햄버거', '스테이크', '떡국']
# print('0 : ', foodList[0])
cnt = 0
for i in foodList:
    print(cnt, ' : ', i)
    cnt += 1

# 튜플목록 출력
t1 = (10, 100, 300, 400, 20)
for i in t1:
    print(i, end=' ')

# 문자열 출력
str1 = 'abcdefg'
for i in str1:
    print(i)

print('-' * 10)

# 딕셔너리 요소 출력
# for key in 딕셔너리이름:
#   print(key, 딕셔너리이름[key])

dict1 = {'a': 'apple', 'b': 'banana', 'd': 'dress'}
for key in dict1:
    # 키값이 출력
    # print(key)
    print(key, ' : ', dict1[key])

# 리스트에서 최대값, 최소값 출력하기
# for 문과 if 문 사용하기
numList = [100, 31, -5, 133, 156, 77, 67]
# 리스트의 첫번째 값이 최대값 초기값으로 지정
maxNum = numList[0]
for i in numList:
    # 최대값 교체
    if i > maxNum:
        maxNum = i
print('최대값은? ', maxNum)

'''
리스트의 최소값 ? ... ?
리스트의 합계 ?  ...  ?
리스트의 평균 ?  ... ?
'''
numList2 = [100, 31, -5, 133, 156, 77, 67]
minNum = numList2[0]
listSum = 0
for i in numList2:
    # 리스트 합계
    listSum += i
    # 최소값 교체
    if i < minNum:
        minNum = i
print('리스트의 최소값 ? ', minNum)
print('리스트의 합계 ? ', listSum)
print('리스트의 평균 ?  %.2f' % (listSum / len(numList2)))

# 학생점수 리스트에서 60점 이상일때 합격,
# 그렇지않으면 불합격
stList = [80, 45, 66, 23, 100, 90, 40]
'''
1번 학생 합격
2번 학생 불합격
...

'''
stNum = 1
for i in stList:
    # print(stNum, '번 학생 : ', i)
    if i >= 60:
        print(stNum, '번 학생 : 합격 ')
    else:
        print(stNum, '번 학생 : 불합격 ')
    stNum += 1

# continue : 현재 단계만 패스. 하단 명령은 실행되지 않는다.
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 홀수값만 출력
for i in numList:
    if i % 2 == 0:
        continue
        # break
    print(i)

# 아래의 학생 점수 리스트에서 60점이상인 학생만
# 번호와 함께 합격을 축하합니다. 메세지 출력
# for .. in list, continue, if 사용
'''
1 번 학생 축하합니다.
3 번 학생 축하합니다. 
...
 
'''
print('\n\n - 합격 메세지 출력하기 - ')
stList2 = [80, 45, 66, 23, 100, 90, 40]
stNum2 = 0
for i in stList2:
    stNum2 += 1
    if i < 60:
        continue
    print(stNum2, '번 학생 합격을 축하합니다. ')

print('-' * 10)
# 2차원 리스트 출력하기
listMulti = [[1, 2, 3],
             ['a', 'b', 'c'],
             ['홍길동', '춘향이', '이몽룡']]
print(listMulti)
print(listMulti[0])  # [1,2,3]
print(listMulti[1][1])  # b
print(listMulti[-1][-1])  # 이몽룡

# for (인덱스1, 인덱스2 ...) in 리스트이름:
#   print( 인덱스1, 인덱스2 ...)

for (i, j, k) in listMulti:
    # 각 행별로 출력
    print(i, j, k)

listMulti2 = [[1, 2],
              ['a', 'b'],
              ['홍길동', '춘향이']]

for (i, j) in listMulti2:
    # 각 행별로 출력
    print(i, j)

# 퀴즈 : 학생이름, 국어, 영어, 수학 으로 구성된
# 2차원 리스트를 생성한다.
# 출력형식은 아래와 같이 한다.
'''
학생이름  국어  영어  수학  합계  평균   
김태희     30   40   100   ?     ?
...

'''
stGradeList = [['김태희', 30, 50, 55],
               ['신민아', 50, 90, 80],
               ['박지민', 50, 90, 40],
               ['김소희', 60, 50, 56],
               ['윤준희', 90, 88, 66]]

print('학생이름  국어  영어  수학   합계   평균 ')
print('-' * 50)
for (name, i, j, k) in stGradeList:
    # print(name, i, j, k, (i+j+k), ((i+j+k)/3))
    print(' %s   %d   %d    %d   %d    %.2f' %
          (name, i, j, k, (i + j + k), ((i + j + k) / 3)))

# for 인덱스 in range(start, end , step)
# range(start, end , step)
# list( range(start, end , step) ) : 순차적으로 숫자로 구성된 리스트
# tuple( range(start, end , step) ) : 순차적으로 숫자로 구성된 튜플
# set( range(start, end , step) ) : 순차적으로 숫자로 구성된 집합

print(range(1, 11))
print(list(range(1, 11)))
print(tuple(range(1, 11)))
print(set(range(1, 11)))
# 1~20 사이의 짝수 또는 홀수로 구성된 리스트 생성하기
listEven = list(range(2, 21, 2))
listOdd = list(range(1, 21, 2))
print(listEven)
print(listOdd)

# for 인덱스 in range(start,end,step):
#   명령문

# 1~10까지 출력하기
for i in range(1, 11):
    print(i)

# 1~100까지 합구하기
# for i in range() 사용하기
total = 0
for i in range(1, 101):
    total += i
print('1~100까지 합 : ', total)

# 1~100까지 짝수합구하기
total1 = 0
for i in range(2, 101, 2):
    total1 += i
print('1~100까지 짝수 합 : ', total1)

# 1~100까지 홀수합구하기
total2 = 0
for i in range(1, 101, 2):
    total2 += i
print('1~100까지 홀수 합 : ', total2)

# 한줄에 1~25 까지 5개씩 출력하기
'''
1 2 3 4 5
6 7 8 9 10
..
21 22 23 24 25
'''
for i in range(1, 26):
    print(i, end=' ')
    if i % 5 == 0:
        print()

# 퀴즈 : 별찍기1
'''
*
**
***
****
*****
'''

# 퀴즈 : 별찍기2
'''
*****
****
***
**
*
'''
print('-' * 10, '\n')
for i in range(1, 6):
    print('* ' * i)

print('-' * 10, '\n')
for i in range(1, 6):
    print('* ' * (6 - i))

# 다중 for문
for i in range(1, 6):
    print('count - ', i)
    for j in range(1, 4):
        print('     sub : ', j)

#  전체 구구단 출력
'''
2단 : 
    2 x 1 = 2
    ...

3단 : 
    3 x 1 = 3
    ...   

'''
print('\n\n\n')
for i in range(2, 10):
    print('== ', i, '단 :')
    for j in range(1, 10):
        print('%d X %d = %d' % (i, j, i * j))
    print('-' * 20)

# 리스트 for
# 리스트이름 = [ 결과값 for ... ]
# 짝수로 구성된 리스트 생성
listA = [i for i in range(2, 21, 2)]
print(listA, type(listA))

# for i in range(2,21,2):
#     print(i)

# 숫자중 3의 배수에서 -1로 구성된 리스트 생성
listB = [i * 3 - 1 for i in range(1, 51)]
print(listB, type(listB))

# 구구단의 결과값으로 구성된 리스트 생성
listC = [i * j for i in range(2, 10) for j in range(1, 10)]
print(listC, type(listC))

# 현재 년,월,일,시,분,초 출력하기
# time 객체를 이용한 모듈 임포트
import datetime

# 현재 시간을 기준으로 년,월,일,시,분,초 변수 생성
now = datetime.datetime.now()
print(now)
print(' 년도 : ', now.year)
print(' 월 : ', now.month)
print(' 날짜 : ', now.day)
print(' 시간 : ', now.hour)

# 오전과 오후 출력하기
if now.hour > 12:
    print('오후 : ', now.hour - 12, '시', now.minute, '분')
else:
    print('오전 : ', now.hour)

# 월에 따라 메세지 출력하기
# 달에 따라 봄, 여름, 가을 ,겨울 메세지 출력
# 12, 1,2 : 겨울
# 3~5 : 봄
# 6~8 : 여름
# 9~11 : 가을
# print( now.month)
# if 3 <= now.month <= 5:
#   print('봄 메세지')
