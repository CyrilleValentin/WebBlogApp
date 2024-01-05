from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')
@login_required
def post_detail(request):
    return render(request, 'post_detail.html')