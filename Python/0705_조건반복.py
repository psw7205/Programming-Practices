a = True

if a:
    print("is true")
else:
    print("is not true")

a = [1, 2, 3]
if 1 in a:
    print('일')
if 2 in a:
    print('이')
if 3 in a:
    print('삼')

furry = True
small = False

if furry:
    if small:
        print("it's a cat")
    else:
        print("it's a bear")
else:
    if small:
        print("it's a skink")
    else:
        print("it's a human")

count = 1
while count <= 10:
    print(count, end=" ")
    count += 1

i = 5
while i > 0:
    print('*' * i)
    i -= 1

myList = []
while True:
    ret = input()
    if ret == 'q':
        break
    elif ret == 'p':
        print(myList)
    else:
        myList.append(ret)

print(myList)

print(range(5))
print(list(range(0, 5)))
print(tuple(range(0, 5)))
print(set(range(0, 5)))

print(list(range(0, 10, 2)))

value = 0
for i in range(20):
    value += i
print(value)

for i in range(5):
    for j in range(i):
        print('*', end='')
    print()

myDict = {'a': 'apple', 'b': 'banana', 'c': 'candy'}
for i in myDict:
    print(i)
    print(myDict[i])

for i in 'abcdefg':
    print(i, end=',')
print()

myList = [1, 2, 3, 4, 5]
print(max(myList))
print(min(myList))

myList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(myList)
for i in myList:
    for j in i:
        print(j, end='/')
    print(f' {i}')

strGradeList = [['박상우', 90, 90, 90],
                ['김민수', 80, 70, 90],
                ['이동진', 70, 90, 90],
                ['김예슬', 80, 90, 70]]
for (name, i, j, k) in strGradeList:
    print(f'{name} {i} {j} {k} {(i + j + k) / 3:.2f}')

print(sum(range(1, 101)))

myList = [i for i in range(1, 10)]
print(myList)

myList = [i * 3 for i in range(1, 10)]
print(myList)

myList = [i * j for i in range(1, 10) for j in range(1, 10)]
print(myList)
