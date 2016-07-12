import enum
from typing import Tuple

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ..models import classes, combos, equipment, party


@login_required
def parties(request: HttpRequest) -> HttpResponse:
    return render(request, 'parties.html', context={'parties': party.Party.objects.all()})


@login_required
def all_classes(request: HttpRequest) -> HttpResponse:
    return render(request, 'classes.html', context={'classes': classes.classes.values()})


@login_required
def class_abilities(request: HttpRequest, class_name: str) -> HttpResponse:
    return render(request, 'browser_abilities.html',
                  context={'cls': classes.get_class(class_name)})


@login_required
def all_combos(request: HttpRequest) -> HttpResponse:
    return render(request, 'browser_combos.html', context={'combos': combos.combos})


@login_required
def all_equipment(request: HttpRequest, wearables: Tuple[equipment.Wearable, ...]) -> HttpResponse:
    return render(request, 'equipment.html',
                  context={'wearables': sorted(wearables, key=lambda wearable: wearable.price),
                           'Rarity': equipment.Rarity})


@login_required
def all_weapons(request: HttpRequest, weapons: Tuple[equipment.Weapon, ...]) -> HttpResponse:
    return render(request, 'weapons.html',
                  context={'weapons': sorted(weapons, key=lambda weapon: weapon.price),
                           'Rarity': equipment.Rarity})


@login_required
def all_items(request: HttpRequest, item_set: Tuple[equipment.Item, ...]) -> HttpResponse:
    return render(request, 'items.html',
                  context={'items': sorted(item_set, key=lambda item: item.price),
                           'Rarity': equipment.Rarity})


@login_required
def pictures(request: HttpRequest, picture_enum: Tuple[enum.Enum, ...]) -> HttpResponse:
    return render(request, 'pictures.html',
                  context={'pictures': sorted([picture for picture in picture_enum],
                                              key=lambda picture: picture.name),
                           'picture_type': list(picture_enum)[0].__class__.__name__})
