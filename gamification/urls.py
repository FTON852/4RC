from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import tasks

app_name = 'main'

urlpatterns = [
    path('', tasks, name='tasks'),
]
