def hello():
    print('Hello World')


def hello2(name):
    print(name, 'Hello')


hello()
hello2('psw')


def def_list(arg, result=[]):
    result.append(arg)
    print(result)


def_list('a')
def_list('b')


def def_list2(arg):
    result = []
    result.append(arg)
    print(result)


def_list2('a')
def_list2('b')


def default_parm(a=0, b=0, c=0):
    return a + b + c


print(default_parm(1))
print(default_parm(1, 2))
print(default_parm(1, 2, 3))


# 위치 인자 모으기
def my_print(str1, str2, *args):
    print('str1 is', str1)
    print('str1 is', str2)
    print('rest', args)


my_print('a', 'b', 'c', 'd', 'e')


# 키워드 인자 모으기
def my_print2(**kwargs):
    print('KeyWord', kwargs)


my_print2(wine='merlot', entree='mutton', dessert='macaroon')


# 일급 시민 함수
def run_function(func):
    func()


run_function(hello)


def run_function2(func, arg1, arg2):
    func(arg1, arg2)


run_function2(my_print, 'abc', 'def')


# 내부 함수
def outer(a, b):
    def inner(c, d):
        return c + d

    return inner(a, b)


outer(1, 2)


# 클로저
def say(arg):
    def inner():
        return f'He say {arg}'

    return inner()


a = say('HaHaHa')
b = say('BlahBlah')
print(a)
print(b)


# 람다
def my_lambda(func, num):
    print(func(num))


my_lambda(lambda x: x * 2, 10)
my_lambda(lambda x: x * 4, 10)
print((lambda x, y: x + y)(10, 20))


# 제너레이터
def my_range(first=0, last=0, step=1):
    number = first
    while number < last:
        yield number
        number += step


for i in my_range(1, 20, 3):
    print(i, end="/")
print();


# 데커레이터
def document_func(func):
    def new_func(*args, **kwargs):
        print('running :', func.__name__)
        print('args :', args)
        print('kwargs :', kwargs)
        result = func(*args, **kwargs)
        print('result :', result)
        return result

    return new_func


def my_add(a, b):
    return a + b


my_decorator = document_func(my_add)
print(my_decorator(10, 20))

cnt = 0


def global_func():
    global cnt
    cnt += 1


global_func()
global_func()
global_func()
global_func()

print(cnt)
