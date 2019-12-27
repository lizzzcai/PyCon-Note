


class TestClass:
    
    def __new__(cls, *args, **kwargs):
        print('new method called')
        instance = super(TestClass, cls).__new__(cls, *args, **kwargs)
        return instance

    def __call__(self, a, b, c):
        self.call_count += 1
        print('called method called')
        return a * b * c
    
    def __init__(self):
        self.call_count = 0
        super(TestClass, self).__init__()
        print('init method called')

    def get_call_count(self):
        return self.call_count
    

a = TestClass()

print(f'a(1,2,3): {a(1,2,3)}')

print(f'a.get_call_count(): {a.get_call_count()}')