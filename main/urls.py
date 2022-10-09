from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index, profile, people_list, pay, all_pay, AccountCreateView

app_name = 'main'

urlpatterns = [
    path('', index, name='main-page'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('people_list/', people_list, name='people_list'),
    path('pay/', pay),
    path('all_pay', all_pay),
    path('add_user', AccountCreateView.as_view()),
]
