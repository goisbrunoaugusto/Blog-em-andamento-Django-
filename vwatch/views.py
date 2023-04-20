from django.shortcuts import render


def home(request):
    return render(request, 'vwatch/pages/home.html')


def evento(request, id):
    return render(request, 'vwatch/pages/evento.html')
