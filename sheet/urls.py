from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<character_id>[0-9]+)/$', views.index, name='Index'),
    url(r'^(?P<character_id>[0-9]+)/stats/$', views.stats, name='Stats'),
    url(r'^(?P<character_id>[0-9]+)/level_up/$', views.level_up, name='Level Up'),
]
