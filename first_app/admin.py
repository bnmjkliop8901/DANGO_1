from django.contrib import admin

# Register your models here.

from first_app.models import BlogPost , PostAuthor , Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass

@admin.register(PostAuthor)
class PostAuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass