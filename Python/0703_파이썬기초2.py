print(True, end=" ")
print(None, end=" ")
print(type(123), end=" ")
print(type(3.14), end=" ")
print(type("hello"), end=" ")
print(type((1, 2, 3)), end=" ")
print(type([1, 2, 3]), end=" ")
print(type(set([1, 2, 3])), end=" ")
print(type({"a": 1, "b": 2}))
print('-' * 30)

print(float(10), end=" ")
print(int(3.14), end=" ")
print(int("123"))
print('-' * 30)

print(2 + 3, end=" ")
print(2 - 3, end=" ")
print(2 * 3, end=" ")
print(2 / 3, end=" ")
print(2 ** 3, end=" ")
print(2 // 3, end=" ")
print(2 % 3)
print('-' * 30)

a = 10
b = 20
print(a is 10, end=" ")
print(not (a is 10), end=" ")
print(a == 10 and b == 10, end=" ")
print(a == 10 or b == 10)
print('-' * 30)

string = "abcdefghijk"
print(string[2])
print(string[-2])
print(string[2:5])
print(string[5:])
print(string[-5:])
print(string[:5])
print(string[:-5])
print(string[-5:-2])
print(string[0:5:2])
print('-' * 30)

today = '수요일'
print('오늘은 %s' % today)
print('%d 더하기 %d 는 %d' % (1, 2, 1 + 2))

pi = 3.141592
print('%f' % pi)
print('%.3f' % pi)
print('%10.2f' % pi)
print('%3.5f' % pi)

print('{0} {1}'.format(today, pi))
print('{1} {0}'.format(today, pi))
print('{a} {b}'.format(a=today, b=pi))
print(f'{today} {pi}')
print('-' * 30)

longText = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
tempor incididunt ut Lorem et dolore magna aliqua. At Lorem at urna condimentum. 
Nisi quis eleifend quam adipiscing vitae. 
Donec massa Lorem faucibus et molestie ac feugiat. 
'''

print(longText.count('a'))
print(longText.count('Lorem'))
print(longText.find('a'))
print(longText.index('a'))
print(longText.find('ㄱ'))
# print(longText.index('ㄱ')) ValueError

print(longText.replace('Lorem', 'MeroL'))
print(longText.upper())  # lower()
print('-' * 30)

text = 'Python'
print('-'.join(text))
myList = ['a', 'b', 'c', 'd', 'e']
print('+'.join(myList))

text = '    python    '
print(text.rstrip())
print(text.strip())

text = 'a,b,c,d,e,f,g'
print(text.split(','))
