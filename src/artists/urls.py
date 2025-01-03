from django.urls import path
from artists.views import ArtistsList, ArtistCreate, ArtistDelete, ArtistDetail, ArtistUpdate

app_name = "artists"

urlpatterns = [
    path('', ArtistsList.as_view(), name='list'),
    path('create/', ArtistCreate.as_view(), name='create'),
    path('<str:slug>', ArtistDetail.as_view(), name='artist'),
    path('edit/<str:slug>', ArtistUpdate.as_view(), name='edit'),
    path('delete/<str:slug>', ArtistDelete.as_view(), name='delete'),
]