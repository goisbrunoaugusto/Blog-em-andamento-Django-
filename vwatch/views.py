from django.shortcuts import render
from utils.vwatch.factory import make_vwatch


def home(request):
    return render(request, 'vwatch/pages/home.html', context={
        'vwatch': [make_vwatch() for _ in range(10)],
    })


def evento(request, id):
    return render(request, 'vwatch/pages/evento.html', context={
        'vwatch': [make_vwatch()],
    })
