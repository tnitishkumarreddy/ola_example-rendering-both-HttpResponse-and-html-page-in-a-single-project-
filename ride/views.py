from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def auto(request):
    return HttpResponse('<h1>Auto is a 3 wheeler</h1>')