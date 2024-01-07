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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Like, self).save(*args, **kwargs)
        self.blog.likes = Like.objects.filter(blog=self.blog).count()
        self.blog.save()

    def delete(self, *args, **kwargs):
        super(Like, self).delete(*args, **kwargs)
        self.blog.likes = Like.objects.filter(blog=self.blog).count()
        self.blog.save()

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
