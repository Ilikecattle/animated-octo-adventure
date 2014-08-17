from django.conf.urls import patterns, include, url

from LOML import views

urlpatterns = patterns('',
    url(r'^get_message/$', views.message, name='LOML.views.message'),
)
