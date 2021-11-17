from django.shortcuts import render

from .models import BlogPost


def posts(request):
    """
    Makes the blog posts accessible and renders the blog template
    """
    all_posts = BlogPost.objects.all()

    template = 'blog/blog.html'
    context = {
        'all_posts': all_posts,
    }
    return render(request, template, context)
