from django.conf.urls import patterns, include, url

from carquizgame import views

urlpatterns = patterns('',
    url(r'^(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<day>\d\d)/$', views.question, name='carquizgame.views.question'),
    url(r'^check_year/$', views.check_year, name='carquizgame.views.check_year'),
    url(r'^', views.index, name='carquizgame.index'),
)
