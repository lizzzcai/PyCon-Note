

def blog_view(request):
    blog = Blog(author=user, content="Hello!", id=1)
    spell_check_service = BlogSpellCheckService()
    blog = spell_check_service.spell_check(blog)
    blog_publish_service = BlogPublishService()
    blog = blog_publish_service.publish_blog(blog)
    blog_metrics_service = BlogMetricsService()
    blog = blog_metrics_service.collection_metrics(blog)

    return Response(blog.to_dict())


class BlogService(object):
    def publish_blog(self, blog):
        blog = Blog(author=user, content="Hello!", id=1)
        spell_check_service = BlogSpellCheckService()
        blog = spell_check_service.spell_check(blog)
        blog_publish_service = BlogPublishService()
        blog = blog_publish_service.publish_blog(blog)
        blog_metrics_service = BlogMetricsService()
        blog = blog_metrics_service.collection_metrics(blog)
