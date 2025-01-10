from django.urls import path

from .views import SignUpView, UserDetailView, UserUpdate, UserDelete, UserFollowingsView, UserInterestedView

app_name = "accounts"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('<str:slug>', UserDetailView.as_view(), name='details'),
    path('<str:slug>/edit', UserUpdate.as_view(), name='edit'),
    path('<str:slug>/delete', UserDelete.as_view(), name='delete'),
    path('<str:slug>/followings', UserFollowingsView.as_view(), name='followings'),
    path('<str:slug>/interested', UserInterestedView.as_view(), name='interested'),
]