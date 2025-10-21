from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render (request, 'firstappever/first_template.html')

def nigga(request):
    return render (request, 'firstappever/nigga.html')