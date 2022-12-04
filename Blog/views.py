from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.db.models.sql import query
from django.http import HttpResponse, request, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, ListView, TemplateView
from requests import post
from django.http import HttpResponseRedirect
from Blog.filters import PostFilter
from Blog.forms import PostForm, CommentForm
from Blog.models import Post, Comment
from django import template
from django.shortcuts import redirect

from newsletter.models import NewsUsers


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'



class CreatePostView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy("home")
    permission_required = 'blog.view_post'

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
    allow_empty = True
    model = Post
    template_name = 'tag_select_list.html'
    def get_queryset(self):  # new
        req = self.request
        tags = None
        if "tag-select-check" in req.path:
            tags = self.__extract_tag_from_checkbox(req.GET)
            if tags is None:
                return
        else:
            tags = self.__extract_tag_from_ahref(self.request.path)
        items = Post.objects.all()
        buffer = set()
        for item in items:
            for tag in tags:
                if tag in item.tags:
                    buffer.add(item.title)
        return Post.objects.filter(title__in=buffer)

    def __extract_tag_from_ahref(self, request):
        tag = str(request).strip().split("/")
        return tag[len(tag) - 1]

    def __extract_tag_from_checkbox(self, request):
        if len(request) == 0:
            return None
        return dict(request)['tag']


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    def post(self, request, *args, **kwargs):
        post_name_bucati = str(request.path).split('/')
        post_name = post_name_bucati[len(post_name_bucati)-1]
        post = get_object_or_404(Post, slug=post_name)
        comments = post.comments.filter(active=True)
        new_comment = None
        # Comment posted
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                # cOMMENT NESALVAT
                new_comment = comment_form.save(commit=True)

                new_comment.post = post
                # sALVEZ IN BAZA
                new_comment.save()
                print(new_comment)
        else:
            comment_form = CommentForm()
        return HttpResponseRedirect(self.request.path_info)
def new_post_newsletter(request,slug):
    if request.method == 'POST':
        link_server = request.build_absolute_uri('/')
        link_server = link_server[:len(link_server)-1]
        link_nou = link_server + str(request.path).replace("/blog/send-newsletter", "")
        users = NewsUsers.objects.all()
        for user in users:
            email = user.email
            send_mail(
              subject="O noua postare!",
              message=f"Hey, {user.name} o noua postare a aparut. Mergi pe: {link_nou}",
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[email]
            )

    return redirect("home")
