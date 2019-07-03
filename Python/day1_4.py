# 문자열 함수
# 샘플문자열 만들기 : https://www.lipsum.com/
# Lorem Ipsum 키워드 검색
sampleTxt = '''
It is a long established fact t
hat a reader will be distracted by the readable 
content of a page when looking at its layout. 
The point of using Lorem Ipsum is 
that it has a more-or-less normal distribution 
of letters, as opposed to using 'Content here, c
ontent here', making it look like readable English. 
Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, 
sometimes on purpose (injected humour and the like).
'''

# 특정 문자열의 갯수 출력
# 문자열.count(찾고자하는문자열)
print('t의 갯수 : ', sampleTxt.count('t'))
print('here의 갯수 : ', sampleTxt.count('here'))

# 특정글자의 위치값 반환
# 문자열.find(찾고자하는문자열)
# 문자열.index(찾고자하는문자열)
print(' f => ', sampleTxt.find('f'))
print(' f => ', sampleTxt.index('f'))
# 찾고자하는 문자열 없다면 -1
print(' 가 => ', sampleTxt.find('가'))
# 찾고자하는 문자열 없다면 ValueError 에러 발생
# print(' 가 => ', sampleTxt.index('가'))


