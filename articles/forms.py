# articles/forms.py

from django import forms
from .models import Comment, Article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "body", "image")  # include the new image field
