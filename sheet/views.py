from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import LevelUpForm
from .models.character import Character


def index(request: HttpRequest, character_id: int) -> HttpResponse:
    return HttpResponse('Welcome {}\n'.format(get_object_or_404(Character, pk=character_id)))


def stats(request: HttpRequest, character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'stats.html', context={'character': character})


def level_up(request: HttpRequest, character_id: int) -> HttpResponse:
    # TODO: Display previous levels.
    # TODO: Allow removal/modification of previous levels.

    if request.method == 'POST':
        level_up_form = LevelUpForm(request.POST)
        if level_up_form.is_valid():
            # TODO: Validate rolls are under maximum value.
            print('VALID!', level_up_form.cleaned_data['hd_roll'],
                  level_up_form.cleaned_data['md_roll'],
                  level_up_form.cleaned_data['sd_roll'], level_up_form.cleaned_data['ad_roll'],
                  level_up_form.cleaned_data['selected_attribute'])

            new_level_up = level_up_form.save(commit=False)
            new_level_up.character = get_object_or_404(Character, pk=character_id)
            new_level_up.save()

            return HttpResponseRedirect('/sheet/{}/stats/'.format(character_id))
    else:
        level_up_form = LevelUpForm()

    return render(request, 'level_up.html',
                  context={'level_up_form': level_up_form,
                           'character_id': character_id})
