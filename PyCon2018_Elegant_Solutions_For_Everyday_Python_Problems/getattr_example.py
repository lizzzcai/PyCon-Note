


class Operations:
    def say_hi(self, name):
        print('Hello', name)
    
    def say_bye(self, name):
        print('Goodbye', name)

    def default(self, arg):
        print('This operation is not supported.')

if __name__ == '__main__':
    operations = Operations()
    # let's assume error handling
    command, argument = input('> ').split()
    getattr(operations, command, operations.default)(argument)