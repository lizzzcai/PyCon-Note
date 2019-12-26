'''
Pattern 2
'''

from abc import ABCMeta, ABC, abstractmethod

class MySingletonABCMeta(ABCMeta):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MySingletonABCMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyAbstractSingletonClass(metaclass=MySingletonABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def my_abstract_method(self):
        pass

'''
>>> MyAbstractSingletonClass()

TypeError: Can't instantiate abstract class MyAbstractSingletonClass with abstract methods my_abstract_method
'''

class MyAbstractSingletonChild(MyAbstractSingletonClass):
    def __init__(self):
        pass

    def my_abstract_method(self):
        pass

a1 = MyAbstractSingletonChild()
b1 = MyAbstractSingletonChild()

print(type(a1), id(a1))
print(type(b1), id(b1))
