from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<character_id>[0-9]+)/$', views.index, name='Index'),
    url(r'^(?P<character_id>[0-9]+)/stats/$', views.stats, name='Stats'),
    url(r'^(?P<character_id>[0-9]+)/class/$', views.cls, name='Class'),
    url(r'^(?P<character_id>[0-9]+)/abilities/$', views.abilities, name='Abilities'),
    url(r'^(?P<character_id>[0-9]+)/equip/$', views.equip, name='Equip'),
    url(r'^(?P<character_id>[0-9]+)/level_up/$', views.level_up, name='Level Up'),
]
