from django import forms
from Blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tags', 'author', 'content', 'tags', 'category','slug']


