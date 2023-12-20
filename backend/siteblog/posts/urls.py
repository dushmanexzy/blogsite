from django.urls import path
from .views import PostList, PostDetail, CommentCreate

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('comments/', CommentCreate.as_view(), name='comment-create'),
]