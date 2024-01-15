from django.urls import path
from blog_app import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('post_detail/<int:blog_id>/', views.post_detail, name='post_detail'),
    path('new_post/', views.new_post, name='new_post'),
    path('create/', views.create_blog, name='create_blog'),
    path('like/', views.like_post, name='like_blog'),
]