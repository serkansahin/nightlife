import datetime
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template.defaultfilters import slugify

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from artists.models import Artist
from events.models import Event

class ArtistsList(ListView):
    model = Artist
    context_object_name = "artists"
    template_name = "artists/artists_list.html"

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')

        return queryset
    
@method_decorator(login_required, name="dispatch")
class ArtistCreate(CreateView):
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