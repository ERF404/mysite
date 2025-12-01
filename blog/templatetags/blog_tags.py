from django import template
from blog.models import Post
from blog.models import Category

register = template.Library()

@register.inclusion_tag('blog/blog-popular-posts.html')
def popular_posts(args=3):
    posts = Post.objects.filter(status=1).order_by('-counted_view')[:args]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count
    return {'categories':cat_dict}

