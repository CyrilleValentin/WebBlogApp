from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Blog, Like


# Create your views here.
@login_required
def home(request):
    blogs = Blog.objects.all()
    user=request.user
    context={
        'blogs':blogs,    
        'user':user,    
    }
    return render(request, 'home.html', {'blogs': blogs})
@login_required
def post_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'post_detail.html', {'blog': blog})

@login_required
def new_post(request):
    return render(request, 'new_post.html')

def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        user = request.user
        blog = Blog(title=title, content=content, image=image, user=user)
        blog.save()
        return redirect('home') 
    return render(request, 'new_post.html')

@login_required
def like_post(request,):
    user=request.user
    if request.method=='POST':
        post_id=request.POST.get('post_id')
        post_obj=Blog.objects.get(id=post_id)
        if user in post_obj.likes.all():
             post_obj.likes.remove(user)
        else:
             post_obj.likes.add(user) 
       # likes, created=Like.objects.get_or_create(user=user,post_id=post_id)   
    return redirect('home')
    


