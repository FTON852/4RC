from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Event


class EventView(LoginRequiredMixin, ListView):
    model = Event
    paginate_by = 9
    template_name = "event_list.html"
    context_object_name = 'events'


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "event.html"
    context_object_name = 'event'
