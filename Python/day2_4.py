# 집합 생성
# 집합이름 = set(리스트|문자열|튜플)
# { 아이템1 , 아이템2 .. }
# 순서가 없다 => 인덱싱 불가
# 중복값이 없다
# 교체 불가, 아이템 추가 가능, 아이템 삭제 가능
set1 = set(['a', 'b', 'b', 'a','c'])
print(set1, type(set1))
# 순서가 없다 => 인덱싱 불가 : TypeError
# print(set1[0])
print('전체 길이 : ', len(set1))
# 문자열구조 => 집합구조
set2 = set('abcd100100')
print(set2, type(set2))
# 튜플구조 => 집합구조
set3 = set(('부산', '울산','광주', '광주', '전주'))
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
s1 = set([1,100,200,5,300])
s2 = set([10,100,200,50,500])
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