# Nina Zakharenko - Elegant Solutions For Everyday Python Problems - PyCon 2018

video: https://www.youtube.com/watch?v=WiQqqB9MlkA
slide: http://bit.ly/elegant-python-2018


Speaker: Nina Zakharenko

Are you an intermediate python developer looking to level up? Luckily, python provides us with a unique set of tools to make our code more elegant and readable by providing language features that make your code more intuitive and cut down on repetition. In this talk, I’ll share practical pythonic solutions for supercharging your code. 

Specifically, I'll cover:

- What magic methods are, and show you how to use them in your own code.
- When and how to use partial methods.
- An explanation of ContextManagers and Decorators, as well as multiple techniques for implementing them.
- How to effectively use `NamedTuples`, and even subclass and extend them!

Lastly, I'll go over some example code that ties many of these techniques together in a cohesive way. You'll leave this talk feeling confident about using these tools and techniques in your next python project!

# Magic methods
Magic method start and end with a double underscore(dunder)
By implementing a few straightforward magic methods, you can make your objects hebave like built-ins such as:
* numbers
* lists
* dictonaries
* and more ...

```python
class Money:
    currency_rates = {
        '$':1,
        '€': 0.88,
    }
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount
    
    def __str__(self):
        return '%s%.2f' % (self.symbol, self.amount)

    def convert(self, other):
        """Convert other amount to our currency"""
        new_amount = (other.amount/self.currency_rates[other.symbol] * self.currency_rates[self.symbol])
        return Money(self.symbol, new_amount)
    
    def __add__(self, other):
        new_amount = self.amount + self.convert(other).amount
        return Money(self.symbol, new_amount)
```

## some magic methods map to symbols
```python
d = {'one':1, 'two':2}
>>> d['two']
2

>>> d.__getitem__('two')
2
```

```python
class SquareShape:
    def __len__(self):
        """Return the number of side in our shape"""
        return 4

my_square = SquareShape()
print(len(my_square))
# >>> 4
```

## Making classes `iterable`
* In order to be iterable, a class needs to implement `__iter__()`

* `__iter__()` must return an iterator

* In order to be an iterator a class neeeds to implement `__next__()` which must raise `StopIteration` when there are no more items to return

### Scenario

* We have a Server instance running services on different ports.
* Some services are active, some are inactive.
* When we loop over our the Server instance, we only want to loop over active services.

```python
class IterableServer:
    services = [
        {'active': False, 'protocol:': 'ftp', 'port': 21},
        {'active': True, 'protocol:': 'ssh', 'port': 22},
        {'active': True, 'protocol:': 'http', 'port': 80},
    ]

    def __init__(self):
        self.current_pos = 0
    
    def __iter__(self):
        # can return self, because __next__ implemented
        return self
    
    def __next__(self):
        while self.current_pos < len(self.services):
            service = self.services[self.current_pos]
            self.current_pos += 1
            if service['active']:
                return service['protocol'], service['port']
        raise StopIteration

```

TIP: use a `generator` when your iterator doesn't need to maintain a lot of state

```python
class Server:
    services = [
        {'active': False, 'protocol': 'ftp', 'port': 21},
        {'active': True, 'protocol': 'ssh', 'port': 22},
        {'active': True, 'protocol': 'http', 'port': 80},
    ]
    def __iter__(self):
        for service in self.services:
            if service['active']:
                yield service['protocol'], service['port']

if __name__ == "__main__":
    for protocol, port in IterableServer():
        print(f"service {protocol} on port {port}")

    for protocol, port in Server():
        print(f"service {protocol} on port {port}")
```

use single parenthesis () to create a `generator comperhension`

```python
my_gen = (num for num in range(10))
# >>> my_gen
# <generator object <genexpr> at 0x7f3f80acd8e0>
```

An iterator must implement `__next__()` and raise `StopIteration` when there are no more elements

## alias method

```python
class Word:
    def __init__(self, word):
        self.word = word
    
    def __repr__(self):
        return self.word
    
    def __add__(self, other_word):
        return Word('%s %s' % (self.word, other_word))
    
    # Add an alias from method __add__ to the method concat
    concat = __add__
```

## getattr method
getattr(object, name, default)

```python
class Dog:
    sound = 'Bark'
    def speak(self):
        print(self.sound + '!', self.sound + '!')

if __name__ == "__main__":
    my_dog = Dog()
    my_dog.speak()
    # Bark! Bark!

    print(getattr(my_dog, 'speak'))
    # <bound method Dog.speak of <__main__.Dog object at 0x7f1bb764bb70>>

    speak_method = getattr(my_dog, 'speak')
    speak_method()
    # Bark! Bark!
```


Example: command line tool with dynamic commands
```python
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
```

additional reading - inverse of `getattr()` is `setattr()`

## functools.partial(func, *args, **kwargs)

- Return a new partial object with behaves like func called with args & kwargs
- if more arguments are passed in, they are appended to args
- if more keyword arguments are passed in, they extend and overide kwargs

```python
from functools import partial

basetwo = partial(int, base=2)

print(basetwo)
# functools.partial(<class 'int'>, base=2)
print(basetwo('10010'))
# 18
```

another example project:
https://github.com/mozilla/agithub


## Context Managers
When should I use one?

    Need to perform an action before and/or after an operation.

Common scenarios:
- Closing a resource after you're done with it (file, network connection)

- Perform cleanup before/ater a function call

Example Problem: Feature Flags

Turn features of your application on and off easily.

Uses of feature flags:
- A/B Testing
- Rolling Releases
- Show Beta version to users opted-in to Beta Testing Program

```python
class feature_flag:
    """Implementing a Context Manager using Magic Method"""

    def __init__(self, name, on=True):
        self.name = name
        self.on = on
        self.old_value = feature_flags.is_on(name)
    
    def __enter__(self):
        feature_flags.toggle(self.name, self.on)

    def __exit__(self, *args):
        feature_flags.toggle(self.name, self.old_value)

'''
The better way: using the contextmanager decorator
'''
from contextlib import contextmanager

@contextmanager
def feature_flag_context(name, on=True):
    """The easier way to create Context Managers"""
    old_value = feature_flags.is_on(name)
    # behavior of __enter__()
    feature_flags.toggle(name, on)
    yield
    # behavior of __exit__()
    feature_flags.toggle(name, old_value)
```


## Decorators
Syntactic sugar that allows modification of an underlying function.

Wrap a function in another function.
- Do something:
  - before the call
  - after the call
  - with provided arguments

```python 
# to avoid lost context when using a decorator
from contextlib import wraps

class User:
    is_authenticated = False

    def __init__(self, name):
        self.name = name

# Throw an exception if trying to access data only for logged in users.

# function without decorator
def display_profile_page_without_decorator(user):
    """Display profile page for logged in User"""
    if not user.is_authenticated:
        raise Exception('User must login.')

    print('Profile: %s' % user.name)


# decorator
def enforce_authentication(func):
    @wraps(func)
    def wrapper(user):
        if not user.is_authenticated:
            raise Exception('User must login.')
        return func(user)
    return wrapper

@enforce_authentication
def display_profile_page_with_decorator(user):
    """Display profile page for logged in User"""
    print('Profile: %s' % user.name)

if __name__ == '__main__':
    user = User('nina')

    print(display_profile_page_with_decorator.__name__)
    display_profile_page_without_decorator(user)
    display_profile_page_with_decorator(user)

```

Tip: `from contextlib import wraps` to avoid lost context when using a decorator

Common uses:
* logging
* timing
* validation
* rate limiting
* mocking/patching

## ContextDecorators
- By using `ContextDecorator` you can eaily write classes that can be used both as decorators with `@` and context managers with the with statement.
- Context Decorator is used by `contextmanager()` so you get this funcionality `automatically`.

## NamedTuple

Useful when you need lightweight repersentations of data.

Create tuple subclasses with named fields.

Give namedTuples default values

```python
RoutingRule = namedtuple(
    'RoutingRule',
    ['prefix', 'queue_name', 'wait_time']
)

# 1. By specifying defaults
RoutingRule.__new__.__defaults__ = (None, None, 20)

# 2. or with _replace to customize a prototype instance
default_rule = RoutingRule(None, None, 20)
user_rule = default_rule._replace(
    prefix='user', queue_name='user-queue'
)
```

NamedTuples can be subclassed and extended
```python
class Person(namedtuple('Person', ['first_name', 'last_name'])):
    """Stores first and last name of a person"""

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

me = Person('L.', 'Cai')
print(str(me))
```