from collections import namedtuple

CacheInfo = namedtuple(
    "CacheInfo", ["hits", "misses", "max_size", "curr_size"]
)

# Give namedTuples default values

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
print(default_rule)
print(user_rule)

# NamedTuples can be subclassed and extended

class Person(namedtuple('Person', ['first_name', 'last_name'])):
    """Stores first and last name of a person"""

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

me = Person('L.', 'Cai')
print(str(me))