from django.db import models
from tinymce import models as tinymce_models




# Create your models here.

class BlogPost(models.Model):
    title=models.CharField(max_length=120)
    subTitle=models.CharField(max_length=120)
    blog_image=models.ImageField(upload_to='post_image')
    content=tinymce_models.HTMLField()
    created_date=models.DateField(auto_now=True)
    

    def __str__(self):
        return self.title

class PostComment(models.Model):
    post=  models.ForeignKey(BlogPost, on_delete=models.CASCADE)     
    comment_body=models.TextField()
    comment_author=models.CharField(max_length=120)

    def __str__(self):
        return self.comment_body

    
