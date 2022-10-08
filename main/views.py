from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Account

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def people_list(request):
    user_id = request.user.id
    people = Account.objects.all()
    return render(request, 'people_list.html', context={'people': people})

