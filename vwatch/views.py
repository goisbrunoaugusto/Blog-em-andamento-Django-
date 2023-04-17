from django.shortcuts import render


def home(request):
    return render(request, 'vwatch/pages/home.html')
