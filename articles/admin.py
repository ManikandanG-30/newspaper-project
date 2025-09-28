# articles/admin.py
from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.StackedInline):  # new
    model = Comment
    extra = 1  # optional: show 1 empty comment form by default
    fields = ("comment", "author")

class ArticleAdmin(admin.ModelAdmin):  # new
    inlines = [CommentInline]
    list_display = ("title", "body", "author")


admin.site.register(Article, ArticleAdmin)  # new
admin.site.register(Comment)
