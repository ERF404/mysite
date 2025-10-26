from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render (request, 'firstappever/index.html')

def about(request):
    return render (request, 'firstappever/about.html')

def contact(request):
    return render (request, 'firstappever/contact.html')

def nigga(request):
    return render (request, 'firstappever/nigga.html')