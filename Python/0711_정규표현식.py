import string
import re

myString = string.printable
print(myString)

print(re.findall('\d', myString))  # 숫자
print(re.findall('\D', myString))  # 숫자가 아닌 것
print(re.findall('\w', myString))  # 알파벳
print(re.findall('\W', myString))  # 알파벳이 아닌 것
print(re.findall('\s', myString))  # 공백문자
print(re.findall('\S', myString))  # 공백문자가 아닌 것

text = "문의사항이 있으면 012-345-6789 으로 연락주시기 바랍니다."

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObj = regex.search(text)
print(matchObj.group())

# 그룹으로 분리       group(1)  group(2)
regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
matchObj = regex.search(text)
areaCode = matchObj.group(1)
num = matchObj.group(2)
fullNum = matchObj.group()
print(f'{areaCode}-{num}')
print(fullNum)

text = '''I wish I may, I wish I might
Have a dish of fish tonight'''

print(re.findall('wish|fish', text))  # or
print(re.findall('^I wish', text))  # 시작위치
print(re.findall('fish.$', text))  # 끝위치
print(re.findall('[wf]ish', text))  # w 또는 f 다음에 ish가 오는 단어
print(re.findall('[wsh]+', text))  # w,s,h가 하나 이상인 단어
print(re.findall('I (?=wish)', text))  # wish 이전에 나오는 I
print(re.findall('(?<=I) wish', text))  # I 이후에 나오는 wish

text = 'Young Frankenstein'
print(re.match('Frank', text))  # 없는 경우 none
print(re.match('You', text))  # 시작 패턴 찾기

print(re.search('Frank', text))  # 첫 번째 일치하는 패턴 찾기
print(re.split('n', text))  # 패턴으로 나누기
print(re.sub('n', '!!!', text))  # 일치하는 패턴 바꾸기
