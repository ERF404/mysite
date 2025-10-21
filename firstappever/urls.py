
from django.urls import path
from firstappever.views import homepage, nigga

urlpatterns = [
    path('',homepage),
    path('nigga', nigga)
]