from django.db import models

# Create your models here.

class PostAuthor(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)

class BlogPost(models.Model):
    title = models.CharField(max_length=55 , unique=True )
    content = models.TextField(null = True , blank=True)
    is_shown = models.BooleanField(default = True)
    created_at = models.DateTimeField()
    authors = models.ManyToManyField(PostAuthor)

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost , on_delete = models.CASCADE)
    author = models.CharField(max_length=55)
    text = models.TextField()