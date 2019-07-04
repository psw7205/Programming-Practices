# 퀴즈 1:
# 아래와 같이 3줄로 글자를 출력하는 4가지 방법은?
'''
파이썬
파이썬
파이썬
'''
print('''
파이썬
파이썬
파이썬
''')

print('파이썬')
print('파이썬')
print('파이썬')

print('파이썬\n파이썬 \n파이썬')

# 퀴즈 2
# 변수 a,b를 입력문을 이용하여 데이터를 저장한다.
# is 연산자나 == 을 이용하여 a,b 가 같은지 True, False 로 출력하여라
'''
a ? 10
b ? 10
True
'''
a = 10
b = 10
print(a == b)

# 퀴즈 3
# 2개의 숫자를 입력받아
# 사칙연산의 결과물을 출력하여라
# 출력시 % 포맷 형식 이용

'''
첫번째 숫자를 입력하세요? 34
두번째 숫자를 입력하세요? 56

결과 :
34 + 56 = 
34 - 56 =
34 * 56 =
34 / 56 =

'''
a = int(input())
b = int(input())

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')

# 퀴즈 4
# 홍길동씨의 주민등록번호는 881120-1068234
# 연월일과 숫자 부분을 나누어서 출력하여라.
'''
연월일 : 881120
숫자 : 1068234
'''
num = '881120-1068234'
print(num.split('-')[0])
print(num.split('-')[1])

# 퀴즈 5
# 2개의 변수를 정의하고 아래와 같이 출력한다.
# format 이용

'''
movie1 = '알라딘'
movie2 = '스파이더맨'

--------------
스파이더맨      :        알라딘
+++   알라딘    +++

'''
movie1 = '알라딘'
movie2 = '스파이더맨'

print('{0:<10} : {1:>10}'.format(movie1, movie2))
print('+++   {0}   +++'.format(movie1))
print(f'+++{movie2:^10}+++')

# 퀴즈 6
# 다음과 같이 교체한다.
# replace() 이용

'''
좋아하는 꽃 - 장미 

좋아하는 꽃 - 백합 

좋아하는 flower - 백합 
'''
text = '좋아하는 꽃 - 장미'
print(text)
print(text.replace('장미', '백합'))
print(text.replace('장미', '백합').replace('꽃', 'flower'))

# 퀴즈 7
# 다음과 같이 문자열 변수를 정의하고 결과값이 출력되도록 한다.
'''
Let thy speech be short, comprehending much in few words.

첫번째 t의 위치 : 3
첫번째 m의 위치 : 28
s 의 갯수 : 3

= 으로 연결 : 
 L=e=t= =t=h=y= =s=p=e=e=c=h= =b=e= =s=h=o=r=t=,= =c=o=m=p=r=e=h=e=n=d=i=n=g= =m=u=c=h= =i=n= =f=e=w= =w=o=r=d=s=.

대문자로 변경 : 
LET THY SPEECH BE SHORT, COMPREHENDING MUCH IN FEW WORDS.
'''
text = 'Let thy speech be short, comprehending much in few words.'

print(text.find('t'))
print(text.find('m'))
print(text.count('s'))
print('='.join(text))
print(text.upper())
