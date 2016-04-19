from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models.character import Attribute, Character, LevelUp


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the views index.")


def stats(request: HttpRequest) -> HttpResponse:
    character = Character.objects.get(pk=1)
    return render(request, 'stats.html', context={'character': character})


def level_up(request: HttpRequest) -> HttpResponse:
    lvl_up = LevelUp()
    return render(request, 'level_up.html',
                  context={'level_up': lvl_up,
                           'attributes': [attribute.name for attribute in Attribute]})
