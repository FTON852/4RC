from django.shortcuts import render
from django.views.generic import ListView

from .models import Achievements


# Create your views here.
class ShowTasks(ListView):
    model = Achievements
    paginate_by = 9
    template_name = "task_list.html"
    context_object_name = 'items'
