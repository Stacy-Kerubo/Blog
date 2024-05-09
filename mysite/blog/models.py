from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES=(
        ('draft','Draft'),
        ('published','Published'),
    )
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    content=models.TextField()
    #author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_post')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    publish=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='Draft')
 
    
    
    class Meta:
        ordering=('-publish')
    def __str__(self):
        return self.title
       
    