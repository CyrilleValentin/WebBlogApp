from django.urls import path
from blog_app import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('post_detail/', views.post_detail, name='post_detail'),
]