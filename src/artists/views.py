import datetime
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests

from artists.forms import ArtistCreateForm
from artists.models import Artist
from events.models import Event
from nightlife.methods import spotify_search

class ArtistsList(ListView):
    model = Artist
    context_object_name = "artists"
    template_name = "artists/artists_list.html"

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')

        return queryset
    
@login_required
def ArtistCreate(request):

    if request.method == "POST":
        form = ArtistCreateForm(request.POST)
        if form.is_valid():
            artist = form.cleaned_data.get('name')
            artist_search = spotify_search("artist", artist)
            playlist_search = spotify_search("playlist", artist)

            new_artist = form.save(commit=False)
            image_url = artist_search["images"][0]["url"]
            image_response = requests.get(image_url)

            if image_response.status_code == 200:
                image_content = ContentFile(image_response.content)
                new_artist.name = artist_search["name"]
                new_artist.slug = slugify(new_artist.name)
                new_artist.biography = form.cleaned_data.get('biography')
                new_artist.spotify = artist_search["id"]
                new_artist.created_on = datetime.datetime.now()
                if playlist_search:
                    new_artist.playlist = playlist_search["id"]
                new_artist.thumbnail.save(f"{new_artist.name}.jpg", image_content)
                new_artist.save()
                return redirect('artists:artist', new_artist.slug)

    else:
        form = ArtistCreateForm()

    return render(request, "artists/artist_create.html", {"form": form})

    
@method_decorator(login_required, name="dispatch")
class ArtistCreateManual(CreateView):
    model = Artist
    template_name = "artists/artist_create.html"
    fields = ['name', 'biography','thumbnail','spotify','soundcloud','instagram','facebook', 'playlist']

    def form_valid(self, form):      
        form.instance.created_on = datetime.datetime.now()
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")
class ArtistUpdate(UpdateView):
    model = Artist
    template_name = "artists/artist_update.html"
    fields = ['name', 'biography','thumbnail','spotify','soundcloud','instagram','facebook', 'playlist']

class ArtistDetail(DetailView):
    model = Artist
    template_name = "artists/artist_detail.html"
    context_object_name = "artist"


@method_decorator(login_required, name="dispatch")
class ArtistDelete(DeleteView):
    model = Artist
    context_object_name = "artist"
    success_url = reverse_lazy("artists:list")


@login_required
def ArtistFollowingView(request, slug):
    context = {}
    artist = get_object_or_404(Artist, slug=slug)
    if artist.followers.filter(id=request.user.id).exists():
        artist.followers.remove(request.user)
    else:
        artist.followers.add(request.user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))