# 퀴즈 1
# 인자값을 받아서 출력하는 구구단 함수를 정의한 후
# 호출하여 출력하여라
'''
def gugu(n):
    ?

gugu(9)

출력 >>
9 X 1 = 9
9 X 2 = 18
9 X 3 = 27
9 X 4 = 36
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81

'''


def gugu(n):
    for i in range(1, 10):
        print(f'{n} X {i} = {n * i}')


gugu(9)

# 퀴즈 2
# 키와 몸무게를 인자로 입력하여
# 메세지가 출력되도록 함수를 정의하고
# bmi 값에 따라 출력한다.
#
# k = 키(입력값) 단위 cm
# w = 체중(입력값)
#
# bmi = 체중(kg)/키(m)의제곱
#
# bmi 값에 따라 다음과 출력한다.
#
# 고도 비만 : 35 보다 클 경우
# 중등도 비만  : 30 - 35 미만
# 경도 비만 : 25 - 30 미만
# 과체중 : 23 - 25 미만
# 정상 : 18.5 - 23 미만
# 저체중 : 18.5 미만

'''
결과값 :

키 :  170
몸무게 :  68
중등도 비만
BMI : 23.53

'''


def bmi(height, weight):
    print(f'키 : {height}')
    print(f'몸무게 : {weight}')
    r = weight / (height ** 2) * 10000
    if r > 35:
        print('고도비만')
    elif r > 30:
        print('중등도 비만')
    elif r > 25:
        print('경도비만')
    elif r > 23:
        print('과체중')
    elif r > 18.5:
        print('정상')
    else:
        print('저체중')
    print(f'BMI : {r:.2f}')


bmi(176, 63)

# 퀴즈 3
# 아래와 함수를 호출하여 메세지가 출력되도록
# 함수를 정의하여라
# 이때 함수 인자는 3개로 구성하며 마지막 man 만 True 형태로
# 초기값을 지정한다.
'''
# 함수 정의 
def say_myself(name, old, man=True):
    ?

# 함수 호출 
say_myself('김철수', 20)
say_myself('백설공주', 15, False)

# 결과값 
나의 이름은 김철수 입니다.
나이는 20살입니다.
남자입니다.
-----------------------------
나의 이름은 백설공주 입니다.
나이는 15살입니다.
여자입니다.

'''


def say_myself(name, old, man=True):
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는 {old}살 입니다.')
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')


say_myself('김철수', 20)
say_myself('백설공주', 15, False)

# 퀴즈 4
# 여러가지 값이 리스트에 저장될 수 있게
# 인자가 가변인 함수를 정의하여라
'''
# 함수 호출 
print(addList(1,2,3,4))
print(addList('가','나','다','라','마'))

결과 >>>
[1, 2, 3, 4]
['가', '나', '다', '라', '마']

'''


def addList(*args):
    return [x for x in args]


print(addList(1, 2, 3, 4))
print(addList('가', '나', '다', '라', '마'))

# 퀴즈 5
# **kwargs 인자 가변 함수를 이용하여
# 함수 호출시 결과값이 다음과 같이 딕셔너리 형태로
# 출력되도록 하여라
'''
# 함수 호출 
dictDefine(a='apple', b='banana', n='nano')
dictDefine(b='banana', n='nano', s='soup', d='dress', q='quit')

결과 >>>

{'a': 'apple', 'b': 'banana', 'n': 'nano'}
a : apple
b : banana
n : nano


{'b': 'banana', 'n': 'nano', 's': 'soup', 'd': 'dress', 'q': 'quit'}
b : banana
n : nano
s : soup
d : dress
q : quit

'''


def dictDefine(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f'{key} : {value}')


dictDefine(a='apple', b='banana', n='nano')
dictDefine(b='banana', n='nano', s='soup', d='dress', q='quit')

# 퀴즈 1
# 입력받은 수식에 관련된 결과계산값을 출력한다.
# eval() 이용
'''
result = input('계산식을 입력하세요?.... ')

3+4*20-100

결과 >>
3+4*20-100 = ?

'''

# 퀴즈 2
# 7개의 입력받은 숫자 값을 리스트로 저장한 후
# 최대값과 최소값을 출력한다.
# max(), min() 활용
'''
숫자 1? .... 56
숫자 2? .... 34
숫자 3? .... 100
숫자 4? .... 23
숫자 5? .... 78
숫자 6? .... 90
숫자 7? .... 3
입력 리스트 :  ['56', '34', '100', '23', '78', '90', '3']
최소값 :  100
최대값 :  90
'''

# # 퀴즈3
# aList = [78,90,80,50]
# bList = [8,100,34,60]
# 두개의 리스트 요소중에서 최대값과 최소값을 출력하여라
# max(), min() 활용
'''
aList = [78,90,80,50]
bList = [8,100,34,60]

최소값 : 8
최대값 : 100
'''

# 퀴즈 4
# enumerate() 함수를 이용하여 아래 리스트를
# 시작 인덱스가 1이 되게 자료 구조를 생성하고
# 아래 형태로 출력한다.
'''
foodList = ['감자탕', '떡국', '모밀냉면', '연어덮밥', '케이준 샐러드']

1 번째 메뉴: 감자탕
2 번째 메뉴: 떡국
3 번째 메뉴: 모밀냉면
4 번째 메뉴: 연어덮밥
5 번째 메뉴: 케이준 샐러드

'''
