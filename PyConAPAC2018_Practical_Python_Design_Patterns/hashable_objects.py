a = [1,2]
# b = {a:1} 
# # TypeError: unhashable type: 'list'
# print(b)

print(a.__hash__) # None
# print(hash(a))
'''
Traceback (most recent call last):
  File "hashable_objects.py", line 7, in <module>
    print(hash(a))
TypeError: unhashable type: 'list
'''
a = (1,2)
b = {a:1} 
print(b)

print(a.__hash__) # None
print(hash(a))


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

a1 = MyHashableClass(1,2,3)
a2 = MyHashableClass(4,5,6)
a3 = MyHashableClass(4,5,8)

print(a1 == a2)

print(a2 == a3)

a = {}

a[a1] = 1
print(a)