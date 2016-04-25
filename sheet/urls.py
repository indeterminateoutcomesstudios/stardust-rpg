from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^characters/$', views.characters, name='sheet-views-characters'),
    url(r'^(?P<character_id>[0-9]+)/stats/$', views.stats, name='sheet-views-stats'),
    url(r'^(?P<character_id>[0-9]+)/class/$', views.cls, name='sheet-views-class'),
    url(r'^(?P<character_id>[0-9]+)/abilities/$', views.unlock_abilities,
        name='sheet-views-abilities'),
    url(r'^(?P<character_id>[0-9]+)/equip/$', views.equip, name='sheet-views-equip'),
    url(r'^(?P<character_id>[0-9]+)/level_up/$', views.level_up, name='sheet-views-level-up'),
    url(r'^(?P<character_id>[0-9]+)/skill_points/$', views.skill_points,
        name='sheet-views-skill-points'),
]
