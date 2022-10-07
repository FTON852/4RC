from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')


def people_list(request):
    return render(request, 'people_list.html')