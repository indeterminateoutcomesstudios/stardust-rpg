from django.conf.urls import url

from . import views
from .models import items

urlpatterns = [
    url(r'^characters/$', views.characters, name='sheet-views-characters'),
    url(r'^classes/$', views.all_classes, name='sheet-views-classes'),
    url(r'^combos/$', views.all_combos, name='sheet-views-all-combos'),
    url(r'^heads/$', views.equipment, {'wearables': items.heads.values()},
        name='sheet-views-heads'),
    url(r'^necks/$', views.equipment, {'wearables': items.necks.values()},
        name='sheet-views-necks'),
    url(r'^chests/$', views.equipment, {'wearables': items.chests.values()},
        name='sheet-views-chests'),
    url(r'^shields/$', views.equipment, {'wearables': items.shields.values()},
        name='sheet-views-shields'),
    url(r'^hands/$', views.equipment, {'wearables': items.hands.values()},
        name='sheet-views-hands'),
    url(r'^feets/$', views.equipment, {'wearables': items.feets.values()},
        name='sheet-views-feets'),
    url(r'^utilities/$', views.equipment, {'wearables': items.utilities.values()},
        name='sheet-views-utilities'),
    url(r'^(?P<character_id>[0-9]+)/stats/$', views.stats, name='sheet-views-stats'),
    url(r'^(?P<character_id>[0-9]+)/class/$', views.cls, name='sheet-views-class'),
    url(r'^(?P<character_id>[0-9]+)/abilities/$', views.unlock_abilities,
        name='sheet-views-abilities'),
    url(r'^(?P<character_id>[0-9]+)/combos/$', views.character_combos, name='sheet-views-combos'),
    url(r'^(?P<character_id>[0-9]+)/equip/$', views.equip, name='sheet-views-equip'),
    url(r'^(?P<character_id>[0-9]+)/level_up/$', views.level_up, name='sheet-views-level-up'),
    url(r'^(?P<character_id>[0-9]+)/skill_points/$', views.skill_points,
        name='sheet-views-skill-points'),
]
