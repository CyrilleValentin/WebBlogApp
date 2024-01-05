
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth_app/', include('auth_app.urls')),
    path('blog_app/', include('blog_app.urls')),
]
