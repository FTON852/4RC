from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import EventView, EventDetailView

app_name = 'event_feed'

urlpatterns = [
    path('events/', EventView.as_view(), name='event_list'),
    path('event/<str:slug>', EventDetailView.as_view(), name='event'),

]
