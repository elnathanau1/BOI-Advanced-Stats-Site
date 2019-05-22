from django.shortcuts import render
from django.http import HttpResponse, Http404

from boi_stats.models import *

import webbrowser

import json

def add_run_req(request):
    if request.POST:
        new_user = request.POST.get('new_user')
        new_seed = request.POST.get('new_seed')

        new_run = Run()
        new_run.user = new_user
        new_run.seed = new_seed
        new_run.save()

        data = {'message': "user: {0}, seed: {1} added".format(new_user, new_seed)}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404
