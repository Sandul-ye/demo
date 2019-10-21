from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {"name":"叶之魂"}
    return HttpResponse(template.render(context))