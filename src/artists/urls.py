from django.urls import path
from artists.views import ArtistsList, ArtistCreate, ArtistCreateSpotifyFollowings, ArtistFollowSpotifyFollowings, ArtistDelete, ArtistDetail, ArtistUpdate, ArtistFollowingView

app_name = "artists"

urlpatterns = [
    path('', ArtistsList.as_view(), name='list'),
    path('create/', ArtistCreate, name='create'),
    path('create/spotify_followings/', ArtistCreateSpotifyFollowings, name='create_spotify_followings'),
    path('follow/spotify_followings/', ArtistFollowSpotifyFollowings, name='follow_spotify_followings'),
    path('<str:slug>', ArtistDetail.as_view(), name='artist'),
    path('<str:slug>/edit', ArtistUpdate.as_view(), name='edit'),
    path('<str:slug>/delete', ArtistDelete.as_view(), name='delete'),
    path('<str:slug>/follow', ArtistFollowingView, name='follow'),
]