'''
Pattern 6
'''

class MyLogger:
    def __init__(self, logger=None):
        self.logger = logger
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.logger is None:
                print(str(func) + "is called")
            else:
                self.logger.info(str(func) + "is called")
            return func(*args, **kwargs)
        return wrapper

class MyLoggingMeta(type):

    def __new__(cls, name, bases, attrs):
        for item, value in attrs.items():
            if callable(value):
                print("Function item:" + str(item), str(value), type(value))
                attrs[item] = MyLogger()(value)
            else:
                print(str(item), str(value), type(value))
        return super(MyLoggingMeta, cls).__new__(cls, name, bases, attrs)

class MyClass1(metaclass=MyLoggingMeta):
    def test_m1(self):
        pass
    
    def test_m2(self):
        pass

a = MyClass1()
a.test_m1()
a.test_m2()