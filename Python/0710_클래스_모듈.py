class Person:
    def __init__(self, name):
        self.name = name

    def my_print(self):
        print('person', self.name)


class Student(Person):
    def __init__(self, name):
        super().__init__('Student ' + name)

    def study(self):
        super().my_print()
        print(self.name, 'study')


class Professor(Person):
    def __init__(self, name):
        super().__init__('Professor ' + name)

    def research(self):
        super().my_print()
        print(self.name, 'research')


student = Student('psw')
student.study()

professor = Professor('psw')
professor.research()


class GetterSetter:
    def __init__(self, _in):
        self.__prop = _in

    def getter(self):
        return self.__prop

    def setter(self, _in):
        self.__prop = _in

    prop = property(getter, setter)


getset = GetterSetter('psw')
print(getset.prop)
getset.prop = 'python'
print(getset.prop)


# print(getset.__prop) # __를 이용하여 직접 접근 X

class DecoratorProp:
    def __init__(self, _in):
        self.__privateProp = _in

    @property
    def prop(self):
        return self.__privateProp

    @prop.setter
    def prop(self, _in):
        self.__privateProp = _in


deco = DecoratorProp('psw')
print(deco.prop)
deco.prop = 'python'
print(deco.prop)


class ClassMethod:
    cnt = 0

    def __init__(self):
        ClassMethod.cnt += 1

    @classmethod
    def return_cnt(cls):
        return cls.cnt

    @staticmethod
    def my_print():
        print('this is staticmethod')


ClassMethod.my_print()

a = ClassMethod()
b = ClassMethod()
c = ClassMethod()
d = ClassMethod()
print(ClassMethod.return_cnt())

ClassMethod.cnt = 10
print(ClassMethod.return_cnt())


class MyWord:
    def __init__(self, _str):
        self.text = _str

    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

    def __add__(self, other):
        return f'{self.text} + {other.text} : ADD'

    def __str__(self):
        return self.text


first = MyWord('psw')
second = MyWord('PSW')

print(first == second)
print(first + second)
print(str(first))

from MyModule import *

print(MyModule.PI)
print(MyModule.Math.solve(5))
print(MyModule.add(1, 2))

print(gugu.guguPrint(7))

print(dir(MyModule))
