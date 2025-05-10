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

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost , on_delete = models.CASCADE)
    author = models.CharField(max_length=55)
    text = models.TextField()

    def __str__(self):
        return f"{self.blog_post} , {self.id}"
        




class ContactUs(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    message = models.TextField()
    additional_data = models.CharField(max_length=55 , null=True , blank=True)