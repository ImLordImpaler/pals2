from django.shortcuts import render
from .models import *



# Create your views here.
def index(request):
    return render(request, 'rachit/index.html')


def reasons(request):
    return render(request, 'rachit/second.html')



