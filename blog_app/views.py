from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Blog


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
    return redirect('home')
    


