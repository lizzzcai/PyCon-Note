# Practical Python Design Patterns - PyCon APAC 2018

video: https://www.youtube.com/watch?v=FbMP187VNTI


## Singleton

![alt text](docs/big_picture.PNG "The big picture")
![alt text](docs/big_picture1.PNG "The big picture")



![alt text](docs/life-cycle.PNG "The life cycle")

The broad idea
Class Behavior changes:
- Use `__new__()` and `__init__()` of meta class

Change Behavior of instance of the class (typical object)
- Use `__call__()` of meta class


## Pattern 1: Abstract Classes

```python
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
```

## Pattern 2: Abstract family of singleton classes

![alt text](docs/abstract_singleton.PNG "The requirement")
```python
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
```

## Pattern 3: Hashable Objects

```python
from collections import Hashable
from abc import ABCMeta, ABC, abstractmethod

class HashableObject(Hashable, metaclass=ABCMeta):
    def __init__(self):
        pass

    def __eq__(self, other):
        return True if isinstance(other, self.__class__) and self.get_key() == other.get_key() else False

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.get_key())

        @abstractmethod
        def get_key(self):
            pass

class MyHashableClass(HashableObject):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def get_key(self):
        return self.a, self.b
```

## Pattern 4: Comparable Objects

```python
from collections import Hashable
from abc import ABCMeta, ABC, abstractmethod

class ComparableObject:
    def __init__(self):
        pass

    def __eq__(self, other):
        return True if isinstance(other, self.__class__) and self.__dict__ == other.__dict__ else False

    def __ne__(self, other):
        return not self == other

class MyComparableObject(ComparableObject):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

c1 = MyComparableObject(1, 2, 3)
c2 = MyComparableObject(4, 5, 6)
c3 = MyComparableObject(1, 2, 3)

print(c1.__dict__)
print(c2.__dict__)


print(c1 == c2)

print(c1 == c3)
```

## Pattern 5: Pooled Objects

```python
class MyBeanMeta(type):
    _instances = {}

    def __call__(cls, *args):
        print(args)
        key = tuple((cls, args))
        if key not in cls._instances:
            cls._instances[key] = super(MyBeanMeta, cls).__call__(*args)
        return cls._instances[key]

class MyBeanClass(metaclass=MyBeanMeta):
    def __init__(self, a):
        self.a = a

bn1 = MyBeanClass(1)
bn2 = MyBeanClass(2)
bn3 = MyBeanClass(3)
bn4 = MyBeanClass(1)

print(id(bn1), id(bn2), id(bn3), id(bn4))
```

## Pattern 6: Logging using Metaclasses

