from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('userena.urls')),
    # url(r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^games/', include('games.urls')),
)
