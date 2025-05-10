from django.contrib import admin

# Register your models here.

from first_app.models import BlogPost , PostAuthor , Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title" , "is_shown" , "created_at")
    list_filter = ("is_shown",)

@admin.register(PostAuthor)
class PostAuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id" , "blog_post" , "author")
    search_fields = ("blog_post__title" ,)
    raw_id_fields = ("blog_post",)