try:
    f = open("존재하지 않는 파일", 'r')
except Exception as err:
    print(err)
print("-" * 30)
myList = [1, 2, 3]
idx = 5

try:
    print(list[idx])
except Exception as err:
    print(err)
print("-" * 30)
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
print("-" * 30)
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)
print("-" * 30)
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
print("-" * 30)


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except Exception as error:
        print("exception :", error)
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
        print("-" * 30)


divide(2, 1)
divide(2, 0)
divide("2", "1")


class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    pass


eagle = Eagle()


# eagle.fly()


class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
