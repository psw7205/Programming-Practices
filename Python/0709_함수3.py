def two_times(x):
    return x * 2


print(list(map(two_times, [1, 2, 3, 4])))

result = map(lambda x: x ** 2, [3, -10, 2, 6])
print(list(result))

for i in map(lambda x: x ** 2, [3, -10, 2, 6]):
    print(i, end=' ')
print()

import random

myList = random.sample(range(1, 20), 10)

print(myList)
print(myList.sort())
print(myList)

myList = random.sample(range(1, 20), 10)
print(sorted(myList))

testWord = 'java1234python2293'

cnt = 0
cnt2 = 0
for i in testWord:
    if i.isdigit():
        cnt += 1
    elif i.isalpha():
        cnt2 += 1

print(cnt, cnt2)

print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))

a = [1, 2, 3]
b = [2, 3, 4]
c = [3, 4, 5]
for i, j, k in zip(a, b, c):
    print(i, j, k)

myFilter = list(filter(lambda x: x > 0, [1, -1, 3, -3, 2]))
print(myFilter)

myList = random.sample(range(1, 25), 20)
myFilter = filter((lambda x: not x % 2), myList)

for i in myFilter:
    print(i, end='/')
print()


print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))

print(dir([1, 2, 3]))

print(random.random())
data = [1, 2, 3, 4, 5]
print(random.shuffle(data))

import calendar

print(calendar.calendar(2019))

calendar.prcal(2019)
calendar.prmonth(2019, 7)

day = ['월', '화', '수', '목', '금', '토', '일']
print(day[calendar.weekday(2019, 7, 10)])

