from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/blog-popular-posts.html')
def popular_posts(args=3):
    posts = Post.objects.filter(status=1).order_by('-counted_view')[:args]
    return {'posts': posts}