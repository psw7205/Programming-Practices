import os

print(os.getcwd())

# r: 읽기 w: 파일이 없으면 생성, 있으면 덮어 쓰기 x: 파일이 없는 경우에만 쓰기 a: 추가
# t: 텍스트 b: 이진
f = open('./data/Yesterday.txt', 'r')
print(f)
print('-' * 30)

data = f.read()
print(data)
print('-' * 30)

print(data[:10])
myList = data.split()
print(myList[:10])
print(len(myList))

f.close()

print('-' * 30)
f = open('./data/Yesterday.txt', 'r')
print(f.readline())
print('-' * 30)
for line in f.readlines()[:3]:
    print(line, end="")

f.close()

f = open('./data/data_kor.txt', 'r')
myList = f.read().split()
sum = 0
for i in myList:
    sum += int(i)

print(f'{sum / len(myList):.2f}')

f.close()

text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nulla facilisis interdum egestas.
Mauris sagittis mi ornare nisl blandit, at gravida enim laoreet.
Vestibulum nulla nisi, tincidunt quis elementum id, tempor ac odio.
Fusce egestas aliquam lacus, quis efficitur tellus commodo a.
Phasellus purus lectus, mollis eu gravida non, pharetra in diam.
'''
fout = open('./data/test.txt', 'wt')
fout.write(text)
fout.close()

string = ""
with open('./data/sample.txt', 'rt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        string += line

print(len(string))

import csv

with open('./data/data.csv', 'rt') as f:
    rdr = csv.reader(f)
    csvList = [x for x in rdr]
    for line in csvList:
        print(line)

for line in csvList[1:]:
    print(line[2])

with open('./data/population.csv', 'rt') as f:
    population = list(csv.reader(f))
    city = [line[0] for line in population[1:]]
    people = [line[1].replace(',', '') for line in population[1:]]
    people = list(map(int, people))
    print(city[people.index(max(people))], max(people))
    print(city[people.index(min(people))], min(people))

myList = [[3, "Paul", False],
          [4, "Peter", True],
          [5, "Thomas", True],
          [6, "Vincent", False],
          [7, "William", False]]

with open('./data/output.csv', 'w') as f:
    wr = csv.writer(f)
    wr.writerow([1, "Antony", False])
    wr.writerow([2, "John", True])
    wr.writerows(myList)
