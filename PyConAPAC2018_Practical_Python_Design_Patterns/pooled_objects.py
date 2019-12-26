

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