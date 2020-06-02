from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, \
    likes, ProfilePostListView, comment, comment_likes

urlpatterns = [
    path('', PostListView.as_view(), name='myApp-home'),
    path('likes/<int:pk>/', likes, name='like'),
    path('comment/<int:pk>/', comment_likes, name='comment_likes'),
    path('post/<int:pk>/comment', comment, name='comment'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user_post'),
    path('post/<str:username>/profile', ProfilePostListView.as_view(), name='user_post_profile'),
]
