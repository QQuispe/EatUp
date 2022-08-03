from django.shortcuts import render
# from map.backend import *
from .backend import *


# Create your views here.


def home(request):
    return render(request, 'map/home.html')

def results(request):
    dic = get_address(request)
    return render(request, 'map/results.html', dic)