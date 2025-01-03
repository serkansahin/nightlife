from django.urls import path

from .views import SignUpView, UserDetailView, UserUpdate, UserDelete

app_name = "accounts"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('users/<str:slug>', UserDetailView.as_view(), name='userdetails'),
    path('edit/<str:slug>', UserUpdate.as_view(), name='useredit'),
    path('delete/<str:slug>', UserDelete.as_view(), name='userdelete'),
]