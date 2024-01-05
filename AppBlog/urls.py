
from django.contrib import admin
from django.urls import path

from auth_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name='register'),
    path('login/', views.login1, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout1, name='logout'),
]
