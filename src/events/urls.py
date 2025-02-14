from django.urls import path
from events.views import EventInterestedView, EventCommentView, EventsList, EventCreate, EventUpdate, EventDetail, EventDelete

app_name = "events"

urlpatterns = [
    path('', EventsList.as_view(), name='list'),
    path('create/', EventCreate.as_view(), name='create'),
    path('<str:slug>', EventDetail.as_view(), name='event'),
    path('<str:slug>/comment', EventCommentView, name='comment'),
    path('<str:slug>/edit', EventUpdate.as_view(), name='edit'),
    path('<str:slug>/delete', EventDelete.as_view(), name='delete'),
    path('<str:slug>/interested', EventInterestedView, name='interested'),
]