from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published'),
    )
    title=models.CharField(max_length=250,Unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='Draft')
    content=models.TextField()
    
    
    class Meta:
        ordering=('-created')
    def __str__(self):
        return self.title
       
    