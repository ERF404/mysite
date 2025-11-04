from django.shortcuts import render

def homepage(request):
    return render (request, 'website/index.html')

def about(request):
    return render (request, 'website/about.html')

def contact(request):
    return render (request, 'website/contact.html')

def nigga(request):
    return render (request, 'website/nigga.html')