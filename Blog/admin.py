from django.contrib import admin

from newsletter.models import NewsUsers
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    list_display =('name','email','date_added',)
admin.site.register(NewsUsers, NewsletterAdmin)
