from django.shortcuts import render
from django.http import HttpResponse, Http404

from boi_stats.models import *

import webbrowser

import json


# Create your views here.
def home(request):
    context = {

    }

    return render(request, 'home.html', context)
