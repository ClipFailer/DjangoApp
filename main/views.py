import re
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context = {
        'title': 'О нас',
        'content': 'Наши контакты:',
        'text_on_page': 'Текст о том, какой этот магазин крутой!'
    }

    return render(request, 'main/about.html', context)