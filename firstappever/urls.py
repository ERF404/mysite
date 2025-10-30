
from django.urls import path
from firstappever.views import homepage, nigga, about, contact

app_name = 'firstappever'

urlpatterns = [
    path('', homepage, name='index'),
    path('nigga/', nigga, name='nigga'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about')
]