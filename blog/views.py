from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(Request):
    blogs = Blog.objects
    return render(Request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})
