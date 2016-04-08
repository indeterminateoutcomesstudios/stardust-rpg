from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .character import Character


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the views index.")


def stats(request: HttpRequest) -> HttpResponse:
    character = Character(hd_rolls=(2, 4))
    return render(request, 'stats.html', context={'character': character})


def level_up(request: HttpRequest) -> HttpResponse:
    return render(request, 'level_up.html')