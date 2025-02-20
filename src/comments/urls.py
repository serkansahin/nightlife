from django.urls import path

from comments.views import CommentView

app_name = "comments"

urlpatterns = [
    path('<str:type>/<str:slug>/comment', CommentView, name='comment'),
]