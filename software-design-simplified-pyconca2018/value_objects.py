'''

'''

from typing import NamedTuple

class User(NamedTuple):
    username: str
    def __repr__(self) -> str:
        return f'<User {self.username}>'

class Blog(NamedTuple):
    author: User
    content: str
    id: int

    def to_dict(self):
        return self._asdict()

class Component(NamedTuple):
    part_number: int
    weight: float
    description: Optional[str] = None

user = User(username="Lize Cai")
blog = Blog(author=user, content="Hello World!", id=1)

print(user)
print(blog)
print(blog.to_dict())