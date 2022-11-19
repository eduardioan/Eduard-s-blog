from django.urls import path

from Blog import views
from Blog.views import CreatePostView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/post/', CreatePostView.as_view(), name='post')
]
