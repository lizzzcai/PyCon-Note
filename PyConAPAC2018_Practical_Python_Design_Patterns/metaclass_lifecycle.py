# Life Cycle with Metaclasses
class MyMetaClass(type):
    _test_attribute = 1
    def __new__(cls, *args, **kwargs):
        print("metaclass new method called")
        return super(MyMetaClass, cls).__new__(cls, *args, **kwargs)
    
    def __call__(cls, *args, **kwargs):
        print("metaclass call method called")
        return super(MyMetaClass, cls).__call__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("metaclass init method called")
        return super(MyMetaClass, self).__init__(*args, **kwargs)

    def test_method_1(self):
        print("MyMetaClass - Test method 1 called")

class MyClass(metaclass=MyMetaClass):
    def __new__(cls, *args, **kwargs):
        print("instance new method called")
        return super(MyClass, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("instance init method called")
        return super(MyClass, self).__init__(*args, **kwargs)

print("-----------------")
ins = MyClass()
print(MyClass._test_attribute)
print(MyClass.__mro__)
print(MyMetaClass.__mro__)
