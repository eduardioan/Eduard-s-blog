from django.urls import path

from Blog import views
from Blog.views import *

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/post/', CreatePostView.as_view(), name='post'),
    path('blog/cuprins/',FullPostList.as_view(), name='cuprins_blog'),
    path('blog/lista-calatorii/',PostListCalatorii.as_view(), name='lista_calatorii'),
    path('blog/lista-carti/',PostListCarti.as_view(), name='lista_carti'),
    path('blog/search/',SearchResultView.as_view(), name='search_blog'),
    path('blog/despre/', show_despre_mine_page, name='despre_mine'),
    path('blog/contact/', show_contact_page, name='contact'),
    path('blog/tag-select/<str:tag>',PostListTag.as_view(), name='tag_select_list'),
    path('blog/tag-select-check/',PostListTag.as_view(), name='tag_select_list_check'),
    path('blog/share/<str:social>/<str:id>', share_on_media, name="share_on_media"),
    # path('blog/share-whatsapp/<str:id>', share_on_whatsapp_func, name="share_on_whatsapp"),
    # path('blog/despre/', DespreMine.as_view(), name='despre_mine'),
    # path('<slug:slug>/', views.post_details, name='post_detail'),
    path('blog/comment/<slug:slug>', views.AddCommentView.as_view(), name='add_comment'),
    path('blog/send-newsletter/<slug:slug>', new_post_newsletter, name='send_newsletter')
]
