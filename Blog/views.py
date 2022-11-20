

from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, ListView

from Blog.forms import PostForm
from Blog.models import Post


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
    template_name = 'cuprins_blog.html'
    success_url = reverse_lazy("home")

