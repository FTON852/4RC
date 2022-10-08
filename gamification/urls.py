from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import ShowTasks

app_name = 'main'

urlpatterns = [
    path('', ShowTasks.as_view(), name='tasks'),
]
