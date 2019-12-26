'''
Pattern 1
'''

from abc import ABCMeta, ABC, abstractmethod


class MyAbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def my_abstract_method(self):
        pass

# MyAbstractClass()

# TypeError: Can't instantiate abstract class MyAbstractClass with abstract methods my_abstract_method

class MyChildClass(MyAbstractClass):
    
    def __init__(self):
        pass

    def my_abstract_method(self):
        pass

mcc = MyChildClass()
print(mcc)