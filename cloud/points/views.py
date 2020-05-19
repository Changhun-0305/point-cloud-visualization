from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import numpy as np

# Create your views here.
def index(request):
    points = np.fromfile("data/lidar/0001.bin", dtype=np.float32).reshape(-1, 4)
    print(points)
    template = loader.get_template('points/index.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))