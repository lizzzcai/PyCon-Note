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
