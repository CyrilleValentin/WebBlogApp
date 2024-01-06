from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from blog_app.models import Blog
# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')
@login_required
def post_detail(request):
    return render(request, 'post_detail.html')
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
       ## return redirect('list_blogs')  

    return render(request, 'new_post.html')