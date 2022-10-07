from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index, profile, people_list

urlpatterns = [
    path('', index, name='main-page'),
    path('profile/', profile, name='profile'),
    path('people_list/', people_list, name='people_list'),
]
