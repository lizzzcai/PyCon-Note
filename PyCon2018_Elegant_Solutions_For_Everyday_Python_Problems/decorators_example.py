
# to avoid lost context when using a decorator
from contextlib import wraps
import logging
import os

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


def debug(func):
    log = logging.getLogger(func.__module__)
    msg = func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.debug(msg)
        return func(*args, **kwargs)
    return wrapper



if __name__ == '__main__':
    user = User('nina')

    print(display_profile_page_with_decorator.__name__)
    display_profile_page_without_decorator(user)
    display_profile_page_with_decorator(user)

    
