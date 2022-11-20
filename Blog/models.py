from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField, CKEditorWidget
from tinymce.models import HTMLField
from django.utils.html import strip_tags
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True, config_name='awesome_ckeditor')

    category = models.CharField(max_length=200, default='calatorii')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.CharField(max_length=200, null=True, default="")


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
