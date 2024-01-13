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
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, default=None,blank=True,related_name='liked_blogs')
    def __str__(self):
        return self.title
    @property
    def number_of_likes(self):
        return self.likes.all().count() 

# Like_CHOICES=(
#     ('Like','Like'),
#     ('Unlike','Unlike')
# ) 
      
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
   # value=models.CharField(choices='Like' or 'Unlike',defaut='Like')
    def __str__(self):
        return str(self.blog)
   
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
        self.blog.comments = Comment.objects.filter(blog=self.blog).count()
        self.blog.save()

    def delete(self, *args, **kwargs):
        super(Comment, self).delete(*args, **kwargs)
        self.blog.comments = Comment.objects.filter(blog=self.blog).count()
        self.blog.save()
