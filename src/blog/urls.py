from django.urls import path
from blog.views import BlogPostList, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostCommentView, BlogPostDelete

app_name = "blog"

urlpatterns = [
    path('', BlogPostList.as_view(), name='list'),
    path('create/', BlogPostCreate.as_view(), name='create'),
    path('<str:slug>', BlogPostDetail.as_view(), name='post'),
    path('<str:slug>/comment', BlogPostCommentView, name='comment'),
    path('<str:slug>/edit', BlogPostUpdate.as_view(), name='edit'),
    path('<str:slug>/delete', BlogPostDelete.as_view(), name='delete'),
]