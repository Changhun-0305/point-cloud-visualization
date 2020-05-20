from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import numpy as np
import json
import array

# Create your views here.
def index(request):
    frames = []
    for i in range(3):
        if i < 10:
            path = "data/lidar/000{}.bin".format(i)
        else:
            path = "data/lidar/00{}.bin".format(i)
        frames.append(np.fromfile(path, dtype=np.float32).reshape(-1, 4).tolist())

        
    template = loader.get_template('points/index.html')
    context = {
        'frames': frames
    }
    return HttpResponse(template.render(context, request))