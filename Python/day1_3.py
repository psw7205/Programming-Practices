################
# 문자열 인덱싱 - p51
# - 인덱싱 첫위치 값은 0
# - 인덱싱 숫자값이 음수면 역순 : -1 (마지막위치값)
# 문자열변수[인덱스값]
myString = 'abcdefg'
print('myString : ', myString)
print('myString[0] : ', myString[0] )
print('myString[-1] : ', myString[-1])
print('myString[3] : ', myString[3])
print('myString[-2] : ', myString[-2])

# 문자열 슬라이싱
# 문자열변수[start:end]  : start 부터 end-1
# 문자열변수[start:end:step] : start 부터 end-1 까지 step 수만큼 건너뛰기
# 문자열변수[start:] : start 부터 끝까지
# 문자열변수[:end] : 첫번째 부터 end-1
myString2 = 'abcdefghijklmn'
print('myString2 : ', myString2)
print('myString2[0:3] : ', myString2[0:3])
print('myString2[:3] : ', myString2[:3])
print('myString2[5:] : ', myString2[5:])
print('myString2[0:5:2] : ', myString2[0:5:2])
print('myString2[-1:] : ', myString2[-1:])
print('myString2[-5:-1] : ', myString2[-5:-1])

print('\n'*5)
# %를 이용한 포맷팅 : p58
# style : 문자열안에 입력, %s, %d, %전체자리수.소숫점자리f
# ' style ' % 변수나값
today = '수요일'
yesterday = '화요일'
print('오늘은 ', today, ' 입니다.')
print('오늘은  %s  입니다. ' % today)
print('오늘은  %s  입니다. 어저께는 %s 입니다. ' % (today, yesterday) )
myNum1 = int(input('숫자를 입력하세요'))
myNum2 = float(input('숫자를 입력하세요'))
print('입력받은 값은 %d 입니다.' % myNum1 )
print('입력받은 값은 %f 입니다.' % myNum2 )

# %전체자릿수.소수점이하자릿수f
pi = 3.14156748
print('pi : %f' % pi )  # 3.141567
print('pi : %.3f' % pi ) # 3.142 (반올림)
print('pi : %10.2f' % pi ) #       3.14
print('pi : %3.5f' % pi ) # 3.14157
print('pi : %15.1f' % pi ) #             3.1

# % 퍼센트 기호 표시
# 오늘의 미세농도는 0.0005 % 입니다.
todayM = 0.0005
# 아래는 에러발생
# print( '오늘의 미세농도는 %f % 입니다.' % todayM)
print( '오늘의 미세농도는 %f %% 입니다.' % todayM)

# %로 공백 지정
# %양수숫자Style(s,f,d) : 왼쪽에 공백 생성
# %음수숫자Style(s,f,d) : 오른쪽에 공백 생성
userName = '홍길동'
print('user Name : %10s ** '%userName)
print('user Name : %-10s ** '%userName)

# format 을 이용한 출력방식
# ' 문자열 {} {}'.format(변수1, 변수2)
# ' 문자열 {index1} {index2}'.format(변수1, 변수2)
color = 'blue'
myNumber = 7
# 인덱스 생략
print(' color {} number {} '.format(color, myNumber))
# 인덱스 지정
print(' 순서교체 : number {1} color {0} '.format(color, myNumber))
# 초기값 다시 지정
# 여러줄 명령 작성시는 백슬라시(\)로 연결한다.
print(' 이름지정 : number {myNumber} color {color} ' \
      .format(myNumber=100, color='red'))

# :>숫자 (앞에 공백생성) , :<숫자(뒤에 공백생성), :^숫자(좌우에 여백생성) : {}안에 입력
# :대체문자>숫자 (앞에 대체문자생성) , :대체문자<숫자(뒤에대체문자생성)
# :대체문자^숫자(좌우에 대체문자)
print('... {} ...'.format('hello world'))
print('... {:>30} ...'.format('hello world'))
print('... {:<30} ...'.format('hello world'))
print('... {:^30} ...'.format('hello world'))
print('... {:*^30} ...'.format('hello world'))









