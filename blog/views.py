from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone


def blog_view (request,**kwargs):

    posts = Post.objects.filter(
        status=1,
        published_date__lte=timezone.now()
        )
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])

    context = {'posts': posts}
    return render (request, 'blog/blog-home.html', context)


def blog_single (request,pid):

    posts = Post.objects.filter(
        status=1,
        published_date__lte=timezone.now()
        ).order_by('id')
    
    post = get_object_or_404(posts,id=pid)

    post.counted_view += 1
    post.save(update_fields=['counted_view'])

    index_list = list(posts)
    post_index = index_list.index(post)
    previous_post = index_list[post_index-1] if post_index > 0 else None
    next_post= index_list[post_index+1] if post_index < len(index_list) - 1 else None

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post
    }

    return render (request, 'blog/blog-single.html', context)