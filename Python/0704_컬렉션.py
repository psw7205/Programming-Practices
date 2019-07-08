'''
리스트 []
튜플 ()
딕셔너리 {}
집합 set()
'''

myString = 'abcdefg' + \
           'hijklmno' + \
           'qrsuv' + \
           'wxyz'

print(myString)

myList = [1, 2, 3, 4, 5]
print(myList)
print(myList[0:2])
print(myList[-2])
print(myList[0::2])
print('-' * 30)

myList = list()
myList.append(True)
myList.append("문자")
myList.append([1, 2, 3])
myList.insert(1, 10)
print(myList)
print(len(myList))
print('-' * 30)

print(myList + myList)
print('-' * 30)

print(myList)
myList[0] = 100
myList[-1] = '리스트'
print(myList)
print('-' * 30)
'''
listC = list()
listC.append(input())
listC.append(input())
listC.append(input())
print(listC)
print('-'*30)
'''
myList = ['a', 'b', 'c', 'd', 'e', 'f']
myList.remove('c')
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(3))
print(myList)
myList.clear()
print(myList)
print('-' * 30)

myList = [20, 10, 30, 50, 40]
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print('-' * 30)

myList = [1, 1, 2, 3, 2, 3, 3, 1]
print(myList.count(1))
print(myList.index(2))
myList.extend([4, 5, 6, 7])
print(myList)
print('-' * 30)

listMulti1 = [1, 2, ['a', 'b', 'c'], ['포도', '수박']]
print(listMulti1, type(listMulti1))
print(listMulti1[0])
print(listMulti1[2])
print(listMulti1[2][0])
print(listMulti1[3][-1])
print('-' * 30)

myString = '도 레 미   파 솔 라 시 솔라시도'
print(myString)
print(myString.split())
print(list(myString))
print('-' * 30)

myList = ['김씨', '박씨', '남궁씨', '신씨', '이영자', '박소영']
print(myList, type(myList))
result1 = str(myList)
print(result1, type(result1))
print(result1[0:3])
print('-' * 30)

result2 = ' '.join(myList)
print(result2, type(result2))
result3 = ','.join(myList)
print(result3, type(result3))
print('-' * 30)

k = [100, 80, 50]
m = [60, 80, 70]
e = [80, 70, 60]
g = [k, m, e]

print(g)

print(g[0][0] + g[1][0] + g[2][0])
print(g[0][1] + g[1][1] + g[2][1])
print(g[0][2] + g[1][2] + g[2][2])
print('-' * 30)

myTuple = ('1',)
myTuple = ('1', '2', '3', '4')
print(myTuple, id(myTuple))
myTuple += ('5', '6')
print(myTuple, id(myTuple))

myList = list(myTuple)
print(myList, type(myList))
myTuple = tuple(myList)
print(myTuple, type(myTuple))
print(str(myTuple), type(str(myTuple)))
print('-'.join(myTuple))

myString = '가나다라마바사' \
           ''
print(tuple(myString))
print('-' * 30)

myDict = {'a': 1, 'b': 2, 'c': 3}
print(myDict)
print(myDict['b'])

myDict['a'] = '일'
myDict['d'] = 4
print(myDict.pop('b'))
del myDict['c']
print(myDict)
print('-' * 30)

mySet = {1, 2, 3, 4}
print(mySet)
mySet = set('1234')
print(mySet)
mySet.add('5')
mySet.update({'7', '6'})
print(mySet)
mySet.remove('2')
mySet.discard('1')
print(mySet)

s1 = set({1, 2, 3, 4, 5})
s2 = set({3, 4, 5, 6, 7})
print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

print(s1 ^ s2)

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'vodka', 'kahlua', 'cream'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'vodka', 'orange juice'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)
print('-' * 30)

for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)
print('-' * 30)

for name, contents in drinks.items():
    if 'vodka' in contents and \
            not contents & {'vermouth', 'orange juice'}:
        print(name)

eng = 'Monday', 'Tuesday', 'Wednesday'
fre = 'Lundi', 'Mardi', ' Mercredi'

print(list(zip(eng, fre)))
print(dict(zip(eng, fre)))

# 표현식 for 항목 in 순회가능한 객체
myList = [number - 1 for number in range(1, 6)]
print(myList)

myList = [number for number in range(1, 20) if number % 2 == 1]
print(myList)

word = 'Letter Count'
myDict = {letter: word.count(letter) for letter in set(word)}
print(myDict)
