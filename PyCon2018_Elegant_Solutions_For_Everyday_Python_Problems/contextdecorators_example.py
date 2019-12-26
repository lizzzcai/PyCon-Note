from contextlib import contextmanager


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


@contextmanager
def feature_flag(name, on=True):
    old_value = feature_flags.is_on(name)
    feature_flags.toggle(name, on)
    yield
    feature_flags.toggle(name, old_value)


def get_homepage_url():
    """Return the path of the page to display"""
    if feature_flags.is_on(FeatureFlags.SHOW_BETA):
        return '/beta'
    else:
        return '/homepage'

# use it as a context manager
with feature_flag(FeatureFlags.SHOW_BETA):
    assert get_homepage_url() == "/beta"

# or use it as a decorator
@feature_flag(FeatureFlags.SHOW_BETA, on=False)
def get_profile_page():
    beta_flag_on = feature_flags.is_on(
        FeatureFlags.SHOW_BETA
    )
    if beta_flag_on:
        return 'beta.html'
    else:
        return 'profile.html'