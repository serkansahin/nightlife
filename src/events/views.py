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

from events.models import Event

class Home(ListView):
    model = Event
    context_object_name = "events"
    template_name = "events/home.html"

    def get_queryset(self):
        queryset = super().get_queryset()

        #Si user connecté, on retourne l'ensemble du queryset, sinon on n'affiche que les events publiés
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)

class EventsList(ListView):
    model = Event
    context_object_name = "events"
    template_name = "events/event_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()

        #Si user connecté, on retourne l'ensemble du queryset, sinon on n'affiche que les events publiés
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)
    
@method_decorator(login_required, name="dispatch")
class EventCreate(CreateView):
    model = Event
    template_name = "events/event_create.html"
    fields = ['title', 'location', 'content','thumbnail',]

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        
        form.instance.created_on = datetime.datetime.now()
        
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")
class EventUpdate(UpdateView):
    model = Event
    template_name = "events/event_update.html"
    fields = ['title', 'content', 'thumbnail', 'published',]

class EventDetail(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"


@method_decorator(login_required, name="dispatch")
class EventDelete(DeleteView):
    model = Event
    context_object_name = "event"
    success_url = reverse_lazy("events:list")