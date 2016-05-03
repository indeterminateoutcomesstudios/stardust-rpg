import enum
import re
from typing import Tuple

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.forms import ValidationError
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CharacterEquipForm, LevelUpForm, SkillPointsForm
from .models.character import Character, UnlockedAbility
from .models.level_up import LevelUp
from .models.abilities import inverse_abilities
from .models import classes, combos, equipment, items

# TODO: Handle exceptions in a user-friendly way.
# TODO: Color equipment based on rarity.


def check_is_admin_or_owns_character(user: User, character: Character) -> None:
    if not (user.username == 'admin' or character.user.username == user.username):
        raise ValidationError('User not authorized to edit this character.')


@login_required
def characters(request: HttpRequest) -> HttpResponse:
    return render(request, 'characters.html', context={'characters': Character.objects.all()})


@login_required
def all_classes(request: HttpRequest) -> HttpResponse:
    return render(request, 'classes.html', context={'classes': classes.classes.values()})


@login_required
def all_combos(request: HttpRequest) -> HttpResponse:
    return render(request, 'browser_combos.html', context={'combos': combos.combos})


@login_required
def all_equipment(request: HttpRequest, wearables: Tuple[equipment.Wearable, ...]) -> HttpResponse:
    return render(request, 'equipment.html',
                  context={'wearables': sorted(wearables, key=lambda wearable: wearable.price)})


@login_required
def all_weapons(request: HttpRequest, weapons: Tuple[equipment.Weapon, ...]) -> HttpResponse:
    return render(request, 'weapons.html',
                  context={'weapons': sorted(weapons, key=lambda weapon: weapon.price)})


@login_required
def pictures(request: HttpRequest, picture_enum: Tuple[enum.Enum, ...]) -> HttpResponse:
    return render(request, 'pictures.html',
                  context={'pictures': sorted([picture for picture in picture_enum],
                                              key=lambda picture: picture.name),
                           'picture_type': list(picture_enum)[0].__class__.__name__})


@login_required
def stats(request: HttpRequest, character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'stats.html', context={'character': character})


@login_required
def cls(request: HttpRequest, character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'class.html', context={'character': character})


@login_required
def unlock_abilities(request: HttpRequest, character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST':
        check_is_admin_or_owns_character(request.user, character)

        for parameter, value in request.POST.items():
            match = re.match(r'^(?P<action_type>lock|unlock)\s(?P<ability_index>[0-9]+)$', value)
            if match is not None:
                ability_index = int(match.group('ability_index'))
                ability = character.cls.abilities[ability_index]

                action_type = match.group('action_type')
                if action_type == 'lock':
                    for unlocked_ability in character.unlockedability_set.all():
                        if unlocked_ability.ability is ability:
                            # Do not allow the player to re-lock an ability if it is a
                            # prerequisite for another ability they have already unlocked.
                            for owned_ability in character.abilities:
                                if ability in owned_ability.prerequisites:
                                    raise ValidationError(
                                        'Cannot lock ability {} because it is a prerequisite '
                                        'for {}.'.format(ability.name, owned_ability.name))
                            unlocked_ability.delete()
                elif action_type == 'unlock':
                    for prerequisite in ability.prerequisites:
                        if prerequisite not in character.abilities:
                            raise ValidationError('Prerequisite {} not met for ability {}.'.format(
                                prerequisite.name, ability.name))

                    new_unlocked_ability = UnlockedAbility(
                        character=character,
                        ability_enum=inverse_abilities[ability])

                    if character.available_ap > 0:
                        new_unlocked_ability.save()
                    else:
                        raise ValidationError('Not enough available AP.')

        return redirect(reverse(unlock_abilities, args=[character_id]))

    return render(request, 'abilities.html', context={'character': character})


@login_required
def character_combos(request: HttpRequest, character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'combos.html', context={'character': character})


@login_required
def equip(request: HttpRequest, character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST':
        check_is_admin_or_owns_character(request.user, character)

        equip_form = CharacterEquipForm(request.POST)
        if equip_form.is_valid():
            character.utility_enum = equip_form.cleaned_data['utility_enum']
            character.head_enum = equip_form.cleaned_data['head_enum']
            character.neck_enum = equip_form.cleaned_data['neck_enum']
            character.chest_enum = equip_form.cleaned_data['chest_enum']
            character.shield_enum = equip_form.cleaned_data['shield_enum']
            character.right_hand_enum = equip_form.cleaned_data['right_hand_enum']
            character.left_hand_enum = equip_form.cleaned_data['left_hand_enum']
            character.feet_enum = equip_form.cleaned_data['feet_enum']
            character.weapon_enum = equip_form.cleaned_data['weapon_enum']

            # Validate character meets requirements for equipment.
            for wearable in character.wearables:
                if character.get_attribute(wearable.min_attribute) < wearable.min_attribute_value:
                    raise ValidationError('Requirements not met for {}.  Need {} {}.'.format(
                        wearable.name, wearable.min_attribute_value, wearable.min_attribute.name))

            if (character.weapon.is_two_handed and
               character.shield_enum is not items.Shields.empty):
                raise ValidationError('Cannot equip a shield and a two-handed weapon.')

            if ((character.right_hand.is_two_handed and
                character.left_hand_enum is not items.Hands.empty) or
                (character.left_hand.is_two_handed and
                 character.right_hand_enum is not items.Hands.empty)):
                raise ValidationError('Cannot equip two-handed Hand item and an item in other '
                                      'hand.')

            if not character.can_use_weapon:
                raise ValidationError('Class {cls} cannot use {style} {type} weapons'.format(
                    cls=character.cls.name, style=character.weapon.style.name,
                    type=character.weapon.type.name))

            character.save()
            return redirect(reverse(stats, args=[character_id]))
    else:
        equip_form = CharacterEquipForm(
            initial={
                'utility_enum': character.utility_enum,
                'head_enum': character.head_enum,
                'neck_enum': character.neck_enum,
                'chest_enum': character.chest_enum,
                'shield_enum': character.shield_enum,
                'right_hand_enum': character.right_hand_enum,
                'left_hand_enum': character.left_hand_enum,
                'feet_enum': character.feet_enum,
                'weapon_enum': character.weapon_enum
            })

    return render(request, 'equip.html',
                  context={'equip_form': equip_form,
                           'character': character})


@login_required
def level_up(request: HttpRequest, character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST':
        check_is_admin_or_owns_character(request.user, character)

        level_up_form = LevelUpForm(request.POST)

        # Check if a delete input button was pressed to remove an old LevelUp.
        for parameter, value in request.POST.items():
            match = re.match(r'^delete\s(?P<levelup_id>[0-9]+)$', value)
            if match is not None:
                LevelUp.objects.get(pk=match.group('levelup_id')).delete()
                return redirect(reverse(level_up, args=[character_id]))

        # Otherwise, user is creating a new LevelUp.
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

            return redirect(reverse(level_up, args=[character_id]))
    else:
        level_up_form = LevelUpForm()

    return render(request, 'level_up.html',
                  context={'level_up_form': level_up_form,
                           'character': character})


@login_required
def skill_points(request: HttpRequest, character_id: int) -> HttpResponse:
    character = get_object_or_404(Character, pk=character_id)

    if request.method == 'POST':
        check_is_admin_or_owns_character(request.user, character)
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
            elif assigned_ath > character.max_sp_per_skill:
                raise ValidationError('Assigned ATH too high. Max: {}'.format(
                    character.max_sp_per_skill))
            elif assigned_ste > character.max_sp_per_skill:
                raise ValidationError('Assigned STE too high. Max: {}'.format(
                    character.max_sp_per_skill))
            elif assigned_for > character.max_sp_per_skill:
                raise ValidationError('Assigned FOR too high. Max: {}'.format(
                    character.max_sp_per_skill))
            elif assigned_apt > character.max_sp_per_skill:
                raise ValidationError('Assigned APT too high. Max: {}'.format(
                    character.max_sp_per_skill))
            elif assigned_per > character.max_sp_per_skill:
                raise ValidationError('Assigned PER too high. Max: {}'.format(
                    character.max_sp_per_skill))
            elif assigned_spe > character.max_sp_per_skill:
                raise ValidationError('Assigned SPE too high. Max: {}'.format(
                    character.max_sp_per_skill))
            else:
                character.assigned_ath = assigned_ath
                character.assigned_ste = assigned_ste
                character.assigned_for = assigned_for
                character.assigned_apt = assigned_apt
                character.assigned_per = assigned_per
                character.assigned_spe = assigned_spe
                character.save()

            return redirect(reverse(skill_points, args=[character_id]))
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
