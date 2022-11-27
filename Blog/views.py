from django.contrib import messages
from django.db.models import Q
from django.db.models.sql import query
from django.http import HttpResponse, request
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, ListView, TemplateView
from requests import post
from django.http import HttpResponseRedirect
from Blog.filters import PostFilter
from Blog.forms import PostForm
from Blog.models import Post
from django import template

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'




class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy("home")
class FullPostList(ListView):
    model = Post
    form_class = PostForm
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'cuprins_blog.html'
    success_url = reverse_lazy("home")


class PostListCalatorii(generic.ListView):
    queryset = Post.objects.filter(status=1,category='calatorii').order_by('-created_on')
    template_name = 'lista_calatorii.html'
class PostListCarti(generic.ListView):
    queryset = Post.objects.filter(status=1,category='carti').order_by('-created_on')
    template_name = 'lista_carti.html'


class SearchResultView(ListView):
    model = Post
    template_name = 'search_blog.html'
    def get_queryset(self):  # new
        query = self.request.GET.get("query")
        object_list = Post.objects.filter(content__icontains=query)
        return object_list

# class TagsList(generic.ListView):
#     queryset = Post.objects.filter(status=1, tags='').order_by('-created_on')
#     template_name = 'tag_search.html'

def show_despre_mine_page(request):
    return render(request, 'despre_mine.html')
def show_contact_page(request):
    return render(request, 'contact.html')
def share_on_media(request, social, id):
    format_title = str(id).replace(" ", "-").lower()
    base_url = ""
    if str(social) == "1":
        base_url = rf'https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2F127.0.0.1%3A8000%2F{format_title}%2F'
    if str(social) == "2":
        base_url = rf'https://api.whatsapp.com/send?text=http%3A//127.0.0.1%3A8000/{format_title}/'
    return HttpResponseRedirect(base_url)

class PostListTag(generic.ListView):
    model = Post
    template_name = 'tag_select_list.html'

    def get_queryset(self):  # new

        tag = str(self.request.path).strip().split("/")
        tag = tag[len(tag)-1]

        items = Post.objects.all()
        buffer = []
        for item in items:
            if tag in item.tags:
                buffer.append(item.title)
        return Post.objects.filter(title__in=buffer)


