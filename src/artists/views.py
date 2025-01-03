import datetime
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.template.defaultfilters import slugify

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from artists.models import Artist

class ArtistsList(ListView):
    model = Artist
    context_object_name = "artists"
    template_name = "artists/artists_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()

        #Si user connecté, on retourne l'ensemble du queryset, sinon on n'affiche que les events publiés
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)
    
@method_decorator(login_required, name="dispatch")
class ArtistCreate(CreateView):
    model = Artist
    template_name = "artists/artist_create.html"
    fields = ['name', 'biography','thumbnail','spotify','soundcloud','instagram','facebook']

    def form_valid(self, form):      
        form.instance.created_on = datetime.datetime.now()
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")
class ArtistUpdate(UpdateView):
    model = Artist
    template_name = "artists/artist_update.html"
    fields = ['name', 'biography','thumbnail','spotify','soundcloud','instagram','facebook']

class ArtistDetail(DetailView):
    model = Artist
    template_name = "artists/artist_detail.html"
    context_object_name = "artist"


@method_decorator(login_required, name="dispatch")
class ArtistDelete(DeleteView):
    model = Artist
    context_object_name = "artist"
    success_url = reverse_lazy("artists:list")