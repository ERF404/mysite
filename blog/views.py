from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


def blog_view (request,**kwargs):

    posts = Post.objects.filter(
        status=1,
        published_date__lte=timezone.now()
        )
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])

    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

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

def blog_search(request):

    posts = Post.objects.filter(
        status=1,
        published_date__lte=timezone.now()
        )
    
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(
                Q(content__contains=s) |
                Q(title__contains=s)
            )

    context = {'posts': posts}
    return render (request, 'blog/blog-home.html', context)
    