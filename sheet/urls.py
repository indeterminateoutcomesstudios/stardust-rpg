from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='Index'),
    url(r'^stats$', views.stats, name='Stats'),
    url(r'^level_up$', views.level_up, name='Level Up'),
]
