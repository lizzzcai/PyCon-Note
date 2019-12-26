'''
Using Magic Methods __enter__ and __exit__
'''


class FeatureFlags:
    SHOW_BETA = 'Show Beta version of Home Page'

    flags = {
        SHOW_BETA: True
    }

    @classmethod
    def is_on(cls, name):
        return cls.flags[name]
    
    @classmethod
    def toggle(cls, name, value):
        cls.flags[name] = value
    
feature_flags = FeatureFlags()


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


# either implementation

def get_homepage_url():
    """Return the path of the page to display"""
    if feature_flags.is_on(FeatureFlags.SHOW_BETA):
        return '/beta'
    else:
        return '/homepage'
    
def test_homepage_url_with_context_manager():
    
    with feature_flag_context(FeatureFlags.SHOW_BETA):
        assert get_homepage_url() == '/beta'
        print('seeing the beta homepage...')

    with feature_flag_context(FeatureFlags.SHOW_BETA, on=False):
        assert get_homepage_url() == '/homepage'
        print('seeing the standard homepage...')


if __name__ == '__main__':
    test_homepage_url_with_context_manager()