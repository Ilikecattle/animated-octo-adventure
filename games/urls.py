from django.conf.urls import patterns, include, url

from games import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>\w+)/$', views.game, name='games.views.detail'),
)
