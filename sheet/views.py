from django.forms import ValidationError
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import CharacterEquipForm, LevelUpForm, SkillPointsForm
from .models.character import Character


def index(request: HttpRequest, character_id: int) -> HttpResponse:
    return HttpResponse('Welcome {}\n'.format(get_object_or_404(Character, pk=character_id)))


def stats(request: HttpRequest, character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'stats.html', context={'character': character})


def cls(request: HttpRequest, character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'class.html', context={'character': character})


def abilities(request: HttpRequest, character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'abilities.html', context={'character': character})


def equip(request: HttpRequest, character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST':
        equip_form = CharacterEquipForm(request.POST)
        if equip_form.is_valid():
            # TODO: Validate character meets requirements for equipment.
            character.utility_enum = equip_form.cleaned_data['utility_enum']
            character.head_enum = equip_form.cleaned_data['head_enum']
            character.neck_enum = equip_form.cleaned_data['neck_enum']
            character.chest_enum = equip_form.cleaned_data['chest_enum']
            character.shield_enum = equip_form.cleaned_data['shield_enum']
            character.hand_enum = equip_form.cleaned_data['hand_enum']
            character.feet_enum = equip_form.cleaned_data['feet_enum']
            character.weapon_enum = equip_form.cleaned_data['weapon_enum']
            character.save()

            return HttpResponseRedirect('/sheet/{}/stats/'.format(character_id))
    else:
        equip_form = CharacterEquipForm(
            initial={
                'utility_enum': character.utility_enum,
                'head_enum': character.head_enum,
                'neck_enum': character.neck_enum,
                'chest_enum': character.chest_enum,
                'shield_enum': character.shield_enum,
                'hand_enum': character.hand_enum,
                'feet_enum': character.feet_enum,
                'weapon_enum': character.weapon_enum
            })

    return render(request, 'equip.html',
                  context={'equip_form': equip_form,
                           'character': character})


def level_up(request: HttpRequest, character_id: int) -> HttpResponse:
    # TODO: Display previous levels.
    # TODO: Allow removal/modification of previous levels.
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST':
        level_up_form = LevelUpForm(request.POST)
        if level_up_form.is_valid():

            hd_roll = level_up_form.cleaned_data['hd_roll']
            if hd_roll > character.cls.hd:
                raise ValidationError('HD roll higher than HD: {}>{}'.format(
                    hd_roll, character.cls.hd))

            md_roll = level_up_form.cleaned_data['md_roll']
            if md_roll > character.cls.md:
                raise ValidationError('MD roll higher than MD: {}>{}'.format(
                    md_roll, character.cls.md))

            sd_roll = level_up_form.cleaned_data['sd_roll']
            if sd_roll > character.cls.sd:
                raise ValidationError('SD roll higher than SD: {}>{}'.format(
                    sd_roll, character.cls.sd))

            new_level_up = level_up_form.save(commit=False)
            new_level_up.character = character
            new_level_up.save()

            return HttpResponseRedirect('/sheet/{}/stats/'.format(character_id))
    else:
        level_up_form = LevelUpForm()

    return render(request, 'level_up.html',
                  context={'level_up_form': level_up_form,
                           'character': character})


def skill_points(request: HttpRequest, character_id: int) -> HttpResponse:
    # TODO: Display previous levels.
    # TODO: Allow removal/modification of previous levels.
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST':
        skill_points_form = SkillPointsForm(request.POST)
        if skill_points_form.is_valid():
            assigned_ath = skill_points_form.cleaned_data['assigned_ath']
            assigned_ste = skill_points_form.cleaned_data['assigned_ste']
            assigned_for = skill_points_form.cleaned_data['assigned_for']
            assigned_apt = skill_points_form.cleaned_data['assigned_apt']
            assigned_per = skill_points_form.cleaned_data['assigned_per']
            assigned_spe = skill_points_form.cleaned_data['assigned_spe']
            if (assigned_ath + assigned_ste + assigned_for + assigned_apt + assigned_per +
               assigned_spe > character.sp):
                raise ValidationError('Too many SP assigned. Max: {}'.format(character.sp))
            else:
                character.assigned_ath = assigned_ath
                character.assigned_ste = assigned_ste
                character.assigned_for = assigned_for
                character.assigned_apt = assigned_apt
                character.assigned_per = assigned_per
                character.assigned_spe = assigned_spe
                character.save()

            return HttpResponseRedirect('/sheet/{}/stats/'.format(character_id))
    else:
        skill_points_form = SkillPointsForm(
            initial={'assigned_ath': character.assigned_ath,
                     'assigned_ste': character.assigned_ste,
                     'assigned_for': character.assigned_for,
                     'assigned_apt': character.assigned_apt,
                     'assigned_per': character.assigned_per,
                     'assigned_spe': character.assigned_spe}
        )

    return render(request, 'skill_points.html',
                  context={'skill_points_form': skill_points_form,
                           'character': character})
