from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Blog, Comment,Tag


# Create your views here.
@login_required
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})
@login_required
def post_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog=blog).order_by('-created_at')

    if request.method == 'POST':
        content = request.POST.get('message') 
        user = request.user
        comment = Comment.objects.create(user=user, blog=blog, content=content)
        return redirect('post_detail', blog_id=blog_id)
    return render(request, 'post_detail.html', {'blog': blog,'comments': comments})

@login_required
def new_post(request):
    tags = Tag.objects.all()
    return render(request, 'new_post.html', {'tags': tags})
@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        user = request.user
        tag_id = request.POST.get('tag')
        tag = Tag.objects.get(id=tag_id)
        blog = Blog(title=title, content=content, tags=tag, image=image, user=user)
        blog.save()
        return redirect('home') 
    return render(request, 'new_post.html')
@login_required
def create_tag(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        # Créez le tag
        Tag.objects.create(name=name)
        return redirect('new_post')
     
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
    return redirect('home')

def categories(request):
    tags = Tag.objects.all()
    categories_with_blogs = []

    for tag in tags:
        blogs = Blog.objects.filter(tags=tag)
        categories_with_blogs.append({'tag': tag, 'blogs': blogs})

    return render(request, 'categories.html', {'categories_with_blogs': categories_with_blogs})

