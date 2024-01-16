from django.utils import timezone
from winreg import HKEY_CURRENT_USER
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    def image_url(self):
        if self.image:
            return self.image.url
        return ''
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    tags = models.ForeignKey(Tag,default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, default=None,blank=True,related_name='liked_blogs')
    comments = models.ManyToManyField(User, default=None, blank=True, related_name='commented_blogs')
    def __str__(self):
        return self.title
    @property
    def number_of_likes(self):
        return self.likes.all().count()
    @property
    def number_of_comments(self):
        return self.comments.all().count() 
    def total_comments(self):
        return self.comments.count()
      
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.blog)
   
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user.username} - {self.blog.title} - {self.created_at}'
    def time_elapsed(self):
        now = timezone.now()
        elapsed_time = now - self.created_at

        if elapsed_time.days > 0:
            return f"{elapsed_time.days} jours"
        elif elapsed_time.seconds // 3600 > 0:
            return f"{elapsed_time.seconds // 3600} heures"
        elif elapsed_time.seconds // 60 > 0:
            return f"{elapsed_time.seconds // 60} minutes"
        else:
            return f"{elapsed_time.seconds} secondes"
   