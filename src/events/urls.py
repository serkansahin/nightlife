from django.urls import path
from events.views import EventsList, EventCreate, EventUpdate, EventDetail, EventDelete

app_name = "events"

urlpatterns = [
    path('', EventsList.as_view(), name='list'),
    path('create/', EventCreate.as_view(), name='create'),
    path('<str:slug>', EventDetail.as_view(), name='event'),
    path('edit/<str:slug>', EventUpdate.as_view(), name='edit'),
    path('delete/<str:slug>', EventDelete.as_view(), name='delete'),
]