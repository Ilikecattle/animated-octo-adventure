from django.conf.urls import patterns, include, url

from LOML import views

urlpatterns = patterns('',
    url(r'^get_message/$', views.message, name='LOML.views.message'),
    url(r'^get_messages/$', views.messages, name='LOML.views.messages'),
    url(r'^get_url/$', views.url, name='LOML.views.url'),
)
