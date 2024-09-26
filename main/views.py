import re
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False,
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    return HttpResponse('About us')