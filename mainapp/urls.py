
from django.urls import path
from mainapp.views import homepage, about, contact

app_name = 'mainapp'

urlpatterns = [
    path('', homepage, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about')
]