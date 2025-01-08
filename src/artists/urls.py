from django.urls import path
from artists.views import ArtistsList, ArtistCreate, ArtistDelete, ArtistDetail, ArtistUpdate, ArtistFollowingView

app_name = "artists"

urlpatterns = [
    path('', ArtistsList.as_view(), name='list'),
    path('create/', ArtistCreate.as_view(), name='create'),
    path('<str:slug>', ArtistDetail.as_view(), name='artist'),
    path('<str:slug>/edit', ArtistUpdate.as_view(), name='edit'),
    path('<str:slug>/delete', ArtistDelete.as_view(), name='delete'),
    path('<str:slug>/follow', ArtistFollowingView, name='follow'),
]