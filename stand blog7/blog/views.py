from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def post_list(request,**kwargs):
    posts=Post.objects.filter(active=1)
    if kwargs.get('auth'):
        posts=posts.filter(author__username=kwargs['auth'])
    elif kwargs.get('age'):
        posts=posts.filter(age=kwargs['age'])
    elif kwargs.get('cat'):
        posts=posts.filter(category__name=kwargs['cat'])

    paginator = Paginator(posts,4) 
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    
    context={"posts":posts}
    return render(request,'blog/blog.html',context)

def post_detail(request,pk):
    # post=Post.objects.get(pk=pk)
    post=get_object_or_404(Post,active=1,pk=pk)
    context={'post':post}
    return render(request,'blog/post-details.html',context)

def search(request):
    if request.method=="GET":
        s=request.GET.get('s')
        posts=Post.objects.filter(Q(content__contains=s)|Q(title__contains=s))
        return render(request,'blog/blog.html',context={'posts':posts})

