'''
Pattern 7
'''


class MySealedMeta(type):

    def __new__(cls, name, bases, attrs):
        all_metaclasses = [type(x) for x in bases]
        if MySealedMeta in all_metaclasses:
            raise TypeError("Sealed class cannot be subclassed")
        return super(MySealedMeta, cls).__new__(cls, name, bases, attrs)

class MySealedClass(metaclass=MySealedMeta):
    pass

class MyChildOfSealed(MySealedClass):
    pass