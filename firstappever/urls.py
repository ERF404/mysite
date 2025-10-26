
from django.urls import path
from firstappever.views import homepage, nigga, about, contact

urlpatterns = [
    path('', homepage),
    path('nigga/', nigga),
    path('contact/', contact),
    path('about/', about)
]