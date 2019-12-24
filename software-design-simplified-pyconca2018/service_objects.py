'''
Service Objects

* A collection of stateless methods for operating on your data.

* Seperation of concerns centers around determining how much a method should do.
'''


from blog.models import BlogVersionModel

class BlogPublishService:

    def __init__(self):
        self.backend = BlogPublishBackend()

    def publish_blog(self, blog):
        # Do some work here ...
        self.backend.publish_blog(blog)
        return blog

class BlogPublishBackend:
    
    def publish_blog(self, blog):
        # Do some work here ...
        newest_version = BlogversionModel(
            **blog.to_dict()
        ).save()
        return blog

service = BlogPublishService()
blog = Blog(author=user, content="Hello!", id=1)
published_blog = service.publish_blog(blog)