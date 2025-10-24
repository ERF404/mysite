from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render (request, 'firstappever/index.html')

def nigga(request):
    return render (request, 'firstappever/nigga.html')