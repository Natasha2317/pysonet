from django.contrib import admin

# Register your models here.

from mptt.admin import MPTTModelAdmin

from src.wall.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Посты
    """
    list_display = ("id", "user", "title", "published", "create_date", "moderation", "view_count")
    list_display_links = ["title"]
    list_filter = ["user"]


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """ Коментарии к постам
    """
    list_display = ("user", "post", "text", "created_date", "update_date", "published", "id")
    list_display_links = ("text", "post")
    list_filter = ("user", "post")
    mptt_level_indent = 15