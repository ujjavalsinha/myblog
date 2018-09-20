from django.conf.urls import url
from blog import views

app_name = 'blog'

urlpatterns = [
    url('about/', views.about,name='about'),
    url('', views.PostListView.as_view(), name= 'post_list'),
    url(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(),
    name='post_detail'),
    url('post/new/',views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name = 'post_remove'),
    url('drafts/', views.DraftListView.as_view(), name = 'post_draft_list'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name = 'comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name= 'comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name = 'post_publish'),


]
