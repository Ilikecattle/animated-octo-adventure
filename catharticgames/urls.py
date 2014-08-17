from django.conf import settings
from django.contrib.sitemaps import GenericSitemap, Sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse

from catharticgames import views

from games.models import Game

from django.contrib import admin
admin.autodiscover()

class StaticViewSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return ['home_page']

    def location(self, item):
        return reverse(item)

info_dict = {
    'queryset': Game.objects.all(),
}

sitemaps = {
    'static' : StaticViewSitemap,
    'games': GenericSitemap(info_dict, priority=0.6),
}

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^games/', include('games.urls')),
    url(r'^loml/', include('LOML.urls')),
    url(r'^$', views.home_page, name='home_page'),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
    {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
