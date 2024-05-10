from django.shortcuts import render,get_object_or_404
from . models import  Post



# Create your views here.

'''creating a view to display list of posts'''

def post_list(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
    return render(request,
                  'blog/post/list.html',
                 {'posts': posts} )
    
'''creating a view to display a single post'''    
def post_detail(request,id):
    post=get_object_or_404(Post,
                           id=id,
                           status=Post.Status. PUBLISHED)
    
    return render(request,
                   'blog/post/detail.html',
                    {'post': post})
    