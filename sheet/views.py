from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render

from .forms import LevelUpForm
from .models.character import Character


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the views index.")


def stats(request: HttpRequest) -> HttpResponse:
    character = Character.objects.get(pk=1)
    return render(request, 'stats.html', context={'character': character})


def level_up(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = LevelUpForm(request.POST)
        if form.is_valid():
            print('VALID!', form.cleaned_data['hd_roll'], form.cleaned_data['md_roll'],
                  form.cleaned_data['sd_roll'], form.cleaned_data['ad_roll'],
                  form.cleaned_data['selected_attribute'])
            return HttpResponseRedirect('/sheet/stats/')
    else:
        form = LevelUpForm()

    return render(request, 'level_up.html',
                  context={'form': form})
