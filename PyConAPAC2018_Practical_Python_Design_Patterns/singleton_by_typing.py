


# Metaclasses

class MySingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MySingletonMeta, cls).__call__(*args)
        return cls._instances[cls]

class MySingletonClass(metaclass=MySingletonMeta):
    def __init__(self):
        self.i = 1

a = MySingletonClass()
b = MySingletonClass()

print(type(a), id(a))
print(type(b), id(b))



