from django.shortcuts import render
from .models import BlogPost, PostComment

# Create your views here.

def homepage(request):
    all_posts=BlogPost.objects.all()
    context={
        "all_posts" : all_posts
    }
    return render(request, 'blog_app/homepage.html', context)


def search(request):
    q=request.GET.get("q","")
    all_posts=BlogPost.objects.filter(title__icontains=q)
    context={
        "all_posts" : all_posts
    }
    return render(request, 'blog_app/homepage.html', context)

def single_post(request, id):
    comment_body=comment_author=None
    if request.method=="POST":
        comment_body= request.POST.get('comment_body')
        comment_author=request.POST.get('comment_author')
    data=BlogPost.objects.get(id=id)
    if comment_body and comment_author:
         comment=PostComment(post=data, comment_body=comment_body, comment_author=comment_author)
         comment.save()

    all_comments=PostComment.objects.filter(post=data)
    context={
        "post": data,
        "all_comments" : all_comments
    }

    return render(request, 'blog_app/single_post.html', context)


    

