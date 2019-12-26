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