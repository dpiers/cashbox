from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'zerocater.core.views',
	url(r'^$', 'index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
