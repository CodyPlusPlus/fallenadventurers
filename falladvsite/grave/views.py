from django.shortcuts import render
from .models import Gravemarker
#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'grave/home.html')

def explore(request):
    context = {
        'gravestones': Gravemarker.objects.all()
    }
    return render(request, 'grave/explore.html', context)

def newgrave(request):
    return render(request, 'grave/newgrave.html')


def about(request):
    return render(request, 'grave/about.html', {'title': 'About'})
