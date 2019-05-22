from django.shortcuts import render
from django.http import HttpResponse, Http404

from boi_stats.models import *

import webbrowser

import json


# Create your views here.
def home(request):

    new_run = Run()
    new_run.user = "test_user"
    new_run.seed = "test_seed"
    new_run.save()

    context = {

    }

    return render(request, 'home.html', context)
