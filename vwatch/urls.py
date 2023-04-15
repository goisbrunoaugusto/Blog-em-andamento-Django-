from django.urls import path
from vwatch.views import home

urlpatterns = [
    path('', home),
]
