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
