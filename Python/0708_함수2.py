print(abs(-1))

print(max([1, 2, 3, 4, 5, 6]))
print(min([1, 2, 3, 4, 5, 6]))

print(divmod(6, 4))

print('-' * 50)
import sys

for place in sys.path:
    print(place)

print('-' * 50)
from collections import defaultdict

counter = defaultdict(int)
for i in ['a', 'a', 'b', 'a', 'c', 'c', 'b', 'c']:
    counter[i] += 1

print(counter)

myDict = {}
for i in ['a', 'a', 'b', 'a', 'c', 'c', 'b', 'c']:
    if not (i in myDict):
        myDict[i] = 0
    myDict[i] += 1

print(myDict)

from collections import Counter

myList = ['a', 'a', 'b', 'a', 'c', 'c', 'b', 'c']
counter = Counter(myList)
print(counter)
print(counter.most_common())

myList = ['c', 'b', 'a', 'b', 'b', 'a', 'c', 'c']
counter2 = Counter(myList)

print('-' * 50)
print(counter)
print(counter2)
print(counter + counter2)
print(counter - counter2)
print(counter & counter2)
print(counter | counter2)

print('-' * 50)
from collections import OrderedDict

oderedDict = OrderedDict([
    ('a', 'apple'),
    ('b', 'banana'),
    ('c', 'carrot'),
    ('d', 'dict'),
])

for i, j in oderedDict.items():
    print(i, j)

print('-' * 50)
from collections import deque


def is_palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        return True


print(is_palindrome('abc'))
print(is_palindrome('level'))


def is_palindrome2(word):
    return word == word[::-1]


print(is_palindrome2('abc'))
print(is_palindrome2('level'))

print((lambda word: word == word[::-1])('abc'))
print((lambda word: word == word[::-1])('토마토'))

myEnum = enumerate(['apple', 'banana', 'carrot', 'dict'])

for i, j in myEnum:
    print(i, j)

myEnum = enumerate(['apple', 'banana', 'carrot', 'dict'], 10)
print(list(myEnum))
